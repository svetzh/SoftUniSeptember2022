width = int(input())
length = int(input())
total_cake_pieces = width * length

while True:
    command = input()
    if command == "STOP":
        print(f"{total_cake_pieces} pieces are left.")
        break
    total_cake_pieces -= int(command)

    if total_cake_pieces <= 0:
        print(f"No more cake left! You need {abs(total_cake_pieces)} pieces more.")
        break

