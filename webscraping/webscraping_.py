# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 13:52:09 2021

@author: moni
"""

from bs4 import BeautifulSoup
import requests

 
def getUrl(URL):
    File = open("out.csv", "a")
    HEADERS = ({'User-Agent':
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                    'AppleWebKit/537.36 (KHTML, like Gecko)'
                            'Chrome/44.0.2403.157 Safari/537.36',
                                'Accept-Language': 'en-US, en;q=0.5'})
    webpage = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(webpage.content, "lxml")
    try:
        title = soup.find("span",attrs={"id": 'productTitle'})
        title_value = title.string
        title_string = title_value.strip().replace(',', '')
        t=title_string.split()[0]
 
    except AttributeError:
        title_string = "NA"
    print("product Title = ", title_string.split()[0])
    File.write(f"{t},")
    try:
        price = soup.find("span", attrs={'class':'a-offscreen'}) .string.strip().replace(',', '')
    except AttributeError:
        price = "NA"
    print("Products price = ", price)
    File.write(f"{price},")
    try:
        available = soup.find("div", attrs={'id': 'availability'})
        available = available.find("span").string.strip().replace(',', '')
    except AttributeError:
        available = "NA"
    print("Availability = ", available)
    File.write(f"{available}\n")
    File.close()

if __name__ == '__main__':
  for i in range(1):
   url=input('enter an url: ')
   getUrl(url)
  
  

   
