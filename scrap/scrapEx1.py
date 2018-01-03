# -*- coding:utf-8 -*-

import builtwith
import whois
import DownloadUtils
import re
import itertools

builtwith.parse('http://example.webscraping.com')  # 识别网站技术
whois.whois('http://www.runoob.com/cplusplus/cpp-pointers.html')  # 寻找网站持有者

# DownloadUtils.download("http://meetup.com")
url = "http://example.webscraping.com/sitemap.xml"
seed_url = "http://example.webscraping.com"


# 网站地图爬虫
def crawl_sitemap(url):
    sitemap = DownloadUtils.download(url)
    links = re.findall("<a href=\"(.*?)\">", sitemap)
    print links
    for link in links:
        html = DownloadUtils.download("http://example.webscraping.com" + link)


# crawl_sitemap(url)

# id遍历爬虫
def id_crawler(url):
    max_error = 5
    num_error = 0
    for page in itertools.count(1):
        url = "http://example.webscraping.com/view/%d" % page
        print url
        html = DownloadUtils.download(url)
        if html is None:
            num_error += 1
            if num_error == max_error:
                break
        else:
            num_error = 0


# id_crawler(url)

# 链接爬虫
def link_crawler(seed_url, link_regex):
    crawl_queue = [seed_url]
    while crawl_queue:
        url = crawl_queue.pop()
        html = DownloadUtils.download(url)
        for link in get_links(html):
            if re.match(link_regex, link):
                crawl_queue.append(link)


def get_links(html):
    webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    return webpage_regex.findall(html)


seed_url = "http://example.webscraping.com"
url1 = "http://example.webscraping.com/index/1"
url2 = "http://example.webscraping.com/index/2"

link_crawler(seed_url, '/(index|view)')
