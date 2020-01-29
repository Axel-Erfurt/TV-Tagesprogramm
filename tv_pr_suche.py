#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
import time
import datetime
import sys
import locale

dictList = {'ard': 71, 'zdf': 37, 'zdf neo': 659, 'zdf info': 276, 'arte': 58, 'wdr': 46, 'ndr': \
            47, 'mdr': 48, 'hr': 49, 'swr': 10142, 'br': 51, 'rbb': 52, '3sat': 56,'alpha': 104, \
            'kika': 57, 'phoenix': 194, 'tagesschau 24': 100, 'one': 146, 'rtl': 38, 'sat 1': 39, \
            'pro 7': 40,'rtl plus': 12033, 'kabel 1': 44, 'rtl 2': 41, 'vox': 42, 'rtl nitro': 763, \
            'n24 doku': 12045, 'kabel 1 doku': 12043, 'sport 1': 64, 'super rtl': 43, \
            'sat 1 gold': 774, 'vox up': 12125, 'sixx': 694, 'servus tv': 660, \
            'welt': 175, 'orf 1': 54, 'orf 2': 55, 'orf 3': 56, 'tele 5': 277, '7maxx': 783, \
            'dmaxx': 507, 'dw': 300, 'fox': 565, 'srf 1': 59, 'srf 2': 60, 'srf info': 231, '3 +': 544}

response = requests.get('http://mobile.hoerzu.de/programbystation')
response_json = response.json()

myday = f"{datetime.date.today():%d}"


def findShow(findString):
    for element in response_json:
        for value in element.get('broadcasts'):
            if findString in value.get('title') \
            or findString.title() in value.get('title')\
            or findString.upper() in value.get('title')\
            or findString.lower() in value.get('title'):
                id = element.get('id')
            
                for v in dictList.keys():
                    if dictList[v] == id:
                        title = value.get('title')
                        st = value.get('startTime')
                        startTime = time.strftime("%-H:%M", time.localtime(st))
                        day = time.strftime("%d", time.localtime(st))
                        if day == myday:
                            print(v.upper(), "heute", startTime, "Uhr", title)
                        else:
                            print(v.upper(), "morgen", startTime, "Uhr", title)

def suche():
    a = input("Suchbegriff:")
    if a == "q":
        sys.exit()
    else:
        findShow(a)
        suche()
        
loc = locale.getlocale()
locale.setlocale(locale.LC_ALL, loc)
dt = f"{datetime.date.today():%-d.%B %Y}"
print(dt,"\n", "drücke q zum Beenden")  
suche()
