###
# Calculates the number of days in a month
#
month = int(input('Enter month number (1..12)'))

if month%2 == 1 :
    days = 31 ## months with 31 days
elif month == 2 :
    days = 28 ## months with 30 days
else :
    days = 30
## February 28 days 

print(f'Month {month} has {days} days')