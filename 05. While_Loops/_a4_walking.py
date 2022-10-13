goal_steps_a_day = 10000
sum_track_steps = 0
while True:
    track_steps = input()
    if track_steps == "Going home":
        track_steps = int(input())
        sum_track_steps += track_steps
        if sum_track_steps >= goal_steps_a_day:
            print("Goal reached! Good job!")
            print(f"{abs(sum_track_steps - goal_steps_a_day)} steps over the goal!")
        else:
            print(f"{goal_steps_a_day - sum_track_steps} more steps to reach goal.")
        break
    sum_track_steps += int(track_steps)
    if sum_track_steps >= goal_steps_a_day:
        print("Goal reached! Good job!")
        print(f"{abs(sum_track_steps - goal_steps_a_day)} steps over the goal!")
        break
