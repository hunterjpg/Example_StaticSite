AUTHOR = 'Hunter M'
SITENAME = 'Horseworld Users Blog'
SITESUBTITLE = 'Personal Blogs for Horseworld Users'
SITEURL = "http://blog.horseworld.ca"
GITHUB_URL = "https://github.com/hunterjpg/Example_StaticSite"


PORT = 8080
BIND = '192.168.224.20'
TIMEZONE = 'America/Vancouver'
DEFAULT_DATE = (2026, 10, 20, 14, 1, 1)

ARTICLE_PATHS       =   ['', '/home/*/public_html']

ARTICLE_EXCLUDES    =   ['pages', 'static', 'images', 'img',                         
                        '/home/*/public_html/pages', '/home/*/public_html/static',
                        '/home/*/public_html/img', '/home/*/public_html/images']

PAGE_PATHS          =   ['pages', '$HOME/public_html/pages']

PAGE_EXCLUDES       =   ['static', 'images', 'img',
                        '/home/*/public_html']

STATIC_PATHS        =   ['theme', 'images', 'img', 'static', 'static/',
                        '/home/*/public_html/images', '/home/*/public_html/img',
                        '/home/*/public_html/static']

THEME_STATIC_PATHS  =   ['theme', 'static', '/static', '/home/*/public_html/static']
OUTPUT_PATH = 'html'
#THEME = 'html/theme'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = [
    ("Main Portal", "http://portal.horseworld.ca/"),
    ("User Pages", "http://users.horseworld.ca/"),
    ("Files", "http://files.horseworld.ca/"),
    ("Info", "http://info.horseworld.ca/"),
    ("Secure", "https://secure.horseworld.ca/"),
    ("PHP", "http://php.horseworld.ca/"),

    ("Alternate Frontpage", "http://www.horseworld.ca/"),
    ("Restricted Area", "http://restricted.horseworld.ca/"),
    ("Secure Admin", "http://admin.horseworld.ca/"),
    ("Webapp", "http://app.horseworld.ca/"),
    ("Blogs", "http://app.horseworld.ca/"),
]


# Social widget
SOCIAL = [
    ("GitHub", "https://github.com/hunterjpg/"),
    ("Other", "#"),
]

DEFAULT_PAGINATION = False
# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
