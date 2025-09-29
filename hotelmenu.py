# menu for restaurant
menu = {
    "pizza" : 60,
    "pasta" : 20,
    "chowmein" : 10,
    "bhalla" : 30,
    "momos" : 10,
}
print(menu)
print("welcome to our restaurant")
print("pizza = 60rs\npasta = 20rs\nchowmein = 10rs\nbhalla = 30rs\nmomos = 10rs")
order_total = 0

item_1 = input("enter the name of item that you want to be order = ")
if item_1 in menu:
    order_total += menu[item_1] # 0+ amount of order
    print(f"your item {item_1} has been added to your order")

else:
    print(f"orderd item {item_1} is not availabe yet")

another_order = input("do you want another item? (yes/no)") 
if another_order == "yes":
    item_2 = input("enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"item {item_2} has been added to order")
    else:
        print(f"ordered itme {item_2} is not available")

print(f"the total amount of your order to pay = {order_total}")        
