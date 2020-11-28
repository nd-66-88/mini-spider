#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 16:46:40 2020

@author: Danni
"""
import html.parser

class MyHTMLParser(html.parser.HTMLParser):
    """
    inherits from html.parser.HTMLParser
    extracts href and img from html webpage
    """
    def __init__(self, output_list=None, output_set={}, img_list=None, img_set={}): 
        html.parser.HTMLParser.__init__(self)
        if output_list is None:
            self.output_list = list()
            self.output_set = set()
            
        else:
             self.output_list = output_list
             self.output_set = output_set
        if img_list is None:
            self.img_list = list()
            self.img_set = set()
        else:
            self.img_list = img_list
            self.img_set = img_set
    
    def handle_starttag(self, tag, data): 
        """
        extracts href from html webpage

        Parameters
        ----------
        tag : string
            html tag.
        data : dict
            data within tag.

        Returns
        -------
        None.

        """
        if(tag == 'a'): 
            self.output_list.append(dict(data).get('href'))
        if(len(self.output_list) > 0):
            for i in range(len(self.output_list)):
                self.output_set.add(self.output_list[i])
                
    def handle_startendtag(self, tag, data):
        """
        extracts img from html webpage

        Parameters
        ----------
        tag : string
            html tag.
        data : dict
            data within tag.

        Returns
        -------
        None.

        """
        if(tag == 'img'): 
            self.output_list.append(dict(data).get('src'))
        
        if(len(self.output_list) > 0):
            for i in range(len(self.output_list)):
                self.output_set.add(self.output_list[i])
            
