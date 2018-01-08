# -*- coding:utf-8 -*-
import requests
from Config import *

def get_request(url):
    header = {'User-agent': USER_AGENT}
    request = requests.get(url, headers=header)
    return request;
