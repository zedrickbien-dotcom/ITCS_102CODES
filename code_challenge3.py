#item = ipad


name = input("enter your name -----> ")
item = input(" what is your item -----> ")
is_fragile = bool(input("what type of item -----> "))

if is_fragile == True:
    print("handle it safely")
else:
    print("not fragile.")

weight = float(input("how much weight is the item (in kg)? "))
distance = float(input("how many distace (in km)? "))

#base cost 
base_cost = weight * 2.50
base_cost2 = distance * 0.15
base_cost3 = base_cost + base_cost2

#total of internal and express
total_int = base_cost3 * 1.40
total_int2 = total_int + 50

#total of express or international shipping
total_or = base_cost3 * 1.20
total_or2 = total_or = 25

#oversize > 30kg and > 1000km
total_os = base_cost3 + 30

#standard rate
total_sr = base_cost3

#free shipping
free_ship = 0

is_express = bool(input("is it express shipping"))
if is_express == True:
    print("answer is true")
else:
    print("okay")

is_international = bool(input("is it international shipping"))
if is_express == 'True' and is_international == true:
      print("the shipping would amount to:",total_int2)
elif is_express == 'True' or is_international == 'True' and weight > 50:
    print("the shipping would amount to:",total_or2)
elif weight > 60 or distance > 100:
     print("package oversize. The shipping would amount to:",total_os)
elif weight <= 5.0 and distance <=100 and is_express != 'True' and is_international != 'True':
     Print("the shipping would amount to:", free_ship)
else:
     print("the shipping would amount to:",base_cost3)