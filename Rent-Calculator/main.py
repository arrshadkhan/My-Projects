print("=" * 40)
print("      ROOM EXPENSE CALCULATOR")
print("=" * 40)

rent = float(input("Enter monthly room rent (₹): "))
electricity_units = float(input("Enter total electricity units consumed: "))
food_cost = float(input("Enter total food cost (₹): "))
roommates = int(input("Enter number of students sharing the room: "))

# Electricity rate
rate_per_unit = 7
electricity_bill = electricity_units * rate_per_unit

# Total expense
total_expense = rent + electricity_bill + food_cost

# Per person expense
per_person_cost = total_expense / roommates

print("\n" + "=" * 40)
print("           EXPENSE SUMMARY")
print("=" * 40)
print(f"Room Rent         : ₹{rent:.2f}")
print(f"Electricity Bill  : ₹{electricity_bill:.2f}")
print(f"Food Cost         : ₹{food_cost:.2f}")
print("-" * 40)
print(f"Total Expense     : ₹{total_expense:.2f}")
print(f"Students Sharing  : {roommates}")
print("-" * 40)
print(f"Cost Per Student  : ₹{per_person_cost:.2f}")
print("=" * 40)