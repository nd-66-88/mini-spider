#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 16:46:40 2020

@author: Danni
"""
import logging
import threading
import re
import time
import ssl
import urllib.request
import urllib.parse

import save_file as saveFile
import request_URL as requestURL
import HTMLParser

ssl._create_default_https_context = ssl._create_unverified_context
threadLock = threading.Lock()
class Spiderx(threading.Thread):
    """
    Spiderx inherits from threading.Thread 
    """
    def __init__(self, url_list, output_directory, max_depth, crawl_interval, 
                 crawl_timeout, target_url, thread_count, wrongurl, seenurl):
        """
        gets parameters from spider.conf
        """
        threading.Thread.__init__(self)
        self.wrongurl = wrongurl
        self.unseenurl= url_list
        self.seenurl = seenurl
        self.output_directory = output_directory
        self.max_depth = max_depth
        self.crawl_interval = crawl_interval
        self.crawl_timeout = crawl_timeout
        self.target_url = target_url
        self.thread_count = thread_count
        self.newException = True
        
    def run(self):
        """
        run threads
        """
        time.sleep(int(self.crawl_interval))
        
        crawler(self.thread_count, self.target_url, self.unseenurl, 
                self.crawl_timeout, self.seenurl, self.max_depth, 
                self.output_directory, self.wrongurl, self.newException)
        


def getEncoding(page):
    if isinstance(page,str):
        return "unicode"
    try:
        page.decode("utf-8")
        return 'utf-8'
    except:
        pass
    try:
        page.decode("gbk")
        return 'gbk'
    except:
        pass
        

def crawler(thread_count, target_url, allurls, crawl_timeout, seenurl, 
            max_depth, output_directory, wrongurl, newException): 
    """
    traverse all the given urls and save files which match the given pattern

    Parameters
    ----------
    thread_count : int
        thread number.
    target_url : string
        pattern that the target webpage/image should match 
    allurls : queue
        all the urls that this program should visit.
    crawl_timeout : int
        time out after ** seconds.
    seenurl : set
        all the urls that this program has visited.
    max_depth : int
        max depth.
    output_directory : string
        the directory where images and webpages will store
    wrongurl : set
        exception raised when visiting this urls.
    newException : bool
        if any new exception has occurred.

    Returns
    -------
    None.

    """
    logging.info('%s crawler start' % str(thread_count))
    try:
        #BFS
        while allurls.qsize() > 0 and newException == True:
            threadLock.acquire()
            pageurllist = allurls.get()
            threadLock.release()
            depth = pageurllist[1]
            pageurl = pageurllist[0]
            is_legal_url = re.match(r'^https?://\w.+$', pageurl, flags=0)
            if is_legal_url is None:
                continue
            if int(depth) <= int(max_depth):
                if pageurl not in wrongurl:
                    if pageurl not in seenurl:
                        m = re.match(target_url, pageurl, flags=0)
                        if m is not None:
                            path = saveFile.saveFile(pageurl, output_directory)
                            logging.info("%s is saved to : %s" % (pageurl, path))
                            threadLock.acquire()
                            seenurl.add(pageurl)
                            threadLock.release()
                        #request url. retry if error occurs
                        page = requestURL.requestURL(pageurl, crawl_timeout, 3)   
                        if page is None:
                            continue
                        threadLock.acquire()
                        seenurl.add(pageurl)
                        threadLock.release()
                        page_encoding = getEncoding(page)
                        if page_encoding is None:
                            continue
                        parser = HTMLParser.MyHTMLParser()
                        parser.feed(page.decode(page_encoding, errors='ignore'))
                        if len(parser.output_list) > 0:
                            depth = depth + 1
                            for d in parser.output_list:
                                if(d not in seenurl):
                                    newurl = urllib.parse.urljoin(pageurl, d)
                                    threadLock.acquire()
                                    allurls.put([newurl, depth])
                                    threadLock.release()
        newException = False
    except Exception as e:
        threadLock.acquire()
        wrongurl.add(pageurl)
        seenurl.add(pageurl)
        threadLock.release()
        logging.error('Exception: %s' % e)
        time.sleep(1)
        newException = True
        pass
    
