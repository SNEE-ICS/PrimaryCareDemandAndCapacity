AUTHOR = 'A.Jarman & I.Khan'
SITENAME = 'Primary Care Demand and Capacity Modelling'
SITEURL = "http://snee-ics.github.io/primarycaredemandandcapacity"

PATH = "content"

TIMEZONE = 'GMT'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("NHS", "https://www.nhs.uk/"),
    ("Suffolk County Council", "https://www.suffolk.gov.uk/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/")
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = False
THEME = "snee_theme"
STATIC_PATHS = ['img','extras']
PAGE_PATHS = ['notebooks-html']

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True