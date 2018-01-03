# -*- coding:utf-8 -*-

import builtwith
import whois
import DownloadUtils

from scrap.Throttle import Throttle

builtwith.parse('http://example.webscraping.com')  # 识别网站技术
whois.whois('http://www.runoob.com/cplusplus/cpp-pointers.html')  # 寻找网站持有者

# DownloadUtils.download("http://meetup.com")
url = "http://example.webscraping.com/sitemap.xml"
seed_url = "http://example.webscraping.com"

# crawl_sitemap(url)

# id_crawler(url)

seed_url = "http://example.webscraping.com"
url1 = "http://example.webscraping.com/index/1"
url2 = "http://example.webscraping.com/index/2"

# link_crawler(seed_url, '/(index|view)')

# 下载限速
# throttle = Throttle(2000)
# throttle.wait(seed_url)
# result = DownloadUtils.download()
