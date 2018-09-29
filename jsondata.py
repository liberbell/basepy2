import urllib.request
import json

def printResult(data):
    theJSON = json.loads(data)

    if 'title' in theJSON['metadata']:
        print(theJSON['metadata']['title'])

    count = theJSON['metadata']['count']
    print(str(count) + ' events recorded')

    for i in theJSON['features']:
        print(i['properties']['place'],['mag'])


def main():
    urlDATA = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson'

    weburl = urllib.request.urlopen(urlDATA)
    print('Result code: ' + str(weburl.getcode()))
    if (weburl.getcode() == 200):
        data = weburl.read()
        printResult(data)
    else:
        print('Received error, can`t parse results')

if __name__ == '__main__':
    main()
