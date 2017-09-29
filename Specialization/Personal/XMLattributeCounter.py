import urllib
import xml.etree.ElementTree as ET

while True:
    address = 'http://python-data.dr-chuck.net/comments_372357.xml?'
    print 'Retrieving', address
    uh = urllib.urlopen(address)
    data = uh.read()
    print 'Retrieved',len(data),'characters'
    tree = ET.fromstring(data)
    lst = tree.findall('comments/comment') #path of data we want 
    print 'Count: ', len(lst) #length of data
    num = 0 #creates list of integers
    for item in lst:
        x = item.find('count').text
        num = num + int(x) #sums to previous number the new one
    print 'Sum: ', num #sum of items
    break

