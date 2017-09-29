fhand = open('mail.txt')
Mon = 0
Tue = 0
Wed = 0
Thu = 0
Fri = 0
Sat = 0
Sun = 0
Total = 0
Lines = 0
for line in fhand:
    line = line.rstrip()
    Lines = Lines + 1
    if not line.startswith('From '): continue
    words = line.split()
    print 'I found: ', words[4]
    Total = Total + 1
    if words[4] == 'Mon' :
        Mon = Mon + 1
    elif words[4] == 'Tue' :
        Tue = Tue + 1
    elif words[4] == 'Wed' :
        Wed = Wed + 1
    elif words[4] == 'Thu' :
        Thu = Thu + 1
    elif words[4] == 'Fri' :
        Fri = Fri + 1
    elif words[4] == 'Sat' :
        Sat = Sat + 1
    elif words[4] == 'Sun':
        Sun = Sun + 1
print 'This is the total per day:'
print 'Mon: ', Mon
print 'Tue: ', Tue    
print 'Wed: ', Wed
print 'Thu: ', Thu
print 'Fri: ', Fri
print 'Sat: ' , Sat
print 'Sun: ', Sun
print 'Total of dates in lines: ', Total
print 'Total of lines in mail: ', Lines
