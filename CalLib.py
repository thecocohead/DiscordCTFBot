import datetime
import urllib.request
import re
import math

url = 'https://calendar.google.com/calendar/ical/e2haqqg2h2m15n1trn1pusavqk%40group.calendar.google.com/public/basic.ics' # Change this! This is your iCal file.


def calendar():
    response = urllib.request.urlopen(url)
    data = response.read()
    text = data.decode('utf-8')
    start = re.findall(r'(?<=DTSTART:).*', text)
    end = re.findall(r'(?<=DTEND:).*', text)
    summary = re.findall(r'(?<=SUMMARY:).*', text)
    return [start, end, summary]


def isEvent():
    now = datetime.datetime.utcnow()
    start = calendar()[0]
    end = calendar()[1]
    summary = calendar()[2]
    date = now.strftime("%Y%m%dT%H%M%SZ")
    length = len(start)
    output = ""
    i = 0
    while i < length:
        if start[i] < date < end[i]:
            return summary[i]
        i += 1
    return False


def nextEvent():
    now = datetime.datetime.utcnow()
    start = calendar()[0]
    length = len(start)
    i = 0
    output = ""
    while i < length:
        start1 = datetime.datetime.strptime(start[i], '%Y%m%dT%H%M%SZ\r')
        timeDt = start1 - now
        timeDt1 = round(timeDt.total_seconds())
        timeDt = re.findall(r'.*(?=\.)', str(timeDt))[0]
        if timeDt1 > 0:
            sum1 = str(calendar()[2][i])
            sum1 = sum1.replace('\r', '')
            output += sum1 + ' starts in ' + str(timeDt) + '\n'

        i += 1
    return output


def startEnd():
    start = calendar()[0]
    end = calendar()[1]
    length = len(start)
    i = 0
    now = datetime.datetime.utcnow()
    date = now.strftime("%Y%m%dT%H%M%SZ\r")
    while i < length:
        if start[i] < date < end[i]:
            start1 = datetime.datetime.strptime(start[i], '%Y%m%dT%H%M%SZ\r')
            end1 = datetime.datetime.strptime(end[i], '%Y%m%dT%H%M%SZ\r')
            timeDt0 = now - start1
            timeDt1 = end1 - now
            return [math.floor(timeDt0.total_seconds()), math.floor(timeDt1.total_seconds())] #0 is time since start, 1 is time until end
        i += 1
    return [0, 0]
