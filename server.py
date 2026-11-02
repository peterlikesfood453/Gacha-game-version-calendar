# -*- coding: utf-8 -*-
"""游戏版本日历 —— 单端口 HTTP 服务。

/                     选择页（服务端把游戏与事件数据注入页面）
/calendar.ics?games=  按所选游戏生成日历
/game/<id>.ics        单个游戏的日历
/all.ics              全部游戏
"""
import json
import os
import posixpath
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, unquote, urlparse

import events as E

BASE = os.path.dirname(os.path.abspath(__file__))
STATIC_EXT = {".css", ".js", ".png", ".jpg", ".svg", ".webp", ".ico", ".woff2"}


def render_index() -> str:
    with open(os.path.join(BASE, "index.html"), encoding="utf-8") as f:
        tpl = f.read()
    payload = {"games": E.GAMES, "events": E.EVENTS, "statusLabel": E.STATUS_LABEL}
    blob = json.dumps(payload, ensure_ascii=False).replace("</", "<\\/")
    return tpl.replace("__DATA_JSON__", blob)


class Handler(BaseHTTPRequestHandler):
    server_version = "GameCalendar/2.0"

    def log_message(self, *args):  # 静音
        pass

    def _send(self, code, body: bytes, ctype: str, extra=None):
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        for k, v in (extra or {}).items():
            self.send_header(k, v)
        self.end_headers()
        if self.command != "HEAD":
            self.wfile.write(body)

    def _ics(self, ids, name, desc=None):
        body = E.calendar(set(ids), name, desc).encode("utf-8")
        self._send(200, body, "text/calendar; charset=utf-8",
                   {"Content-Disposition": 'inline; filename="game-calendar.ics"'})

    def do_HEAD(self):
        self.do_GET()

    def do_GET(self):
        url = urlparse(self.path)
        path = unquote(url.path)
        qs = parse_qs(url.query)

        if path in ("/", "/index.html"):
            self._send(200, render_index().encode("utf-8"), "text/html; charset=utf-8")
            return

        if path == "/calendar.ics":
            raw = (qs.get("games", [""])[0] or "").split(",")
            ids = [x for x in (i.strip() for i in raw) if x in E.GAME_BY_ID]
            if not ids:
                ids = [g["id"] for g in E.GAMES]
            # 保持 GAMES 的定义顺序
            ids = [g["id"] for g in E.GAMES if g["id"] in ids]
            self._ics(ids, "二游版本日历 · " + "、".join(E.GAME_BY_ID[i]["short"] for i in ids))
            return

        if path == "/all.ics":
            ids = [g["id"] for g in E.GAMES]
            self._ics(ids, "二游版本日历")
            return

        if path.startswith("/game/") or path.startswith("/sub/"):
            prefix = "/game/" if path.startswith("/game/") else "/sub/"
            if not path.endswith(".ics"):
                self._send(404, b"not found", "text/plain; charset=utf-8")
                return
            gid = path[len(prefix):-len(".ics")]
            if gid in E.GAME_BY_ID:
                g = E.GAME_BY_ID[gid]
                self._ics([gid], g["short"] + " · 版本日历",
                          "只订阅「%s」的前瞻与版本更新。不玩了就删掉这个日历，其他游戏不受影响。"
                          % g["name"])
                return
            self._send(404, b"unknown game", "text/plain; charset=utf-8")
            return

        rel = posixpath.normpath(path).lstrip("/")
        fp = os.path.join(BASE, *rel.split("/"))
        if (os.path.isfile(fp) and os.path.commonpath([BASE, os.path.abspath(fp)]) == BASE
                and os.path.splitext(fp)[1].lower() in STATIC_EXT):
            ctype = {".css": "text/css", ".js": "application/javascript",
                     ".svg": "image/svg+xml", ".png": "image/png",
                     ".ico": "image/x-icon"}.get(os.path.splitext(fp)[1].lower(),
                                                 "application/octet-stream")
            with open(fp, "rb") as f:
                self._send(200, f.read(), ctype + "; charset=utf-8" if ctype.startswith("text") else ctype)
            return

        self._send(404, "404 Not Found".encode(), "text/plain; charset=utf-8")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8000"))
    ThreadingHTTPServer(("0.0.0.0", port), Handler).serve_forever()
