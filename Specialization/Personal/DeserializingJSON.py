import json
input = '''[
    { "id" : "001",
    "x" : "2",
    "name" : "Tania"
    } ,
    { "id" : "009",
    "x" : "7",
    "name" : "Grace"
    } ,
       { "id" : "023",
    "x" : "8",
    "name" : "Clara"
    } ,
       { "id" : "012",
    "x" : "9",
    "name" : "Grego"
    }
    
]''' # [] means list, {} are objects (things):
#thing 0 and thing 1 in this case.

info = json.loads(input)
print 'User count:', len(info)

for item in info: #looks into objects (standard python)
    print 'Name:', item['name']
    print 'ID:', item['id']
    print 'Attribute', item['x']
