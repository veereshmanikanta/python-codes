#control flow program
   
'''lastBall=6
if (lastBall==6):
    print('won the match')
else:
    print('lost the match')'''
    
'''#check whether a number is even or odd
number=int(input('Enter a number'))
if (number%2==0):
    print(number,' is even number')
else:
    print(number,' is odd number')'''
#nested if
#write a program to check whether a number is divided by both 2 and 4
'''number=int(input('Enter a number'))
if (number%2==0):
    if(number%4==0):
        print(number,'is divided by boyh 2 and 4')
    else:
        print(number,'is not divided by boyh 2 and 4')
else:
    print(number,'is not divided by boyh 2 and 4')'''
#if-elif ladder
#Counselling for B.Tech colleges.
#Based on EAMCET rank we prefer colleges...
'''rank = 37400, write a program to assign collegeA if the rank 
 is less than or equal to 1000, assign collegeB if the rank is 
 between 1000 and 10000, assign collegeC if the rank is between 10000 and 40000. 
 If the rank is above 40000 then say 
'Sorry no colleges available for your rank'.'''

''''rank=int(input('Enter your rank'))
if(rank<=1000):
    print('you got college A')
elif (rank>1000 and rank<=10000):
          print('you got college B')
elif (rank>10000 and rank<=40000):
    print('you got college C')
else:
    print('sorry, no colleges available for your rank') '''
#shorthand if
'''rank=1200
if(rank<=1000): print('you got college A')'''
#shorthand if-else
#syntax:statementifTrue if condition else statementifFalse
a=15
#print('even') if (a%2==0) else print('odd')
#For loop
'''numbersList=[1,2,25,36,46,100]
for number in numbersList:
    print(number*5)
    
name='veeresh'
for letter in name:
    print(letter)    '''
#write a program to print 1 to 10 number    
'''for number in range(1,10):
    print(number)'''
 #write a program to print numbers from 100 to 1 in one line
'''for number in range(100,0,-1):
     print(number)'''
'''write a program to print your last 2 characters from your name
and repeat it from 1 to 10'''         
'''name=input('Enter your name')
#print(name[-2:])  
lastTwoCharacters=name[-2:]
for number in range(1,11):
    print(lastTwoCharacters*number)'''
# find vowels and consonents in your name
'''name=input('Enter your name')
vowelsList=['a','e','i','o','u']
for character in name:
    if character in vowelsList:
        print(character,'is vowel')
    else:
        print(character,'is consonent')'''    
#find if your name has a vowel in your name
'''name=input('Enter your name')
vowelsList=['a','e','i','o','u']
for character in name:
    if character in vowelsList:
         print(character,'is vowel')
         break'''
#to find sum of total marks using for loop
'''marks=input('Enter your marks')
marks=[int(z) for z in marks.split(' ')]                                      
sum=0
for number in marks:
     sum=sum+number
print(sum) '''
#while loop
'''i=1
while (i<=10):
    print(i)
    i=(i+1)'''
    
'''Write a program to print 1 to 10
Book cricket:
Consider you have a book of 30 pages
Flip the book till you get 500
Print all the values(scores)
Print number of flips taken to complete the 500 score'''
import random
#print(random.randint(1,30)) 
score=0
scoreInfo=[]
while score<500:
    scoreValue = random.randint(1,30)
    score=score + scoreValue
    scoreInfo.append(scoreValue)
print(len(scoreInfo),scoreInfo,score)    
