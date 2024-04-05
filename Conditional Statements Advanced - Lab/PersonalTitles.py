age_input = float(input())
gender_input = str(input())

if age_input >= 16:
    if gender_input == "m":
        print("Mr.")
    elif gender_input == "f":
        print("Ms.")
elif age_input < 16:
    if gender_input == "m":
        print("Master")
    elif gender_input == "f":
        print("Miss")