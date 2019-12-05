amount= int(input())
notes_100 = 0
notes_50 = 0
notes_20 = 0
notes_10 = 0
notes_5 = 0
notes_2 = 0
notes_1 = 0
print(amount)

if amount>=100 :
    notes_100 = amount/100
    notes_100 = int(notes_100)
    amount = amount % 100
if amount>=50 :
    notes_50 = amount/50
    notes_50 = int(notes_50)
    amount = amount % 50
if amount>=20 :
    notes_20 = amount/20
    notes_20 = int(notes_20)
    amount = amount % 20
if amount>=10 :
    notes_10= amount/10
    notes_10 = int(notes_10)
    amount = amount % 10
if amount>=5:
    notes_5 = amount/5
    notes_5 = int(notes_5)
    amount = amount % 5
if amount >= 2:
    notes_2 = amount/2
    notes_2 = int(notes_2)
    amount = amount % 2
if amount>=1 :
    notes_1 = amount
    notes_1=int(notes_1)

print(notes_100,'nota(s) de R$ 100,00')
print(notes_50,'nota(s) de R$ 50,00')
print(notes_20,'nota(s) de R$ 20,00')
print(notes_10,'nota(s) de R$ 10,00')
print(notes_5,'nota(s) de R$ 5,00')
print(notes_2,'nota(s) de R$ 2,00')
print(notes_1,'nota(s) de R$ 1,00')


