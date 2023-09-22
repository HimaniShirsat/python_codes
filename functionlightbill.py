def calculate_bill(units):
    if units<=200:
        amount=0
    elif units<=400:
        amount=(units-200)*4
    else:
        amount=200*4+(units-400)*7  
    return amount
unit_consumed=560
total_amount=calculate_bill(unit_consumed)
print(f'the toatl unit consumed is{unit_consumed} the total bill is {total_amount}')               