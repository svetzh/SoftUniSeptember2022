exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

sum_exam_mins = (exam_hour * 60) + exam_minute
sum_arrival_mins = (arrival_hour * 60) + arrival_minute

diff_mins = abs(sum_exam_mins - sum_arrival_mins)

if sum_arrival_mins > sum_exam_mins:
    print("Late")
    if diff_mins >= 60:
        hour = diff_mins // 60
        minutes = diff_mins % 60
        print(f"{hour}:{minutes:02d} hours after the start")
    else:
        print(f"{diff_mins} minutes after the start")
elif sum_exam_mins == sum_arrival_mins or diff_mins <= 30:
    print("On time")
    if diff_mins > 0:
        print(f"{diff_mins} minutes before the start")
else:
    print("Early")
    if diff_mins >= 60:
        hour = diff_mins // 60
        minutes = diff_mins % 60
        print(f"{hour}:{minutes:02d} hours before the start")
    else:
        print(f"{diff_mins} minutes before the start")
