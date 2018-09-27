import urllib.request


def main():
    weburl = urllib.request.urlopen('https://www.google.com')
    print('Result code: ' + str(weburl.getcode()))


if __name__ == '__main__':
    main()
