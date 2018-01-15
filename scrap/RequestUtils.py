# -*- coding:utf-8 -*-
import requests
from Config import *


def get_request(url, retries=2):
    header = {'User-agent': USER_AGENT}
    try:
        request = requests.get(url, headers=header)
    except requests.exceptions.ConnectionError as e:
        if (retries > 0):
            get_request(url, retries - 1)

    return request;
