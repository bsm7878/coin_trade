from api.order_list_one import order_list_one
import pandas as pd
from api.coin_order import CoinOrder
from common.money_change import money_change
import time

pd.set_option('display.max_row', 500)
pd.set_option('display.max_columns', 30)
pd.set_option('display.width', 2000)


class MethodOne:
    coin_order = CoinOrder()

    # 30분마다 코인 구매
    while True:
        for i in ['KRW-QTUM', 'KRW-DOT', 'KRW-LOOM']:
            res = coin_order.coin_buy(i, 1500)
            time.sleep(2)
            uniq_num = res['uuid']

            amount = order_list_one(uniq_num)[1]
            price = money_change(order_list_one(uniq_num)[0], 1.002)

            print(i, amount, price)
            coin_order.coin_sell(i, amount, price)

        time.sleep(900)

if __name__ == "__main__":
    pass
