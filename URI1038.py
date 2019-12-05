n = input().split(" ")
code = int(n[0])
quantity = int(n[1])
price = 0
if code==1:
    price = 4.00*quantity
if code==2:
    price = 4.50*quantity
if code==3:
    price = 5.00*quantity
if code==4:
    price = 2.00*quantity
if code==5:
    price = 1.50*quantity
print("Total: R$ %0.2f" %price)