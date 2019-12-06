N = input().split(" ")
x = float(N[0])
y = float(N[1])
if x>0 and y>0:
    print("Q1")
if x<0 and y>0:
    print("Q2")
if x<0 and y<0:
    print("Q3")
if x>0 and y<0:
    print("Q4")
if y==0 and x!=0:
    print("Eixo X")
if x==0 and y!=0:
    print("Eixo Y")
if x==0 and y==0:
    print("Origem")