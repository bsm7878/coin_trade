"""


Title
- Upbit api 호출 횟수 제한


"""
import time, asyncio


def api_limit(response):
    if (int(response.headers['Remaining-Req'].split('sec=')[1]) == 1):
        time.sleep(1)

