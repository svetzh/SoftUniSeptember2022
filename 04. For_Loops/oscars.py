name_actor = input()
academy_points = float(input())
count_critics = int(input())

for i in range(count_critics):
    critics_name = input()
    length_of_critics_name = len(critics_name)
    critics_points = float(input())
    academy_points += length_of_critics_name * critics_points / 2

    if academy_points > 1250.5:
        break

control_number = 1250.5

if academy_points > control_number:
    print(f"Congratulations, {name_actor} got a nominee for leading role with {academy_points:.1f}!")
else:
    print(f"Sorry, {name_actor} you need {(control_number - academy_points):.1f} more!")