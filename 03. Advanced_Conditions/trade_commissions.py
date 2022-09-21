city = input()
volume_sales = float(input())
commission = 0

valid_city_is = True
sales_valid = True

if city == "Sofia":
    if 0 <= volume_sales <= 500:
        commission = volume_sales * .05
    elif 500 < volume_sales <= 1000:
        commission = volume_sales * .07
    elif 1000 < volume_sales <= 10000:
        commission = volume_sales * .08
    elif volume_sales > 10000:
        commission = volume_sales * .12
    else:
        sales_valid = False
elif city == "Varna":
    if 0 <= volume_sales <= 500:
        commission = volume_sales * .045
    elif 500 < volume_sales <= 1000:
        commission = volume_sales * .075
    elif 1000 < volume_sales <= 10000:
        commission = volume_sales * .1
    elif volume_sales > 10000:
        commission = volume_sales * .13
    else:
        sales_valid = False
elif city == "Plovdiv":
    if 0 <= volume_sales <= 500:
        commission = volume_sales * .055
    elif 500 < volume_sales <= 1000:
        commission = volume_sales * .08
    elif 1000 < volume_sales <= 10000:
        commission = volume_sales * .12
    elif volume_sales > 10000:
        commission = volume_sales * .145
    else:
        sales_valid = False
else:
    valid_city_is = False

if valid_city_is and sales_valid:
    print(f"{commission:.2f}")
else:
    print("error")


