name = input()
salary = float(input())
sale = float(input())
sale_rev = (sale*15)/100
t_salary = salary + sale_rev
print('TOTAL = R$ %0.2f' %t_salary)