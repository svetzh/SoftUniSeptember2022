budget = float(input())
video_cards_count = int(input())
processors_count = int(input())
ram_memory_count = int(input())

video_card_price = video_cards_count * 250
processors_price = processors_count * (video_card_price * .35)
ram_memory_price = ram_memory_count * (video_card_price * .1)

overall_price = video_card_price + processors_price + ram_memory_price

if video_cards_count > processors_count:
    discount = overall_price - (overall_price * .15)
    if budget >= discount:
        money_left = abs(budget - discount)
        print(f"You have {money_left:.2f} leva left!")
    else:
        money_left = abs(discount - budget)
        print(f"Not enough money! You need {money_left:.2f} leva more!")

if processors_count > video_cards_count:
    if budget >= overall_price:
        money_left = abs(budget - overall_price)
        print(f"You have {money_left:.2f} leva left!")

    else:
        money_left = abs(overall_price - budget)
        print(f"Not enough money! You need {money_left:.2f} leva more!")
