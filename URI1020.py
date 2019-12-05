days =int(input())
print(int(days/365),'ano(s)')
print(int(days%365/30),'mes(es)')
print(int(days%365%30),'dia(s)')