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

from twython import Twython

twitter = Twython(consumer_key, consumer_secret, access_token, access_token_secret)


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


def Earth():
    with open("/var/www/astrometry/orbital.json", "r") as O:
        orbit = json.load(O)
        picture = orbit["Earth"][0]["Picture"]
        W = orbit["Earth"][0]["PicW"]
        H = orbit["Earth"][0]["PicH"]
        #indexFile = open("main.html", "a")
        d0 = date(Percentage.current_year, 1, 1)
        d1 = date(Percentage.current_year, Percentage.thisMonth, Percentage.today)
        d1 = d1 + timedelta(days=1)  # Year, month, day
        d2 = date(Percentage.current_year, 12, 31)
        d3 = d2 - d0
        d3 = str(d3)
        d3 = d3.split()
        d3 = int(d3[0])
        d3 = d3 + 1
        ValuePercent = d3 / 100
        delta = d1 - d0
        delta = str(delta)
        delta = delta[:6]
        new = re.sub("[^0-9]", "", str(delta))
        new = str(new)
        new = new[:6]
        new = int(new)
        Percentage.EarthResult = new / ValuePercent
        Percentage.EarthResult = round(Percentage.EarthResult, 2)
        Percentage.earth = (
            ("Planet : Earth")
            + str("\n")
            + str(("Day of the year : ") + str("Day ") + str(new))
            + str("\n")
            + str(("Year progress : ") + str(Percentage.EarthResult))
        )
        print(Percentage.earth)
        percent = Percentage.EarthResult
        barre = (
            "["
            + "#" * int((50 / 100) * percent)
            + "_" * int((50 / 100) * (100 - percent))
            + "]"
        )
        Percentage.earthHTML = (
            ("Planet : Earth")
            + ("\n")
            + str(("Day of the year : ") + str("Day ") + str(new))
            + ("\n")
            + str(("Year progress : ") + str(Percentage.EarthResult) + str("%"))
            + ("\n")
            + str(barre)
        )

        Percentage.BarrEarth = "Percent of this year : " + (barre) + str("\n\n")
        print(Percentage.BarrEarth)
        Percentage.BarrEarthHTML = "Percent of this year : " + (barre) + ("<br />")


Earth()
message = str(Percentage.earthHTML) + str("\n#Astronomy #Space #Espace #Astrometry")

photo = open("/var/www/astrometry/pictures/terre.png", "rb")
response = twitter.upload_media(media=photo)
twitter.update_status(status=message, media_ids=[response["media_id"]])
