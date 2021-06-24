import requests, asyncio, time
from api.coin_kind import coin_kind
from common.api_limit import api_limit


def now_price_one(coin):
    url = "https://api.upbit.com/v1/ticker"
    querystring = {"markets":f"{coin}"}
    response = requests.get(url, params=querystring)

    # API 요청 수 제한
    api_limit(response)

    return(response.json()[0]['trade_price'])


if __name__ == "__main__":
    start = time.time()

    for coin in coin_kind():
        a = now_price_one(coin)
        print(a)


    print("time :", time.time() - start)

    # 16-17초
