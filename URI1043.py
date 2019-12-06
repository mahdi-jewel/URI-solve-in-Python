n = input().split(" ")
a = float(n[0])
b = float(n[1])
c = float(n[2])

if a + b > c and b + c > a and a + c > b:
    perimeter = a + b + c
    print("Perimetro = %0.1f" %perimeter)
else:
    area = 0.5 * (a + b) * c
    print("Area = %0.1f" %area)
