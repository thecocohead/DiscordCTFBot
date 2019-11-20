from datetime import datetime
import urllib.request
import re


def isEvent():
    now = datetime.utcnow()
    url = 'https://calendar.google.com/calendar/ical/e2haqqg2h2m15n1trn1pusavqk%40group.calendar.google.com/public/basic.ics'
    response = urllib.request.urlopen(url)
    data = response.read()
    text = data.decode('utf-8')
    start = re.findall(r'(?<=DTSTART:).*', text)
    end = re.findall(r'(?<=DTEND:).*', text)
    summary = re.findall(r'(?<=SUMMARY:).*', text)
    date = now.strftime("%Y%m%dT%H%M%SZ")
    length = len(start)
    i = 0
    while i < length:
        if start[i] < date < end[i]:
            return summary[i]
        i += 1
    return "false"

def leftInEvent():
    now = datetime.utcnow()
    url = 'https://calendar.google.com/calendar/ical/e2haqqg2h2m15n1trn1pusavqk%40group.calendar.google.com/public/basic.ics'
    response = urllib.request.urlopen(url)
    data = response.read()
    text = data.decode('utf-8')
    start = re.findall(r'(?<=DTSTART:).*', text)
    end = re.findall(r'(?<=DTEND:).*', text)
    date = now.strftime("%Y%m%dT%H%M%SZ\r")
    length = len(start)
    i = 0
    while i < length:
        if start[i] < date < end[i]:
            end1 = datetime.strptime(end[i], '%Y%m%dT%H%M%SZ\r')
            return re.findall(r'.*(?=\.)', str(end1 - now))[0]
        i += 1
    return "false"

def timeToNextPing():
    now = datetime.utcnow()
    url = 'https://calendar.google.com/calendar/ical/e2haqqg2h2m15n1trn1pusavqk%40group.calendar.google.com/public/basic.ics'
    response = urllib.request.urlopen(url)
    data = response.read()
    text = data.decode('utf-8')
    start = re.findall(r'(?<=DTSTART:).*', text)
    end = re.findall(r'(?<=DTEND:).*', text)
    date = now.strftime("%Y%m%dT%H%M%SZ\r")
    length = len(start)
    i = 0
    while i < length:
        if start[i] < date < end[i]:
            end1 = datetime.strptime(end[i], '%Y%m%dT%H%M%SZ\r')
            timeDt = end1 - now
            return timeDt.total_seconds()
        i += 1
    return "false"

def nextEvent():
    now = datetime.utcnow()
    url = 'https://calendar.google.com/calendar/ical/e2haqqg2h2m15n1trn1pusavqk%40group.calendar.google.com/public/basic.ics'
    response = urllib.request.urlopen(url)
    data = response.read()
    text = data.decode('utf-8')
    start = re.findall(r'(?<=DTSTART:).*', text)
    end = re.findall(r'(?<=DTEND:).*', text)
    summary = re.findall(r'(?<=SUMMARY:).*', text)
    date = now.strftime("%Y%m%dT%H%M%SZ\r")
    length = len(start)
    i = 0
    output = ""
    while i < length:
        start1 = datetime.strptime(start[i], '%Y%m%dT%H%M%SZ\r')
        timeDt = start1 - now
        timeDt1 = round(timeDt.total_seconds())
        timeDt = re.findall(r'.*(?=\.)', str(timeDt))[0]
        if timeDt1 > 0:
            sum1 = str(summary[i])
            sum1 = sum1.replace('\r', '')
            output += sum1 + ' starts in ' + str(timeDt) + '\n'
            #TODO: Flip output order

        i += 1
    return output

def timeSinceStart():
    now = datetime.utcnow()
    url = 'https://calendar.google.com/calendar/ical/e2haqqg2h2m15n1trn1pusavqk%40group.calendar.google.com/public/basic.ics'
    response = urllib.request.urlopen(url)
    data = response.read()
    text = data.decode('utf-8')
    start = re.findall(r'(?<=DTSTART:).*', text)
    end = re.findall(r'(?<=DTEND:).*', text)
    date = now.strftime("%Y%m%dT%H%M%SZ\r")
    length = len(start)
    i = 0
    while i < length:
        if start[i] < date < end[i]:
            start1 = datetime.strptime(start[i], '%Y%m%dT%H%M%SZ\r')
            timeDt = now - start1
            return timeDt.total_seconds()
        i += 1
    return -1