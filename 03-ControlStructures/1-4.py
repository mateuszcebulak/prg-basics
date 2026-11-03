###
# Credit card payment 
#
payment = 0
account_balance = 500
total_payment = int(input('Give me amount needed to be paid: '))

if total_payment <= account_balance:
    print('Payment completed')
else:
    print('No funds')