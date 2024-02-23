film_budget = float(input())
extras_number = int(input())
gear_per_person_cost = float(input())

film_decor = film_budget * 0.10
if extras_number > 150:
    gear_per_person_cost -= gear_per_person_cost * 0.10

total_cost = (gear_per_person_cost * extras_number) + film_decor
if film_budget < total_cost:
    print(f'Not enough money!')
    print(f'Wingard needs {total_cost - film_budget:.2f} leva more.')
else:
    print(f'Action!')
    print(f'Wingard starts filming with {film_budget - total_cost:.2f} leva left.')