needed_trip_money = float(input())
puzzle_count = int(input())
dolls_count = int(input())
bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())

puzzle_p = 2.60
dolls_p = 3
bears_p = 4.10
minions_p = 8.20
trucks_p = 2

total_sum = (puzzle_count * 2.6) + (dolls_count * 3) + (bears_count * 4.10) + (minions_count * 8.20) + (trucks_count * 2)
total_count = puzzle_count + dolls_count + bears_count + minions_count + trucks_count

if total_count  >= 50:
    total_sum