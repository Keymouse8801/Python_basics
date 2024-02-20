# Needed Inputs:
naylon_needed = int(input())
paint_needed = int(input())
thinner_needed = int(input())
hours_needed = int(input())

# prices
naylon_price = (naylon_needed + 2) * 1.50
paint_price = (paint_needed + (paint_needed * 0.10)) * 14.50
thinner_price = thinner_needed * 5.00
add_cost = 0.40
total_material = naylon_price + paint_price + thinner_price + add_cost
hour_cost = total_material * 0.30
total_work_cost = hours_needed * hour_cost

all_costs = total_work_cost + total_material
print(all_costs)