needed_money = float(input())
owned_money = float(input())
day_count = 0
days_spending_money = 0

while owned_money < needed_money and days_spending_money < 5:
    type_action = input()
    money = float(input())
    day_count += 1

    if type_action == "spend":
        owned_money -= money
        days_spending_money += 1
        if owned_money < 0:
            owned_money = 0
    elif type_action == "save":
        owned_money += money
        days_spending_money = 0
if days_spending_money == 5:
    print(f'You can\'t save the money.')
    print(f"{day_count}")
else:
    print(f"You saved the money for {day_count} days.")