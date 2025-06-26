# main.py
# Importing functions from modular files
from read import read_product_file
from write import write_bill, save_product_file
from process import display_products, restock_product

# Load products from file
filename = "products.txt"
product_list = read_product_file(filename)

# Initialize empty cart to hold purchased items
cart = []

# Main menu loop
while True:
    print("\n1. Display Products")
    print("2. Purchase Products")
    print("3. Restock Product")
    print("4. Generate Bill & Exit")

    option = input("Choose an option: ")

    # Option 1: Show all products
    if option == "1":
        display_products(product_list)

    # Option 2: Purchase flow
    elif option == "2":
        while True:
            display_products(product_list)
            choice = input("\nEnter product index to purchase (or 'f' to finish): ")
            if choice.lower() == 'f':
                break

            try:
                index = int(choice)

                # Check for valid index
                if index < 0 or index >= len(product_list):
                    print("Invalid index.")
                    continue

                selected = product_list[index]
                available_quantity = int(selected[2])

                print("Selected: " + selected[0] + " (" + str(available_quantity) + " in stock)")

                # Ask for paid quantity; calculate free based on Buy 3 Get 1 Free
                paid_quantity = int(input("Enter quantity to pay for (Buy 3 Get 1 Free): "))
                if paid_quantity <= 0:
                    print("Quantity must be positive.")
                    continue

                free = paid_quantity // 3
                total_quantity_needed = paid_quantity + free

                # Check stock availability
                if total_quantity_needed > available_quantity:
                    print("Not enough stock. You need " + str(total_quantity_needed) + " (including " + str(free) + " free).")
                    continue

                # Update stock and add to cart
                product_list[index][2] = str(available_quantity - total_quantity_needed)
                cart.append([selected[0], paid_quantity, free, selected[3]])

                print("Added to cart. You get " + str(free) + " free!")

            except ValueError:
                print("Invalid input. Try again.")

    # Option 3: Restock a selected product
    elif option == "3":
        restock_product(product_list)

    # Option 4: Finalize and generate bill, then exit
    elif option == "4":
        if cart:
            customer_name = input("Enter name: ")
            customer_phone = input("Enter Phone number: ")
            write_bill(cart, customer_name, customer_phone)

        # Save updated product list back to file
        save_product_file(filename, product_list)
        print("Thank you, have a nice day.")
        break

    # Invalid menu option
    else:
        print("Invalid option. Please try again.")

