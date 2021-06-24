"""

Title
- 내 원화 계좌 정보 가지고 오기



Input
- None

Output
- ['잔액', '묶여있는 금액'] => list

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


    my_krw_account = []
    my_krw_account.append(res.json()[0]['balance'])
    my_krw_account.append(res.json()[0]['locked'])

    return my_krw_account





if __name__ == "__main__":
    print(my_krw_account())
