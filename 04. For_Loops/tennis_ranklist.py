count_tournaments = int(input())
starting_points = int(input())

average_points = 0
percent_all_tournaments = 0
current_average_points = 0
final_points = 0
won_tours = 0

for a_tour in range(1, count_tournaments + 1):
    stage = input()

    if stage == "W":
        average_points = 2000
        starting_points += average_points
        won_tours += 1

    elif stage == "F":
        average_points = 1200
        starting_points += average_points

    elif stage == "SF":
        average_points = 720
        starting_points += average_points

    current_average_points += average_points
    final_points = starting_points

earned_averaged_points = current_average_points // count_tournaments
percent_all_tournaments = (won_tours / count_tournaments) * 100

print(f"Final points: {final_points}")
print(f"Average points: {earned_averaged_points}")
print(f"{percent_all_tournaments:.2f}%")
