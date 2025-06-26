# read.py

# Function to read product data from a file
def read_product_file(filename):
    # Initialize an empty list to hold product data
    products = []

    # Open the file in read mode
    with open(filename, 'r') as file:
        # Read all lines from the file
        lines = file.readlines()

    # Loop through each line in the file
    for line in lines:
        # Remove extra spaces and newline characters, then split by commas
        parts = line.replace(" ", "").replace("\n", "").split(',')

        # If the line has exactly 5 parts (Name, Brand, Quantity, Price, Country)
        if len(parts) == 5:
            # Create a product list from the parts
            product = [parts[0], parts[1], parts[2], parts[3], parts[4]]
            
            # Add the product to the products list
            products.append(product)

    # Return the list of products
    return products
