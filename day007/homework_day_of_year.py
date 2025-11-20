# 练习5：计算指定的年月日是这一年的第几天
def day_of_year(date_str):
    total_day_of_month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    year = int(date_str[:4])
    month = int(date_str[5:7])
    day = int(date_str[8:10])

    is_leap_year = year % 4 == 0 and year % 100 != 0 or year % 400 == 0

    count = 0
    for the_month in range(1, month):
        count += total_day_of_month_list[the_month-1]
    count += day

    if (month > 2 and is_leap_year):
        count += 1

    return count


dates = ['2024-03-03', '2025-11-21', '2100-03-03']
for date in dates:
    n = day_of_year(date)
    print(f"{date} 是那一年的第{n}天")
