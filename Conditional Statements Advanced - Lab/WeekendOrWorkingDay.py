weekDay = str(input())

if weekDay == "Saturday" or weekDay == "Sunday":
    print("Weekend")
elif (weekDay == "Monday" or
      weekDay == "Tuesday" or
      weekDay == "Wednesday" or
      weekDay == "Thursday" or
      weekDay == "Friday"):
    print("Working day")
else:
    print("Error")