#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 18:43:52 2020

@author: Danni
"""
import urllib.request
import logging

def requestURL(url, crawl_timeout, num_retries):
    """
    send request to given url

    Parameters
    ----------
    url : string
        requested url.
    crawl_timeout : int
        timeout value.
    num_retries : int
        try xx times.

    Returns
    -------
    object
        url page.

    """
    target = ' '
    headerstr = ['Mozilla/5.0 (Windows NT 6.1; Win64; x64)', 
                'AppleWebKit/537.36 (KHTML, like Gecko)', 
                'Chrome/62.0.3202.62 Safari/537.36']
    headers = {'User-Agent': target.join(headerstr)}
    try:
        url = url.replace(' ', '')
        req = urllib.request.Request(url=url, headers=headers)
        page = urllib.request.urlopen(req, timeout=int(crawl_timeout)).read()
    except urllib.request.URLError as e:
        page = None
        if num_retries > 0:
            if hasattr(e, 'code') and 300 <= e.code:
                logging.info("retry: %s" % num_retries)
                logging.info("e.code: %s" % e.code)
                return requestURL(url, crawl_timeout, num_retries-1)
    return page
