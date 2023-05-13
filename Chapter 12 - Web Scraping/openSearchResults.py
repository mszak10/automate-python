# openSearchResults.py - Opens several search results.
# from lib2to3.pgen2 import driver
# from selenium.webdriver.common.by import By
import bs4
import pyinputplus as pyip
import requests
import webbrowser


inp = pyip.inputStr(prompt="What are you looking for? ")
print('Searching...')
headers = {"User-Agent": "Mozilla/5.0"}
cookies = {"CONSENT": "YES+cb.20210720-07-p0.en+FX+410"}
res = requests.get('https://google.com/search?q=' + ' '.join(inp), headers=headers, cookies=cookies)
res.raise_for_status()
print(f"Status: {res.status_code}")

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, 'html.parser')
linkElems = soup.select('.BVG0Nb')  # works as of May 13, 2023

numOpen = min(5, len(linkElems))
for i in range(numOpen):
    urlToOpen = 'https://google.com' + linkElems[i].get('href')
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)
