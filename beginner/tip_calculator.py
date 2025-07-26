print("welcome to the Tip Calculator! 😊")

bill = float(input("What was the total bill? 💲"))
tip = int(input("What amount tip would you like to give? 10%, 12%, or 15%💸 "))
people = int(input("How many people split the bill?🧑🏽‍🤝‍🧑🏼 "))
tip_percent = tip/100
tip_total = bill*tip_percent
bill_total = bill+tip_total
bill_per_person = bill_total/people
#round() func - (eg. round(value, n)) where n is decimal places.
final_amount = round(bill_per_person, 2)
#format string or f-string is to interpolate values, variables and objects into a string.
print(f"Each person should pay 💲{final_amount}")