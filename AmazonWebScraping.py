
## Import Libraries

from bs4 import BeautifulSoup
import requests
import smtplib
import time
import datetime
import csv
import pandas as pd

## Connect To Website

URL = 'https://www.amazon.com.tr/Acer-Predator-PT314-51s-766L-Notebook-i7-11370H/dp/B0B2R5L7KX/ref=sr_1_15?__mk_tr_TR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=14WW76XPO7Y1B&keywords=acer+laptop&qid=1662901934&sprefix=acer+laptop%2Caps%2C201&sr=8-15'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36", "Accept-Encoding": "gzip, deflate, br", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Upgrade-Insecure-Requests": "1"}
page = requests.get(URL, headers=headers)
Soup1 = BeautifulSoup(page.content, "html.parser")
Soup2 = BeautifulSoup(Soup1.prettify(), "html.parser")
title = Soup2.find(id='productTitle').get_text()
price = Soup2.find("span", {"class":"a-offscreen"}).get_text()
title = title.strip()[0:27]
price = price.strip()[0:6]

today = datetime.date.today()

## Create CSV

header = ['Title', 'Price', 'Data Collected']
data = [title, price, today]

with open('AmazonScrapingData.csv', 'w', newline='',encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)

## Append To CSV

with open('AmazonScrapingData.csv', 'a+', newline='',encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)

## Automate CSV

def check_price():
    import datetime
    import csv
    URL = 'https://www.amazon.com.tr/Acer-Predator-PT314-51s-766L-Notebook-i7-11370H/dp/B0B2R5L7KX/ref=sr_1_15?__mk_tr_TR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=14WW76XPO7Y1B&keywords=acer+laptop&qid=1662901934&sprefix=acer+laptop%2Caps%2C201&sr=8-15'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Upgrade-Insecure-Requests": "1"}
    page = requests.get(URL, headers=headers)
    Soup1 = BeautifulSoup(page.content, "html.parser")
    Soup2 = BeautifulSoup(Soup1.prettify(), "html.parser")
    title = Soup2.find(id='productTitle').get_text()
    price = Soup2.find("span", {"class": "a-offscreen"}).get_text()
    title = title.strip()[0:27]
    price = price.strip()[0:6]
    today = datetime.date.today()

    header = ['Title', 'Price', 'Data Collected']
    data = [title, price, today]

    with open('AmazonScrapingData.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)

while(True):
    check_price()
    time.sleep(86400)











