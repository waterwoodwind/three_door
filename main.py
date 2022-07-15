import random

random_list = []
total = 100000000
print(("总次数： %s")%(total))
for i in range(1,total):
    random_index = random.randint(1,3)
    #print(random_index)
    random_list.append(random_index)

#print(random_list)
print("chose 1 : %s"%(random_list.count(1)/total))
print("chose 2 : %s"%(random_list.count(2)/total))
print("chose 3 : %s"%(random_list.count(3)/total))

#选1的时候，主持人去掉一个错误选项，1，0，0，还是正确位置1，010正确位置还是2，001去掉中间一个变2
chose_1_list = []
for i in range(1, len(random_list)):
    if random_list[i] == 3:
        chose_1_list.append(2)
    else:
        chose_1_list.append(random_list[i])

print(("还是选1的概率：%s")%(chose_1_list.count(1)/total))
print(("换一个的概率：%s")%(chose_1_list.count(2)/total))


