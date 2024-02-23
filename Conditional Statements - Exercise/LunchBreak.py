import math
series_name = str(input())
series_lenght = int(input())
break_lenght = int(input())

lunch_time = break_lenght / 8
rest_time = break_lenght * 0.25
time_for_series = break_lenght - (lunch_time + rest_time)

if time_for_series >= series_lenght:
    print(f'You have enough time to watch {series_name} and left with {math.ceil(time_for_series - series_lenght)} minutes free time.')
else:
    print(f"You don't have enough time to watch {series_name}, you need {math.ceil(series_lenght - time_for_series)} more minutes.")
