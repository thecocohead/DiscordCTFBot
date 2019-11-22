import datetime
import urllib.request
import re

url = 'https://calendar.google.com/calendar/ical/e2haqqg2h2m15n1trn1pusavqk%40group.calendar.google.com/public/basic.ics'

def calendar():
    response = urllib.request.urlopen(url)
    data = response.read()
    text = data.decode('utf-8')
    start = re.findall(r'(?<=DTSTART:).*', text)
    end = re.findall(r'(?<=DTEND:).*', text)
    summary = re.findall(r'(?<=SUMMARY:).*', text)
    return [start,end,summary]

def isEvent():
    now = datetime.datetime.utcnow()
    start = calendar()[0]
    end = calendar()[1]
    summary = calendar()[2]
    date = now.strftime("%Y%m%dT%H%M%SZ")
    length = len(start)
    i = 0
    while i < length:
        if start[i] < date < end[i]:
            return summary[i]
        i += 1
    return "false"

def leftInEvent():
    now = datetime.datetime.utcnow()
    start = calendar()[0]
    end = calendar()[1]
    date = now.strftime("%Y%m%dT%H%M%SZ\r")
    length = len(start)
    i = 0
    while i < length:
        if start[i] < date < end[i]:
            end1 = datetime.datetime.strptime(end[i], '%Y%m%dT%H%M%SZ\r')
            return re.findall(r'.*(?=\.)', str(end1 - now))[0]
        i += 1
    return "false"

def timeToNextPing():
    now = datetime.datetime.utcnow()
    text = calendar()
    start = calendar()[0]
    end = calendar()[1]
    date = now.strftime("%Y%m%dT%H%M%SZ\r")
    length = len(start)
    i = 0
    while i < length:
        if start[i] < date < end[i]:
            end1 = datetime.datetime.strptime(end[i], '%Y%m%dT%H%M%SZ\r')
            timeDt = end1 - now
            return timeDt.total_seconds()
        i += 1
    return "false"

def nextEvent():
    now = datetime.datetime.utcnow()
    text = calendar()
    start = calendar()[0]
    start = calendar()[3]
    length = len(start)
    i = 0
    output = ""
    while i < length:
        start1 = datetime.datetime.strptime(start[i], '%Y%m%dT%H%M%SZ\r')
        timeDt = start1 - now
        timeDt1 = round(timeDt.total_seconds())
        timeDt = re.findall(r'.*(?=\.)', str(timeDt))[0]
        if timeDt1 > 0:
            sum1 = str(summary[i])
            sum1 = sum1.replace('\r', '')
            output += sum1 + ' starts in ' + str(timeDt) + '\n'

        i += 1
    return output

def timeSinceStart():
    now = datetime.datetime.utcnow()
    start = calendar()[0]
    end = calendar()[1]
    date = now.strftime("%Y%m%dT%H%M%SZ\r")
    length = len(start)
    i = 0
    while i < length:
        if start[i] < date < end[i]:
            start1 = datetime.datetime.strptime(start[i], '%Y%m%dT%H%M%SZ\r')
            timeDt = now - start1
            return timeDt.total_seconds()
        i += 1
    return -1