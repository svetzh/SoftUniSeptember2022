import sys

input_1 = input()
maxi_num = -sys.maxsize

while input_1 != "Stop":
    num = int(input_1)

    if num > maxi_num:
        maxi_num = num
    input_1 = input()
if maxi_num != -sys.maxsize:
    print(maxi_num)
