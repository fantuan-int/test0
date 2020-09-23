#冒泡

def bubbleSort(arr):
    n = len(arr)
 
    # 遍历所有数组元素
    for i in range(n):
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
 
arr = [64, 34, 25, 12, 22, 11, 90]
#arr = input("输入一组数")
# arr = input("")    #输入一个一维数组，每个数之间使空格隔开

# num = [int(n) for n in arr.split()]    #将输入每个数以空格键隔开做成数组

# print(num)        #打印数组

bubbleSort(arr)
 
print ("排序后的数组:")
for i in range(len(arr)):
    print ("%d" %arr[i]),