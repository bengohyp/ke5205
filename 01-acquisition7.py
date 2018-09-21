from selenium import webdriver
import time
from bs4 import BeautifulSoup

from selenium import webdriver
import time
from bs4 import BeautifulSoup

drive=webdriver.Chrome("chromedriver")
drive.set_page_load_timeout(10)
drive.get("https://www.tripadvisor.com.sg/Hotel_Review-g294265-d301583-Reviews-Raffles_Hotel_Singapore-Singapore.html")
#drive.maximize_window()
time.sleep(10)

el = drive.find_element_by_class_name("ulBlueLinks")
el.click()

print("clicked first page...")

time.sleep(2)
data = drive.page_source
soup = BeautifulSoup(data, "html.parser")
i=1
for link in soup.find_all("div", {"class":"review-container"}):
    print(i)
    print(link.find('p').text)
    i=i+1