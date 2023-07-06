menu=[]
def display_menu():
    print("Welcome to Khana App: Foodies Delight Dash")
    print("========================================")
    print("1. Display the All orders")
    print("2. Add a new dish to the menu")
    print("3. Remove a dish from the menu")
    print("4. Update dish availability")
    print("5. Take a new order")
    print("6. Display menu")
    print("7. Upadate the order details")
    print("8. Exit")

# display_menu()

# print the menu

def show_menu():
    if len(menu)==0:
        print("This menu is empty.")
    else:
        print("Current Menu:")
        print("============")
        for dish in menu:
            print(f"Dish ID: {dish['id']}")
            print(f"Name:{dish['name']}")
            print(f"Price: {dish['price']}")
            print(f"Availability: {'Available' if dish['available'] else 'Not available'}")
            print("-----------------------------------------------")
    # show_menu()

# add new menu

def add_dish():
    dish_id=input("Enter the dish ID: ")
    dish_name=input("Enter the dish name: ")
    dish_price=float(input("Enter the dish price: "))
    dish_available=input("Is the dish available? (yes/no): ").lower()=="yes"

    new_dish={
        "id":dish_id,
        "name":dish_name,
        "price":dish_price,
        "available":dish_available
    }

    menu.append(new_dish)
    print(f"Dish `{dish_name}` has been added to the menu.")
# add_dish()

# remove the dish

def remove_dish():
    dish_id=input("Enter the dish ID to remove: ")
    removed=False

    for dish in menu:
        if dish['id']==dish_id:
            menu.remove(dish)
            removed=True
            print(f"Dish ID `{dish_id}` has been removed from the menu.")
            break

        if not removed:
            print(f"No dish found with ID `{dish_id}.`")
# remove_dish()

def update_dish_availability():
    dish_id=input("Enter the dish ID to update availability: ")
    availability=input("Is the dish available? (yes/no): ").lower()=="yes"
    updated=False

    for dish in menu:
        if dish["id"]==dish_id:
            dish["available"]=availability
            updated=True
            print(f"Dish with ID `{dish_id}` availability has been updated.")
            break

        if not updated:
            print(f"No dish found with ID `{dish_id}`.")

# update_dish_availability()

# new order
# Define the orders list
orders = []

# Function to take a new order
def take_order():
    customer_name = input("Enter customer name: ")
    dish_ids = input("Enter the dish IDs (comma-separated) the customer wants to order: ").split(",")

    new_order = {
        "customer_name": customer_name,
        "dish_ids": dish_ids,
        "status": "received"
    }

    if len(orders) == 0:
        new_order["order_id"] = 1
    else:
        new_order["order_id"] = orders[-1]["order_id"] + 1

    orders.append(new_order)

    print("New order has been placed.")



# take_order()

# order status

# Function to update order status
def update_order_status():
    order_id = input("Enter the order ID to update status: ")
    new_status = input("Enter the new status of the order: ")

    updated = False

    for order in orders:
        print (order["order_id"])
        if str(order["order_id"]) == order_id:
            order["status"] = new_status
            updated = True
            print(f"Order with ID '{order_id}' status has been updated.")
            break

    if not updated:
        print(f"No order found with ID '{order_id}'.")




# revew the all orders

# Function to review all orders
def review_orders():
    if len(orders) == 0:
        print("No orders to review.")
    else:
        print("All Orders:")
        print("============")
        for order in orders:
            print(f"Order ID: {order['order_id']}")
            print(f"Customer Name: {order['customer_name']}")
            print(f"Dish IDs: {', '.join(order['dish_ids'])}")
            print(f"Status: {order['status']}")
            print("------------------------")

# Call the review_orders() function to review all orders
review_orders()

# review_orders()

# exit the program

def exit_program():
    print("Thank you for using Khana App. Have a great day!")
    exit()

# exit_program()


# Main program loop
while True:
    display_menu()

    choice = input("Enter your choice: ")

    if choice == "1":
        review_orders()
    elif choice == "2":
        add_dish()
    elif choice == "3":
        remove_dish()
    elif choice == "4":
        update_dish_availability()
    elif choice == "5":
        take_order()
    elif choice == "6":
        show_menu()
    elif choice == "7":
        update_order_status()
    elif choice == "8":
        exit_program()
    else:
        print("Invalid choice. Please try again.")
    print()
