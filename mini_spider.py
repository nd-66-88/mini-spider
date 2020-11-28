#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 16:46:40 2020

@author: Danni
"""
import logging
import argparse

import log
import spiderx
import read_configs as readconfigs

if __name__ == '__main__':
    log.startlogging('./log/msg')
    ps = argparse.ArgumentParser(usage='mini crawler program', 
                                 add_help=True, 
                                 description='This is a crawler program', 
                                 epilog=None, 
                                 formatter_class=argparse.HelpFormatter)
    ps.add_argument('-c', '--configuration', action='store', 
                    default='conf/spider.conf', help='configuration')
    ps.add_argument('-v', '--version', action='version', version='PROG 1.0')
    params = ps.parse_args()                

    #read configs
    logging.info('reading config file')
    # readConfigs(params.configuration)
    # cf = configparser.ConfigParser()
    # cf.read(params.configuration)
    url_list = readconfigs.getURLList(params)
    output_directory = readconfigs.getOutputDirectory(params)
    max_depth = readconfigs.getMaxDepth(params)
    crawl_interval = readconfigs.getCrawlInterval(params)
    crawl_timeout = readconfigs.getTimeOut(params)
    target_url = readconfigs.getTargetURL(params)
    thread_count = readconfigs.getThreadCount(params)
    wrongurl = set()
    seenurl = set()
    crawlerthreads = list()
            
    for i in range(int(thread_count)):
        t = spiderx.Spiderx(url_list, output_directory, max_depth, 
                            crawl_interval, crawl_timeout, target_url, i, 
                            wrongurl, seenurl)
        crawlerthreads.append(t)
    for i in range(int(thread_count)):
        crawlerthreads[i].start()
    for i in range(int(thread_count)):
        crawlerthreads[i].join()
    logging.info('finished')
