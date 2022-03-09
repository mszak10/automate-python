# downloadComics.py - Downloads all XKCD comics

import bs4
import os
import requests

url = 'https://xkcd.com'  # homepage (first URL)
os.makedirs('xkcd', exist_ok=True)  # store comics in ./xkcd
while not url.endswith('#'):
    print(f"Downloading page {url}..")
    res = requests.get(url)  # download the page with a comic
    res.raise_for_status()
    print(f"Status: {res.status_code}")

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # Find the comic image element
    comicElem = soup.select('#comic img')

    # Check if the image is found
    if not comicElem:
        print('Could not find comic image.')
    else:  # if found, continue
        comicUrl = 'https:' + comicElem[0].get('src')  # comic address
        print(f'Downloading image {comicUrl}...')
        res = requests.get(comicUrl)  # download the comic
        res.raise_for_status()
        print(f"Status: {res.status_code}")

        # Save the image to ./xkcd folder
        with open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb') as imageFile:
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)

        # Get the Prev button's element
        prevLink = soup.select('a[rel="prev"]')[0]
        url = 'https://xkcd.com' + prevLink.get('href')  # set the URL to next (previous) comic

print('Done!')
