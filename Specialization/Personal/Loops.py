
''' While x is less than 10 it will print x and add 1 to that number,
    then print it and so on until that condition is false, which is
    when x equals 10 '''

condition = input('Enter number: ')
x = int(condition)
print (' ')
print ('While loop:')
while x <= 10:
    print (x)
    x += 1
    # will stop adding 1 when it reaches 11

while x > 10:
    print('True')
    print (x)
    print('Number is higher than 10')
    break # otherwise it will print True forever, like this:
# uncomment to run and watch:
'''
while True:
    print('infinite')
'''
print (' ')
print ('For Loop: ')

exampleList = [1,6,7,3,6,9,0]
print (' ')
print ('See code for reference')
print (' ')
for thing in exampleList:
    print (thing)
print (' ')
print ('For x in range loop:')
print (' ')
for x in range (1,11): # range is not in list, this is separate
    print (x)

