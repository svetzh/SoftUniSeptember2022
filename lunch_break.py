from math import ceil

series_name = input()
episode_duration = int(input())
break_duration = int(input())

lunch_time = break_duration * 1 / 8
chill_out_time = break_duration * 1 / 4
time_left = break_duration - (lunch_time + chill_out_time)

if episode_duration <= time_left:
    print(f"You have enough time to watch {series_name} and "
          f"left with {ceil(time_left - episode_duration)} minutes free time.")
else:
    print(f"You don't have enough time to watch {series_name}, you need {ceil(episode_duration - time_left)} "
          f"more minutes.")