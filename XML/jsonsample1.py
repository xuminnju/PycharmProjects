import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter location:')
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')
info = json.loads(data)
print('Count:', len(info['comments']))

sum = 0
for result in info['comments']:
    sum += int(result['count'])

print('Sum:',sum)