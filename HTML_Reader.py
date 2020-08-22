import urllib.request, urllib.error, urllib.parse

def website_fetcher():

    with open(r"D:\Code\AI-assisted child protection\HTML_cache\data.txt","r") as f:
        url = f.readline()
        url = url.replace(",","")
        f.close()
        parsed = urllib.parse.urlparse(url)
    
    if (parsed.netloc == "www.youtube.com"):
        return True
    else:
        response = urllib.request.urlopen(url)
        webContent = response.read()
        f = open('cache.html', 'wb')
        f.write(webContent)
        f.close()
        return False