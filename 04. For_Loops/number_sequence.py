input_number = int(input())

for i in range(input_number):
    current_number = int(input())
    if i == 0:
        min_size = current_number
        max_size = current_number
    if current_number > max_size:
        max_size = current_number
    if current_number < min_size:
        min_size = current_number

print(f"Max number: {max_size}")
print(f"Min number: {min_size}")
