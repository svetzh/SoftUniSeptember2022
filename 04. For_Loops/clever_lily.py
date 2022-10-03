age_of_Lily = int(input())
price_washing_machine = float(input())
toy_price = int(input())

money_received = 0
brother_interest = 0
received_toy = 0
add_money = 0
for birthday in range(1, age_of_Lily + 1):
    if birthday % 2 == 0:
        add_money = add_money + 10
        money_received = money_received + add_money
        brother_interest += 1
    else:
        received_toy += 1
saved_money = money_received + (received_toy * toy_price) - brother_interest

diff = saved_money - price_washing_machine
if saved_money >= price_washing_machine:
    print(f"Yes! {abs(diff):.2f}")
else:
    print(f"No! {abs(diff):.2f}")