early_tax = int(input())

sneakers_price = early_tax - (early_tax * 0.40)
gear_price = sneakers_price - (sneakers_price * 0.20)
ball_price = gear_price * 0.25
accessories_price = ball_price * 0.20

total_cost = early_tax + sneakers_price + gear_price + ball_price + accessories_price
print(total_cost)