menu={
    "Coffe":40,
     "Tea":20,
    "Noodles":90,
    "Fired Rice":90,
    "Burger":120,
    "juice":60,
}
print("welcome to the hotel \n here is the menu" )
print("Coffe = 40rs\n tea = 20rs\n Noodles = 90rs\nFried Rice= 90rs\nBurger = 120rs\n juice = 60\n")
total_order =0
item1=input('enter the item name you want to order')
if item1 in menu:
    total_order += menu[item1]
    print(f"your added item {item1} will be served soon")
else:
    print("your item is not avilabel")

decision=input("do u want to order any thing else, type yes or no")
if decision == "yes":
    item2=input("enter the second item")
    if item2 in menu:
     total_order += menu[item2]
    print(f"your item is added {item2} will be served soon")
else:
    print("your item is not avilabel ")

print(f"the total amount of item you ordered {total_order} ")








