"""

Title
- (미체결) 주문 내역

Return
- 체결대기만 불러옴
- 없을 수도 있음
- uuid: 주문 고유 id
- side: bid(매수)
- price: 주문 금액
- market: 코인 이름
- created_at: 주문 시간
- volume: 주문 양


"""

import os
import jwt
import uuid
import hashlib
from urllib.parse import urlencode
import requests
import pandas as pd


#DataFrame 설정
pd.set_option('display.max_row', 500)
pd.set_option('display.max_columns', 30)
pd.set_option('display.width', 3000)


def order_list():
    access_key = os.environ['UPBIT_OPEN_API_ACCESS_KEY']
    secret_key = os.environ['UPBIT_OPEN_API_SECRET_KEY']
    server_url = 'https://api.upbit.com'


    payload = {
        'access_key': access_key,
        'nonce': str(uuid.uuid4()),
        'query_hash_alg': 'SHA512',
    }

    jwt_token = jwt.encode(payload, secret_key).decode('utf-8')
    authorize_token = 'Bearer {}'.format(jwt_token)
    headers = {"Authorization": authorize_token}

    res = requests.get(server_url + "/v1/orders", headers=headers)

    return res.json()

if __name__ == "__main__":


    df = pd.DataFrame(order_list())
    print(df)