# -*- coding: utf-8 -*-
"""游戏版本日历的数据与 ICS 生成。

双语：每条数据都带中文原文和英文文案（*_en 字段）。
build_event() / calendar() 接收 lang 参数，缺英文时回落到中文，不会崩。
"""
from datetime import datetime, timedelta, timezone

BJ = timezone(timedelta(hours=8))
STAMP = "20261102T120000Z"

# 顺序即页面展示顺序
GAMES = [
    {"id": "genshin", "name": "原神", "name_en": "Genshin Impact", "short": "原神", "short_en": "Genshin",
     "ver": "7.2", "color": "#C9A227",
     "cycle": "42 天 · 周三更新 · 前瞻约提前 12 天（周五 20:00）",
     "cycle_en": "42-day cycle · Wednesday updates · Special Program ~12 days earlier (Fri 20:00)"},
    {"id": "hsr", "name": "崩坏：星穹铁道", "name_en": "Honkai: Star Rail", "short": "星铁", "short_en": "Star Rail",
     "ver": "4.7", "color": "#7B6CF6",
     "cycle": "42 天 · 周三更新 · 前瞻约提前 12 天（周五 19:30）",
     "cycle_en": "42-day cycle · Wednesday updates · Special Program ~12 days earlier (Fri 19:30)"},
    {"id": "zzz", "name": "绝区零", "name_en": "Zenless Zone Zero", "short": "绝区零", "short_en": "ZZZ",
     "ver": "3.3", "color": "#D99A00",
     "cycle": "42 天 · 周三更新 · 前瞻约提前 12 天（周五 19:30）",
     "cycle_en": "42-day cycle · Wednesday updates · Special Program ~12 days earlier (Fri 19:30)"},
    {"id": "wuwa", "name": "鸣潮", "name_en": "Wuthering Waves", "short": "鸣潮", "short_en": "WuWa",
     "ver": "3.7", "color": "#2E7D8F",
     "cycle": "约 42 天 · 周四更新 · 前瞻约提前 6 天（周五 19:00）",
     "cycle_en": "~42-day cycle · Thursday updates · Preview broadcast ~6 days earlier (Fri 19:00)"},
    {"id": "endfield", "name": "明日方舟：终末地", "name_en": "Arknights: Endfield", "short": "终末地",
     "short_en": "Endfield", "ver": "1.6", "color": "#5A6472",
     "cycle": "42 天 · 周四更新 · 前瞻约提前 9 天（周二 19:30）",
     "cycle_en": "42-day cycle · Thursday updates · Special Program ~9 days earlier (Tue 19:30)"},
    {"id": "nte", "name": "异环", "name_en": "Neverness to Everness", "short": "异环", "short_en": "NTE",
     "ver": "1.5", "color": "#D94F3D",
     "cycle": "42 天 · 周四更新 · 前瞻约提前 8 天（周三 19:30）",
     "cycle_en": "42-day cycle · Thursday updates · Special Program ~8 days earlier (Wed 19:30)"},
    {"id": "wwm", "name": "燕云十六声", "name_en": "Where Winds Meet", "short": "燕云", "short_en": "Where Winds Meet",
     "ver": "2.3", "color": "#7A5C3E",
     "cycle": "更新不固定，按赛季/大区域推进，无统一前瞻",
     "cycle_en": "Irregular schedule, driven by seasons and region drops; no regular preview stream"},
    {"id": "hokw", "name": "王者荣耀世界", "name_en": "Honor of Kings: World", "short": "王世界", "short_en": "HoK: World",
     "ver": "S1", "color": "#2B7CD3",
     "cycle": "按赛季推进，S2 尚未公布确切日期",
     "cycle_en": "Season-based; Season 2 date not announced yet"},
]

# status: official 官方确认 / est 按周期推算 / tbd 日期待官方公布
EVENTS = [
    # ---------- 原神 ----------
    dict(g="genshin", ver="7.2", kind="release", dt="2026-11-04 11:00", dur=30,
         title="原神 7.2「坏灭肇始之时」版本更新", status="official",
         desc="06:00 起停服维护，预计 11:00 前后开服。新五星雷系「米提亚」+ 芙宁娜复刻，至冬新主线与新地图。",
         title_en="Genshin Impact 7.2 Version Update",
         desc_en="Servers go down for maintenance at 06:00 and should be back around 11:00 (UTC+8). "
                 "Adds a new 5-star Electro character, a Furina rerun, and a new Snezhnaya story chapter with a new map area."),
    dict(g="genshin", ver="7.3", kind="preview", dt="2026-12-04 20:00", dur=60,
         title="原神 7.3 前瞻特别节目", status="est",
         desc="按 42 天周期推算。B站 / 抖音 / 米游社 官方直播间，直播中发 3 组兑换码，合计 300 原石。",
         title_en="Genshin Impact 7.3 Special Program",
         desc_en="Projected from the 42-day cycle. Streamed on the official channels; three redemption codes "
                 "(300 Primogems total) are shown during the stream."),
    dict(g="genshin", ver="7.3", kind="release", dt="2026-12-16 11:00", dur=30,
         title="原神 7.3 版本更新", status="est",
         desc="按 42 天版本周期推算（7.2 于 11/4 上线）。",
         title_en="Genshin Impact 7.3 Version Update",
         desc_en="Projected from the 42-day cycle (7.2 launched on Nov 4)."),
    dict(g="genshin", ver="7.4", kind="preview", dt="2027-01-15 20:00", dur=60,
         title="原神 7.4 前瞻特别节目", status="est",
         desc="推算日期，官方一般提前约 12 天公布确切时间。",
         title_en="Genshin Impact 7.4 Special Program",
         desc_en="Projected date. The exact time is usually confirmed about 12 days ahead."),
    dict(g="genshin", ver="7.4", kind="release", dt="2027-01-27 11:00", dur=30,
         title="原神 7.4 版本更新（海灯节）", status="est",
         desc="海灯节版本，按 42 天周期推算。",
         title_en="Genshin Impact 7.4 Version Update (Lantern Rite)",
         desc_en="Lantern Rite version, projected from the 42-day cycle."),

    # ---------- 崩坏：星穹铁道 ----------
    dict(g="hsr", ver="4.7", kind="release", dt="2026-11-11 11:00", dur=30,
         title="星穹铁道 4.7「此刻，将群星付之一笑」版本更新", status="official",
         desc="星神「阿哈」首次进池，卡池一直开到 12/22 15:00。版本 11:00 前后开服。",
         title_en="Honkai: Star Rail 4.7 Version Update",
         desc_en="Aha the Aeon enters the banner pool for the first time, and the warp runs until Dec 22, 15:00 (UTC+8). "
                 "Servers open around 11:00."),
    dict(g="hsr", ver="4.8", kind="preview", dt="2026-12-11 19:30", dur=60,
         title="星穹铁道 4.8 前瞻特别节目", status="est",
         desc="按 42 天周期、前瞻提前 12 天推算（4.7 于 11/11 上线）。",
         title_en="Honkai: Star Rail 4.8 Special Program",
         desc_en="Projected from the 42-day cycle, with the stream about 12 days before launch (4.7 launched Nov 11)."),
    dict(g="hsr", ver="4.8", kind="release", dt="2026-12-23 11:00", dur=30,
         title="星穹铁道 4.8 版本更新", status="est",
         desc="4.7 卡池排到 12/22 15:00，4.8 大概率 12/23 上线。",
         title_en="Honkai: Star Rail 4.8 Version Update",
         desc_en="4.7's warp ends Dec 22, 15:00, so 4.8 most likely lands on Dec 23."),
    dict(g="hsr", ver="5.0", kind="preview", dt="2027-01-22 19:30", dur=60,
         title="星穹铁道 5.0 前瞻特别节目", status="est",
         desc="推算日期，按 42 天周期。",
         title_en="Honkai: Star Rail 5.0 Special Program",
         desc_en="Projected date, based on the 42-day cycle."),
    dict(g="hsr", ver="5.0", kind="release", dt="2027-02-03 11:00", dur=30,
         title="星穹铁道 5.0 版本更新", status="est",
         desc="推算日期，按 42 天周期。",
         title_en="Honkai: Star Rail 5.0 Version Update",
         desc_en="Projected date, based on the 42-day cycle."),

    # ---------- 绝区零 ----------
    dict(g="zzz", ver="3.4", kind="preview", dt="2026-11-20 19:30", dur=90,
         title="绝区零 3.4 前瞻特别节目", status="official",
         desc="新虚狩「挽昼」登场，同时开启与崩坏：星穹铁道联动（知更鸟、卡芙卡），发 300 菲林兑换码。",
         title_en="Zenless Zone Zero 3.4 Special Program",
         desc_en="Introduces a new Void Hunter alongside a Honkai: Star Rail crossover (Robin and Kafka). "
                 "Three redemption codes worth 300 Polychrome."),
    dict(g="zzz", ver="3.4", kind="release", dt="2026-12-02 11:00", dur=30,
         title="绝区零 3.4 版本更新", status="official",
         desc="3.3 版本于 12/2 06:00 结束，3.4 同日开启。维护通常 06:00–11:00。",
         title_en="Zenless Zone Zero 3.4 Version Update",
         desc_en="Version 3.3 ends at 06:00 on Dec 2 and 3.4 starts the same day. Maintenance usually runs 06:00-11:00 (UTC+8)."),
    dict(g="zzz", ver="3.5", kind="preview", dt="2027-01-01 19:30", dur=90,
         title="绝区零 3.5 前瞻特别节目", status="est",
         desc="推算日期，按 42 天版本周期。",
         title_en="Zenless Zone Zero 3.5 Special Program",
         desc_en="Projected date, based on the 42-day cycle."),
    dict(g="zzz", ver="3.5", kind="release", dt="2027-01-13 11:00", dur=30,
         title="绝区零 3.5 版本更新", status="est",
         desc="推算日期，按 42 天版本周期。",
         title_en="Zenless Zone Zero 3.5 Version Update",
         desc_en="Projected date, based on the 42-day cycle."),

    # ---------- 鸣潮 ----------
    dict(g="wuwa", ver="3.8", kind="preview", dt="2026-11-06 19:00", dur=90,
         title="鸣潮 3.8 前瞻通讯", status="official",
         desc="官方直播间。公布 3.8 卡池与新五星「莉莉」，发 300 星声兑换码。",
         title_en="Wuthering Waves 3.8 Preview Broadcast",
         desc_en="Official livestream. Covers the 3.8 convene banners and the new 5-star, plus three codes worth 300 Astrite."),
    dict(g="wuwa", ver="3.8", kind="release", dt="2026-11-12 11:00", dur=30,
         title="鸣潮 3.8 版本更新", status="official",
         desc="11/10 开放预下载。更新后邮件领 600 星声修复补偿。",
         title_en="Wuthering Waves 3.8 Version Update",
         desc_en="Pre-download opens Nov 10. A 600-Astrite compensation arrives by in-game mail after the update."),
    dict(g="wuwa", ver="4.0", kind="preview", dt="2026-12-18 19:00", dur=90,
         title="鸣潮 4.0 前瞻通讯", status="est",
         desc="推算日期。鸣潮约 6 周一个版本，前瞻一般安排在更新前 6 天。",
         title_en="Wuthering Waves 4.0 Preview Broadcast",
         desc_en="Projected. Wuthering Waves runs roughly 6-week versions and usually holds the preview 6 days before launch."),
    dict(g="wuwa", ver="4.0", kind="release", dt="2026-12-24 11:00", dur=30,
         title="鸣潮 4.0 版本更新", status="est",
         desc="推算日期，按 6 周周期（3.8 于 11/12 上线）。",
         title_en="Wuthering Waves 4.0 Version Update",
         desc_en="Projected on the 6-week cycle (3.8 launches Nov 12)."),

    # ---------- 明日方舟：终末地 ----------
    dict(g="endfield", ver="1.7", kind="preview", dt="2026-11-17 19:30", dur=90,
         title="终末地 1.7 前瞻特别节目", status="est",
         desc="1.6 前瞻比上线早 9 天（周二），照此外推。前瞻奖励需到专题网页领，不再直邮。",
         title_en="Arknights: Endfield 1.7 Special Program",
         desc_en="The 1.6 program aired 9 days before launch (a Tuesday), so this follows the same pattern. "
                 "Preview rewards now have to be claimed on the event site - they are no longer mailed."),
    dict(g="endfield", ver="1.7", kind="release", dt="2026-11-26 11:00", dur=30,
         title="终末地 1.7 版本更新", status="tbd",
         desc="社区情报指向 11/26（周四），与 1.6 相隔 42 天。官方尚未正式公告，以官方为准。",
         title_en="Arknights: Endfield 1.7 Version Update",
         desc_en="Community reports point to Nov 26 (a Thursday), 42 days after 1.6. Not officially announced yet - "
                 "treat the official date as authoritative."),
    dict(g="endfield", ver="1.8", kind="preview", dt="2026-12-29 19:30", dur=90,
         title="终末地 1.8 前瞻特别节目", status="est",
         desc="推算日期，按 42 天周期。",
         title_en="Arknights: Endfield 1.8 Special Program",
         desc_en="Projected date, based on the 42-day cycle."),
    dict(g="endfield", ver="1.8", kind="release", dt="2027-01-07 11:00", dur=30,
         title="终末地 1.8 版本更新", status="est",
         desc="推算日期，按 42 天周期。",
         title_en="Arknights: Endfield 1.8 Version Update",
         desc_en="Projected date, based on the 42-day cycle."),

    # ---------- 异环 ----------
    dict(g="nte", ver="1.5", kind="release", dt="2026-11-05 11:00", dur=30,
         title="异环 1.5「致电，空想迷数」版本更新", status="official",
         desc="新 S 级「曳尔沐」上半、Exe 下半，新增城市物流与坦克对战。版本持续到 12/17。",
         title_en="Neverness to Everness 1.5 Version Update",
         desc_en="A new S-rank character in the first half and an EX-tier in the second half, plus a new city logistics "
                 "mode and tank battles. The version runs until Dec 17."),
    dict(g="nte", ver="1.6", kind="preview", dt="2026-12-09 19:30", dur=90,
         title="异环 1.6 前瞻特别节目", status="est",
         desc="1.5 前瞻比上线早 8 天（周三），照此外推。",
         title_en="Neverness to Everness 1.6 Special Program",
         desc_en="The 1.5 program aired 8 days before launch (a Wednesday), so this follows the same pattern."),
    dict(g="nte", ver="1.6", kind="release", dt="2026-12-17 11:00", dur=30,
         title="异环 1.6 版本更新", status="official",
         desc="1.5 的卡池与活动排期全部写到 12/17 05:59，1.6 以此接档。",
         title_en="Neverness to Everness 1.6 Version Update",
         desc_en="Every 1.5 banner and event is scheduled to end Dec 17, 05:59 (UTC+8), so 1.6 takes over from there."),

    # ---------- 燕云十六声 ----------
    dict(g="wwm", ver="2.4", kind="release", dt="2026-11-06 10:00", dur=30,
         title="燕云十六声 新赛季「南吕相和·下」+ 双枪「鸣金·霆」", status="official",
         desc="国服节点。同日开放未央城新区域「幻术森林」、新侠迹「归兮归兮」。双枪是今年第三个新武学流派。",
         title_en="Where Winds Meet - New Season (Pt. 2) + Twin Spears",
         desc_en="China server date. The same day opens a new Weiyang City area and a new questline. "
                 "Twin spears are the third new weapon style added this year."),
    dict(g="wwm", ver="2.4", kind="release", dt="2026-11-13 10:00", dur=30,
         title="燕云十六声「滹沱」大版本 + 全球一周年", status="official",
         desc="新战场区域「滹沱」、中渡桥之战主线、两名新世界 BOSS，同步开启一周年活动。国际服以此日期为准。",
         title_en="Where Winds Meet - Major Update + Global 1st Anniversary",
         desc_en="A new battlefield region, the Zhongdu Bridge main story and two new world bosses, alongside "
                 "first-anniversary events. The global release follows this date."),

    # ---------- 王者荣耀世界 ----------
    dict(g="hokw", ver="S2", kind="release", dt="2026-11-26 10:00", dur=30,
         title="王者荣耀世界 S2 赛季更新（待定）", status="tbd",
         desc="S2 体验服 11 月中上旬开测，正式服预计 11 月下旬。官方还没公布确切日期，这里是占位。",
         title_en="Honor of Kings: World - Season 2 Update (TBC)",
         desc_en="Season 2 hits the test server in mid-November and the live server is expected in late November. "
                 "No official date yet - this entry is a placeholder."),
]

STATUS_LABEL = {"official": "官方确认", "est": "预估", "tbd": "待定", "rule": "规则推算"}
STATUS_LABEL_EN = {"official": "Confirmed", "est": "Estimated", "tbd": "TBC", "rule": "Computed"}
KIND_LABEL = {"preview": "前瞻直播", "release": "版本更新", "code": "兑换码失效"}
KIND_LABEL_EN = {"preview": "Preview stream", "release": "Version update", "code": "Codes expire"}

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
    "genshin": dict(day=3, at="12:00", note="直播后第 3 天中午 12:00", note_en="12:00 on day 3 after the stream"),
    "hsr":     dict(day=1, at="23:59", note="直播次日 23:59", note_en="23:59 the day after the stream"),
    "zzz":     dict(day=2, at="23:59", note="直播后第 2 天 23:59", note_en="23:59 on day 2 after the stream"),
    "wuwa":    dict(day=2, at="23:59", note="直播后第 2 天 23:59", note_en="23:59 on day 2 after the stream"),
    "nte":     dict(day=4, at="23:59", note="直播后第 4 天 23:59", note_en="23:59 on day 4 after the stream"),
}

CODE_REWARD = {
    "genshin": "3 组码合计 300 原石，外加精锻用魔矿、大英雄的经验、摩拉",
    "hsr":     "3 组码合计 300 星琼，外加角色与光锥培养材料",
    "zzz":     "3 组码合计 300 菲林",
    "wuwa":    "3 组码合计 300 星声",
    "nte":     "3 组码合计 300 环石",
}
CODE_REWARD_EN = {
    "genshin": "Three codes worth 300 Primogems total, plus Mystic Enhancement Ore, Hero's Wit and Mora",
    "hsr":     "Three codes worth 300 Stellar Jade total, plus character and Light Cone ascension materials",
    "zzz":     "Three codes worth 300 Polychrome total",
    "wuwa":    "Three codes worth 300 Astrite total",
    "nte":     "Three codes worth 300 premium currency total",
}

CODE_ENTRY = {
    "genshin": "游戏内 设置 → 账户 → 兑换码，或米游社「兑换中心」网页",
    "hsr":     "游戏内 手机 → 右上角「···」→ 兑换码，或米哈游兑换中心网页",
    "zzz":     "游戏内 更多 → 兑换码",
    "wuwa":    "游戏内 设置 → 其他设置（扳手图标）→ 兑换",
    "nte":     "游戏内手机 → 右上角「···」→ 兑换码",
}
CODE_ENTRY_EN = {
    "genshin": "in game under Settings > Account > Redemption Code, or on the official redemption website",
    "hsr":     "in game under Phone > the ... menu (top right) > Redemption Code, or on the official redemption website",
    "zzz":     "in game under More > Redemption Code",
    "wuwa":    "in game under Settings > Other Settings (wrench icon) > Redeem",
    "nte":     "in game under Phone > the ... menu (top right) > Redemption Code",
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
        e["desc_en"] = (e.get("desc_en") or "") + "\n\nCodes expire at %s (UTC+8), %s - %d hours after the stream ends." % (
            dead.strftime("%b %d, %H:%M"), rule["note_en"], hours)

        added.append(dict(
            g=e["g"], ver=e["ver"], kind="code",
            dt=dead.strftime("%Y-%m-%d %H:%M"), dur=15,
            title="%s %s 前瞻兑换码失效" % (g["short"], e["ver"]),
            title_en="%s %s - Redemption codes expire" % (g["short_en"], e["ver"]),
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
            desc_en=("\n".join([
                "Valid %d hours: stream starts %s, codes die %s (UTC+8)." % (
                    hours, start.strftime("%b %d, %H:%M"), dead.strftime("%b %d, %H:%M")),
                "",
                CODE_REWARD_EN[e["g"]] + ".",
                "Once they expire they are gone - no reissues, no appeals.",
                "",
                "Redeem " + CODE_ENTRY_EN[e["g"]] + ".",
                "Missed the stream? The VOD description and the official preview page usually list all three codes.",
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


def _base_slug(e: dict) -> str:
    return "%s-%s-%s" % (e["g"], e["ver"].replace(".", ""), e["kind"])


# 同款同版本可能有多条同类型日程（如燕云 2.4 有两场更新）。
# UID 冲突时，最早那一条保留原 UID（已导入的不会重复），其余补日期区分。
# 注意：UID 与语言无关，中英文两版共用同一套 UID，切换语言不会产生重复日程。
_SUFFIX = set()
_seen = set()
for _e in sorted(EVENTS, key=lambda x: x["dt"]):
    _b = _base_slug(_e)
    if _b in _seen:
        _SUFFIX.add((_b, _e["dt"]))
    else:
        _seen.add(_b)


def slug(e: dict) -> str:
    b = _base_slug(e)
    if (b, e["dt"]) in _SUFFIX:
        return "%s-%s" % (b, e["dt"][:10].replace("-", ""))
    return b


def build_event(e: dict, lang: str = "zh") -> str:
    en = lang == "en"
    start = datetime.strptime(e["dt"], "%Y-%m-%d %H:%M").replace(tzinfo=BJ)
    end = start + timedelta(minutes=e["dur"])
    game = GAME_BY_ID[e["g"]]
    game_name = game["name_en"] if en else game["name"]

    title = (e.get("title_en") or e["title"]) if en else e["title"]
    desc = (e.get("desc_en") or e["desc"]) if en else e["desc"]
    labels = STATUS_LABEL_EN if en else STATUS_LABEL
    label = "" if e["status"] == "official" else (" (%s)" if en else "（%s）") % labels[e["status"]]

    if en:
        place = {"preview": " - Official stream", "release": "", "code": " - Redemption page"}[e["kind"]]
        tail = "\n".join([
            "",
            "",
            "All times are Beijing time (UTC+8).",
            "Entries marked Estimated or TBC are projected from version cycles and may shift once officially announced.",
        ])
        alarm = {
            "preview": [("-PT30M", "Special Program starts in 30 minutes")],
            "code": [("-PT2H", "Codes expire in 2 hours - redeem now if you haven't"),
                     ("-PT30M", "Codes expire in 30 minutes, no reissues")],
            "release": [("-P1D", "Version update tomorrow"),
                        ("-PT2H", "Version update - servers opening soon")],
        }[e["kind"]]
    else:
        place = {"preview": " 官方直播间", "release": "", "code": " 兑换入口"}[e["kind"]]
        tail = "\n".join([
            "",
            "",
            "时间均为北京时间 UTC+8。",
            "标注「预估 / 待定」的日期是按版本周期推算的，官方公布后会有偏差。",
        ])
        alarm = {
            "preview": [("-PT30M", "前瞻直播 30 分钟后开始")],
            "code": [("-PT2H", "兑换码 2 小时后失效，还没换的现在去换"),
                     ("-PT30M", "兑换码 30 分钟后失效，过期不补")],
            "release": [("-P1D", "明天是版本更新日"),
                        ("-PT2H", "版本更新，准备开服")],
        }[e["kind"]]

    lines = [
        "BEGIN:VEVENT",
        "UID:%s@game-version-calendar" % slug(e),
        "DTSTAMP:%s" % STAMP,
        "DTSTART:%s" % utc_str(start),
        "DTEND:%s" % utc_str(end),
        fold("SUMMARY:" + esc(title + label)),
        fold("DESCRIPTION:" + esc(desc + tail)),
        fold("LOCATION:" + esc(game_name + place)),
        fold("CATEGORIES:" + esc(game_name)),
        "STATUS:CONFIRMED",
        "TRANSP:TRANSPARENT",
    ]
    for trigger, text in alarm:
        lines += ["BEGIN:VALARM", "TRIGGER:%s" % trigger, "ACTION:DISPLAY",
                  fold("DESCRIPTION:" + esc(text)), "END:VALARM"]
    lines.append("END:VEVENT")
    return "\r\n".join(lines)


CAL_QUIT = ("不玩了：iPhone 直接删掉本日历；"
            "安卓在「日程账号管理」里关掉「显示」开关，别点删除（会连带其他订阅）。")
CAL_QUIT_EN = ("Leaving a game? On iPhone just delete that calendar. "
               "On Android, switch OFF \"show\" in Calendar account settings instead of tapping Delete - "
               "deleting one URL subscription removes all of them.")

CAL_DESC = "前瞻与版本更新的提醒。" + CAL_QUIT
CAL_DESC_EN = "Preview streams and version updates. " + CAL_QUIT_EN


def game_cal_name(g: dict, lang: str = "zh") -> str:
    return (g["short_en"] + " - Version Calendar") if lang == "en" else (g["short"] + " · 版本日历")


def game_cal_desc(g: dict, lang: str = "zh") -> str:
    if lang == "en":
        return ("Only %s previews and version updates. " % g["name_en"]) + CAL_QUIT_EN
    return ("只订阅「%s」的前瞻与版本更新。" % g["name"]) + CAL_QUIT


def page_games(lang: str = "zh"):
    """页面只需要展示字段，把另一种语言的文案剥掉，减小体积。"""
    en = lang == "en"
    return [{
        "id": g["id"],
        "name": g["name_en"] if en else g["name"],
        "short": g["short_en"] if en else g["short"],
        "ver": g["ver"],
        "color": g["color"],
    } for g in GAMES]


def page_events(lang: str = "zh"):
    en = lang == "en"
    return [{
        "g": e["g"], "ver": e["ver"], "kind": e["kind"], "dt": e["dt"],
        "dur": e["dur"], "status": e["status"],
        "title": (e.get("title_en") or e["title"]) if en else e["title"],
        "desc": (e.get("desc_en") or e["desc"]) if en else e["desc"],
    } for e in EVENTS]



def calendar(game_ids, title: str = None, desc: str = None, lang: str = "zh") -> str:
    picked = [e for e in EVENTS if e["g"] in game_ids]
    picked.sort(key=lambda e: e["dt"])
    en = lang == "en"

    if title is None:
        joined = (" & ".join if en else "、".join)
        title = ((  "Gacha Version Calendar - " if en else "二游版本日历 · ")
                 + joined(GAME_BY_ID[i]["short_en" if en else "short"]
                          for i in [g["id"] for g in GAMES if g["id"] in game_ids]))
    if desc is None:
        desc = CAL_DESC_EN if en else CAL_DESC

    head = ("BEGIN:VCALENDAR\r\nVERSION:2.0\r\n"
            "PRODID:-//WorkBuddy//Game Version Calendar//%s\r\n"
            "CALSCALE:GREGORIAN\r\nMETHOD:PUBLISH\r\n" % ("EN" if en else "CN"))
    head += fold("X-WR-CALNAME:" + esc(title)) + "\r\n"
    head += fold("X-WR-CALDESC:" + esc(desc)) + "\r\n"
    head += ("X-WR-TIMEZONE:Asia/Shanghai\r\n"
             "REFRESH-INTERVAL;VALUE=DURATION:PT6H\r\n"
             "X-PUBLISHED-TTL:PT6H\r\n")
    return head + "".join(build_event(e, lang) + "\r\n" for e in picked) + "END:VCALENDAR\r\n"
