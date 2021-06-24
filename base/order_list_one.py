import os
import jwt
import uuid
import hashlib
from urllib.parse import urlencode

import requests



def order_list_one(uniq_num):
    access_key = os.environ['UPBIT_OPEN_API_ACCESS_KEY']
    secret_key = os.environ['UPBIT_OPEN_API_SECRET_KEY']
    server_url = 'https://api.upbit.com'

    query = {
        'uuid': f'{uniq_num}',
    }
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

    res = requests.get(server_url + "/v1/order", params=query, headers=headers).json()

    return (res['trades'][0]['price'], res['trades'][0]['volume'])

if __name__ == "__main__":
    print(
        order_list_one('ccda4b77-4346-4479-a2f1-30512537c3cd')
    )
