import math

record_in_seconds = float(input())
lenght_in_meters = float(input())
meter_per_second = float(input())

add_time_seconds = math.floor(lenght_in_meters / 15) * 12.5
total_time_seconds = (lenght_in_meters * meter_per_second) + add_time_seconds



if total_time_seconds < record_in_seconds:
    print(f"Yes, he succeeded! The new world record is {total_time_seconds:.2f} seconds.")
else:
    print(f'No, he failed! He was {total_time_seconds - record_in_seconds:.2f} seconds slower.')