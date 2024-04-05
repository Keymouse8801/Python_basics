fruit = str(input())
weekday = str(input())
quantity = float(input())
item_price = 0

if weekday == "Monday" \
        or weekday == "Tuesday" \
        or weekday == "Wednesday" \
        or weekday == "Thursday" \
        or weekday == "Friday":
        if fruit == "banana":
            item_price = 2.50
        elif fruit == "apple":
            item_price = 1.20
        elif fruit == "orange":
            item_price = 0.85
        elif fruit == "grapefruit":
            item_price = 1.45
        elif fruit == "kiwi":
            item_price = 2.70
        elif fruit == "pineapple":
            item_price = 5.50
        elif fruit == "grapes":
            item_price = 3.85
elif weekday == "Saturday" \
        or weekday == "Sunday":
        if fruit == "banana":
            item_price = 2.70
        elif fruit == "apple":
            item_price = 1.25
        elif fruit == "orange":
            item_price = 0.90
        elif fruit == "grapefruit":
            item_price = 1.60
        elif fruit == "kiwi":
            item_price = 3.00
        elif fruit == "pineapple":
            item_price = 5.60
        elif fruit == "grapes":
            item_price = 4.20

if item_price == 0:
    print("error")
else:
    print(f'{(item_price * quantity):.2f}')