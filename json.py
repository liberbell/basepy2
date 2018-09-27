import urllib.request
import json

def printResult(data):
    theJSON = json.loads(data)

def main():
    urlDATA = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson'

    weburl = urllib.request.urlopen(urlDATA)
    print('Result code: ' + str(weburl.getcode()))
    print()

if __name__ == '__main__':
    main()
