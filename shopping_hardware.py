budget = float(input())

video_cards_count = int(input())
processors_count = int(input())
ram_memory_count = int(input())

video_card_price = video_cards_count * 250
processors_price = processors_count * (video_card_price * .35)
ram_memory_price = ram_memory_count * (video_card_price * .1)

overall_price = video_card_price + processors_price + ram_memory_price

price_after_15_percent_discount = overall_price - (overall_price * .15)
