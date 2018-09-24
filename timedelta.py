from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

print(timedelta(days=365, hours=5, minutes=1))

now = datetime.now()
print('Today is: ' + str(now))

print('One year from now it will be: ' + str(now + timedelta(days=365)))

print('In 2 days and 3 weeks, It will be: ' +
    str(now + timedelta(days=2, weeks=3)))

t = datetime.now() - timedelta(weeks=1)
s = t.strftime('%A %B %d, %Y')
print('One week ago it was: ' + s)

# def main():
#
#
#
# if __name__ == '__main__':
#     main()
