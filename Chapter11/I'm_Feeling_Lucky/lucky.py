# lucky.py - Opens several Google search results.

import requests, sys,webbrowser,bs4

print('Googling...') # display text while downloading the Google page
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# TODO: Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, features="html.parser")

# TODO: Open a broswer tab for each result.
linkElems = soup.select('div#main > div > div > div > a') # Selects a pattern and located it in the source code of the site
for link in linkElems:
    print(f'link: {link}')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))
