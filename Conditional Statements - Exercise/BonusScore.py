points = int(input())
bonus = 0
total_points = points + bonus

if points <= 100:
    bonus = 5
elif 1000 >= points > 100:
    bonus = 0.2 * points
elif points > 1000:
    bonus = 0.1 * points

add_bonus = 0
if total_points % 2 == 0:
    add_bonus = 1
elif total_points % 10 == 5:
    add_bonus = 2

print(bonus + add_bonus)
print(bonus + add_bonus + points)
