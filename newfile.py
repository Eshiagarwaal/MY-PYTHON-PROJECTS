print("welcome to the tip calculator!")
bill_amount = float(input('enter your total bill amount'))
tip_percentage = int(input('how much tip you would like to give 10, 12, 15?'))
tip_amount = float(bill_amount *tip_percentage/100)
total_bill_amount = bill_amount + tip_amount
no_of_person = int(input('enter the no of person to split the bill amount in'))
amount_person = ( total_bill_amount/ no_of_person)
print(f"your bill amount per person is",amount_person)