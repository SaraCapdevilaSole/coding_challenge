#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TXODDS Applicant Test

Name: Sara Capdevila Solé

Date: 28.04.2022

Code 1/2
"""
import re
from collections import deque
from bs4 import BeautifulSoup
import requests
import requests.exceptions
from urllib.request import urlopen
        
class Href_extractor:
    """
    Input: 
        List of strings containing URLs
    
    Returns: 
        List of hrefs and htmls of working URLs 
    """
    
    def __init__(self, string_urls):
        self.url_list = string_urls #re.findall(filtering, string_urls))
        self.validated_urls = deque([]) #deque of validated urls
        self.working_urls = [] #working urls
        self.not_working_urls = [] #broken urls
        self.hrefs = [] #hyperlinks
        self.htmls = [] #htmls 
        
        self.filtering = re.compile(
            r"(\w+://)?"
            r"(\w+\.)?"                 
            r"((\w+)\.(\w+))"           
            r"(\.\w+)*"                 
            r"([\w\-\._\~/]*)*(?<!\.)" 
        ) #filtering methods for malformed URLs (hosts, ip, ports, protocol, path, (top-level) domains...)
        
        
    def extract_hrefs(self):
        """
        Filtering of malformed strings in list and non-valid urls
        """
        
        for link in self.url_list:
            
            #checking if link is of a valid form
            
            state_validity = self.filtering.match(link).span()[1] - self.filtering.match(link).span()[0] == len(link)
            
            if state_validity == True:
                
                self.validated_urls.append(link) #add validated link to list
                
        while len(self.validated_urls): #reads queue until it is empty
            
            """
            This runs the function only when the url works:
                1. Url is valid:
                    It will process the url and find its html, hrefs 
                    Will add url to "working_urls"
                2. Url is not valid:
                    Will add it to not working urls
            A not working url will not break the code (e.g. connection error, invalid url...)
            """
            
            url = self.validated_urls.popleft() 
            #print(url)
            
            try: 
                response = requests.get(url) #testing if url works
                
                page = urlopen(url) #open url
                
                html = page.read().decode("utf-8") #extract html
                
                soup = BeautifulSoup(html, "html.parser") #create nested data structure that allows us to find url references easily
                
                link = soup.find_all("a") #assume references are in the form <a href="">
        
                hrefs_link = []
            
                for l in link: # iterate and find all hyperlinks of url
                    anchor = l.attrs["href"] if "href" in l.attrs else ""
                    hrefs_link.append(anchor) 
                
                self.working_urls.append(url) # add url that works to a list 
                                                #this is done to keep track of all the urls processed
                
                self.hrefs.append(hrefs_link) #add the processed hrefs to a list
                self.htmls.append(link) #adds the processed htmls to a list
                
                print("Working with %s" % url)  #print the working url  
            
            except(requests.exceptions.ConnectionError, requests.exceptions.InvalidURL, 
                   requests.exceptions.InvalidSchema, requests.exceptions.MissingSchema): 
                
                self.not_working_urls.append(url)  # add broken url to list
                                                        #if memory is a problem, comment this step
                
                print("This is broken %s" % url) #print broken url
  








