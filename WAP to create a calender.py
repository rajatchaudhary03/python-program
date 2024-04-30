import calendar

def display_calendar(year, month):
    cal = calendar.TextCalendar(calendar.SUNDAY)
    calendar_text = cal.formatmonth(year, month)
    print(calendar_text)

year = int(input("Enter the year: "))
month = int(input("Enter the month (1-12): "))

display_calendar(year, month)
