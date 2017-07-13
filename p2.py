# p2.py

import random

number = random.randint(1, 10)
tmp = input("不妨猜一猜小甲鱼现在心里想的是哪个数字:")
guess = int(tmp)
cnt = 3

while (cnt > 0) & (guess != number):
    print("第" + str(4 - cnt) + "次输入")
    tmp = input("哎呀, 猜错了, 重新输入吧:")
    guess = int(tmp)
    cnt = cnt - 1

    if guess == number:
        print("哎呀,你是小甲鱼肚子里面的蛔虫吗?!")
        print("哼 猜中了 也没有奖励!")
    else:
        if guess > number:
            print("哥,大了大了~~")
        else:
            print("嘿,小了小了~~")
print("游戏结束,不玩了 ^-^")
