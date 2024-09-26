#namespace and scope
#example 1:
sum =10 #global scope
def calculate():
    currentSum =200 #local scope
    totalSum=sum+currentSum
    print ('example1 output is:',totalSum)
calculate();

#example 2:
sum=100
def calculate():
    currentSum=500
    totalSum=sum+currentSum
    print('example2 output is:',totalSum)
calculate();
#print(currentSum)

#example 3:
sum=100
def calculate():
    sum=700
    sum=sum+200
    currentSum=100
    totalSum=sum+currentSum
    print('example3 output is:',totalSum)
calculate();
print ("\t"*5,sum)

#example4:
sum=50
def calculate():
    global sum
    sum=100
    currentSum=200
    totalSum=sum+currentSum
    print('example4 output is:',totalSum)
calculate();
print("\t"*4+"   ",sum)