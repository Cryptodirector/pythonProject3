from CryptoScalpBot.binance_api import Binance


bot = Binance(
    API_KEY='CDFCd1niyKneYgogvDetgfcXCRECpwlwd9ikyjHWUihJ6iLhWDxiVnoVvF7mPYFv',
    API_SECRET='qnckfcVRDEbulbOm8rkp8x5BKLAQJafbGeo1VXsObpdjwxh03hNsuW7vY77yLZEI'
)


def price_coin():
    coin = bot.futuresSymbolPriceTicker()
    for i in coin:
        if float(i['priceChangePercent'][:4]) <= 0.1:
            print(i['symbol'], ':', i['priceChangePercent'][:4] + '%')


price_coin()