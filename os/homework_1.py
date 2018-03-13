import os,datetime

flag = '<DIR>' if os.path.isdir('.') else ' '


list = os.listdir('.')
for i in list:
    fname = i
    fsize = os.path.getsize(fname)
    ftime = (datetime.datetime.fromtimestamp(os.path.getmtime(fname))).strftime('%Y/%m/%d  %H:%M')
    flag = '<DIR>' if os.path.isdir(i) else ' '
    print('%s\t\t%s\t%10d\t\t%s' %(ftime,flag,fsize,fname))
