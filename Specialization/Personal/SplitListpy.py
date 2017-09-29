fh = open('Python/romeo.txt')
lst = list()                       
for line in fh:                   
    word= line.rstrip().split()  
    for element in word:              
        if element in lst:         
            continue              
        else :                    
            lst.append(element)        
lst.sort()                        
print lst                
