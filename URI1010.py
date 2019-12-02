product1 = input().split(" ")
product2 = input().split(" ")

qt1 = int(product1[1])
qt2 = int(product2[1])
pr1 = float(product1[2])
pr2 = float(product2[2])

total = ((qt1*pr1)+(qt2*pr2))
print('VALOR A PAGAR: R$ %0.2f' %total)