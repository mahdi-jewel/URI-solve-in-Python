import math
num = input().split(" ")
a=float(num[0])
b=float(num[1])
c=float(num[2])
if a==0 or (b ** 2) - (4 * a * c)<0:
    print("Impossivel calcular")
else:
    R1 = ((-b + math.sqrt((b ** 2) - (4 * a * c))) / (2 * a))
    R2 = ((-b - math.sqrt((b ** 2) - (4 * a * c))) / (2 * a))
    print('R1 = %0.5f' %R1)
    print('R2 = %0.5f' %R2)

