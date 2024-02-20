chicken_orders = int(input())
fish_orders = int(input())
veg_orders = int(input())
delivery = 2.50

chicken_cost = chicken_orders * 10.35
fish_cost = fish_orders * 12.40
veg_cost = veg_orders * 8.15
desert = 0.20 * (chicken_cost + fish_cost + veg_cost)
total_cost = desert + chicken_cost + fish_cost + veg_cost + 2.50
print(total_cost)
