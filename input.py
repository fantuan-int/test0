import random
a = 3
b = random.randint(1,10)
while a :
    a -= 1
    c = int(input("请输入你猜的银行卡余额(1~10)"))
    if b < c :
        print("你猜大了,你还有"+str(a),"次机会")
    elif b > c :
        print("你猜小了,你还有"+str(a),"次机会")
    else :
        print("恭喜你，答对了")
        break
else:
    print(f'你真蠢，这都猜不到，正确答案是{b}')