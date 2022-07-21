#对btc进行随机跳动，生成走势图
import random
import matplotlib.pyplot as plt
import numpy as np

total_count = 10000000
X=np.linspace(0,total_count,total_count)  # X轴坐标数据
#Y =X*X                   # Y轴坐标数据
last_price = 10
price_list = []
price_list.append(last_price)
for i in range(1, total_count):
    sell_price = last_price + random.randint(-5, 5)
    while sell_price < 1:
        sell_price = last_price + random.randint(-5, 5)
    #print(sell_price)
    price_list.append(sell_price)
    last_price = sell_price


# plt.plot(X,Y,lable="$sin(X)$",color="red",linewidth=2)

plt.figure(figsize=(8,6))  # 定义图的大小
plt.xlabel("count")     # X轴标签
plt.ylabel("price")        # Y轴坐标标签
plt.title("")      #  曲线图的标题

plt.plot(X,price_list)            # 绘制曲线图
#在ipython的交互环境中需要这句话才能显示出来
plt.show()
