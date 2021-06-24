"""


Title
- 코인 실시간 현재가(Rest Api 이용)

Input
- None

Output
- (코인 이름, 현재가)

"""
import time
import asyncio
from api.now_price_one import now_price_one
from api.coin_kind import coin_kind



async def async_now_price_all(start, end):
    coroutines = []
    for coin in coin_kind()[start:end]:
        coroutines.append(now_price_one(coin))

    await asyncio.wait(coroutines, timeout=60)


def now_price_all():
    for i in range(len(coin_kind())//10):
        asyncio.run(async_now_price_all(i*10, i*10+10))
        time.sleep(0.82)

if __name__ == "__main__":
    start = time.time()

    now_price_all()



    print("time :", time.time() - start)
