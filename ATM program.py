#ATM program
'''pin=input('enter your pin')
cash=input('enter your cash')'''
pin,cash=input ('Enter your PIN and cash' ).split(' ')
cashValue=int(cash)
atmAmount=50000
balanceAmount=atmAmount-cashValue
'''print('please collect your cash',cashValue)
print('balanceAmount is: ',balanceAmount)
print('Thank you for using ATM')'''
#placeholder{}
print('Take your cash{}\nbalanceAmount in your account is{}'.format(cashValue,balanceAmount))