from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

print(timedelta(days=365, hours=5, minutes=1))

now = datetime.now()
print('Today is: ' + str(now))

print('One year from now it will be: ' + str(now + timedelta(days=365)))

# def main():
#
#
#
# if __name__ == '__main__':
#     main()
