# Finding a product scans the list item by item -> O(n)
 
def find_product_in_list(product_list, target_sku):

    for sku, price in product_list:

        if sku == target_sku:

            return price

    return None
 
 
product_list = []
 
with open("products.csv", "r") as file:

    file.readline()  # Skip header row

    for line in file:

        parts = line.strip().split(",")

        sku = parts[0]

        price = parts[1]

        product_list.append((sku, price))
 
 
# Versus
 
 
# Finding a product jumps straight to the key -> O(1)
 
def find_product_in_dict(product_dictionary, target_sku):

    return product_dictionary.get(target_sku)
 
 
product_dictionary = {}
 
with open("products.csv", "r") as file:

    file.readline()  # Skip header row

    for line in file:

        parts = line.strip().split(",")

        sku = parts[0]

        price = parts[1]

        product_dictionary[sku] = price
 