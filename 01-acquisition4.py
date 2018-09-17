import urllib
import urllib.request
from bs4 import BeautifulSoup

theurl="https://twitter.com/realDonaldTrump"
thepage=urllib.request.urlopen(theurl)
soup=BeautifulSoup(thepage, "html.parser")

i=0
for link in soup.find_all('a'):
#print(link.get('href'))
    print(i)
    print(link)
    print(link.text)
    i=i+1
    
j=1
for link in soup.find_all("div", {"class":"js-tweet-text-container"}):
    print(j)
    print(link.text)
    j=j+1