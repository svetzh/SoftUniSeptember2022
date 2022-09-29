n1 = int(input())
n2 = int(input())
symbol = input()

result = 0
# is_even = True
even_or_odd = ""

if symbol == "+":
    add_result = n1 + n2
    if add_result % 2 == 0:
        even_or_odd = "even"
        print(f"{n1} {symbol} {n2} = {add_result} - {even_or_odd}")
    elif add_result % 2 != 0:
        even_or_odd = "odd"
        print(f"{n1} {symbol} {n2} = {add_result} - {even_or_odd}")
elif symbol == "-":
    subt_result = n1 - n2
    if subt_result % 2 == 0:
        even_or_odd = "even"
        print(f"{n1} {symbol} {n2} = {subt_result} - {even_or_odd}")
    elif subt_result % 2 != 0:
        even_or_odd = "odd"
        print(f"{n1} {symbol} {n2} = {subt_result} - {even_or_odd}")
elif symbol == "*":
    mult_result = n1 * n2
    if mult_result % 2 == 0:
        even_or_odd = "even"
        print(f"{n1} {symbol} {n2} = {mult_result} - {even_or_odd}")
    elif mult_result % 2 != 0:
        even_or_odd = "even"
        print(f"{n1} {symbol} {n2} = {mult_result} - {even_or_odd}")
elif symbol == "/" and n2 != 0:
    dev_result = n1 / n2
    print(f"{n1} / {n2} = {dev_result:.2f}")
elif symbol == "%" and n2 != 0:
    mod_result = n1 % n2
    print(f"{n1} % {n2} = {mod_result}")

if n2 == 0:
    print(f"Cannot divide {n1} by zero")