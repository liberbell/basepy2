from datetime import date
from datetime import time
from datetime import datetime

def main():
    today = date.today()
    print('Today`s date is ', today)

    print('Date compornets: ', today.day, today.month, today.year)

    print('Todays weekday # is ', today.weekday())
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    print('Which is a:', days[today.weekday()])


if __name__ == '__main__':
    main()
