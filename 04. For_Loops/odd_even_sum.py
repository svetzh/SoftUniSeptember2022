n_of_numbers = int(input())
odd_sum = 0
even_sum = 0
for position in range(1, n_of_numbers + 1):
    current_num = int(input())
    if position % 2 != 0:
        odd_sum += current_num
    else:
        even_sum += current_num
if even_sum == odd_sum:
    print("Yes")
    print(f"Sum = {even_sum}")
else:
    print("No")
    print(f"Diff = {abs(even_sum - odd_sum)}")
