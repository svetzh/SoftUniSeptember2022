import sys
n = int(input())

max_num = -sys.maxsize
min_num = sys.maxsize
total_suma = 0

for i in range(1, n + 1):
    current_num = int(input())

    if current_num > max_num:
        max_num = current_num

    total_suma = total_suma + current_num

other_num_sum = total_suma - max_num

if other_num_sum == max_num:
    print("Yes")
    print(f"Sum = {max_num}")
else:
    print("No")
    print(f"Diff = {abs(other_num_sum - max_num)}")
