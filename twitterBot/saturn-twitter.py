#!/usr/bin/env python3

# Developer : Hamdy Abou El Anein
# hamdy.aea@protonmail.com

# percentage of the year for the earth, the moon, jupiter, Saturn, etc...
# Lunar Perigee and Apogee Calculator : https://www.fourmilab.ch/earthview/pacalc.html
# Mercury and others : https://in-the-sky.org/newscalyear.php


from datetime import date, datetime, timedelta
import re
import json

from keys import *

import tweepy

class Percentage:
    def __init__(self):
        self.current_year
        self.today
        self.thisMonth
        self.EarthResult
        self.earthHTML
        self.BarrEarth
        self.BarrEarthHTML
        self.NewobjectPerihelion
        self.objectPerihelion
        self.objectResult
        self.objectHTML
        self.barrobject
        self.barrobjectHTML


Percentage.current_year = date.today().year
Percentage.today = int(datetime.today().strftime("%d"))
Percentage.thisMonth = int(datetime.today().strftime("%m"))


def perihelion(object, years1, years):
    with open("/var/www/astrometry/orbital.json", "r") as O:
        orbit = json.load(O)
        thisYear = orbit[object][0]["Peri"]
        picture = orbit[object][0]["Picture"]
        W = orbit[object][0]["PicW"]
        H = orbit[object][0]["PicH"]
        for i in thisYear:
            d0Year = i[:4]
            d0Year = int(d0Year)
            d0Month = i[5:7]
            d0Month = int(d0Month)
            d0Day = i[8:10]
            d0Day = int(d0Day)
            d0 = date(d0Year, d0Month, d0Day)
            d1 = date(Percentage.current_year, Percentage.thisMonth, Percentage.today)
            # d1 = d1 + timedelta(days=1)
            if d0 >= d1 - timedelta(days=years1) and d0 <= d1:
                Percentage.objectPerihelion = d0
        for i in thisYear:
            d0Year = i[:4]
            d0Year = int(d0Year)
            d0Month = i[5:7]
            d0Month = int(d0Month)
            d0Day = i[8:10]
            d0Day = int(d0Day)
            d0 = date(d0Year, d0Month, d0Day)
            d1 = date(Percentage.current_year, Percentage.thisMonth, Percentage.today)
            if d0 <= d1 + timedelta(days=years) and d0 > d1:
                Percentage.NewobjectPerihelion = d0
                d1 = date(
                    Percentage.current_year, Percentage.thisMonth, Percentage.today
                )
                d3 = Percentage.NewobjectPerihelion - Percentage.objectPerihelion
                d3 = str(d3)
                d3 = d3.split()
                d3 = int(d3[0])
                d3 = d3 + 1
                ValuePercent = d3 / 100
                delta = d1 - Percentage.objectPerihelion
                delta = str(delta)
                delta = delta.split()
                delta = delta[0]
                new = re.sub("[^0-9]", "", str(delta))
                new = str(new)
                new = new[:6]  #:4
                new = int(new)
                new = new + 1
                Percentage.objectResult = new / ValuePercent
                Percentage.objectResult = round(Percentage.objectResult, 2)

                print(str(orbit[object][0]["info"]) + str(" : ") + str(object))
                print(("Day of the year : ") + str("Day ") + str(new))
                print(("Year progress : ") + str(Percentage.objectResult) + str("%"))

                percent = Percentage.objectResult
                barre = (
                    "["
                    + "#" * int((50 / 100) * percent)
                    + "_" * int((50 / 100) * (100 - percent))
                    + "]"
                )
                print("Percent of this year : " + (barre))
                print("\n")

                Percentage.objectHTML = (
                    (str(orbit[object][0]["info"]) + str(" : ") + str(object))
                    + ("\n")
                    + str(("Day of the year : ") + str("Day ") + str(new))
                    + ("\n")
                    + str(
                        ("Year progress : ")
                        + str(Percentage.objectResult)
                        + str("%")
                        + ("\n")
                        + str(barre)
                    )
                )

                Percentage.barrobject = "Percent of this year : " + (barre) + str("\n")
                Percentage.barrobjectHTML = "Percent of this year : " + (barre) + ("\n")


perihelion("Saturn", 10719, 10719)

message = str(Percentage.objectHTML) + str("\n#Astronomy #Space #Espace #Astrometry")
photo = '/var/www/astrometry/pictures/saturn.jpg'
auth = tweepy.OAuth1UserHandler(
   API_Key, API_Key_Secret, access_token, access_token_secret
)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
api.update_status_with_media(filename=photo,status=message)
