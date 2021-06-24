"""

Title
- 업비트 최소 주문 금액 계산 / 수익률 계산한 금액

Input
- (금액, 수익률)


"""


import math

def money_change(X, ratio):
    X = float(X) * ratio

    if X < 10:
        #0.01
        return math.ceil(X * 100) / 100
    elif 10 <= X < 100:
        #0.1
        return math.ceil(X * 10) / 10
    elif 100 <= X < 1000:
        #1
        return math.ceil(X)
    elif 1000 <= X < 10000:
        #5
        last_num = int(str(math.ceil(X))[-1])
        if last_num == 0 or last_num == 5:
            return math.ceil(X)
        elif last_num > 0 and last_num < 5:
            return int(str(math.ceil(X))[:-1] + '5')
        else:
            return int(str(math.ceil(X)+10)[:-1] + '0')
    elif 10000 <= X < 100000:
        #10
        if math.ceil(X)%10 == 0:
            return math.ceil(X)
        else:
            return int((math.ceil(X) + 10) / 10)*10
    elif 100000 <= X < 500000:
        #50
        if int(str(math.ceil(X))[-2:]) < 50:
            return int(math.ceil(X)/100) * 100 + 50
        else:
            return int(math.ceil(X) / 100) * 100 + 100
    elif 500000 <= X < 1000000:
        # 100
        if math.ceil(X) % 100 == 0:
            return math.ceil(X)
        else:
            return int((math.ceil(X) + 100) / 100) * 100
    elif 1000000 <= X < 2000000:
        # 500
        if int(str(math.ceil(X))[-3:]) < 500:
            return int(math.ceil(X) / 1000) * 1000 + 500
        else:
            return int(math.ceil(X) / 1000) * 1000 + 1000
    elif 2000000 <= X:
        # 1000
        if math.ceil(X) % 1000 == 0:
            return math.ceil(X)
        else:
            return int((math.ceil(X) + 1000) / 1000) * 1000


if __name__ == "__main__":
    a = 18.8
    print(money_change(a, 1.002))
