#!/usr/bin/python

import requests as r
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import sys
import re

hub = ".*pornhub.com.*"
searched = set()


def search(path, rest):
    url = path[-1]
    base_url = urlparse(url)

    if re.match(hub, base_url.geturl()):
        return (path, 0)

    if rest <= 0:
        return ([],-1)
    
    print("requesting: " + url)
    req = r.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')

    for link in soup.find_all('a', href=True):
        new_url = urlparse(link['href'])
        
        #relative path
        if new_url.scheme == '' and new_url.path != '':
            new_url = new_url._replace(netloc=base_url.netloc)
            new_url = new_url._replace(scheme=base_url.scheme)


        if new_url.scheme != '' and new_url.geturl() not in searched:
            searched.add(new_url.geturl())
            p, dist = search(path + [new_url.geturl()], rest -1)

            if dist >= 0:
                return (p, dist +1)

    return ([],-1)


def print_links(url):
    req = r.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')

    print(soup.content)
    for link in soup.find_all('a', href=True):
        print(link['href'])


url = "https://en.wikipedia.org/wiki/%s" % sys.argv[1]
# url = "https://duckduckgo.com/?q=test"

# print_links(url)
path, dist = search([url], 8)
# print(res)
print("found link with distance: %d\nand path: %s" %(dist, path))
