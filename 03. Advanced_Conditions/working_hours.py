number: int = int(input())
day = str(input())

working_hours = ""
if 10 <= number <= 18:
    if day == "Monday":
        working_hours = "open"
    elif day == "Tuesday":
        working_hours = "open"
    elif day == "Wednesday":
        working_hours = "open"
    elif day == "Thursday":
        working_hours = "open"
    elif day == "Friday":
        working_hours = "open"
    elif day == "Saturday":
        working_hours = "open"
    elif day == "Sunday":
        working_hours = "closed"
else:
    working_hours = "closed"
print(working_hours)