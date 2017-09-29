import urllib
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break
#correct way of writing the address:
    url = serviceurl + urllib.urlencode({'sensor':'false',
                                         'address': address})
    print 'Retreiving: ', url
    uh = urllib.urlopen(url) 
    data = uh.read() #read the whole thing
    print 'Retreived: ', len(data), 'characters'
#if data is bad we want to exit:
    try : js = json.loads(str(data))
    except: js = None
    if 'status' not in js or js['status'] != 'OK' :
        print '==== Failure To Retrieve ====' # status is not OK
        print data
        continue

    print json.dumps(js, indent=4) #takes js dictionary
    # and pretty printing for humans to read
#Parsing:
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
#results is a list
    #[0]subzero is to look at the first element in the list
    print 'latitude:', lat, 'longitude:', lng
    location = js['results'][0]['formatted address']

    print location
