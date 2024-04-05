city = input()
sales_volume = float(input())

if sales_volume < 0 or city not in ["Sofia", "Varna", "Plovdiv"]:
    print("error")
else:
    commission = 0

    if 0 <= sales_volume <= 500:
        if city == "Sofia":
            commission = 0.05
        elif city == "Varna":
            commission = 0.045
        elif city == "Plovdiv":
            commission = 0.055
    elif 500 < sales_volume <= 1000:
        if city == "Sofia":
            commission = 0.07
        elif city == "Varna":
            commission = 0.075
        elif city == "Plovdiv":
            commission = 0.08
    elif 1000 < sales_volume <= 10000:
        if city == "Sofia":
            commission = 0.08
        elif city == "Varna":
            commission = 0.1
        elif city == "Plovdiv":
            commission = 0.12
    elif sales_volume > 10000:
        if city == "Sofia":
            commission = 0.12
        elif city == "Varna":
            commission = 0.13
        elif city == "Plovdiv":
            commission = 0.145

    total_commission = sales_volume * commission
    print(f'{total_commission:.2f}')