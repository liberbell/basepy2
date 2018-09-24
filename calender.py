import calendar

c = calendar.TextCalendar(calendar.SUNDAY)
# hc = calendar.HTMLCalendar(calendar.SUNDAY)
# st = hc.formatmonth(2018, 9)
# print(st)
for i in c.itermonthdays(2018, 9):
    print(i)
