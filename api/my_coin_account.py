"""

Title
- 내 코인 계좌 정보 가지고 오기



Input
- None

Output
- [['코인 이름', '잔액', '묶여있는 금액', '매수 평균가'], ...] => list

"""

import os
import jwt
import uuid
import requests





def my_krw_account():
    access_key = os.environ['UPBIT_OPEN_API_ACCESS_KEY']
    secret_key = os.environ['UPBIT_OPEN_API_SECRET_KEY']
    server_url = 'https://api.upbit.com/v1/accounts'

    payload = {
        'access_key': access_key,
        'nonce': str(uuid.uuid4()),
    }

    jwt_token = jwt.encode(payload, secret_key)
    authorize_token = 'Bearer {}'.format(jwt_token)
    headers = {"Authorization": authorize_token}
    res = requests.get(server_url, headers=headers)

    my_account = []
    for i in res.json()[1:-1]:
        temp = []
        temp.append("KRW-" + i['currency'])
        temp.append(i['balance'])
        temp.append(i['locked'])
        temp.append(i['avg_buy_price'])

        my_account.append(temp)


    return my_account





if __name__ == "__main__":
    print(my_krw_account())
