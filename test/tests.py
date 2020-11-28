#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 20:40:13 2020

@author: Danni
"""
import unittest
import os
import urllib.parse
import urllib.request
import argparse
import sys
sys.path.append("..") 

import save_file as saveFile
import request_URL as requestURL
import read_configs as readconfigs

ps = argparse.ArgumentParser(usage='mini crawler program', 
                                 add_help=True, 
                                 description='This is a crawler program', 
                                 epilog=None, 
                                 formatter_class=argparse.HelpFormatter)
conf_file = '../conf/test.conf'
ps.add_argument('-c', '--configuration', action='store', default=conf_file)
params = ps.parse_args()
class SaveFileTest(unittest.TestCase):
    """
    unit test
    """
        
    def test_savefile(self):
        """
        save url to see if this program functions well

        Returns
        -------
        None.

        """
        pageurl = 'https://www.runoob.com/html/html-tutorial.html'
        output_directory = '../output'
        quoteurl = urllib.parse.quote(pageurl).replace('/', '_')
        expected_path = os.path.join(output_directory, quoteurl)
        filepath = saveFile.saveFile(pageurl, output_directory)
        self.assertEqual(filepath, expected_path)
        
class RequestURLTest(unittest.TestCase):
    """
    unit test
    """
    def test_requestURL(self):
        """
        send request to given url

        Returns
        -------
        None.

        """
        pageurl = 'https://www.runoob.com/html/html-tutorial.html'
        target = ' '
        headerstr = ['Mozilla/5.0 (Windows NT 6.1; Win64; x64)', 
                'AppleWebKit/537.36 (KHTML, like Gecko)', 
                'Chrome/62.0.3202.62 Safari/537.36']
        headers = {'User-Agent': target.join(headerstr)}
        req = urllib.request.Request(url=pageurl, headers=headers)
        expected_page = urllib.request.urlopen(req, timeout=5).read()
        page = requestURL.requestURL(pageurl, 5, 3)
        self.assertEqual(page, expected_page)



class readConfigsTest(unittest.TestCase):
    """
    unit test
    """
    
    def test_getURLList(self):
        """
        get url list from test.conf

        Returns
        -------
        None.

        """
        urllist = readconfigs.getURLList(params)
        expected_urllist = set()
        expected_urllist.add('http://www.baidu.com')
        expected_urllist.add('http://cup.baidu.com/spider/')
        expected_urllist.add('http://www.sina.com.cn')
        newset = set()
        # self.assertEqual(urllist, expected_urllist)
        while urllist.qsize() > 0:
            urlpair = urllist.get()
            url = urlpair[0]
            depth = urlpair[1]   
            self.assertEqual(depth, 0)
            newset.add(url)
        self.assertEqual(newset, expected_urllist)
                
    def test_getOutputDirectory(self):
        """
        get output dir from test.conf

        Returns
        -------
        None.

        """
        expected_outputdir = '../test_output'
        outputdir = readconfigs.getOutputDirectory(params)
        self.assertEqual(outputdir, expected_outputdir)
            
    def test_getMaxDepth(self):
        """
        get max depth from test.conf

        Returns
        -------
        None.

        """
        expected_depth = '5'
        depth = readconfigs.getMaxDepth(params)
        self.assertEqual(depth, expected_depth)
        
    def test_getCrawlInterval(self):
        """
        get crawl interval from test.conf

        Returns
        -------
        None.

        """
        expected_interval = '1'
        interval = readconfigs.getCrawlInterval(params)
        self.assertEqual(interval, expected_interval)
    
    def test_getTimeOut(self):
        """
        get timeout from test.conf

        Returns
        -------
        None.

        """
        expected_timeout = '10'
        timeout = readconfigs.getTimeOut(params)
        self.assertEqual(timeout, expected_timeout)
    
    def test_getTargetURL(self):
        """
        get target url from test.conf

        Returns
        -------
        None.

        """
        expected_targetURL = '.*\.(html|gif|bmp|png|jpg)$'
        targeturl = readconfigs.getTargetURL(params)
        self.assertEqual(targeturl, expected_targetURL)
    
    def test_getThreadCount(self):
        """
        get thread count from test.conf

        Returns
        -------
        None.

        """
        expected_count = '3'
        count = readconfigs.getThreadCount(params)
        self.assertEqual(count, expected_count)
        
unittest.main()
        
