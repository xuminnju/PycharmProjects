import re
file = open('regex_sum_70597.txt').read()
num = re.findall('[0-9]+', file)
sum = 0
for i in num:
    sum = sum + int(i)
print(sum)