AUTHOR = 'Hunter M'
SITENAME = 'Horseworld Users Blog'
SITEURL = "blog.horseworld.ca"

PORT = 8080
BIND = '192.168.224.20'
TIMEZONE = 'America/Vancouver'

ARTICLE_PATHS       =   ['', '$HOME/public_html']

ARTICLE_EXCLUDES    =   ['pages', 'static', 'images', 'img',                         
                        '$HOME/public_html/pages', '$HOME/public_html/static',
                        '$HOME/public_html/img', '$HOME/public_html/images']

PAGE_PATHS          =   ['pages', '$HOME/public_html/pages']

PAGE_EXCLUDES       =   ['static', 'images', 'img',
                        '$HOME/public_html/static', '$HOME/public_html/img',
                        '$HOME/public_html/images']

STATIC_PATHS        =   ['images', 'img', 'static', 
                        '$HOME/public_html/images', '$HOME/public_html/img',
                        '$HOME/public_html/static']

THEME_STATIC_PATHS  =   ['static', '$HOME/public_html/static']
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
    ("Guestbook", "http://www.horseworld.ca/"),
    ("Files", "http://files.horseworld.ca/"),
    ("Info", "http://info.horseworld.ca/"),
    ("Secure", "https://secure.horseworld.ca/"),
    ("PHP", "http://php.horseworld.ca/"),
]


# Social widget
SOCIAL = [
    ("GitHub", "https://github.com/hunterjpg/Example_StaticSite")
]

DEFAULT_PAGINATION = False
# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
