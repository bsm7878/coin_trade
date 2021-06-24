"""


Title
- 코인 실시간 현재가(소켓 이용)

Input
- None

Output
- (코인 이름, 현재가)

"""
import websockets
import asyncio
import json
from api.coin_kind import coin_kind


async def real_time_price_all():
    uri = "wss://api.upbit.com/websocket/v1"


    async with websockets.connect(uri) as websocket:
        subscribe_fmt = [
            {"ticket":"test"},
            {
                "type": "ticker",
                "codes": coin_kind(),
                "isOnlyRealtime": True
            },
            {"format":"SIMPLE"}
         ]
        subscribe_data = json.dumps(subscribe_fmt)
        await websocket.send(subscribe_data)

        while True:
            data = await websocket.recv()
            data = json.loads(data)
            print (data['cd'],data['tp'])


async def main():
    await real_time_price_all()

if __name__ == "__main__":
    asyncio.run(main())
