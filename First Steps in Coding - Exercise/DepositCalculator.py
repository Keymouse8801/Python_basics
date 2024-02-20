deposit_sum = float(input())
deposit_length = int(input())
early_gains = float(input())

# calculate interest
interest = deposit_sum * (early_gains / 100)
monthly_interest = interest / 12

# calculate total sum
total_sum = deposit_sum + (deposit_length * monthly_interest)
print(total_sum)