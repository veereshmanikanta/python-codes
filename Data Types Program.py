#Numeric (int,float,complex)
marks=765
percentage=(marks/1000)*100
print('Your percentage is',percentage)
print(type(percentage),type(marks))

#complex
x=10+5j
y=5+2j
print(type(x))
print(x.real)
print(x.imag)
print(x.conjugate())
print(x+y)

#sequence types(strings,lists,tuple)
#strings
myName='veeresh manikanta'
print(myName)
myName="veeresh manikanta"
print(myName)
myName='''veeresh manikanta'''#used for multi line string
print(myName)
print(len(myName))#to know the length of the string
print(myName[5])#indexing positive
print(myName[-16])#indexing negative
#slicing [start:end:step] to get sub string in a string
print(myName[8:17])
print(myName[8:17:2])#step by default is 1
print(myName[::1])

#string operations
#1) string concatenation
myName='veeresh manikanta'+'barla'
print(myName)
myName='veeresh manikanta'*3
print(myName)

#Membership operators
myName='veeresh manikanta'
print("barla "in myName)
myName='veeresh manikanta'
print("barla" not in myName) 

#list:
#example for list
names=['veeresh','kumar','vasu','prasanth']
marks=[70,75,85,70]
print(names)
print(type(names))
print(len(names))
print(marks)
print(type(marks))
print(len(marks))
#nested list or multidimension list
bioData=['muralinagar',9866968813,names[0]]
print(bioData)
print('second friend',names[1])#indexing
print('last friend',names[-1])
print('third friend',bioData[2][2])
#updating an item from list using assignment operator=
marks[3]=80 
print(marks)
#list concatenation
print(names+marks)
print(names*2)
#add item/items to the list
names.append('narendra')#for single item .append
print(names)
names.extend(['ravi','chandu'])#for multiple items .extend
print(names)
#how to add at specific position
#'veeresh', 'kumar', 'vasu', 'prasanth', 'narendra', 'ravi', 'chandu'
#70, 75, 85, 80
marks.insert(4,'85')#using .insert for single item
print(marks)
marks[5:5]=["70","75"]#using slicing for multiple items
print(marks)
#delete/Remove list
del names[0]
print(names)#for specific item delete
names.remove('kumar')
print (names)
print(marks.pop(0))
print(marks.pop()) 

#tuple
names=('raju','ramu')
print(names)
print(type(names))
#del names
print(names)

#boolean (true,false)
a=True
print(type(a))
b=False
print(type(b))
a=0
b=1000
print(a!=b)
print(bool(a))

#set
names={'raju','ramu','rakesh'}
print(type(names))
emptySet={}
print(type(emptySet))
emptySet=set()#to create empty set
print(type(emptySet))
#names={'raju','ramu','rakesh',[1,2,3,4]}#we can not keep mutable items in set
#print(names)
names={'raju','ramu','rakesh','raju'}#does not allow duplicate eliments and unordered
print(names)
#we can not use indexind and slicing
#add/update
names.add('ramesh')#to add single item use .add
print(names)
names.update(['sanjay','arjun'])#to add multiple items use .update[]
print(names)
#remove/discard(both operations are)
names.discard('ramesh')
print(names)
names.discard('veeresh')#if item is not in set, no error will come
print(names)

names.remove('raju')
print(names)
#names.remove('veeresh')#if item is not in set,error will come
print(names)
#pop(removes and returns item randomly,because unordered)
names.clear()#to clear the set
print(names)

#Dictionary
#syntax:names={key:value,key:value,key:value}
bioData={'age':'21','city':'vsp',"state":"AP"}
print(bioData)
#nested dictionary
information={'age':'25','city':'hyd',"state":"TS","nested dic":bioData}
print(information)
print(information["age"])
print(bioData.get('age'))

D1={12:{'branch':'EEE','CGPA':80.00},
13:{'branch':'EEE','CGPA':75.00},
14:{'branch':'EEE','CGPA':70.00}}
pin=int(input('Enter your pin'))
CGPA=D1[pin]['CGPA']
if(CGPA>73):
    print('PASS')
else:
    print('FAIL')
