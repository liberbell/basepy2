from datetime import date
from datetime import time
from datetime import datetime

def main():
    # today = date.today()
    # print('Today`s date is ', today)
    #
    # print('Date compornets: ', today.day, today.month, today.year)
    #
    # print('Todays weekday # is ', today.weekday())
    # days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    # print('Which is a:', days[today.weekday()])
    today = datetime.now()
    print('The current day and time is ', today)

    t = datetime.time(datetime.now())
    print(t)


if __name__ == '__main__':
    main()
