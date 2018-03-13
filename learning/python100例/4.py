y = int(input('年份：\n'))
m = int(input('月份：\n'))
d = int(input('日期：\n'))
month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]

def base(i):
    collection = 0
    for i in range(0, m):
        collection += month[i]
    return collection
if y < 0 or m < 0 or m > 12 or d < 0 or d > 31:
    print('输入错误！')
else:
    if (y%100 == 0 and y%400 ==0) or (y%100 != 0 and y%4 ==0):
        if m <=2:
            result = base(m) + d
        if m > 2:
            result = base(m) + d + 1
    else:
        result = base(m) + d
    print('这一天是一年的第%d天' %result)