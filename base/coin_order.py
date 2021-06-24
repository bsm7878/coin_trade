"""

Title
- 주문

Input
- 매수(시장가) : (코인이름, 얼마치 살지)
- 매수(희망가) : (코인이름, 희망가, 얼마치 살지)

- 매도(희망가) : (코인이름, 얼마나 팔지, 얼마에 팔지)


"""

import os
import jwt
import uuid
import hashlib
from urllib.parse import urlencode
import requests


#공통 api
def call_order_api(query):
    access_key = os.environ['UPBIT_OPEN_API_ACCESS_KEY']
    secret_key = os.environ['UPBIT_OPEN_API_SECRET_KEY']
    server_url = 'https://api.upbit.com'

    query_string = urlencode(query).encode()

    m = hashlib.sha512()
    m.update(query_string)
    query_hash = m.hexdigest()

    payload = {
        'access_key': access_key,
        'nonce': str(uuid.uuid4()),
        'query_hash': query_hash,
        'query_hash_alg': 'SHA512',
    }

    jwt_token = jwt.encode(payload, secret_key).decode('utf-8')
    authorize_token = 'Bearer {}'.format(jwt_token)
    headers = {"Authorization": authorize_token}

    response = requests.post(server_url + "/v1/orders", params=query, headers=headers)
    return response




class CoinOrder:

    # 매수(시장가)
    def coin_buy(self, coin, price):
        query = {
            # coin 이름
            'market': f'{coin}',

            # bid: 매수
            'side': 'bid',

            # 얼마나 살건지
            'price': f'{price}',

            # price: 시장가 주문
            'ord_type': 'price',
        }

        # 주문 공통 api 불러오기
        res = call_order_api(query)
        return (res.json())


    # 매수(희망가)
    def coin_buy_want(self, coin, now_price, want_price):
        amount = round(want_price/now_price, 8)

        query = {
            # coin 이름
            'market': f'{coin}',

            # bid: 매수
            'side': 'bid',

            # 얼마나 살건지
            'volume': f'{amount}',

            # 얼마에 살건지
            'price': f'{now_price}',

            # price: 시장가 주문
            'ord_type': 'limit',
        }

        #주문 공통 api 불러오기
        res = call_order_api(query)
        return (res.json())


    #매도(희망가)
    def coin_sell(self, coin, amount, price):
        query = {
            # coin 이름
            'market': f'{coin}',

            # ask: 매도
            'side': 'ask',

            # 얼마나 팔건지
            'volume' : f'{amount}',

            # 얼마에 팔건지
            'price': f'{price}',

            # price: 지정가 주문
            'ord_type': 'limit',
        }

        # 주문 공통 api 불러오기
        res = call_order_api(query)
        return (res.json())

    # 매도(시장가)
    def coin_sell_auto(self, coin, amount):
        query = {
            # coin 이름
            'market': f'{coin}',

            # ask: 매도
            'side': 'ask',

            # 얼마나 팔건지
            'volume': f'{amount}',

            # price: 시장가 주문
            'ord_type': 'market',
        }


        #주문 공통 api 불러오기
        call_order_api(query)
        res = call_order_api(query)

if __name__ == "__main__":

    order = CoinOrder()

    a = order.coin_sell('KRW-QTUM', 0.38184752, 3960)
    print(a)





