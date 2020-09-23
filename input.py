# import random
# a = 3
# b = random.randint(1,10)
# while a :
#     a -= 1
#     c = int(input("请输入你猜的银行卡余额(1~10)"))
#     if b < c :
#         print("你猜大了,你还有"+str(a),"次机会")
#     elif b > c :
#         print("你猜小了,你还有"+str(a),"次机会")
#     else :
#         print("恭喜你，答对了")
#         break
# else:
#     print(f'你真蠢，这都猜不到，正确答案是{b}')
# 九九乘法表
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print(f'{j}x{i}={i*j}\t', end='')
#     print()
#arr = input("输入一组数")
arr = int(input(""))    #输入一个一维数组，每个数之间使空格隔开

#num = [int(n) for n in arr.split()]    #将输入每个数以空格键隔开做成数组

print(arr)        #打印数组