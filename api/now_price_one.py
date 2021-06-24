"""


Title
- 코인 현재가

Input
- 코인 이름('KRW_STRK') => str

Output
- 코인 거래 가격 => float


"""

import requests, asyncio,time
import requests_async
from common.api_limit import api_limit


async def now_price_one(coin):
    url = "https://api.upbit.com/v1/ticker"
    querystring = {"markets":f"{coin}"}
    response = requests.get(url, params=querystring)


    print(response.json()[0]['trade_price'])



if __name__ == "__main__":
    asyncio.run(now_price_one('KRW-HBAR'))
