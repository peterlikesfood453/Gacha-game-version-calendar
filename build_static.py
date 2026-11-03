# -*- coding: utf-8 -*-
"""把 events.py 的数据编译成纯静态站（中英两版）。

输出：
    static/index.html        中文勾选页（数据已内联，不需要服务器）
    static/en/index.html     英文勾选页
    static/ics/<id>.ics      中文：每款游戏一份订阅文件 + all.ics
    static/en/ics/<id>.ics   英文：同上

用法：python build_static.py
改完 events.py 或 strings.py 记得跑一次，再把 static/ 一起提交。
"""
import json
import os

import events as E
import strings as S

BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, "static")


def write(path: str, text: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    # newline="" 保持 ics 里的 \r\n 原样，不被 Windows 再转一次
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


def build_page(lang: str, tpl: str, href_zh: str, href_en: str) -> str:
    payload = {
        "games": E.page_games(lang),
        "events": E.page_events(lang),
        "statusLabel": E.STATUS_LABEL_EN if lang == "en" else E.STATUS_LABEL,
        "ui": S.JS[lang],
        "stamp": E.STAMP,
        "latest": max(e["dt"] for e in E.EVENTS),
    }
    blob = json.dumps(payload, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    page = S.render(tpl, lang, ("href_zh", href_zh), ("href_en", href_en))
    return page.replace("__DATA_JSON__", blob)


def build_ics(lang: str) -> int:
    en = lang == "en"
    sub = "en/ics" if en else "ics"
    for g in E.GAMES:
        write(os.path.join(OUT, sub, g["id"] + ".ics"),
              E.calendar({g["id"]}, title=E.game_cal_name(g, lang),
                         desc=E.game_cal_desc(g, lang), lang=lang))
    write(os.path.join(OUT, sub, "all.ics"),
          E.calendar({g["id"] for g in E.GAMES},
                     title=("Gacha Version Calendar - All" if en else "二游版本日历 · 全部"),
                     lang=lang))
    return len(E.GAMES) + 1


def main() -> None:
    tpl_path = os.path.join(OUT, "template.html")
    with open(tpl_path, encoding="utf-8") as f:
        tpl = f.read()
    if "__DATA_JSON__" not in tpl:
        raise SystemExit("template.html 里找不到 __DATA_JSON__ 占位符")

    # 中文在根，英文在 /en/，两个页面的 hreflang 互为镜像
    write(os.path.join(OUT, "index.html"), build_page("zh", tpl, "./", "en/"))
    write(os.path.join(OUT, "en", "index.html"), build_page("en", tpl, "../", "./"))

    n_zh = build_ics("zh")
    n_en = build_ics("en")

    print("已生成:")
    print("  static/index.html            %d 款游戏 / %d 条日程 (zh)" % (len(E.GAMES), len(E.EVENTS)))
    print("  static/en/index.html         %d 款游戏 / %d 条日程 (en)" % (len(E.GAMES), len(E.EVENTS)))
    print("  static/ics/                  %d 份 (zh)" % n_zh)
    print("  static/en/ics/               %d 份 (en)" % n_en)


if __name__ == "__main__":
    main()
