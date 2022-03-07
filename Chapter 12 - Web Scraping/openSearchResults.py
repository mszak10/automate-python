# openSearchResults.py - Opens several search results.
# TODO: To be fixed - passing "Before you continue to Google Search" window

import bs4
import os
import pyinputplus as pyip
import requests
import webbrowser

inp = pyip.inputStr(prompt="What are you looking for? ")
print('Searching...')
res = requests.get('https://google.com/search?q=' + ' '.join(inp))
res.raise_for_status()
print(f"Status: {res.status_code}")

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, 'html.parser')
print(soup)  # output the css and html (temporarly for debugging)
# Open a browser tab for each result.
linkElems = soup.select('.package-snippet')

numOpen = min(5, len(linkElems))
for i in range(numOpen):
    urlToOpen = 'https://google.com' + linkElems[i].get('href')
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)
