init_hours = int(input())
init_minutes = int(input())

total_time_min = (init_hours * 60) + init_minutes + 15

hour = total_time_min // 60
minutes = total_time_min % 60

if hour > 23:
    hour = 0

if minutes < 10:
    print(f"{hour}:0{minutes}")
else:
    print(f"{hour}:{minutes}")
