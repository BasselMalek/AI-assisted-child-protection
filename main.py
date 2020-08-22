import json
import urllib.request, urllib.error, urllib.parse
from HTML_Reader import website_fetcher
from HTML_search import website_linter
from nsfw_scanner import image_scan
import image_download as imgd

while True:
    if (website_fetcher() == True):
        #youtube_caption()
        pass
    elif (website_fetcher() == False):
        imgd.maitestn()
        nsfw_scan = website_linter()
        if (nsfw_scan == True):
            image_scan()
        elif (nsfw_scan == False):
            pass


