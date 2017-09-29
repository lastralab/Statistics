import urllib
from BeautifulSoup import *

url = raw_input('Enter website address - ')

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

#Retrieve a list of the anchor tags
#Each tag is like a dictionary of HTML attributes

tags = soup('a')

for tag in tags:

    print 'Retrieving: ', tag.get('href', None)
    
