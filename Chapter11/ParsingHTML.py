'''Parsing HTML with the BeautifulSoup Module '''
import bs4, requests

res = requests.get('http://nostarch.com')   # request for home page data
print(res.raise_for_status())               # sets alert 
noStarchSoup = bs4.BeautifulSoup(res.text)  # passes data to bs4
type(noStarchSoup)

'''# You can load and HTML file from HDD
exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile)
type(exampleSoup)'''