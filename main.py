from bs4 import BeautifulSoup
from telegram.ext import Updater, CommandHandler, MessageHandler, ConversationHandler
import os,logging, requests, json
token = "639358022:AAHtST1qHa5OZRG7O4-Du4X5IZBflLaY-DQ"
url = "http://stockr.net/Toronto/GasPrice.aspx"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


#oldPrice = soup.findAll("",{"id":"lPrice2"})
#oldPrice = soup.findAll("",{"class":"gasPrice"})

def main():
    updater = Updater(token,use_context=True)

    # register handlers
    dp = updater.dispatcher 
    #dp.add_handler(CommandHandler("start",start))
    start_handler = CommandHandler("start",start)
    dp.add_handler(start_handler)
    dp.add_handler(CommandHandler("gasme",priceCompare))
    updater.start_polling()
    updater.idle()
    url = get_url()
    response = requests.get(url)
    content = response.content.decode("utf8")

    #print(content)
    #print(url)

def start(update,context):
    #context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
    update.message.reply_text('Hi!')

def get_url():
    telegram_url = "https://api.telegram.org/bot{}/sendMessage?chat_id=690011658&text={}".format(token,final_text)
    return telegram_url

def priceCompare():
    oldPrice = float(soup.find("",{"id":"lPrice2"}).text)
    oldDate = soup.find("",{"id":"lDate2"}).text
    #Check to see if newPrice is updated yet
    newPrice = (soup.find("",{"id":"lPrice1"}).text)
    if newPrice == "&nbsp" or newPrice == "\xa0":
        newPrice = 0
    else:
        newPrice = float(newPrice)   
    newDate = soup.find("",{"id":"lDate1"}).text
    difference = abs(float(newPrice)-float(oldPrice))
    text = ""
    if newPrice == "" or newPrice == "&nbsp;":
        text="No update yet"
        return text
    elif difference > 10:
        text = "This value doesn't seem right"
        return text
    elif newPrice == oldPrice:
        text = "No change."
        return text
    elif newPrice > oldPrice:
        text= "Tomorrow's price will increase by " + str(difference) + "¢"
        return text
    elif newPrice < oldPrice:
        text = "Tomorrow's price will decrease by " + str(difference) + "¢"
        return text

def gasme():
    #context.bot.send _message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
    update.message.reply_text('GASSSS')
#final_text = priceCompare()

def error(update,context):
    #logs errors
    logger.warning('Update "&s" caused error "&s"', update,context.error)

if __name__ == '__main__':
    main()