sec = int(input())
hr=0
min=0
if sec>=3600:
    hr = int(sec/3600)
    sec = sec%3600
if sec>=60:
    min = int(sec/60)
    sec =sec%60
if sec<60:
    sec = sec
print("{}:{}:{}".format(hr,min,sec))