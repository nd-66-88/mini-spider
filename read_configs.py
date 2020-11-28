#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 18:45:16 2020

@author: Danni
"""
import configparser
import logging
import queue
import os

cf = configparser.ConfigParser()
def getURLList(params):
    """
    get URL list from configuration

    Parameters
    ----------
    params : object
        input parameter.

    Returns
    -------
    queue
        url list.

    """
    cf.read(params.configuration)
    sections = cf.sections()
    if len(sections) != 0:
        logging.info('sections: %s' % sections)
    else:
        logging.error('section does not exist')
    for op in sections:
        item = cf.items(op)
        logging.info('items: %s' % item)
    if cf.get("spider", "url_list_file"):
        url_list_file = cf.get("spider", "url_list_file")
        fr = open(url_list_file, "r")
        url_list = queue.Queue()
        for line in fr.readlines():
            line = line.strip()
            url_list.put([line, 0])
        return url_list
    else:
        logging.error('url list file does not exist')
        return False

def getOutputDirectory(params):
    """
    get output dir from configuration

    Parameters
    ----------
    params : object
        input parameter.

    Returns
    -------
    string
        output directory.

    """
    cf.read(params.configuration)
    if cf.get("spider", "output_directory"):
        output_directory = cf.get("spider", "output_directory")
        if not (os.path.isdir(output_directory)):
            os.makedirs(output_directory)
        return output_directory
    else:
        logging.error('output_directory does not exist')
        return False

def getMaxDepth(params):
    """
    get max depth from configuration

    Parameters
    ----------
    params : object
        input params.

    Returns
    -------
    int
        max depth.

    """
    cf.read(params.configuration)
    if cf.getint("spider", "max_depth"):
        max_depth = cf.get("spider", "max_depth")  
        return max_depth
    else: 
        logging.error('max_depth does not exist')
        return False
    
def getCrawlInterval(params):
    """
    get crawl interval from configuration

    Parameters
    ----------
    params : object
        input params.

    Returns
    -------
    int
        crawl interval.

    """
    cf.read(params.configuration)
    if cf.getint("spider", "crawl_interval"):
        crawl_interval = cf.get("spider", "crawl_interval")
        return crawl_interval
    else:
        logging.error('crawl_interval does not exist')
        return False

def getTimeOut(params):
    """
    get time out value from configuration

    Parameters
    ----------
    params : object
        input params.

    Returns
    -------
    int
        time out value.

    """
    cf.read(params.configuration)
    if cf.getint("spider", "crawl_timeout"):
        crawl_timeout = cf.get("spider", "crawl_timeout")
        return crawl_timeout
    else:
        logging.error('crawl_timeout does not exist')
        return False
    
def getTargetURL(params):
    """
    get target url pattern from configuration

    Parameters
    ----------
    params : object
        input params.

    Returns
    -------
    string
        url pattern.

    """
    cf.read(params.configuration)
    if cf.get("spider", "target_url"):
        target_url = cf.get("spider", "target_url")
        return target_url
    else:
        logging.error('target_url does not exist')    
        return False
    
def getThreadCount(params):
    """
    get number of threads from configuration

    Parameters
    ----------
    params : object
        input params.

    Returns
    -------
    int
        number of threads.

    """
    cf.read(params.configuration)
    if cf.getint("spider", "thread_count"):
        thread_count = cf.get("spider", "thread_count")
        return thread_count
    else:
        logging.error('thread_count does not exist')   
        return False
