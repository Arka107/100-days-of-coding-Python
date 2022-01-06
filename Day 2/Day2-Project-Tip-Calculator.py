print("Start of the Project")
print("Welcome to Tip Calculator")
bill = float((input("What was the total bill? ")))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
group = int(input("How many people to split the bill?"))
value = (tip/100)+1
final_amount = float(((bill/group)*value))
print(f"Each person has to pay ${final_amount:0.2f}.")
