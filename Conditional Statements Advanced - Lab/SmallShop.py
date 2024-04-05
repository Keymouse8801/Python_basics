product_input = str(input())
city_input = str(input())
quantity_input = float(input())
price = 0

# Sofia products
if city_input == "Sofia":
    if product_input == "coffee":
        price = quantity_input * 0.50
    elif product_input == "water":
        price = quantity_input * 0.80
    elif product_input == "beer":
        price = quantity_input * 1.20
    elif product_input == "sweets":
        price = quantity_input * 1.45
    elif product_input == "peanuts":
        price = quantity_input * 1.60
# Plovdiv products
elif city_input == "Plovdiv":
    if product_input == "coffee":
        price = quantity_input * 0.40
    elif product_input == "water":
        price = quantity_input * 0.70
    elif product_input == "beer":
        price = quantity_input * 1.15
    elif product_input == "sweets":
        price = quantity_input * 1.30
    elif product_input == "peanuts":
        price = quantity_input * 1.50
# Varna products
elif city_input == "Varna":
    if product_input == "coffee":
        price = quantity_input * 0.45
    elif product_input == "water":
        price = quantity_input * 0.70
    elif product_input == "beer":
        price = quantity_input * 1.10
    elif product_input == "sweets":
        price = quantity_input * 1.35
    elif product_input == "peanuts":
        price = quantity_input * 1.55

print(price)
