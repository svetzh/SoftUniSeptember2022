from sys import maxsize

_input = input()
min_num = maxsize

while _input != "Stop":
    number = int(_input)
    if number < min_num:
        min_num = number
    _input = input()
if min_num != maxsize:
    print(min_num)