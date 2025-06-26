# write.py
from datetime import datetime

# Function to save product data back to a file
def save_product_file(filename, products):
    # Open the file in write mode
    with open(filename, 'w') as file:
        # Loop through each product and write it to the file
        for product in products:
            # Create a line for each product with comma-separated values
            line = product[0] + "," + product[1] + "," + product[2] + "," + product[3] + "," + product[4] + "\n"
            # Write the line to the file
            file.write(line)

# Function to generate and save a bill based on the cart items
def write_bill(cart, customer_name, customer_phone):
    # If the cart is empty, print a message and exit the function
    if not cart:
        print("No products purchased.")
        return

    # Get the current date and time
    now = datetime.now()
    
    # Format the date and time as a string in "YYYY-MM-DD HH:MM:SS" format
    showtime = str(now.year) + "-" + str(now.month).zfill(2) + "-" + str(now.day).zfill(2)
    showtime += " " + str(now.hour).zfill(2) + ":" + str(now.minute).zfill(2) + ":" + str(now.second).zfill(2)

    # Print the bill details on the console
    print("\n--- Bill ---")
    print("Date & Time: " + showtime)
    print("Customer Name: " + customer_name)
    print("Customer Phone Number: " + customer_phone)
    print("-" * 80)
    print("Product Name\tPaid Qty\tFree Qty\tUnit Price(Rs)\tTotal (Rs)")
    print("-" * 80)

    # Initialize a variable to store the total cost
    total_cost = 0
    # List to hold the lines for saving the bill to a file
    lines = []

    # Loop through each product in the cart and calculate the total cost
    for product in cart:
        name, paid_quantity, free, price = product
        price = float(price)  # Convert price to float
        total = paid_quantity * price  # Calculate total price for the product
        total_cost += total  # Add to the total cost

        # Adjust tab spacing for product name alignment
        name_tab = "\t\t" if len(name) <= 13 else "\t"
        # Create the line to display in the bill
        line = name + name_tab + str(paid_quantity) + "\t" + str(free) + "\t\t" + str(price) + "\t\t" + str(total)
        # Add the line to the list of bill lines
        lines.append(line)
        # Print the product line in the bill
        print(line)

    # Print the total cost in the bill
    print("-" * 80)
    print("Total Cost: Rs " + str(total_cost))

    # Save the bill details to a text file
    with open("bill.txt", "w") as file:
        file.write("--- Bill ---\n")
        file.write("Date & Time: " + showtime + "\n")
        file.write("Customer Name: " + customer_name + "\n")
        file.write("Customer Phone: " + customer_phone + "\n")
        file.write("-" * 80 + "\n")
        file.write("Product Name\tPaid Qty\tFree Qty\tUnit Price (Rs)\tTotal (Rs)\n")
        file.write("-" * 80 + "\n")
        # Write each line for the products to the file
        for line in lines:
            file.write(line + "\n")
        # Write the total cost to the file
        file.write("-" * 80 + "\n")
        file.write("Total Cost: Rs " + str(total_cost) + "\n")

    # Print a message to indicate that the bill has been saved
    print("Bill saved to bill.txt")
