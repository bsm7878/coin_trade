import requests
import math
from common.api_limit import api_limit
from api.coin_kind import common_coin
from api.now_price_one import now_price
from api.coin_order import CoinOrder
from api.order_list_one import order_list_one
import pandas as pd
import time
from api.my_account import my_account
coin_list = ['POLY', 'SXP', 'REP', 'SRN', 'BAT', 'STMX', 'MARO', 'XEM', 'SOLVE', 'EDR', 'DMT', 'SBD', 'PXL', 'BCHA', 'MED', 'ETC', 'WAXP', 'MTL', 'MLK', 'ATOM', 'ADA', 'QTUM', 'LOOM', 'LAMB', 'ORBS', 'OMG', 'EOS', 'IOST', 'SAND', 'SC', 'XTZ', 'JST', 'ADX', 'KMD', 'KAVA', 'BSV', 'ETH', 'OBSR', 'ANKR', 'ELF', 'CHZ', 'MVL', 'OST', 'NPXS', 'TSHP', 'LTC', 'STEEM', 'MANA', 'LBC', 'CVC', 'GTO', 'STRAX', 'MFT', 'ENJ', 'VET', 'EMC2', 'HUNT', 'LSK', 'DOT', 'CBK', 'QTCON', 'BCH', 'PLA', 'MOC', 'ARDR', 'PCI', 'HIVE', 'ZRX', 'LINK', 'BORA', 'POWR', 'WAVES', 'XRP', 'RFR', 'DKA', 'TON', 'AERGO', 'STPT', 'SNT', 'AQT', 'GLM', 'GRS', 'META', 'TRX', 'SSX', 'ZIL', 'XLM', 'STORJ', 'SPND', 'IGNIS', 'AHT', 'CRO', 'ARK', 'SRM', 'FCT2', 'UPP', 'BTT']


for i in coin_list:

    coin_order = CoinOrder()

    # 원화로 가격
    krw_price = now_price(f'KRW-{i}')

    # 비트코인으로 가격
    now_btc_price = now_price(f'BTC-{i}')
    btc_price_origin = now_price('KRW-BTC') * now_btc_price
    if btc_price_origin > 100:
        btc_price = int(btc_price_origin)
    else:
        btc_price = round(btc_price_origin, 2)


    # KRW Market > BTC Market
    # 1. KRW Market에서 BTC 구매
    # 2. BTC Market에서 해당 Coin 구매
    # 3. 해당 Coin을 KRW Market에 판매
    if (krw_price > btc_price) and now_btc_price > 0.000002 and (((krw_price-btc_price)/btc_price) * 100 > 7):
        krw_name = 'KRW-' + i
        btc_name = 'BTC-' + i

        coin_order.coin_buy('KRW-BTC', 20000)

        balance = 0
        for j in my_account():
            if j['currency'] == 'BTC':
                balance = j['balance']
                break
        amount = round(float(balance) * 0.9974, 8)
        coin_order.coin_buy_want(btc_name, now_btc_price, amount)

        balance2 = 0
        for j in my_account():
            if j['currency'] == i:
                balance2 = j['balance']
                break

        time.sleep(3)
        coin_order.coin_sell_auto(krw_name, balance2)


    # KRW Market < BTC Market
    # 1. KRW Market에서 해당 Coin 구매
    # 2. 해당 Coin을 BTC Market에 판매
    # 3. KRW Market에서 BTC 판매
    elif krw_price < btc_price and now_btc_price > 0.000002 and ((btc_price-krw_price)/krw_price) * 100 > 7:
        print("2", i, krw_price, btc_price, ((btc_price-krw_price)/krw_price) * 100)

        krw_name = 'KRW-' + i
        btc_name = 'BTC-' + i

        coin_order.coin_buy(krw_name, 20000)
        time.sleep(2)
        balance = 0
        for j in my_account():
            if j['currency'] == i:
                balance = j['balance']
                break
        amount = round(float(balance) * 0.9974, 8)
        price = round(now_btc_price * 0.99, 8)
        print(amount, price)
        coin_order.coin_sell(btc_name, amount, price)

        time.sleep(3)
        balance2 = 0
        for j in my_account():
            if j['currency'] == 'BTC':
                balance2 = j['balance']
                break

        time.sleep(3)
        coin_order.coin_sell_auto('KRW-BTC', balance2)


    else:
        continue



