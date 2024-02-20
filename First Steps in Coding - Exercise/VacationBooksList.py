pages_current_book = int(input())
pages_per_hour = int(input())
days = int(input())

total_time_per_book = pages_current_book / pages_per_hour
hours_reading = total_time_per_book / days

print(int(hours_reading))

