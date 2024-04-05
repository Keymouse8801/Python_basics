product = str(input())
Ptype = ""

if product == "banana" or \
    product == "apple" or \
    product == "kiwi" or \
    product == "cherry" or \
    product == "lemon" or \
    product == "grapes":
    Ptype = "fruit"
elif product == "tomato" or \
    product == "cucumber" or \
    product == "pepper" or \
    product == "carrot":
    Ptype = "vegetable"
else:
    Ptype = "unknown"

print(Ptype)