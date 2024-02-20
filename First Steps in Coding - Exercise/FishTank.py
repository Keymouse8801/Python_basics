# Един литър вода се равнява на един кубичен дециметър/ 1л=1 дм3/.

input_one = int(input())
input_two = int(input())
input_three = int(input())
percentage = float(input()) / 100

total_volume = input_one * input_two * input_three
total_volume_in_dcm = total_volume / 1000
total_taken_volume = total_volume_in_dcm * (1 - percentage)
print(total_taken_volume)
