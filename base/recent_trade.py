"""


Title
- 코인 최근 체결 내역

Input
- (코인이름, 갯수)

Return
- market: 코인 이름
- trade_date_utc: 날짜
- trade_time_utc: 시간
- trade_price: 거래금액
- trade_volume: 거래량
- ask_bid: 매도/매수


"""

import requests
from common.api_limit import api_limit
import pandas as pd
import datetime
from api.coin_kind import coin_kind
import time

pd.set_option('display.max_row', 200)
pd.set_option('display.max_columns', 30)
pd.set_option('display.width', 2000)


#최근 거래 내역
def recent_trade(coin, count):
    url = "https://api.upbit.com/v1/trades/ticks"
    # querystring = {"market": f"{coin}", "to": f"{time}", "count": f"{count}"}
    querystring = {"market": f"{coin}", "count": f"{count}"}
    response = requests.request("GET", url, params=querystring)

    # API 요청 수 제한
    api_limit(response)

    return response.json()







if __name__ == "__main__":
    data = recent_trade('KRW-BTC', '12:33:00', '500')
    df = pd.DataFrame(data)
    df['utc-time'] = df['trade_date_utc'] + 'T' + df['trade_time_utc']
    df = df[['market', 'utc-time','ask_bid', 'trade_volume']]

    korea_time = []
    utc_time_list = df['utc-time'].tolist()
    time_gap = datetime.timedelta(hours=9)
    for i in utc_time_list:
        utc_time = datetime.datetime.strptime(i, "%Y-%m-%dT%H:%M:%S")
        kor_time = utc_time + time_gap
        korea_time.append(kor_time)

    df['korea_time'] = pd.DataFrame(korea_time)
    print(df['ask_bid'].value_counts())

    data = recent_trade('KRW-BTC', '500')
    df = pd.DataFrame(data)
    print(df['ask_bid'].value_counts())

    coin = [
        'KRW-ETH', 'KRW-BTC', 'KRW-HBAR', 'KRW-XRP', 'KRW-DOT', 'KRW-GTO', 'KRW-HUNT', 'KRW-ADA', 'KRW-ANKR',
        'KRW-ENJ', 'KRW-XLM', 'KRW-BCH', 'KRW-LAMB', 'KRW-LTC', 'KRW-MOC', 'KRW-EOS', 'KRW-BSV', 'KRW-PXL',
    ]
    ratio = []
    for i in coin:
        data = recent_trade(i, '500')
        df = pd.DataFrame(data)
        result = (df['ask_bid'].value_counts()['BID'] - df['ask_bid'].value_counts()['ASK'])/500 * 100
        ratio.append(result)

    df = pd.DataFrame()
    df['coin'] = coin
    df['ratio'] = ratio
    print(df.sort_values(by=['ratio'], ascending=False))


    while True:
        data = recent_trade('KRW-QTUM', 150)
        df = pd.DataFrame(data)
        result = (df['ask_bid'].value_counts()['BID'] - df['ask_bid'].value_counts()['ASK'])/150 * 100
        print(result)
        print("----------")
        time.sleep(10)