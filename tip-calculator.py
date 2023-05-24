# introduction
print("Welcome to the tip calculator\n")
# store bill total amount and convert string to float
bill_total = float(input("What was the total bill?\n$"))
# get percentage tip
percentage_tip = float(input("What percentage tip would you like to give?\nEnter a value between 0 and 100.\n")) / 100
# get amount of people
amount_of_people = int(input("How many people should split the bill?\n"))
# calculate the amount that each person has to pay
each_person_amount = round((bill_total / amount_of_people) * (percentage_tip + 1),2)
# print the amount to the console
print(f"Each person should pay: ${each_person_amount}")