student_name = input()
years_graduated = 1
faulty_year = 0
godisha_ocenka = 0.0
sum_grade = 0
is_excluded = False
while years_graduated <= 12:
    godisha_ocenka = float(input())
    if godisha_ocenka < 4.00:
        faulty_year += 1
        if faulty_year == 2:
            is_excluded = True
            break
        continue
    sum_grade += godisha_ocenka
    years_graduated += 1


average_grade = sum_grade / 12

if is_excluded:
    print(f"{student_name} has been excluded at {years_graduated} grade")
else:
    print(f"{student_name} graduated. Average grade: {average_grade:.2f}")