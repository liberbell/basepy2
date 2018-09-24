import calendar

hc = calendar.HTMLCalendar(calendar.SUNDAY)
st = hc.formatmonth(2018, 9)
print(st)
