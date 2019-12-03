arr = input().split(" ")
a = int(arr[0])
b = int(arr[1])
c = int(arr[2])
great = (a+b+abs(a-b))/2
great = (great+c+abs(great-c))/2
print(int(great), "eh o maior")