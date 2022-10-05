count_payments = input()
total_sum = 0.0
while count_payments != "NoMoreMoney":
    amount = float(count_payments)

    if amount < 0:
        print("Invalid operation!")
        break
    total_sum += amount
    print(f"Increase: {amount:.2f}")
    count_payments = input()
print(f"Total: {total_sum:.2f}")