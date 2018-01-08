# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import RequestUtils


def get_beautiful_soup(url):
    print url;
    request = RequestUtils.get_request(url)
    soup = BeautifulSoup(request.content.decode('utf-8', 'ignore'), 'lxml')
    return soup
