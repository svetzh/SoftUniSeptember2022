width = int(input())
length = int(input())
height = int(input())

free_space = width * length * height

while True:
    box = input()
    if box == "Done":
        print(f"{free_space} Cubic meters left.")
        break
    free_space -= int(box)

    if free_space <= 0:
        print(f'No more free space! You need {abs(free_space)} Cubic meters more.')
        break
