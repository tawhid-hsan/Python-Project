print("Thanks For Choosing Our Sportswear Shop")

# Initialize the item dictionary
item_dict = {}

# Load data from file
f = open("F:/Sports Wear.txt", "r")
while True:
        item = f.readline()
        if item == "":
            break
        quantity = f.readline()
        price = f.readline()
        item = item.strip()
        quantity = int(quantity.strip())
        price = float(price.strip())
        item_dict[item] = [quantity, price]

ml = 40
iml = 30

def show_dict():
    print(ml * "=")
    print("Available Sports Equipments and Quantity")
    print(ml * "=")
    for x in item_dict:
        print(x, (iml - len(x)) * " ", (6 - len(str(item_dict[x][0]))) * " ", item_dict[x][0])
    print(ml * "-")

def dec_quant(key, val):
    item_dict[key][0] -= val

def inc_quant(key, val):
    item_dict[key][0] += val

def process_order():
    print("Input Order Details:")
    while True:
        item = input("Items (Enter 'x' to stop): ").strip()
        if item.lower() == "x":
            break
        value = int(input("Quantity: "))
        if item not in item_dict:
            print("New Item Found!")
            uprice = float(input("Unit Price: "))
            item_dict[item] = [value, uprice]
        else:
            inc_quant(item, value)

def sell_order():
    print("Output Sell:")
    order_list = []

    while True:
        item = input("Items (Enter 'x' to stop): ").strip()
        if item.lower() == "x":
            break
        if item not in item_dict:
            print(f"The item '{item}' is not available")
            continue
        value = int(input("Quantity: "))
        if value > item_dict[item][0]:
            print(f"Only {item_dict[item][0]} quantity is available")
            continue
        dec_quant(item, value)
        order_list.append([item, value, item_dict[item][1], value * item_dict[item][1]])

    # Printing the payment receipt
    print(ml * "=")
    print("** Payment Receipt **".center(ml))
    print(ml * "=")
    print("Item"," " *7 ,"Quant.", " ", "U.Price", "  ", "S.Total")
    print(ml * "-")
    
    tprice = 0
    for x in order_list:
        tprice += x[3]
        print(f"{x[0].title():<10}{x[1]:>7}{x[2]:>10.2f}{x[3]:>12.2f}")
    
    print(ml * "-")
    print(f"Total Price: {tprice:.2f}")
    print(order_list)

# Main program
while True:
    show_dict()
    print("Choose an Option:")
    print("Type '1': To Process Order")
    print("Type '2': To Sell Order")
    print("Type '3': To Exit The Program")
    choice = input("Choice: ").strip()
    if choice == '1':
        process_order()
    elif choice == '2':
        sell_order()
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please try again.")
