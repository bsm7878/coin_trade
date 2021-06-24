"""


Title
- 분 캔들

Input
- (코인이름, 캔들 개수, 분 단위)
- ('KRW_BTC', 200, 240)

# 캔들 개수 : 최대 200개까지 요청 가능
# 분 단위 : 1, 3, 5, 10, 15, 30, 60, 240


Output
- (마켓명, utc 시간, kst 시간, 시가, 고가, 저가, 종가, 해당 캔들에서 마지막 틱이 저장된 시각, 누적 거래 금액, 누적 거래량, 분 단위)

# utc_time = datetime.datetime.strptime(a, "%Y-%m-%dT%H:%M:%S")
# time_gap = datetime.timedelta(hours=9)

"""
import requests






def min_candle(coin, count, unit):

    url = f"https://api.upbit.com/v1/candles/minutes/{unit}"
    querystring = {"market": f"{coin}", "count": f"{count}"}
    headers = {"Accept": "application/json"}
    response = requests.request("GET", url, headers=headers, params=querystring)


    return response.json()




if __name__ == "__main__":
    # print(min_candle('KRW-BTC', '10', '1'))
    for i in min_candle('KRW-BTC', '200', '240'):
        print(i)
