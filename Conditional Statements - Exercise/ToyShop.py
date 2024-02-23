vacation_price = float(input())
puzzle_order = int(input())
doll_order = int(input())
bear_order = int(input())
minion_order = int(input())
truck_order = int(input())
discount = 0
total_items_order = puzzle_order + doll_order + bear_order + minion_order + truck_order
if total_items_order >= 50:
    discount = 0.25


puzzle_price = puzzle_order * 2.60
doll_price = doll_order * 3
bear_price = bear_order * 4.10
minion_price = minion_order * 8.20
truck_price = truck_order * 2

earnings = puzzle_price + doll_price + bear_price + minion_price + truck_price
discounted_earnings = earnings - (earnings * discount)
clean_earnings = discounted_earnings - (discounted_earnings * 0.10)

if clean_earnings >= vacation_price:
    print(f'Yes! {clean_earnings - vacation_price:.2f} lv left.')
else:
    print(f'Not enough money! {vacation_price - clean_earnings:.2f} lv needed.')

