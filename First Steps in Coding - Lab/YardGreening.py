work_meters = float(input())

sq_meter_price = 7.61
sq_meter_total_price = work_meters * sq_meter_price
discount = sq_meter_total_price * 0.18
discount_total = sq_meter_total_price - discount

print(f'The final price is: {discount_total} lv.')
print(f'The discount is: {discount} lv.')