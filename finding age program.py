#find age of a person by asking their birth year
from datetime import date
birthYear=int(input('Enter your birthyear'))
currentYear=(date.today().year)
presentAge=currentYear-birthYear
print('your age is:',presentAge)

'''from datetime import date
from dateutil.relativedelta import relativedelta

# Get the birth date from the user
day, month, year = map(int, input('Enter your birth day, month, and year (separated by spaces): ').split())

# Get the current date
current_date = date.today()

# Calculate the difference between current date and birth date
birth_date = date(year, month, day)
difference = relativedelta(current_date, birth_date)

# Output the age in years, months, and days
print(f'Your age is: {difference.years} years, {difference.months} months, and {difference.days} days.')
'''