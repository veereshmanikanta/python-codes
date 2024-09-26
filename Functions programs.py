#functions program
'''To check whether the given numbers are even or odd 
with and without using function'''
'''number1=39
number2=12
number3=9
if (number1%2==0):
    print(number1,'is even')
else:
    print(number1,'is odd')
if (number2%2==0):
    print('{} is even'.format(number2))
else:
    print('{} is odd'.format(number2))
if (number3%2==0):
    print('{} is even'.format(number3))
else:
    print('{} is odd'.format(number3)) '''
#same program using function
'''def evenOrOdd (number):
    "This function is used to check whether the given numberis even or odd"
    if(number%2==0):
        print('{} is even'.format(number))
    else:
        print('{} is odd'.format(number))
evenOrOdd (39)
evenOrOdd (12)
evenOrOdd (9)                  
print(evenOrOdd.__doc__)
print(print.__doc__)'''        
#returning from a function
#prigram to return data from function
'''def cubeOfANumber(number):
    cube=number**3
    return cube
cube=cubeOfANumber(7)
print('result is',cube)'''
#pass by reference, pass by value
#memory locations
#example1
'''a=10
list=[10,20,30]
print(a)
print(list)
list=a
print(list)'''
#example2
'''a=10
list=[10,20,30]
print(a)
print(list)
list[1]=a
print(list)'''
#example1:
'''def calculate(myMarks):
    myMarks[2]=70
marks=[80,98,32,78,89]
calculate(marks)
print(marks)    '''
#example2:
'''def calculate(myMarks):
    myMarks=[70,20,30]
marks=[80,98,32,78,89]
calculate(marks)
print(marks)'''    
#example3:
'''def luckyNumber(number):
    number=20
    return number
number=10
print(luckyNumber(number))
print(number)'''
'''#Default arguments
def box(x=70):
    print(x)
box(90)
box()'''
#keyword arguments
'''def bottleDetails(name,colour,capacity,height):
    print('name: {} colour: {} capacity: {} height: {}'.format(name,colour,capacity,height))
bottleDetails('milton','red','10L','30cm')'''    
'''def bottleDetails(name,colour,capacity,height):
    print('name: {} colour: {} capacity: {} height: {}'.format(name,colour,capacity,height))
bottleDetails(name='milton',colour='red',capacity='10L',height='30cm')'''
#variable number of arguments
'''def alphabets(*letters):
    for alphabet in letters:
        print (alphabet)
alphabets(1,2,3,4) '''
