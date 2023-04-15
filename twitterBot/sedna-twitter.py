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


def sedna(object):
    Percentage.Goblin_current_year = date.today().year + 96
    Percentage.Goblin_today = int(datetime.today().strftime("%d"))
    Percentage.Goblin_thisMonth = int(datetime.today().strftime("%m"))
    with open("/var/www/astrometry/orbital.json", "r") as O:
        orbit = json.load(O)
        picture = orbit[object][0]["Picture"]
        W = orbit[object][0]["PicW"]
        H = orbit[object][0]["PicH"]
        d2 = date(1000, 1, 1)
        d1 = date(
            Percentage.Goblin_current_year,
            Percentage.Goblin_thisMonth,
            Percentage.Goblin_today,
        )
        d0 = date(2140, 1, 1)
        d3 = d0 - d2
        d3 = str(d3)
        d3 = d3.split()

        d3 = int(d3[0])
        d3 = d3 + 1
        ValuePercent = d3 / 100
        delta = d1 - d2
        delta = str(delta)
        delta = delta.split()
        delta = delta[0]
        new = re.sub("[^0-9]", "", str(delta))
        new = int(new)
        new = new + 1
        Percentage.objectResult = new / ValuePercent
        Percentage.objectResult = round(Percentage.objectResult, 2)
        new = new + 3753103

        print(str(orbit[object][0]["info"]) + str(" : ") + str(object))
        print(("Day of the year : ") + str("Day ") + str(new))
        print("Last perihelion : " + str(orbit[object][0]["Peri"][0]))
        print("Next perihelion : " + str(orbit[object][0]["Peri"][1]))
        print(str("Orbital period : ") + str(orbit[object][0]["orperiod"]))
        print(("Year progress : ") + str(Percentage.objectResult) + str("%"))

        percent = Percentage.objectResult

        barre = (
            "["
            + "#" * int((25 / 100) * percent)
            + "-" * int((25 / 100) * (100 - percent))
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

        Percentage.object = "Percent of this year : " + (barre) + str("\n")
        #Percentage.objectHTML = "Percent of this year : " + (barre) + ("\n")



sedna("90377 Sedna")

message = str(Percentage.objectHTML) + str("\n#Astronomy #Space #Espace #Astrometry")
photo = '/var/www/astrometry/pictures/Nasasedna.jpg'
auth = tweepy.OAuth1UserHandler(
   API_Key, API_Key_Secret, access_token, access_token_secret
)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
api.update_status_with_media(filename=photo,status=message)
