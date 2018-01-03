# -*- coding:utf-8 -*-


# 下载网页
import urllib2
import urlparse


def download(url, user_agent='wswp', proxy=None, num_retries=2):
    """
    :param url:下载地址
    :param user_agent:用户代理
    :param proxy:代理
    :param num_retries: 重新下载次数
    :return:
    """
    print "download:", url
    headers = {'User-agent': user_agent}
    request = urllib2.Request(url, headers=headers)

    opener = urllib2.build_opener()
    if proxy:
        proxy_params = {urlparse.urlparse(url).scheme: proxy}
        opener.add_handler(urllib2.ProxyHandler(proxy_params))
    try:
        html = opener.open(request).read()
        html = urllib2.urlopen(request).read()
    except urllib2.URLError as e:
        print e.reason
        html = None
        if (num_retries > 0):  # 重新下载
            if hasattr(e, 'code') and 500 <= e.code < 600:
                return download(url, user_agent, proxy, num_retries - 1)
    return html
