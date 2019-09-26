from bs4 import BeautifulSoup
from telegram.ext import Updater, CommandHandler
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
    telegram_url = "https://api.telegram.org/bot{}/sendMessage?chat_id=690011658&text={}".format(token,final_text)
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
        return text
    elif difference > 10:
        text = "This value doesn't seem right"
        return text
    elif newPrice > oldPrice:
        text= "Tomorrow's price will increase by " + str(difference) + "¢"
        return text
    elif newPrice < oldPrice:
        text = "Tomorrow's price will decrease by " + str(difference) + "¢"
        return text
    elif newPrice == oldPrice:
        text = "No change."
        return text

final_text = priceCompare()

if __name__ == '__main__':
    telegram_url = "https://api.telegram.org/bot{}/sendMessage?chat_id=690011658&text={}".format(token,final_text)
    main(telegram_url)

""" updater = Updater(token) #define updater
    dp = updater.dispatcher #define dispatcher
    dp.add_handler(CommandHandler('gasme',priceCompare))
    updater.start_polling()
    updater.idle()"""