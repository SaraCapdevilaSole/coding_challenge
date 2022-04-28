#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TXODDS Applicant Test

Name: Sara Capdevila Solé

Date: 28.04.2022

Code 2/2
"""
#IMPORT and RUN file 1 (TXODDS_test.py) and then RUN file 2 (TXODDS_test_analyse.py)
from TXODDS_test import Href_extractor

#%% - input some list of urls to process
links = ["http://imperial.ac.uk", 
    "http://1.2.3.4.png.",
    "https://linkedin.com",
    "www.artsy.com",
    "https://www.apple.com",
    "www.1234.es",
    "https://google.co."]

#%% - run programme

x = Href_extractor(links)
x.extract_hrefs() 

#%% - extract output

print(x.url_list) #urls that we input

print(x.validated_urls) # should print an empty deque, all links have been processed

print(x.htmls) #print htmls of processed links

print(x.hrefs) #print hrefs of processed links


