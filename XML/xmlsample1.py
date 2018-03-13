import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter location:')
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)

sum = 0
results = tree.findall('.//count')
for result in results:
    sum += int(result.text)
print('Count:', len(results))
print('Sum:',sum)