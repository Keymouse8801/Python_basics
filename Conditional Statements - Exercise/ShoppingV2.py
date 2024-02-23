peter_budget = float(input())
num_videocards = int(input())
num_processor = int(input())
num_ram = int(input())

price_videocards = num_videocards * 250
price_processor = price_videocards * 0.35
price_ram = price_videocards * 0.1

total_videocards = price_videocards
total_processor = price_processor * num_processor
total_ram = price_ram * num_ram
total_cost = total_videocards + total_processor + total_ram

if num_videocards > num_processor:
    total_cost *= (1-0.15)

if peter_budget >= total_cost:
    print(f"You have {peter_budget-total_cost:.2f} leva left!")
elif peter_budget < total_cost:
    print(f"Not enough money! You need {total_cost-peter_budget:.2f} leva more!")