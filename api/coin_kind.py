"""

Title
- 원화(KRW) 거래 코인 종류 불러오기



Input
- None

Output
- ['BTC', 'ETH', 'NEO', 'MTL', 'LTC', ....] => list


"""

import requests, time



def coin_kind():

    # Upbit Api 호출
    url = "https://api.upbit.com/v1/market/all"
    querystring = {"isDetails":"false"}
    headers = {"Accept": "application/json"}
    response = requests.request("GET", url, headers=headers, params=querystring)

    # 'KRW-xxx' 코인 추출
    coin = []
    for i in response.json():
        if i['market'][:3] == 'KRW':
            coin.append(i['market'])
        

    return(coin)


if __name__ == "__main__":
    print(coin_kind())
    print(len(coin_kind()))
