count_of_numbers = int(input())

for number in range(count_of_numbers):
    current_num = int(input())
    if number == 0:
        min_num = current_num
        max_num = current_num
    if current_num > max_num:
        max_num = current_num
    if current_num < min_num:
        min_num = current_num
print(f"Max number: {max_num}")
print(f"Min number: {min_num}")

