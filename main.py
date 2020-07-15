#!/usr/bin/python

import requests as r
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import sys
import re

hub = r".*pornhub\.com.*"
searched = set()


def get_links(url):
    res = set()
    
    print("requesting: %s" % url)
    try:
        req = r.get(url)
        soup = BeautifulSoup(req.content, 'html.parser')
        
        for link in soup.find_all('a', href=True):
            new_url = urlparse(link['href'])
            if not re.match(r".*\.pdf", new_url.geturl()) \
                    and not re.match(r"^(en).wiki.*", new_url.netloc) \
                    and new_url.scheme != '':

                res.add(new_url.geturl())
    except r.exceptions.HTTPError as e:
        print("HTTPError: %s" % e.response)
    except r.exceptions.ConnectionError as e:
        print("ConnectionError: %s" % e.response)
    except r.exceptions.TooManyRedirects as e:
        print("TooManyRedirects: %s" % e.response)


    return res


def search(url, maxdepth):
    searched = set()
    links = get_links(url)

    
    for i in range(maxdepth):
        new_links = set()

        for link in links:
            if re.match(hub, link):
                return i + 1

        for link in links:
            new_links.update(get_links(link).difference(searched))
        
        searched.update(new_links)


       

url = "https://en.wikipedia.org/wiki/%s" % sys.argv[1]

# print("\n".join(get_links(url)))

dist = search(url, 4)
print("found link with distance: %d" %dist)
