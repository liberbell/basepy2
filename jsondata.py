import urllib.request
import json

def printResult(data):
    theJSON = json.loads(data)

    if 'title' in theJSON['metadata']:
        print(theJSON['metadata']['title'])

    count = theJSON['metadata']['count']
    print(str(count) + ' events recorded')

    for i in theJSON['features']:
        print(i['properties']['place'], i['properties']['mag'])
    print('----------\n')

    for i in theJSON['features']:
        if i['properties']['mag'] >= 4.0:
            print('%2.1f' % i['properties']['mag'], i['properties']['place'])
    print('----------\n')

    print('Events that were felt:')
    for i in theJSON['features']:
        feltReport = i['properties']['felt']
        if feltReport != None:
            if feltReport > 0:
                print('%2.1f' % i['properties']['mag'], i['properties']['place'],
                ' Reported ' + str(feltReport) +' peoples')
    print('-----------\n')
    
    for i in theJSON['features']:
        feltReport = i['properties']['felt']
        location = i['coordinates']['longitude']
        if feltReport != None:
            if feltReport > 5:
                print('%2.1f' % i['properties']['mag'], i['properties']['place'],
                ' Reported ' + str(feltReport) +' peoples', i['coordinates']['longitude'])

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
