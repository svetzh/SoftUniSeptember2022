count_of_number = int(input())
left_sum = 0
right_sum = 0

for numbers in range(2 * count_of_number):
    current_number = int(input())
    if numbers < count_of_number:
        left_sum += current_number
    else:
        right_sum += current_number

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    print(f"No, diff = {abs(left_sum - right_sum)}")
