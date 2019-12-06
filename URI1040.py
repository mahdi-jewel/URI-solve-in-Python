N=input().split(" ")
n1 = float(N[0])
n2 = float(N[1])
n3 = float(N[2])
n4 = float(N[3])
avg = ((n1*2)+(n2*3)+(n3*4)+(n4*1))/10
print('Media: %0.1f' %avg)
if avg >=7.0:
    print("Aluno aprovado.")
if avg<5.0:
    print("Aluno reprovado.")
if avg >=5.0 and avg <= 6.9:
    print("Aluno em exame.")
    score = float(input())
    print("Nota do exame:", score)
    avg_final = (avg+score)/2
    if avg_final>=5.0:
        print("Aluno aprovado.")
    if avg_final<=4.9:
        print("Aluno reprovado.")
    print("Media final: %.1f" %avg_final)