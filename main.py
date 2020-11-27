date_to_format = input("enter what date you want to format\ne.g. 1975 4 21\n")
date_to_format_split = date_to_format.split()

def formatter(year: str, month: str, day: str):
    print_result = True
    month_int = int(month)
    day_int = int(day)
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    if month_int > 12:
        print("Month must be between 1 and 12")
    else:
        try:
            if day_int >= month_days[month_int]:
                print(f"{str(months[month_int - 1])} only has {month_days[month_int - 1]} days.")
                print_result = False
        except IndexError:
            print(f"{str(months[month_int - 1])} only has {month_days[month_int - 1]} days.")
            print_result = False

        try:
            month = month.replace(month, str(months[month_int - 1]))
        except IndexError:
            print("Month must be between 1 and 12")
            print_result = False

        if len(day) == 2:
            if day[1] == "1":
                day = day + "st"
            elif day[1] == "2":
                day = day + "nd"
            elif day[1] == "3":
                day = day + "rd"
            elif day == "11":
                day = day + "th"
            elif day == "12":
                day = day + "th"
            elif day == "13":
                day = day + "th"
            else:
                day = day + "th"
        elif len(day) == 1:
            if day[0] == "1":
                day = day + "st"
            elif day[0] == "2":
                day = day + "nd"
            elif day[0] == "3":
                day = day + "rd"
            else:
                day = day + "th"

        if print_result:
            print(day, month, year)


formatter(date_to_format_split[0], date_to_format_split[1], date_to_format_split[2])
