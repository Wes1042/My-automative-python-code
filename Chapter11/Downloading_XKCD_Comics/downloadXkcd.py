# downloadXkcd.py -Downloads every single XKCD comic.
import requests,os,bs4

url = 'http://xkcd.com'             # starting url
os.makedirs('xkcd', exist_ok=True)  # stores comics in ./xkcd
while not url.endswith('#'):
    # TODO: Download the page.
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)

    # TODO: FInd the url of the comic image
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        comicUrl = comicElem[0].get('src')
    # TODO: Download the image
    print('Downloading image %s...' % (comicUrl))
    res = requests.get(comicUrl)
    res.raise_for_status()
    # TODO: Save the image to ./xkcd

    # TODO: Get the Prev button's url.

print('Done.')