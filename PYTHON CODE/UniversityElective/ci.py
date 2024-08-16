def calculate_interest(principal, rate, time):
    amount = principal * (1 + rate/100)**time
    return amount
principal = float(input('Enter Principal Amount: '))
rate = float(input('Enter Annual Interest Rate: '))
time = int(input('Enter Time Period (in Years): '))
amount = calculate_interest(principal, rate, time)
print('Amount after {} years is ₨{}'.format(time, amount))