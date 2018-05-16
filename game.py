import random
import re
import sys

list_num = []   #棋子个数
list_num_b = [] #棋子个数二进制
for i in range(4):
    num = random.randint(1, 10)
    list_num.append(num)
    list_num_b.append(bin(num))
print('四堆棋子个数:', list_num)
# print(list_num_b)
# s = 0
# for n1 in list_num:
#     s ^= n1
# print(bin(s))
# while list_num[0] != 0 or list_num[1] != 0 or list_num[2] != 0 or list_num[3] != 0:
while [x for x in list_num if x != 0]:  #列表为空即为false
    i = input('请玩家选择拿走第几堆的几个棋子:')
    res = re.match(r'\d\s\d',i) #正则表达式，匹配‘1 2’
    if res == None:
        print('对不起，您的输入有误')
        continue
    else:
        # print(res.group())
        a, b = res.group().split()
        if list_num[int(a)-1] - int(b) < 0:
            print('对不起，该堆没有足够的棋子')
            continue
        list_num[int(a) - 1] -= int(b)  #更新棋子个数
        list_num_b[int(a) - 1] = bin(list_num[int(a) - 1])  #更新棋子个数二进制

    print('目前棋子个数:', list_num)
    # print(list_num_b)
    sum = 0 #棋子个数二进制相加的和(十进制)
    for n in list_num:
        sum ^= n    #异或即为二进制相加，十进制异或结果为十进制
    # print(bin(sum))
    if sum == 0:
        print('聪明的你知道算法，恭喜你赢了')
        sys.exit()

    #和的二进制的最高位，注意是从第0位开始的。bin()函数将十进制转为以0b开头的二进制的字符串，例：10-->‘0b1010’
    high_bit = len(bin(sum)) - 3
    # print(high_bit)
    # print(1 << high_bit)

    list_bit = []   #存放棋子个数二进制在和的最高位上的数字，例：1010在第2位是0(从第0位开始）
    for i in range(4):
        list_bit.append(list_num[i] & (1 << high_bit))
    # print(list_bit)

    count = 0
    left = 0    #剩下棋子个数
    for x in list_bit:
        if x != 0:
            #二进制在和的最高位为1的棋子个数与和异或即为剩下棋子个数，如果有多个在和的最高位为1的个数，取第一个即可
            left = list_num[count] ^ sum
            break
        count += 1
    # print(count)
    # print(left)

    print('电脑决定取走第{}堆的{}个棋子'.format(count + 1, list_num[count] - left))
    list_num[count] = left

    print('目前棋子个数:', list_num)

print('你输了')
