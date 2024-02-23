input_hour = int(input())
input_minute = int(input())

current_minutes = input_minute + 15
if current_minutes > 59:
    input_hour = input_hour + 1
    current_minutes = current_minutes % 60

if input_hour > 23:
    input_hour = input_hour % 24


if current_minutes < 10:
    print(f'{input_hour}:0{current_minutes}')
if current_minutes >= 10:
    print(f'{input_hour}:{current_minutes}')