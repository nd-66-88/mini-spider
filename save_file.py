#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 18:38:28 2020

@author: Danni
"""

import os
import urllib.parse
import logging

def saveFile(pageurl, output_directory): 
    """
    saves html webpages and images which match the given pattern

    Parameters
    ----------
    pageurl : string
        url string
    output_directory : string
        the directory where images and webpages will store
        
    Returns
    -------
    save_path : string
        the directory and name of the file

    """
    quoteurl = urllib.parse.quote(pageurl).replace('/', '_')
    save_path = os.path.join(output_directory, quoteurl)
    logging.info("start to retrieve")
    urllib.request.urlretrieve(pageurl, save_path)
    logging.info("download %s successfully" % pageurl)
    return save_path
