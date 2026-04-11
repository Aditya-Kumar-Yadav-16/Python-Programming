# Rent Calculator!- mini project
# input- total rent,total food ordered,Electricity units spend, charge per unit!
# output- total amount to pay

rent= int(input("Entre your hostel rent: "))
food = int(input("Enter your total food cost: "))
electricity_units = int(input("Enter electricity units spent: "))
charge_per_unit = int(input("Enter charge per unit: "))
person=int(input("Enter number of people sharing the rent: "))
total_electricity_cost = electricity_units * charge_per_unit

amount_per_person = (rent + food + total_electricity_cost) / person
print("Each person has to pay: ", amount_per_person)
