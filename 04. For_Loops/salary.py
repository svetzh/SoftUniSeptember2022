count_open_tabs = int(input())
salary = int(input())

for number_websites_count in range(1, count_open_tabs + 1):
    if salary <= 0:
        break
    website_url = input()

    if website_url == "Facebook":
        salary -= 150
    elif website_url == "Instagram":
        salary -= 100
    elif website_url == "Reddit":
        salary -= 50

if salary > 0:
    print(salary)
else:
    print("You have lost your salary.")
