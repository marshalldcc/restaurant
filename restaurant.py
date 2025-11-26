# two - dimensional list for menu items and prices
menu = [["Croissant", 3.95], ["King Cake Slice", 4.95], ["Crawfish", 3.65], 
        ["Catfish Poboy", 14.95], ["Roast Beef Poboy", 13.95], ["Sausage Poboy", 12.95],
        ["Gumbo", 5.95]]

# initial variable declaration
sales_tax = .0945
pies = 0
done = False
subtotal = 0.00

# menu printout
print("Boudreaux & Thibodeaux's Po-Boy Shop")
print("------------------------------------")
print("1. Croissant: $3.95")
print("2. King Cake Slice: $4.95")
print("3. Crawfish Pie (By the Slice): $3.65")
print("4. Catfish Poboy: $14.95")
print("5. Roast Beef Poboy: $13.95")
print("6. Sausage Poboy: $12.95")
print("7. Gumbo: $5.95")
print("-------------------------------------")

# POS function declaration
def point_of_sale():

    pos_total = 0.00
    user_quantity = int(input("Quantity: "))

    if user_choice == 3:
        if (user_quantity >= 8 and (user_quantity % 8 > 0)):
            pies = ((user_quantity - (user_quantity % 8)) / 8)
            print("Item added: {} x Crawfish Pie - ${:.4}".format((pies), (22.00 * pies)))
            pos_total = pos_total + (22.00 * pies)
            user_quantity = user_quantity - (pies * 8)
        if user_quantity > 0:
            print("Item added: {} x Crawfish Slice - ${:.4}".format(user_quantity, (user_quantity * 3.65)))
            pos_total = pos_total + (user_quantity * 3.65)
        return pos_total
    else:
        for item_num in range(len(menu)):
            if item_num == user_choice - 1:
                print("Item added: {} x {} - ${:.4}".format(user_quantity, menu[item_num][0], user_quantity * menu[item_num][1]))
                pos_total = pos_total + (user_quantity * menu[item_num][1])
                return pos_total    
try:
    while done == False:
        user_choice = ""
        user_quantity = ""

        user_choice = input("What would you like to order? " \
        "Type the appropriate number of the menu item or DONE when the order is completed: ")
        if user_choice.lower() != "done":
            user_choice = int(user_choice)
            subtotal += point_of_sale()
        else:
            print("-------------------------------------")
            print("Your total is ${:.4}".format(subtotal + (subtotal * sales_tax)))
            done = True
except:
    print("An error has occurred, this program will only accept a whole number from 1 - 7 or \"done\".")