###
# Checks whether at least one number entered
# from the keyboard is not negative
# 
x = int(input('Enter first number: '))
y = int(input('Enter second number: '))

if not x < 0 or not y <2 :
    print(f'At least one of the numbers {x} and {y} is not negative')
else :
    print(f'neither of those numbers are non negative')
