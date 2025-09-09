name = input("What is your name?\n")

# MENU
menu = ["chicken", "burger", "pasta"]
prices = {"chicken": 12, "burger": 10, "pasta": 8}

if name.strip().lower() == "ben":
    answer = input("Ben, are you evil?\n").strip().lower()
    if answer == "yes":
        print("Get out!!!!!!")
        exit()
    else:
        print(f"Hello {name}, what would you like from our menu? We have: {', '.join(menu)}")
        order = input().strip().lower()
        respond = input("Ben, I am glad you are not evil. I hate evil Bens. You look good today.\n").strip().lower()
        if respond != "thanks":
            print("Where is your manners Ben? Get out!!!")
            exit()
else:
    print(f"Hello {name}, what would you like from our menu? We have: {', '.join(menu)}")
    order = input().strip().lower()

while order not in menu:
    print(f"We do not have that. Please choose from: {', '.join(menu)}")
    order = input().strip().lower()

price = prices[order]
print(f"{order.capitalize()} will be £{price}")

amount = input("How many do you want?\n")
total = int(amount) * price

if int(amount) > 1:
    print(f"Sounds good {name}, we will have the {order}'s ready for you in a moment. Your total will be £{total}.")
else:
    print(f"Sounds good {name}, we will have the {order} ready for you in a moment. Your total will be £{total}.")
print("\n-------RECIEPT-------")
print(order.capitalize(),"x", amount, "=", "£" + str(prices[order]))
print("TOTAL: ","£", total)
print("---------------------\n")
print("Thanks for your order", name, "Enjoy the meal!")