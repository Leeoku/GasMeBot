from bs4 import BeautifulSoup
import os
import requests
import json
token = "639358022:AAHtST1qHa5OZRG7O4-Du4X5IZBflLaY-DQ"

url = "http://stockr.net/Toronto/GasPrice.aspx"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

#oldPrice = soup.findAll("",{"id":"lPrice2"})
#oldPrice = soup.findAll("",{"class":"gasPrice"})

def main(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def priceCompare():
    oldPrice = float(soup.find("",{"id":"lPrice2"}).text)
    oldDate = soup.find("",{"id":"lDate2"}).text
    newPrice = float(soup.find("",{"id":"lPrice1"}).text)
    newDate = soup.find("",{"id":"lDate1"}).text
    difference = abs(float(newPrice)-float(oldPrice))
    text = ""
    if newPrice == "":
        text="No update yet"
        print(text)
        return text
    elif difference > 10:
        text = "This value doesn't seem right"
        print(text)
        return text
    elif newPrice > oldPrice:
        text= "Tomorrow's price will increase by " + str(difference) + "¢"
        print(text)
        return text
    elif newPrice < oldPrice:
        text = "Tomorrow's price will decrease by " + str(difference) + "¢"
        print(text)
        return text
    elif newPrice == oldPrice:
        text = "No change."
        print("No change.")
        return text

final_text = priceCompare()
telegram_url = "https://api.telegram.org/bot{}/sendMessage?chat_id=690011658&text={}".format(token,final_text)
#print(telegram_url)
main(telegram_url)
