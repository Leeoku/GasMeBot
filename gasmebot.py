from bs4 import BeautifulSoup
import os
import requests
import json
token = "639358022:AAHtST1qHa5OZRG7O4-Du4X5IZBflLaY-DQ"
telegram_url = "https://api.telegram.org/bot{}/getupdates".format(token)
print(telegram_url)
url = "http://stockr.net/Toronto/GasPrice.aspx"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

#oldPrice = soup.findAll("",{"id":"lPrice2"})
#oldPrice = soup.findAll("",{"class":"gasPrice"})

def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    print(content)


def priceCompare():
    oldPrice = soup.find("",{"id":"lPrice2"}).text
    oldDate = soup.find("",{"id":"lDate2"}).text
    newPrice = soup.find("",{"id":"lPrice1"}).text
    newDate = soup.find("",{"id":"lDate1"}).text

    if newPrice == "":
        print("No update yet")
    elif newPrice > oldPrice:
        print("Tomorrow's price will increase by " + (abs(newPrice-oldPrice)) + "¢")
    elif newPrice < oldPrice:
        print("Tomorrow's price will decrease by " + (abs(newPrice-oldPrice)) + "¢")
    elif newPrice == oldPrice:
        print("No change.")

priceCompare()
get_url(telegram_url)