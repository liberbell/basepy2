import calendar

c = calendar.TextCalendar(calendar.SATURDAY)
# hc = calendar.HTMLCalendar(calendar.SUNDAY)
# st = hc.formatmonth(2018, 9)
# print(st)
# for i in c.itermonthdays(2018, 9):
#     print(i)
for name in calendar.month_name:
    print(name)

for day in calendar.day_name:
    print(day)
