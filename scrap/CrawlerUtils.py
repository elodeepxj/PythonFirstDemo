# -*- coding:utf-8 -*-
import DownloadUtils
import re
import itertools
import urlparse


# 网站地图爬虫
def crawl_sitemap(url, proxy=True):
    sitemap = DownloadUtils.download(url, proxy=proxy)
    links = re.findall("<a href=\"(.*?)\">", sitemap)
    print links
    for link in links:
        html = DownloadUtils.download("http://example.webscraping.com" + link, proxy=proxy)


# id遍历爬虫
def id_crawler():
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


# 链接爬虫
def link_crawler(seed_url, link_regex, max_depth=2):
    max_depth = 2
    seen = {}
    depth = seen[seed_url]

    crawl_queue = [seed_url]
    seen = set(crawl_queue)
    while crawl_queue:
        url = crawl_queue.pop()
        html = DownloadUtils.download(url)
        for link in get_links(html):
            if re.match(link_regex, link):
                link = urlparse.urljoin(seed_url, link)
                if link not in seen:
                    seen.add(link)
                    crawl_queue.append(link)


def get_links(html):
    webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    return webpage_regex.findall(html)
