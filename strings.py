# -*- coding: utf-8 -*-
"""页面文案。模板里写 {{key}}，构建时按语言替换。

改文案只改这里，中英两版一起变。
JS 里要用的短文案走 js()，注入到 __UI_JSON__。
"""

UI = {
    "zh": {
        # ---- head ----
        "html_lang": "zh-CN",
        "title": "我的二游版本日历",
        "meta_desc": "勾选在玩的二游，一键把前瞻直播、版本更新、兑换码失效时间加进手机日历。",
        "lang_switch": "English",
        "lang_href": "en/",

        # ---- header ----
        "h1": "我的二游版本日历",
        "sub": "勾选你在玩的游戏，生成一份专属日历",
        "meta_v1": "更新于 2026-11-02 · 时间为北京时间 UTC+8",
        "meta_static": '静态版 · 日程最远到 <span id="latest">—</span> · 时间为北京时间 UTC+8',
        "wx_warn": '当前在微信里打开。微信不允许直接导入日历，请点右上角 <b>···</b> → <b>在浏览器打开</b> 再操作。',

        # ---- 选择区 ----
        "pick_title": "选择游戏",
        "btn_all": "全选",
        "btn_none": "清空",
        "preview_title": "日程预览",

        # ---- 怎么加 ----
        "how_title": "怎么加到自己手机上",
        "how_v1_1": "<b>iPhone</b>：用系统自带 Safari 打开本页 → 点底部黑按钮 → 弹窗点 <b>「全部添加」</b>。",
        "how_v1_2": "<b>安卓 / 华为 / 小米</b>：点黑按钮会下载 .ics 文件，再用系统日历的「导入」选中它。",
        "how_v1_3": "提醒都设好了：前瞻提前 30 分钟；兑换码失效提前 2 小时和 30 分钟；版本更新提前 1 天和 2 小时。",
        "how_v1_4": "只想长期跟着更新，就用下面那行的「订阅日历」，以后我改日历你手机自动同步。",
        "how_static_1": "<b>iPhone</b>：用 Safari 打开本页 → 点底部黑按钮。只选了一款会直接跳进日历，弹窗点 <b>「全部添加」</b>；选了好几款会下载一个文件，到「文件」App 里点开它即可。",
        "how_static_2": "<b>安卓 / 华为 / 小米</b>：点黑按钮会下载 .ics 文件，再用系统日历的「导入」选中它。",
        "how_static_3": "想长期跟着更新，别用导入，用下面的<b>订阅</b>：以后数据更新了，手机上自动同步。",
        "how_static_4": "提醒都设好了：前瞻提前 30 分钟；兑换码失效提前 2 小时和 30 分钟；版本更新提前 1 天和 2 小时。",
        "how_fine": "日程里那条「兑换码失效」，时间就是官方的截止时刻。各游戏口径不同：原神是直播后第 3 天中午 12:00，星铁是次日 23:59，绝区零和鸣潮是第 2 天 23:59，异环是第 4 天 23:59。终末地、燕云十六声、王者荣耀世界不发前瞻兑换码，所以没有这一条。",

        # ---- 订阅与取消 ----
        "sub_title": "订阅与取消",
        "sub_lead": "一个游戏一个日历。退坑了，关掉或删掉对应那一个日历，那个游戏的前瞻和更新提醒就一起没了，其他游戏照常。iPhone 可以直接删；安卓要看清下面那条红字。",
        "merge_btn": "合并订阅全部 · 一个日历",
        "sub_sh_v1": "或者分开订阅（推荐，退坑好取消）",
        "sub_sh_static": "按游戏订阅",

        "cx_hd": "取消「」的提醒",
        "cx_danger": '<b>安卓先看这条，别直接点删除。</b>很多国产日历（vivo / OPPO / 小米 / 华为）用「导入账号 · 从网址订阅」加进去的多个日历，会全部塞在同一个叫 <b>Subscription Calendar</b> 的账号下面。你在账号管理里删掉其中一个，会把<b>所有同类订阅一起删掉</b>，原神和星铁同时消失就是这么来的。这不是本站的问题，是厂商日历 App 的实现方式。安卓请按下面第 2 条做。',
        "cx_ios_plat": "iPhone / iPad",
        "cx_ios_1": '打开<b>日历</b> App，点屏幕最下方的<b>「日历」</b>按钮',
        "cx_ios_2": '<b id="cxname">原神 · 版本日历</b>，点它右边的 <b>ⓘ</b>',
        "cx_ios_3": "往下滑，点<b>删除日历</b>并确认。iOS 每个订阅是独立的，只删这一个",
        "cx_and_plat": "安卓（想单独关掉某一款）",
        "cx_and_1": "进日历 App 的<b>设置 → 日程账号管理</b>（各家叫法略有不同）",
        "cx_and_2": '点 <b id="cxname2">原神 · 版本日历</b> 那一行（这几行的标题都写「Subscription Calendar」，认下面那行小字）',
        "cx_and_3": "用里面<b>「显示」开关关掉</b>，<b>不要点「删除」</b>",
        "cx_and_4": "关掉后这个游戏的提醒立刻停，其他游戏不受影响。想真正逐个删干净，用下面说的 ICSx⁵",
        "cx_alt_plat": "不想折腾：换一个日历 App",
        "cx_alt_p": "装 <b>ICSx⁵</b>（开源免费，应用商店搜得到），每条订阅在它里面是独立日历，删哪条就删哪条，不会连带。把订阅地址粘进去即可，本站的「订阅」按钮复制出来的就是地址。",
        "cx_alt_note": "只是暂时不想被打扰，不用删：把那个日历的「显示」关掉（隐藏），提醒也会停；或者进订阅设置点「移除提醒」，日程留着。",

        "imp_import_summary": "我是「一次性导入」的，怎么取消",
        "imp_import_p": "一次性导入的日程存在你手机本地，外面够不着，只能在日历 App 里删：",
        "imp_import_1": "打开日历 App，搜索框输入游戏名，比如「原神」",
        "imp_import_2": "搜出来的每一条都能单独删（iPhone 点进去 → 删除日程；安卓长按 → 删除）",
        "imp_import_3": "嫌麻烦就改用上面的订阅，以后取消只需删一个日历",

        "imp_android_summary": '安卓怎么订阅（按钮提示"已复制"时看这里）',
        "imp_android_p1": '安卓的日历 App 不吃 <b class="k">webcal://</b> 开头的地址，所以按钮会改成复制 <b class="k">https://</b> 开头的地址。',
        "imp_android_p2": '<b>推荐做法</b>：装 <b>ICSx⁵</b>（开源免费）。打开它 → 右上角「+」→ 粘贴地址 → 保存。以后每款游戏在它里面是一个独立日历，删哪个都不会连带，也不受厂商日历的账号机制影响。',
        "imp_android_p3": "用系统日历也行，但有代价：",
        "imp_android_1": "打开日历 App，找「设置」或「添加日历」里的 <b>从网址添加</b> / <b>通过网址订阅</b>",
        "imp_android_2": "把地址粘进去，命名随便写，确认",
        "imp_android_3": "它会定期去这个网址拉最新数据。注意：这样加的多个订阅会被塞进同一个账号，删一个会全删，取消时改用「显示」开关",

        "why_fine": "为什么这里不能点一下就远程删掉？日历订阅是只读的，谁订了只有谁的手机知道。所以取消这一步只能在手机端做，我把它压到三次点击以内。",

        # ---- 静态版说明 ----
        "static_title": "这是静态版，和完整版有什么区别",
        "static_lead": "本页所有内容都由浏览器自己算，没有任何服务器参与，所以能免费挂在 GitHub Pages 上，谁都能开一份。",
        "static_1": "<b>能做的事</b>：勾选任意几款，一键生成合并的日历文件导进手机；按游戏订阅固定的一份。",
        "static_2": '<b>做不到的事</b>：给"原神 + 鸣潮"这种任意组合生成一个可订阅的网址。订阅地址只能是一个事先做好的文件，所以只有按游戏一份、和全部一份。',
        "static_3": '<b>数据怎么更新</b>：维护者改了 <b class="k">events.py</b> 并重新生成，页面和订阅文件一起变；订阅的人手机自动跟上，导入的人需要重新导一次。',
        "static_fine": "需要任意组合的订阅链接，用仓库里的完整版（Python 服务端），那边一个网址就能按你选的组合现算。",

        # ---- footer ----
        "foot1": "标「官方确认」的来自官方公告，「预估」是按版本周期推算，「待定」是官方还没公布日期。",
        "foot2": "「规则推算」是兑换码截止时刻：官方还没公布，但按每款游戏历次的口径能卡到分钟，误差一般在 1 小时内。",
        "foot3": "过期不补发，这条日程别当参考价看。",

        # ---- 底栏 ----
        "bar_meta": '已选 <b id="pn">0</b> 个游戏 · <b id="en">0</b> 条日程',
        "bar_btn": "加入手机日历",
        "bar_link": "订阅日历 · 退坑可以单独取消 ›",
    },

    "en": {
        "html_lang": "en",
        "title": "Gacha Version Calendar",
        "meta_desc": "Pick the gacha games you play and add every preview stream, version update and promo-code expiry to your phone calendar in one tap.",
        "lang_switch": "中文",
        "lang_href": "../",

        "h1": "Gacha Version Calendar",
        "sub": "Pick the games you play, get a calendar that only has what you need",
        "meta_v1": "Updated Nov 2, 2026 · All times Beijing time (UTC+8)",
        "meta_static": 'Static build · schedule runs to <span id="latest">—</span> · All times Beijing time (UTC+8)',
        "wx_warn": 'You are in the WeChat browser. WeChat will not open calendar files - tap <b>···</b> (top right) → <b>Open in browser</b> first.',

        "pick_title": "Choose games",
        "btn_all": "All",
        "btn_none": "None",
        "preview_title": "Upcoming",

        "how_title": "How to get it on your phone",
        "how_v1_1": "<b>iPhone</b>: open this page in Safari, tap the black button, then tap <b>Add All</b> in the popup.",
        "how_v1_2": "<b>Android / Huawei / Xiaomi</b>: the button downloads a .ics file - import it with your calendar app.",
        "how_v1_3": "Reminders are already set: 30 min before a stream, 2 h and 30 min before codes expire, 1 day and 2 h before a version update.",
        "how_v1_4": "To follow updates long-term, use <b>Subscribe</b> below instead - your phone syncs automatically.",
        "how_static_1": "<b>iPhone</b>: open this page in Safari and tap the black button. With one game selected it opens straight in Calendar - tap <b>Add All</b>. With several, it downloads a file: open it from the Files app.",
        "how_static_2": "<b>Android / Huawei / Xiaomi</b>: the button downloads a .ics file - import it with your calendar app.",
        "how_static_3": "To follow updates long-term, skip importing and use <b>Subscribe</b> below - your phone syncs automatically when the data changes.",
        "how_static_4": "Reminders are already set: 30 min before a stream, 2 h and 30 min before codes expire, 1 day and 2 h before a version update.",
        "how_fine": 'The "codes expire" entry is the official cut-off time exactly. The rule differs per game: Genshin noon on day 3 after the stream, Star Rail 23:59 the next day, ZZZ and WuWa 23:59 on day 2, NTE 23:59 on day 4. Endfield, Where Winds Meet and HoK: World do not hand out preview codes, so they have no such entry.',

        "sub_title": "Subscribe &amp; remove",
        "sub_lead": "One game, one calendar. If you quit a game, turn off or delete just that calendar and its reminders go away while the rest keep working. iPhone can delete directly; on Android read the red box below first.",
        "merge_btn": "Merge everything - one calendar",
        "sub_sh_v1": "Or subscribe per game (recommended, easier to drop)",
        "sub_sh_static": "Subscribe per game",

        "cx_hd": "Stop reminders for",
        "cx_danger": '<b>Android: read this before deleting anything.</b> Many Chinese calendar apps (vivo / OPPO / Xiaomi / Huawei) put every URL subscription you add under a single account called <b>Subscription Calendar</b>. Deleting one of them there <b>deletes all of them at once</b> - that is why Genshin and Star Rail vanished together. This is how the vendor app works, not a bug in this site. On Android, use step 2 below.',
        "cx_ios_plat": "iPhone / iPad",
        "cx_ios_1": 'Open the <b>Calendar</b> app and tap <b>Calendars</b> at the bottom',
        "cx_ios_2": 'Find <b id="cxname">Genshin - Version Calendar</b> and tap the <b>ⓘ</b> next to it',
        "cx_ios_3": "Scroll down, tap <b>Delete Calendar</b> and confirm. Every iOS subscription is independent, so only this one goes away",
        "cx_and_plat": "Android (turn off a single game)",
        "cx_and_2": 'Tap the <b id="cxname2">Genshin - Version Calendar</b> row (the titles all read "Subscription Calendar" - match the small text underneath)',
        "cx_and_1": "Open your calendar app: <b>Settings → Calendar accounts</b> (names vary by vendor)",
        "cx_and_3": "Switch <b>\"show\" off</b> - <b>do not tap Delete</b>",
        "cx_and_4": "Reminders for that game stop immediately and nothing else is affected. To delete them properly one by one, use ICSx⁵ below",
        "cx_alt_plat": "Not worth the hassle: use a different calendar app",
        "cx_alt_p": "Install <b>ICSx⁵</b> (open source, free, on every app store). Each subscription becomes an independent calendar there, so deleting one never touches the others. Just paste the subscribe URL - the Subscribe button copies it for you.",
        "cx_alt_note": "Only want some quiet? You do not have to delete anything: switch that calendar's visibility off and reminders stop too, or hit \"remove alerts\" in the subscription settings and keep the events.",

        "imp_import_summary": "I imported the file once - how do I undo it?",
        "imp_import_p": "Imported events live on your phone, so nothing on my side can reach them. Delete them in the calendar app:",
        "imp_import_1": "Open your calendar app and search for the game name",
        "imp_import_2": "Each result can be deleted on its own (iPhone: tap in → Delete Event; Android: long-press → Delete)",
        "imp_import_3": "Or switch to subscribing instead - then removing a game means deleting one calendar",

        "imp_android_summary": 'How to subscribe on Android (when the button says "copied")',
        "imp_android_p1": 'Android calendar apps do not accept <b class="k">webcal://</b> links, so the button copies an <b class="k">https://</b> URL instead.',
        "imp_android_p2": "<b>Recommended</b>: install <b>ICSx⁵</b> (open source, free). Open it → <b>+</b> (top right) → paste the URL → save. Every game becomes its own calendar, deleting one never affects the others, and you dodge the vendor account behaviour entirely.",
        "imp_android_p3": "The built-in calendar app works too, with a catch:",
        "imp_android_1": 'Open the calendar app and find <b>Add calendar from URL</b> / <b>Subscribe by URL</b> in settings',
        "imp_android_2": "Paste the URL, name it whatever you like, confirm",
        "imp_android_3": "It re-fetches the URL periodically. Note that subscriptions added this way all land in one account, so deleting one deletes all - turn off \"show\" instead when you stop playing a game",

        "why_fine": "Why can't this page just delete it remotely? Calendar subscriptions are read-only - only your own phone knows what you subscribed to. So removal has to happen on your device. I kept it to three taps.",

        "static_title": "This is the static build - how is it different?",
        "static_lead": "Everything on this page is computed in your browser, with no server involved, so it can live on GitHub Pages for free and anyone can host a copy.",
        "static_1": "<b>What works</b>: tick any set of games and download one merged .ics file for your phone; subscribe per game to a pre-built file.",
        "static_2": "<b>What does not</b>: a subscribable URL for an arbitrary mix like \"Genshin + WuWa\". A subscription URL has to point at a file made in advance, so you get one per game plus one for everything.",
        "static_3": '<b>How data updates</b>: the maintainer edits <b class="k">events.py</b> and rebuilds - page and subscriptions change together. Subscribers sync automatically; people who imported need to import again.',
        "static_fine": "Need a subscribe link for a custom mix? Use the full version in the repo (a small Python server) - there the URL is generated from whatever you pick.",

        "foot1": "Confirmed comes from official announcements, Estimated is projected from the version cycle, TBC means no date announced yet.",
        "foot2": "Computed is the code expiry time: not announced officially, but derived from each game's past record to the minute - usually within an hour.",
        "foot3": "Expired codes are never reissued, so do not treat that entry as a price reference.",

        "bar_meta": '<b id="pn">0</b> games · <b id="en">0</b> events',
        "bar_btn": "Add to phone calendar",
        "bar_link": "Subscribe · drop one game anytime ›",
    },
}

# JS 运行时用到的短文案
JS = {
    "zh": {
        "week": ["周日", "周一", "周二", "周三", "周四", "周五", "周六"],
        "empty": "至少选一个游戏",
        "pick_first": "先选一个游戏",
        "add_btn": "加入手机日历（%d 条）",
        "sorted": "按时间排序",
        "kind_code": "兑换码",
        "suf_release": " 开服",
        "suf_code": " 失效",
        "suf_preview": " 开播",
        "current": "当前 %s",
        "sub": "订阅",
        "cancel": "取消",
        "sub_count": "%d 条",
        "all_label": "全部游戏 · 一个日历",
        "cal_suffix": " · 版本日历",
        "cal_prefix": "二游版本日历 · ",
        "cal_join": "、",
        "cx_title": "取消「%s」的提醒",
        "toast_ios": "已生成 %d 条，去「文件」App 点开它",
        "toast_gen": "已生成 %d 条，选「日历」打开",
        "toast_copy": "订阅地址已复制，去日历 App「从网址添加」粘贴",
        "file_one": "%s-版本日历.ics",
        "file_many": "二游版本日历-%d款.ics",
        "label_wrap": "（%s）",
        "prodid": "CN",
        "cal_desc": "前瞻与版本更新的提醒。不玩了：iPhone 直接删掉本日历；安卓在「日程账号管理」里关掉「显示」开关，别点删除（会连带其他订阅）。",
        "ics_tail": "\n\n时间均为北京时间 UTC+8。\n标注「预估 / 待定」的日期是按版本周期推算的，官方公布后会有偏差。",
        "loc": {"preview": " 官方直播间", "release": "", "code": " 兑换入口"},
        "alarm": {"preview": ["前瞻直播 30 分钟后开始"],
                  "code": ["兑换码 2 小时后失效，还没换的现在去换", "兑换码 30 分钟后失效，过期不补"],
                  "release": ["明天是版本更新日", "版本更新，准备开服"]},
    },
    "en": {
        "week": ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"],
        "empty": "Pick at least one game",
        "pick_first": "Pick a game first",
        "add_btn": "Add to phone calendar (%d)",
        "sorted": "Sorted by date",
        "kind_code": "Codes",
        "suf_release": " live",
        "suf_code": " expires",
        "suf_preview": " starts",
        "current": "Current %s",
        "sub": "Subscribe",
        "cancel": "Remove",
        "sub_count": "%d events",
        "all_label": "All games - one calendar",
        "cal_suffix": " - Version Calendar",
        "cal_prefix": "Gacha Version Calendar - ",
        "cal_join": " & ",
        "cx_title": "Stop reminders for %s",
        "toast_ios": "Created %d events - open the file from the Files app",
        "toast_gen": "Created %d events - choose Calendar to open it",
        "toast_copy": "Subscribe URL copied - paste it into your calendar app",
        "file_one": "%s-Version-Calendar.ics",
        "file_many": "Gacha-Version-Calendar-%d-games.ics",
        "label_wrap": " (%s)",
        "prodid": "EN",
        "cal_desc": "Preview streams and version updates. Leaving a game? On iPhone just delete that calendar. On Android, switch OFF \"show\" in Calendar account settings instead of tapping Delete - deleting one URL subscription removes all of them.",
        "ics_tail": "\n\nAll times are Beijing time (UTC+8).\nEntries marked Estimated or TBC are projected from version cycles and may shift once officially announced.",
        "loc": {"preview": " - Official stream", "release": "", "code": " - Redemption page"},
        "alarm": {"preview": ["Special Program starts in 30 minutes"],
                  "code": ["Codes expire in 2 hours - redeem now if you haven't", "Codes expire in 30 minutes, no reissues"],
                  "release": ["Version update tomorrow", "Version update - servers opening soon"]},
    },
}


def render(tpl: str, lang: str, *extra: tuple) -> str:
    """把模板里的 {{key}} 换成该语言的文案。extra 是额外注入的 (key, html)。"""
    table = dict(UI[lang])
    table.update(dict(extra))
    out = tpl
    for k, v in table.items():
        out = out.replace("{{%s}}" % k, v)
    # 漏掉的占位符直接报错，免得线上出现 {{xxx}}
    if "{{" in out:
        import re
        missing = sorted(set(re.findall(r"\{\{(\w+)\}\}", out)))
        raise KeyError("%s 版模板缺少文案: %s" % (lang, ", ".join(missing) or "（见模板里的 {{ }}）"))
    return out
