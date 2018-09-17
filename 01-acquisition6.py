#Import library
import urllib
import urllib.request
from bs4 import BeautifulSoup

#Get an URL
#theurl="https://www.tripadvisor.com.sg/Hotel_Review-g294265-d301583-Reviews-Raffles_Hotel_Singapore-Singapore.html"

#Define a function
def make_soup(url):
    thepage=urllib.request.urlopen(url)
    soupdata=BeautifulSoup(thepage, "html.parser")
    return soupdata
  
#soup=make_soup(theurl)

#https://www.tripadvisor.com.sg/Hotel_Review-g294265-d301583-Reviews-or50-Raffles_Hotel_Singapore-Singapore.html

numbers=[i for i in range(5,20,5)]
j=1
for i in numbers:

    string1='https://www.tripadvisor.com.sg/Hotel_Review-g294265-d301583-Reviews-or'
    string2=i
    string2=str(string2)
    string3='-Raffles_Hotel_Singapore-Singapore.html'
    longstring=string1+string2+string3
    #print(longstring)


    soup=make_soup(longstring)

    for link in soup.find_all("div", {"class":"review-container"}):
        print(j)
        print(link.find('p').text.encode('ascii', 'ignore'))
        j=j+1