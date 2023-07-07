# ambrevar
c.auto_save.session = True
c.session.default_name = "default"
c.completion.shrink = True
c.confirm_quit = ["downloads"]
c.content.cache.size = 5242880
c.content.pdfjs = True
c.content.blocking.method = "both"
c.content.blocking.whitelist = ['www.googleadservices.com']
c.downloads.location.directory = "~/Downloads"
c.downloads.location.prompt = True
c.downloads.location.remember = True
c.downloads.remove_finished = 0 #milliseconds
c.hints.scatter = False
c.hints.uppercase = True
c.input.partial_timeout = 2000
c.tabs.tabs_are_windows = False
c.new_instance_open_target = "tab"
# c.colors.webpage.preferred_color_scheme = "light"

# c.window.title_format = "{title}{title_sep}{host}"

# lazy_restore does not work when idle.
c.session.lazy_restore = True

c.content.notifications.enabled = True

config.bind('ye', ':spawn emacsclient --eval "(kill-new \\"{url}\\")"', mode='normal')
config.bind(',r', ':spawn emacsclient --eval "(github-pull-readme \\"{url}\\")"', mode='normal')
config.bind(',l', ':spawn emacsclient "org-protocol://store-link?url={url}" ', mode='normal')
config.bind(',c', ':spawn emacsclient "org-protocol://capture?url={url}" ', mode='normal')

# config.bind('tb', 'config-cycle statusbar.hide true false')
# config.bind("tt", 'config-cycle tabs.show never always')
config.bind('<Alt-l>', 'tab-next')
config.bind('<Alt-h>', 'tab-prev')
config.bind('J', 'scroll-page 0 1')
config.bind('K', 'scroll-page 0 -1')
config.bind('<Space><Space>', 'set-cmd-text :')

config.bind("u", 'undo --window')
config.bind(',,', 'mode-enter passthrough', mode='normal')
config.bind(',,', 'mode-enter normal', mode='passthrough')
config.bind('<Ctrl-Space>', 'toggle-selection', mode='caret')

config.bind('<Escape>', 'mode-enter normal')
# config.bind(',v',':spawn vlc {url}', mode='normal')
config.bind(',v', ':spawn mpv {url}', mode='normal')


config.bind('<Ctrl-Escape>', 'mode-enter normal' , mode='passthrough')

# config.bind(',p', 'spawn --userscript qute-pass --dmenu-invocation dmenu --password-only', mode='insert')
config.bind('<Space>t', 'spawn --userscript translate', mode='normal')
config.bind(';t', 'hint userscript link translate')
config.bind(';T', 'hint userscript all translate --text')

c.tabs.position = "top"
c.tabs.show = "switching"
c.tabs.show_switching_delay = 2000
c.tabs.new_position.unrelated = "next"
# c.tabs.max_width = 0

c.url.default_page = "https://google.com/"


c.url.searchengines = {
    'DEFAULT': "https://google.com/search?q={}",
    'xyz'    : "https://searx.fmac.xyz/?q={}",
    'duck'   : 'https://duckduckgo.com/?q={}',
    'wa'     : 'https://wiki.archlinux.org/?search={}',
    "so"     : "http://stackoverflow.com/search?q={}",
    "ex"     : "https://examine.com/search/?q={}",
    "leo"    : "http://dict.leo.org/frde/index_de.html#/search={}",
    "aur"    : "https://aur.archlinux.org/packages?O=0&K={}",
    "yt"     : "http://www.youtube.com/results?search_query={}",
    "goo"    : "https://www.google.com/search?q={}",
    'gg'     : 'https://g4gsearch.com/ws/search/search?a=true&c=%7B%7D&e=true&m&p=1&q={}&s=_score&w=%5B%5D',
    'wi'     : 'https://en.wikipedia.org/wiki/{}',
    "clja"   : 'https://clojars.org/search?q={}',

    "gsm"    : 'https://www.gsmarena.com/res.php3?sSearch={}'

    # 'un'     : 'https://docs.unity3d.com/ScriptReference/30_search.html?q={}',
    # 'glab'   : 'https://gitlab.botogames.com/search?search={}',
    # 'drive'  : 'https://drive.google.com/drive/search?q={}',
    # 'jir'    : 'https://singularitygroup.atlassian.net/issues/?jql=text~'
    
}


c.editor.command = ['emacsclient', "--eval", "(progn (find-file-other-window \"{file}\") (markdown-mode))" ]

config.load_autoconfig(True)
