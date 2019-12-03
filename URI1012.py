arr = input().split(" ")
A = float(arr[0])
B = float(arr[1])
C = float(arr[2])
pi = 3.14159
tri = 0.5*A*C
cir = pi*C**2
tra = 0.5*(A+B)*C
sqr = B**2
rec = A*B
print("TRIANGULO: %0.3f\nCIRCULO: %0.3f\nTRAPEZIO: %0.3f\nQUADRADO: %0.3f\nRETANGULO: %0.3f" % (tri, cir,tra,sqr,rec))
