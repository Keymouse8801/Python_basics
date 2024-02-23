peter_budget = float(input())
video_cards = int(input())
processors = int(input())
rams = int(input())

discount = 0
if video_cards > processors:
    discount = 0.15

video_price = video_cards * 250
processor_price = (0.35 * video_price) * processors
ram_price = (0.10 * video_price) * rams

total_price = video_price + processor_price + ram_price
total_discount_price = total_price - (total_price * discount)

if peter_budget >= total_discount_price:
    print(f'You have {peter_budget - total_discount_price:.2f} leva left!')
else:
    print(f'Not enough money! You need {total_discount_price - peter_budget:.2f} leva more!')
