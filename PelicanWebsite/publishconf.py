# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

sys.path.append(os.curdir)

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITENAME = 'Primary Care Demand and Capacity Modelling'
SITEURL = "http://snee-ics.github.io/primarycaredemandandcapacity"
RELATIVE_URLS = False

FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"

DELETE_OUTPUT_DIRECTORY = True
THEME = "snee_theme"
DELETE_OUTPUT_DIRECTORY = True
PATH = 'content'
TIMEZONE = 'GMT'
STATIC_PATHS = ['img','extras']
PAGE_PATHS = ['notebooks-html']
PAGE_ORDER_BY = 'order'
ARTICLE_ORDER_BY = 'order'

# Following items are often useful when publishing

# DISQUS_SITENAME = ""
# GOOGLE_ANALYTICS = ""