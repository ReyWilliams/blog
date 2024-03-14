from datetime import datetime

AUTHOR = 'Rey Williams'
SITENAME = "Rey's Corner"
SITEURL = ""
SITELOGO = '/images/profile.png'


PATH = "content"

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'English'

STATIC_PATHS = [
    "images",
]


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Web Resume", "https://web.reywilliams.com"),

)

# Social widget
SOCIAL = (
    ("LinkedIn", "https://www.linkedin.com/in/rey-williams"),
    ("GitHub", "https://github.com/ReyWilliams/"),

)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True


CC_LICENSE = {
    "name": "Creative Commons Attribution-ShareAlike",
    "version": "4.0",
    "slug": "by-nc"
}
COPYRIGHT_NAME = 'Rey Williams'
COPYRIGHT_YEAR = datetime.now().year

THEME_COLOR = 'dark'
THEME_COLOR_ENABLE_USER_OVERRIDE = True
PYGMENTS_STYLE = 'emacs'
PYGMENTS_STYLE_DARK = 'monokai'

MENUITEMS = (
    ("Archives", "/archives.html"),
    ("Categories", "/categories.html"),
    ("Tags", "/tags.html"),
)