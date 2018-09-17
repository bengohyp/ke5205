#Import library
import urllib
import urllib.request
from bs4 import BeautifulSoup

#Get an URL
theurl="https://www.tripadvisor.com.sg/Hotel_Review-g294265-d301583-Reviews-Raffles_Hotel_Singapore-Singapore.html"

#Define a function
def make_soup(url):
    thepage=urllib.request.urlopen(url)
    soupdata=BeautifulSoup(thepage, "html.parser")
    return soupdata
  
def add_five(x):
    y=x+5
    return y
  
add_five(5)

soup=make_soup(theurl)

#Show the content in the soup
#print(soup.prettify())

#Getting the review data
j=1
for link in soup.find_all("div", {"class":"review-container"}):
    print(j)
    #print(link.find('p').text)
    j=j+1
    
#Explain for loop
for m in [1,2,3,5,6]:
    print(m)
    
#Get review date and rating
j=1

for link in soup.find_all("div", {"class":"reviewSelector"}):
    print(j)
#print(link)
#print(link.find_all('span')[0])
    print(link.find_all('span')[4].attrs['class'][1])
    print(link.find_all('span')[5].attrs['title'])
#print(link.find_all('span')[1].text)
    j=j+1
  
j=1
set1=[]
for link in soup.find_all("div", {"class":"review-container"}):
#print(j)
#print(link.find('p').text)
    set1.append(link.find('p').text)
    j=j+1
print(type(set1),len(set1))

set2=[]
set3=[]
j=1
for link in soup.find_all("div", {"class":"reviewSelector"}):
#print(j)
#print(link.find_all('span')[0].attrs['class'][1])
    set2.append(link.find_all('span')[4].attrs['class'][1])
    set3.append(link.find_all('span')[5].attrs['title'])
    j=j+1
print(type(set2),len(set2))
print(type(set3),len(set3))

import pandas as pd
df = pd.DataFrame({ 'c1': set1,'c2': set2,'c3': set3})
print(df.head())

df.columns=['Review','Rate','Date']

print(df.head())