# Scrapy settings for darazscraper project
import os
from decouple import AutoConfig

BOT_NAME = "darazscraper"

SPIDER_MODULES = ["darazscraper.spiders"]
NEWSPIDER_MODULE = "darazscraper.spiders"

# Build paths inside the project like this: BASE_DIR / 'subdir'.
ENV_BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ENV_FILE = os.path.join(ENV_BASE_DIR, '..', '.env')

config = AutoConfig(search_path=ENV_FILE)

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = "darazscraper (+http://www.yourdomain.com)"
SCRAPEOPS_API_KEY = config('SCRAPEOPS_API_KEY')
SCRAPEOPS_FAKE_USER_AGENT_ENDPOINT = config(
    'SCRAPEOPS_FAKE_USER_AGENT_ENDPOINT')
SCRAPEOPS_FAKE_USER_AGENT_ENABLED = config(
    'SCRAPEOPS_FAKE_USER_AGENT_ENABLED', default=True, cast=bool)
SCRAPEOPS_NUM_RESULTS = 50

# Obey robots.txt rules
ROBOTSTXT_OBEY = config('ROBOTSTXT_OBEY', default=False, cast=bool)

# File path of proxy list
ROTATING_PROXY_LIST_PATH = 'proxy_list.txt'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    "darazscraper.middlewares.DarazscraperSpiderMiddleware": 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    # Fake Browser Header Middleware
    'darazscraper.middlewares.ScrapeOpsFakeBrowserHeaderAgentMiddleware': 400,
    # Proxy Rotation Middleware
    'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
    'rotating_proxies.middlewares.BanDetectionMiddleware': 620,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    "darazscraper.pipelines.DarazscraperPipeline": 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = "httpcache"
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
