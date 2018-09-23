from datetime import datetime

def main():
    now = datetime.now()
    print(now.strftime('The current year is: %Y'))
    print(now.strftime('%a, %d %B, %y'))

    print(now.strftime('Local date and time: %c'))
    print(now.strftime('Local date: %x'))
    print(now.strftime('Local time: %X'))

    print(now.strftime('Current time: %I:%M:%S %p'))
    print(now.strftime('24-hour time: %H:%M %p'))


if __name__ == '__main__':
    main()
