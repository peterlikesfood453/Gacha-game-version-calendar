# -*- coding: utf-8 -*-
"""把 events.py 的数据编译成纯静态站。

输出：
    static/index.html      勾选页（数据已内联，不需要服务器）
    static/ics/<id>.ics    每款游戏一份订阅文件
    static/ics/all.ics     全部游戏

用法：python build_static.py
改完 events.py 记得跑一次，再把 static/ 一起提交。
"""
import json
import os

import events as E

BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, "static")
ICS_DIR = os.path.join(OUT, "ics")


def write(path: str, text: str) -> None:
    # newline="" 保持 ics 里的 \r\n 原样，不被 Windows 再转一次
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


def main() -> None:
    os.makedirs(ICS_DIR, exist_ok=True)

    payload = {
        "games": E.GAMES,
        "events": E.EVENTS,
        "statusLabel": E.STATUS_LABEL,
        "stamp": E.STAMP,
        "latest": max(e["dt"] for e in E.EVENTS),
    }
    blob = json.dumps(payload, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")

    tpl_path = os.path.join(OUT, "template.html")
    with open(tpl_path, encoding="utf-8") as f:
        tpl = f.read()
    if "__DATA_JSON__" not in tpl:
        raise SystemExit("template.html 里找不到 __DATA_JSON__ 占位符")

    write(os.path.join(OUT, "index.html"), tpl.replace("__DATA_JSON__", blob))

    for g in E.GAMES:
        body = E.calendar({g["id"]}, g["short"] + " · 版本日历",
                          "只订阅「%s」的前瞻与版本更新。不玩了：iPhone 直接删掉本日历；安卓在「日程账号管理」里关掉「显示」开关，别点删除（会连带其他订阅）。"
                          % g["name"])
        write(os.path.join(ICS_DIR, g["id"] + ".ics"), body)

    write(os.path.join(ICS_DIR, "all.ics"),
          E.calendar({g["id"] for g in E.GAMES}, "二游版本日历 · 全部"))

    print("已生成:")
    print("  static/index.html            %d 款游戏 / %d 条日程" % (len(E.GAMES), len(E.EVENTS)))
    print("  static/ics/*.ics             %d 份单游戏订阅 + 1 份全量" % len(E.GAMES))


if __name__ == "__main__":
    main()
