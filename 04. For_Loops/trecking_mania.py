climbers_groups = int(input())

persons_group1_musala = 0
persons_group2_monblanc = 0
persons_group3_kilimanjaro = 0
persons_group4_k2 = 0
persons_group5_everest = 0

count_climbers_in_group = 0
sum_of_climbers_in_group = 0

for i in range(climbers_groups):
    count_climbers_in_group = int(input())
    sum_of_climbers_in_group += count_climbers_in_group

    if count_climbers_in_group <= 5:
        persons_group1_musala += count_climbers_in_group
    elif count_climbers_in_group <= 12:
        persons_group2_monblanc += count_climbers_in_group
    elif count_climbers_in_group <= 25:
        persons_group3_kilimanjaro += count_climbers_in_group
    elif count_climbers_in_group <= 40:
        persons_group4_k2 += count_climbers_in_group
    else:
        persons_group5_everest += count_climbers_in_group

percent_musala = persons_group1_musala / sum_of_climbers_in_group * 100
print(f"{percent_musala:.2f}%")
percent_monblanc = persons_group2_monblanc / sum_of_climbers_in_group * 100
print(f"{percent_monblanc:.2f}%")
percent_kili = persons_group3_kilimanjaro / sum_of_climbers_in_group * 100
print(f"{percent_kili:.2f}%")
percent_k2 = persons_group4_k2 / sum_of_climbers_in_group * 100
print(f"{percent_k2:.2f}%")
percent_everest = persons_group5_everest / sum_of_climbers_in_group * 100
print(f"{percent_everest:.2f}%")