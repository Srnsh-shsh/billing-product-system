# process.py
# Function to display all available products
def display_products(products):
    # If product list is empty, inform the user
    if not products:
        print("No products to display.")
        return

    # Display table header
    print("\n--- Available Products ---")
    print("Index\tProduct Name\tBrand\t\tQuantity\tCost Price (Rs)\tCountry")
    print("-" * 80)

    # Loop through the product list using a while loop
    i = 0
    while i < len(products):
        product = products[i]

        # Adjust tab spacing if brand name is short
        brand_tab = "\t" if len(product[1]) < 8 else ""

        # Print product details in a formatted row
        print(
            str(i) + "\t" + product[0] + "\t" + product[1] + brand_tab +
            "\t" + product[2] + "\t\t" + product[3] + "\t\t" + product[4]
        )
        i += 1

# Function to restock an existing product
def restock_product(products):
    # First, show the list of products
    display_products(products)
    try:
        # Ask user which product to restock (by index)
        index = int(input("\nEnter the index of the product to restock: "))
        
        # Validate index range
        if index < 0 or index >= len(products):
            print("Invalid index.")
            return

        # Ask how many units to add
        amount = int(input("Enter the quantity to add: "))
        if amount <= 0:
            print("Invalid quantity.")
            return

        # Update the quantity of the selected product
        current_quantity = int(products[index][2])
        products[index][2] = str(current_quantity + amount)
        print("Product restocked successfully.")

    except ValueError:
        # Handle non-integer input errors
        print("Invalid input. Please enter numbers only.")
