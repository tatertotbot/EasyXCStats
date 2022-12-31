import requests
from requests_html import HTMLSession
from datetime import datetime, timedelta

def getRecentRun(userID):
    global name
    global date
    global minutes
    global seconds
    global distance
    s = HTMLSession()
    f = open("result.html", 'wb')
    url = 'https://strava.com/athletes/' + userID

    res = s.get(url)
    f.write(res.content)
    f.close()
    name = res.html.search(',&quot;name&quot;:&quot;{word}&quot;,&quot;type&quot;:&quot;run&quot;')['word']
    date = res.html.search('startDateLocal&quot;:&quot;{word}&quot;')['word']
    time = res.html.search('movingTime&quot;:&quot;{word}&quot;')['word']
    distance = res.html.search('distance&quot;:&quot;{word} mi&quot;')['word']

    #converts time given by Strava to version readable by XCStats
    if len(time) > 5:
        time_object = datetime.strptime(time, '%H:%M:%S')
    elif len(time) > 2:
        time_object = datetime.strptime(time, '%M:%S')
    else:
        time_object = datetime.strptime(time, '%S')

    minutes = time_object.strftime('%M')
    seconds = time_object.strftime('%S')

    #converts date given by Strava to version readable by XCStats
    if date == 'Today':
        date = datetime.now().strftime('%m/%d/%Y')
    elif date == 'Yesterday':
        date = (datetime.now() - timedelta(1)).strftime('%m/%d/%Y')
    else:
        date_object = datetime.strptime(date, '%B %d, %Y')
        date = date_object.strftime('%m/%d/%Y')
