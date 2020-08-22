import requests
import os
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin, urlparse
from tqdm import tqdm

def is_valid(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)
def get_all_images(url):
    soup = bs(requests.get(url).content, "html.parser")
    urls = []
    for img in tqdm(soup.find_all("img"), "Extracting images"):
        img_url = img.attrs.get("src")
        if not img_url:
        # if img does not contain src attribute, just skip
            continue
                    # make the URL absolute by joining domain with the URL that is just extracted
        img_url = urljoin(url, img_url)
        try:
            pos = img_url.index("?")
            img_url = img_url[:pos]
        except ValueError:
            pass
                    # finally, if the url is valid
        if is_valid(img_url):
            urls.append(img_url)
    return urls
def download(url):
    # download the body of response by chunk, not immediately
    response = requests.get(url, stream=True)
    # get the total file size
    file_size = int(response.headers.get("Content-Length", 0))
    filename = os.path.join(r"D:\Code\AI-assisted child protection\HTML_cache\images", url.split("/")[-1])
    # progress bar, changing the unit to bytes instead of iteration (default by tqdm)
    progress = tqdm(response.iter_content(1024), f"Downloading {filename}", total=file_size, unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "wb") as f:
        for data in progress:
            # write data read to the file
            f.write(data)
            # update the progress bar manually
            progress.update(len(data))
def maitestn():
    f = open(r"D:\Code\AI-assisted child protection\HTML_cache\data.txt","r")
    url = f.readline()
    url = url.replace(",","")
    f.close()
    # get all images
    imgs = get_all_images(url)
    for img in imgs:
        # for each image, download it
        download(img)




            
    

