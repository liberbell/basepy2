import os
from os import path
import datetime
from datetime import date, time, timedelta
import time

def main():
    print(os.name)

    print('Item exists: ' + str(path.exists('textfile.txt')))
    print('Item is a file: ' +str(path.isfile('textfile.txt')))

if __name__ == '__main__':
    main()
