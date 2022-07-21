#模拟 封闭系统内，固定资金，固定人数，10万次交易
import random

total_person = 100
list_rmb_btc = []
for i in range(0, total_person):
    list_rmb_btc.append([1000, 10])

print(list_rmb_btc)

count = 10000000
last_price = 10
for j in  range(0, count):
    sell_person = random.randint(0,total_person - 1 )
    sell_price = last_price + random.randint(-5, 5)
    while sell_price < 0:
        sell_price = last_price + random.randint(-5, 5)
    buy_person = random.randint(0,total_person - 1 )
    #print("sell price: %s \n sell person: %s \n buy_person: %s \n"%(sell_price,sell_person, buy_person))
    if sell_price > list_rmb_btc[buy_person][0]:
        continue
    if list_rmb_btc[sell_person][1] == 0:
        continue
    list_rmb_btc[sell_person][0] = list_rmb_btc[sell_person][0] + sell_price
    list_rmb_btc[sell_person][1] = list_rmb_btc[sell_person][1] - 1

    list_rmb_btc[buy_person][0] = list_rmb_btc[buy_person][0] - sell_price
    list_rmb_btc[buy_person][1] = list_rmb_btc[buy_person][1] + 1
    last_price = sell_price
print(list_rmb_btc)
print(last_price)


