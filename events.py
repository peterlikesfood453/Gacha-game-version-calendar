# -*- coding: utf-8 -*-
"""游戏版本日历的数据与 ICS 生成。"""
from datetime import datetime, timedelta, timezone

BJ = timezone(timedelta(hours=8))
STAMP = "20261102T120000Z"

# 顺序即页面展示顺序
GAMES = [
    {"id": "genshin",  "name": "原神",              "short": "原神",   "ver": "7.2",  "color": "#C9A227",
     "cycle": "42 天 · 周三更新 · 前瞻约提前 12 天（周五 20:00）"},
    {"id": "hsr",      "name": "崩坏：星穹铁道",     "short": "星铁",   "ver": "4.7",  "color": "#7B6CF6",
     "cycle": "42 天 · 周三更新 · 前瞻约提前 12 天（周五 19:30）"},
    {"id": "zzz",      "name": "绝区零",            "short": "绝区零", "ver": "3.3",  "color": "#D99A00",
     "cycle": "42 天 · 周三更新 · 前瞻约提前 12 天（周五 19:30）"},
    {"id": "wuwa",     "name": "鸣潮",              "short": "鸣潮",   "ver": "3.7",  "color": "#2E7D8F",
     "cycle": "约 42 天 · 周四更新 · 前瞻约提前 6 天（周五 19:00）"},
    {"id": "endfield", "name": "明日方舟：终末地",   "short": "终末地", "ver": "1.6",  "color": "#5A6472",
     "cycle": "42 天 · 周四更新 · 前瞻约提前 9 天（周二 19:30）"},
    {"id": "nte",      "name": "异环",              "short": "异环",   "ver": "1.5",  "color": "#D94F3D",
     "cycle": "42 天 · 周四更新 · 前瞻约提前 8 天（周三 19:30）"},
    {"id": "wwm",      "name": "燕云十六声",        "short": "燕云",   "ver": "2.3",  "color": "#7A5C3E",
     "cycle": "更新不固定，按赛季/大区域推进，无统一前瞻"},
    {"id": "hokw",     "name": "王者荣耀世界",      "short": "王世界", "ver": "S1",   "color": "#2B7CD3",
     "cycle": "按赛季推进，S2 尚未公布确切日期"},
]

# status: official 官方确认 / est 按周期推算 / tbd 日期待官方公布
EVENTS = [
    # ---------- 原神 ----------
    dict(g="genshin", ver="7.2", kind="release", dt="2026-11-04 11:00", dur=30,
         title="原神 7.2「坏灭肇始之时」版本更新", status="official",
         desc="06:00 起停服维护，预计 11:00 前后开服。新五星雷系「米提亚」+ 芙宁娜复刻，至冬新主线与新地图。"),
    dict(g="genshin", ver="7.3", kind="preview", dt="2026-12-04 20:00", dur=60,
         title="原神 7.3 前瞻特别节目", status="est",
         desc="按 42 天周期推算。B站 / 抖音 / 米游社 官方直播间，直播中发 3 组兑换码，合计 300 原石。"),
    dict(g="genshin", ver="7.3", kind="release", dt="2026-12-16 11:00", dur=30,
         title="原神 7.3 版本更新", status="est",
         desc="按 42 天版本周期推算（7.2 于 11/4 上线）。"),
    dict(g="genshin", ver="7.4", kind="preview", dt="2027-01-15 20:00", dur=60,
         title="原神 7.4 前瞻特别节目", status="est",
         desc="推算日期，官方一般提前约 12 天公布确切时间。"),
    dict(g="genshin", ver="7.4", kind="release", dt="2027-01-27 11:00", dur=30,
         title="原神 7.4 版本更新（海灯节）", status="est",
         desc="海灯节版本，按 42 天周期推算。"),

    # ---------- 崩坏：星穹铁道 ----------
    dict(g="hsr", ver="4.7", kind="release", dt="2026-11-11 11:00", dur=30,
         title="星穹铁道 4.7「此刻，将群星付之一笑」版本更新", status="official",
         desc="星神「阿哈」首次进池，卡池一直开到 12/22 15:00。版本 11:00 前后开服。"),
    dict(g="hsr", ver="4.8", kind="preview", dt="2026-12-11 19:30", dur=60,
         title="星穹铁道 4.8 前瞻特别节目", status="est",
         desc="按 42 天周期、前瞻提前 12 天推算（4.7 于 11/11 上线）。"),
    dict(g="hsr", ver="4.8", kind="release", dt="2026-12-23 11:00", dur=30,
         title="星穹铁道 4.8 版本更新", status="est",
         desc="4.7 卡池排到 12/22 15:00，4.8 大概率 12/23 上线。"),
    dict(g="hsr", ver="5.0", kind="preview", dt="2027-01-22 19:30", dur=60,
         title="星穹铁道 5.0 前瞻特别节目", status="est",
         desc="推算日期，按 42 天周期。"),
    dict(g="hsr", ver="5.0", kind="release", dt="2027-02-03 11:00", dur=30,
         title="星穹铁道 5.0 版本更新", status="est",
         desc="推算日期，按 42 天周期。"),

    # ---------- 绝区零 ----------
    dict(g="zzz", ver="3.4", kind="preview", dt="2026-11-20 19:30", dur=90,
         title="绝区零 3.4 前瞻特别节目", status="official",
         desc="新虚狩「挽昼」登场，同时开启与崩坏：星穹铁道联动（知更鸟、卡芙卡），发 300 菲林兑换码。"),
    dict(g="zzz", ver="3.4", kind="release", dt="2026-12-02 11:00", dur=30,
         title="绝区零 3.4 版本更新", status="official",
         desc="3.3 版本于 12/2 06:00 结束，3.4 同日开启。维护通常 06:00–11:00。"),
    dict(g="zzz", ver="3.5", kind="preview", dt="2027-01-01 19:30", dur=90,
         title="绝区零 3.5 前瞻特别节目", status="est",
         desc="推算日期，按 42 天版本周期。"),
    dict(g="zzz", ver="3.5", kind="release", dt="2027-01-13 11:00", dur=30,
         title="绝区零 3.5 版本更新", status="est",
         desc="推算日期，按 42 天版本周期。"),

    # ---------- 鸣潮 ----------
    dict(g="wuwa", ver="3.8", kind="preview", dt="2026-11-06 19:00", dur=90,
         title="鸣潮 3.8 前瞻通讯", status="official",
         desc="官方直播间。公布 3.8 卡池与新五星「莉莉」，发 300 星声兑换码。"),
    dict(g="wuwa", ver="3.8", kind="release", dt="2026-11-12 11:00", dur=30,
         title="鸣潮 3.8 版本更新", status="official",
         desc="11/10 开放预下载。更新后邮件领 600 星声修复补偿。"),
    dict(g="wuwa", ver="4.0", kind="preview", dt="2026-12-18 19:00", dur=90,
         title="鸣潮 4.0 前瞻通讯", status="est",
         desc="推算日期。鸣潮约 6 周一个版本，前瞻一般安排在更新前 6 天。"),
    dict(g="wuwa", ver="4.0", kind="release", dt="2026-12-24 11:00", dur=30,
         title="鸣潮 4.0 版本更新", status="est",
         desc="推算日期，按 6 周周期（3.8 于 11/12 上线）。"),

    # ---------- 明日方舟：终末地 ----------
    dict(g="endfield", ver="1.7", kind="preview", dt="2026-11-17 19:30", dur=90,
         title="终末地 1.7 前瞻特别节目", status="est",
         desc="1.6 前瞻比上线早 9 天（周二），照此外推。前瞻奖励需到专题网页领，不再直邮。"),
    dict(g="endfield", ver="1.7", kind="release", dt="2026-11-26 11:00", dur=30,
         title="终末地 1.7 版本更新", status="tbd",
         desc="社区情报指向 11/26（周四），与 1.6 相隔 42 天。官方尚未正式公告，以官方为准。"),
    dict(g="endfield", ver="1.8", kind="preview", dt="2026-12-29 19:30", dur=90,
         title="终末地 1.8 前瞻特别节目", status="est",
         desc="推算日期，按 42 天周期。"),
    dict(g="endfield", ver="1.8", kind="release", dt="2027-01-07 11:00", dur=30,
         title="终末地 1.8 版本更新", status="est",
         desc="推算日期，按 42 天周期。"),

    # ---------- 异环 ----------
    dict(g="nte", ver="1.5", kind="release", dt="2026-11-05 11:00", dur=30,
         title="异环 1.5「致电，空想迷数」版本更新", status="official",
         desc="新 S 级「曳尔沐」上半、Exe 下半，新增城市物流与坦克对战。版本持续到 12/17。"),
    dict(g="nte", ver="1.6", kind="preview", dt="2026-12-09 19:30", dur=90,
         title="异环 1.6 前瞻特别节目", status="est",
         desc="1.5 前瞻比上线早 8 天（周三），照此外推。"),
    dict(g="nte", ver="1.6", kind="release", dt="2026-12-17 11:00", dur=30,
         title="异环 1.6 版本更新", status="official",
         desc="1.5 的卡池与活动排期全部写到 12/17 05:59，1.6 以此接档。"),

    # ---------- 燕云十六声 ----------
    dict(g="wwm", ver="2.4", kind="release", dt="2026-11-06 10:00", dur=30,
         title="燕云十六声 新赛季「南吕相和·下」+ 双枪「鸣金·霆」", status="official",
         desc="国服节点。同日开放未央城新区域「幻术森林」、新侠迹「归兮归兮」。双枪是今年第三个新武学流派。"),
    dict(g="wwm", ver="2.4", kind="release", dt="2026-11-13 10:00", dur=30,
         title="燕云十六声「滹沱」大版本 + 全球一周年", status="official",
         desc="新战场区域「滹沱」、中渡桥之战主线、两名新世界 BOSS，同步开启一周年活动。国际服以此日期为准。"),

    # ---------- 王者荣耀世界 ----------
    dict(g="hokw", ver="S2", kind="release", dt="2026-11-26 10:00", dur=30,
         title="王者荣耀世界 S2 赛季更新（待定）", status="tbd",
         desc="S2 体验服 11 月中上旬开测，正式服预计 11 月下旬。官方还没公布确切日期，这里是占位。"),
]

STATUS_LABEL = {"official": "官方确认", "est": "预估", "tbd": "待定", "rule": "规则推算"}
KIND_LABEL = {"preview": "前瞻直播", "release": "版本更新", "code": "兑换码失效"}

GAME_BY_ID = {g["id"]: g for g in GAMES}

# 各游戏前瞻兑换码的官方失效口径：以前瞻直播当天为第 0 天，往后数 day 天的 at 时刻截止。
# 依据（2026 年官方公告实例）：
#   原神   7.2 前瞻 10/23 20:00 → 码 10/26 12:00:00 失效（第 3 天中午）
#   星铁   4.7 前瞻 10/30 19:30 → 码 10/31 23:59:59 失效（次日）
#   绝区零 3.3 前瞻 10/09 20:00 → 码 10/11 23:59:59 失效（第 2 天）
#   鸣潮   3.7 前瞻 09/19 22:24 → 码 09/21 23:59 失效（第 2 天）
#   异环   1.5 前瞻 10/28 19:30 → 码 11/01 23:59 失效（第 4 天）
# 终末地/燕云/王世界没有「前瞻兑换码」这一说，不生成。
CODE_RULE = {
    "genshin": dict(day=3, at="12:00", note="直播后第 3 天中午 12:00"),
    "hsr":     dict(day=1, at="23:59", note="直播次日 23:59"),
    "zzz":     dict(day=2, at="23:59", note="直播后第 2 天 23:59"),
    "wuwa":    dict(day=2, at="23:59", note="直播后第 2 天 23:59"),
    "nte":     dict(day=4, at="23:59", note="直播后第 4 天 23:59"),
}

CODE_REWARD = {
    "genshin": "3 组码合计 300 原石，外加精锻用魔矿、大英雄的经验、摩拉",
    "hsr":     "3 组码合计 300 星琼，外加角色与光锥培养材料",
    "zzz":     "3 组码合计 300 菲林",
    "wuwa":    "3 组码合计 300 星声",
    "nte":     "3 组码合计 300 环石",
}

CODE_ENTRY = {
    "genshin": "游戏内 设置 → 账户 → 兑换码，或米游社「兑换中心」网页",
    "hsr":     "游戏内 手机 → 右上角「···」→ 兑换码，或米哈游兑换中心网页",
    "zzz":     "游戏内 更多 → 兑换码",
    "wuwa":    "游戏内 设置 → 其他设置（扳手图标）→ 兑换",
    "nte":     "游戏内手机 → 右上角「···」→ 兑换码",
}


def _hm(s: str):
    h, m = s.split(":")
    return int(h), int(m)


def add_code_events():
    """给每个前瞻直播补一条「兑换码失效」事件，时间精确到分钟。"""
    added = []
    for e in EVENTS:
        if e["kind"] != "preview":
            continue
        rule = CODE_RULE.get(e["g"])
        if not rule:
            continue
        start = datetime.strptime(e["dt"], "%Y-%m-%d %H:%M").replace(tzinfo=BJ)
        hh, mm = _hm(rule["at"])
        dead = (start + timedelta(days=rule["day"])).replace(hour=hh, minute=mm, second=0)
        hours = int(round((dead - start).total_seconds() / 3600))
        g = GAME_BY_ID[e["g"]]

        e["desc"] += "\n\n兑换码有效期至 %s（%s），即直播结束后 %d 小时。" % (
            dead.strftime("%m/%d %H:%M"), rule["note"], hours)

        added.append(dict(
            g=e["g"], ver=e["ver"], kind="code",
            dt=dead.strftime("%Y-%m-%d %H:%M"), dur=15,
            title="%s %s 前瞻兑换码失效" % (g["short"], e["ver"]),
            status="rule",
            desc=("\n".join([
                "有效 %d 小时：%s 开播 → %s 截止（北京时间）。" % (
                    hours, start.strftime("%m/%d %H:%M"), dead.strftime("%m/%d %H:%M")),
                "",
                CODE_REWARD[e["g"]] + "。",
                "过期立即作废，官方不补发，也不接受事后申诉。",
                "",
                "兑换入口：" + CODE_ENTRY[e["g"]] + "。",
                "没看直播也能补：官方前瞻回放的简介区、米游社前瞻专题页都会挂出这三组码。",
            ])),
        ))
    return added


EVENTS += add_code_events()
EVENTS.sort(key=lambda e: e["dt"])


def esc(t: str) -> str:
    return (t.replace("\\", "\\\\").replace(";", "\\;")
             .replace(",", "\\,").replace("\n", "\\n"))


def fold(line: str) -> str:
    """按 RFC 5545 折叠长行，且不把转义序列（\\n \\, \\;）拆到两行。"""
    out, cur, limit = [], "", 75
    for ch in line:
        if len((cur + ch).encode("utf-8")) > limit:
            if cur.endswith("\\"):
                out.append(cur[:-1])
                cur, limit = cur[-1] + ch, 74
            else:
                out.append(cur)
                cur, limit = ch, 74
        else:
            cur += ch
    out.append(cur)
    return "\r\n ".join(out)


def utc_str(dt: datetime) -> str:
    return dt.astimezone(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def slug(e: dict) -> str:
    return "%s-%s-%s" % (e["g"], e["ver"].replace(".", ""), e["kind"])


def build_event(e: dict) -> str:
    start = datetime.strptime(e["dt"], "%Y-%m-%d %H:%M").replace(tzinfo=BJ)
    end = start + timedelta(minutes=e["dur"])
    game = GAME_BY_ID[e["g"]]["name"]
    label = "" if e["status"] == "official" else "（%s）" % STATUS_LABEL[e["status"]]
    place = {"preview": " 官方直播间", "release": "", "code": " 兑换入口"}[e["kind"]]
    body = "\n".join([
        e["desc"],
        "",
        "时间均为北京时间 UTC+8。",
        "标注「预估 / 待定」的日期是按版本周期推算的，官方公布后会有偏差。",
    ])
    lines = [
        "BEGIN:VEVENT",
        "UID:%s@game-version-calendar" % slug(e),
        "DTSTAMP:%s" % STAMP,
        "DTSTART:%s" % utc_str(start),
        "DTEND:%s" % utc_str(end),
        fold("SUMMARY:" + esc(e["title"] + label)),
        fold("DESCRIPTION:" + esc(body)),
        fold("LOCATION:" + esc(game + place)),
        fold("CATEGORIES:" + esc(game)),
        "STATUS:CONFIRMED",
        "TRANSP:TRANSPARENT",
    ]
    if e["kind"] == "preview":
        lines += ["BEGIN:VALARM", "TRIGGER:-PT30M", "ACTION:DISPLAY",
                  fold("DESCRIPTION:" + esc("前瞻直播 30 分钟后开始")), "END:VALARM"]
    elif e["kind"] == "code":
        lines += ["BEGIN:VALARM", "TRIGGER:-PT2H", "ACTION:DISPLAY",
                  fold("DESCRIPTION:" + esc("兑换码 2 小时后失效，还没换的现在去换")), "END:VALARM",
                  "BEGIN:VALARM", "TRIGGER:-PT30M", "ACTION:DISPLAY",
                  fold("DESCRIPTION:" + esc("兑换码 30 分钟后失效，过期不补")), "END:VALARM"]
    else:
        lines += ["BEGIN:VALARM", "TRIGGER:-P1D", "ACTION:DISPLAY",
                  fold("DESCRIPTION:" + esc("明天是版本更新日")), "END:VALARM",
                  "BEGIN:VALARM", "TRIGGER:-PT2H", "ACTION:DISPLAY",
                  fold("DESCRIPTION:" + esc("版本更新，准备开服")), "END:VALARM"]
    lines.append("END:VEVENT")
    return "\r\n".join(lines)


def calendar(game_ids, name="二游版本日历", desc=None) -> str:
    picked = [e for e in EVENTS if e["g"] in game_ids]
    picked.sort(key=lambda e: e["dt"])
    if desc is None:
        desc = "前瞻直播与版本更新的提醒。退坑了就在日历 App 里删掉本日历，提醒会一起消失。"
    head = ("BEGIN:VCALENDAR\r\nVERSION:2.0\r\n"
            "PRODID:-//WorkBuddy//Game Version Calendar//CN\r\n"
            "CALSCALE:GREGORIAN\r\nMETHOD:PUBLISH\r\n")
    head += fold("X-WR-CALNAME:" + esc(name)) + "\r\n"
    head += fold("X-WR-CALDESC:" + esc(desc)) + "\r\n"
    head += ("X-WR-TIMEZONE:Asia/Shanghai\r\n"
             "REFRESH-INTERVAL;VALUE=DURATION:PT6H\r\n"
             "X-PUBLISHED-TTL:PT6H\r\n")
    return head + "".join(build_event(e) + "\r\n" for e in picked) + "END:VCALENDAR\r\n"
