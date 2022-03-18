from email import message
import requests
import time
import telebot



api_key = 'a566e92a-1812-4a39-8be1-e77f6d485d60'
bot_id = '5139271512:AAGAVCLv4wJvLVoFI4i7eo9hX8Qi0fg9eEA'
user_id = 755276080
time_sleep = 1440 //300
bot = telebot.TeleBot(bot_id)

def get_price():
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
    parameters = {
        'start':'1',
        'limit':'200',
        'convert':'USD'
        }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key,
        }
    respond = requests.get(url, headers= headers , params= parameters ).json()
    t = respond['data'][0]['quote']['USD']['price']
    return t 


@bot.message_handler(commands=['start'])
def send_message(mesage = ''):
    bot.send_message(chat_id= user_id , text=mesage)

def main():
    while True:
        price = get_price()
        send_message(mesage= f"اشتغل يا ولاد المرة")
        time.sleep(time_sleep)

main()