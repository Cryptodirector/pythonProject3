from binance.client import Client
import time
from CryptoScalpBot.binance_api import Binance
import telebot
import logging
from binance.futures import Futures as Client
from binance.lib.utils import config_logging
from binance.error import ClientError

bot = Binance(
    API_KEY='CDFCd1niyKneYgogvDetgfcXCRECpwlwd9ikyjHWUihJ6iLhWDxiVnoVvF7mPYFv',
    API_SECRET='qnckfcVRDEbulbOm8rkp8x5BKLAQJafbGeo1VXsObpdjwxh03hNsuW7vY77yLZEI'
)

config_logging(logging, logging.DEBUG)

key = "CDFCd1niyKneYgogvDetgfcXCRECpwlwd9ikyjHWUihJ6iLhWDxiVnoVvF7mPYFv"
secret = "qnckfcVRDEbulbOm8rkp8x5BKLAQJafbGeo1VXsObpdjwxh03hNsuW7vY77yLZEI"

bot_slava = telebot.TeleBot('5371941587:AAFi-0lS1LWQPKNfX9hawWz9-VGvKBY3bFg')
ID_slava = '847449845'
bot_egor = telebot.TeleBot('5371941587:AAFi-0lS1LWQPKNfX9hawWz9-VGvKBY3bFg')
ID_egor = '985754010'
# Api key
api_key = 'CDFCd1niyKneYgogvDetgfcXCRECpwlwd9ikyjHWUihJ6iLhWDxiVnoVvF7mPYFv'
# Secret Api key
api_secret = 'qnckfcVRDEbulbOm8rkp8x5BKLAQJafbGeo1VXsObpdjwxh03hNsuW7vY77yLZEI'
# Client

print('SHORT BOT:')


def message_slava(text):
    bot_slava.send_message(ID_slava, text)



def loss6_massage_success_slava():
    message_slava('Вошла в сделку, монета: DAR')


def message_egor(text):
    bot_egor.send_message(ID_egor, text)



def loss6_massage_success_egor():
    message_egor('Вошла в сделку монета: DAR')


def position_short():
    client = Client(key, secret, base_url="https://fapi.binance.com")
    params = [{"symbol": "DARUSDT", "side": "SELL", "type": "MARKET", "quantity": "10", 'recWindow': '5000'}]
    try:
        response = client.new_batch_order(params)
        logging.info(response)
    except ClientError as error:
        logging.error(
            "Found error. status: {}, error code: {}, error message: {}".format(
                error.status_code, error.error_code, error.error_message
            )
        )


def position_long():
    client = Client(key, secret, base_url="https://fapi.binance.com")
    params = [{'symbol': 'DARUSDT', 'type': 'TRAILING_STOP_MARKET', 'side': 'BUY', 'quantity': '10', 'callbackRate': '0.3',
               'recWindow': '5000'}]
    try:
        response = client.new_batch_order(params)
        logging.info(response)
    except ClientError as error:
        logging.error(
            "Found error. status: {}, error code: {}, error message: {}".format(
                error.status_code, error.error_code, error.error_message
            )
        )


def short(symbol):
    try:
        print('В РАБОТЕ: DARUSDT')
        while True:
            coin = float(bot.tickerPrice(symbol=symbol)['price'])
            trade = float(coin * 2 / 100 + coin)
            time.sleep(7)
            coin = float(bot.tickerPrice(symbol=symbol)['price'])
            if coin >= trade:
                position_short()
                position_long()
                loss6_massage_success_slava()
                loss6_massage_success_egor()
                time.sleep(80)
                short('DARUSDT')
    except:
        short('DARUSDT')


def main():
    short('DARUSDT')


if __name__ == '__main__':
    main()
