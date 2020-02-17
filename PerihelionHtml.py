#!/usr/bin/env python3

# Developer : Hamdy Abou El Anein
# hamdy.aea@protonmail.com

# percentage of the year for the earth, the moon, jupiter, Saturn, etc...
# Lunar Perigee and Apogee Calculator : https://www.fourmilab.ch/earthview/pacalc.html
# Mercury and others : https://in-the-sky.org/newscalyear.php

from datetime import date, datetime, timedelta
import re
import json


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

startHtml = (
    str("<!DOCTYPE html>")
    + str("\n")
    + str("<html>")
    + str("\n")
    + str("<head>")
    + str("\n")
    + str(
        '<script data-ad-client="ca-pub-2332306020792478" async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>'
    )
    + str("\n")
    + str("<title>Percent Progress of the Solar System</title>")
    + str("\n")
    + str(
        "<style>a:link {color: #ffffff;}/* visited link */a:visited {color: #ffffff;}/* mouse over link */a:hover {color: #ffffff;}/* selected link */a:active {color: #ffffff;}</style>"
    )
    + str("<style>")
    + str("\n")
    + str("body {")
    + str("\n")
    + str("background-image: url('nightsky.jpg');")
    + str("\n")
    + str("background-size: 1920px 1920px;")
    + str("\n")
    + str("<basefont face = 'Monospace'>")
    + str("\n")
    + str("}")
    + str("\n")
    + str("</style>")
    + str("\n")
    + str("</head>")
    + str("\n")
    # + str('<body bgcolor="#000000">')
    + str("\n")
    + str('<font color="white">')
    + str("\n")
    + str("<font face = 'Monospace' size ='6' color='white'>")
    + str("\n")
    + str("<p>")
    + str("\n")
    + str(
        '<img src="peri.png" alt="perihelion" width="500" height="333">'
        + str("\n")
        + str("<br />")
        + str("\n")
        + str("<br />")
        + str("\n")
        + str("<br />")
    )
)
indexFile = open("/var/www/html/main.html", "w")
indexFile.write(startHtml)
indexFile.close()

def goblin(object):
    Percentage.Goblin_current_year = date.today().year + 2522
    Percentage.Goblin_today = int(datetime.today().strftime("%d"))
    Percentage.Goblin_thisMonth = int(datetime.today().strftime("%m"))
    indexFile = open("/var/www/html/main.html", "a")
    with open("/var/www/html/orbital.json", "r") as O:
        orbit = json.load(O)
        picture = orbit[object][0]["Picture"]
        W = orbit[object][0]["PicW"]
        H = orbit[object][0]["PicH"]
        d2 = date(1000, 1, 1)
        d1 = date(Percentage.Goblin_current_year, Percentage.Goblin_thisMonth, Percentage.Goblin_today)
        d0 = date(4600, 1, 1)
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

        print(str(orbit[object][0]["info"]) + str(" : ") + str(object))
        print(("Day of the year : ") + str("Day ") + str(new))
        print(("Year progress : ") + str(Percentage.objectResult) + str("%"))

        percent = Percentage.objectResult
        barre = (
            "["
            + "#" * int((50 / 100) * percent)
            + "-" * int((50 / 100) * (100 - percent))
            + "]"
        )
        print("Percent of this year : " + (barre))
        print("\n")
        Percentage.objectHTML = (
            (str(orbit[object][0]["info"]) + str(" : ") + str(object))
            + ("<br />")
            + str(("Day of the year : ") + str("Day ") + str(new))
            + ("<br />")
            + str(
                ("Year progress : ")
                + str(Percentage.objectResult)
                + str("%")
                + ("<br />")
            )
        )
        percent = Percentage.objectResult
        barre = (
            "["
            + "#" * int((50 / 100) * percent)
            + "_" * int((50 / 100) * (100 - percent))
            + "]"
        )
        Percentage.barrobject = "Percent of this year : " + (barre) + str("\n")
        Percentage.barrobjectHTML = (
            "Percent of this year : " + (barre) + ("<br />")
        )
        indexFile.write("<br />")
        indexFile.write("<br />")
        indexFile.write(
        str("<img src=")
        + str('"')
        + str(picture)
        + str('" ')
        + str(
            'alt="object" width='
            + str('"')
            + str(W)
            + str('"')
            + str(" height=")
            + str('"')
            + str(H)
            + str('">')
        )
        )

        indexFile.write("<br />")
        indexFile.write(Percentage.objectHTML)
        indexFile.write(Percentage.barrobjectHTML)
        indexFile.close()

def Earth():
    with open("/var/www/html/orbital.json", "r") as O:
        orbit = json.load(O)
        contentHtml = open("/var/www/html/main.html", "a")
        picture = orbit["Earth"][0]["Picture"]
        W = orbit["Earth"][0]["PicW"]
        H = orbit["Earth"][0]["PicH"]
        indexFile = open("main.html", "a")
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
        Percentage.earthHTML = (
            ("Planet : Earth")
            + ("<br />")
            + str(("Day of the year : ") + str("Day ") + str(new))
            + ("<br />")
            + str(("Year progress : ") + str(Percentage.EarthResult) + str("%"))
            + ("<br />")
        )
        percent = Percentage.EarthResult
        barre = (
            "["
            + "#" * int((50 / 100) * percent)
            + "_" * int((50 / 100) * (100 - percent))
            + "]"
        )
        Percentage.BarrEarth = "Percent of this year : " + (barre) + str("\n\n")
        print(Percentage.BarrEarth)
        Percentage.BarrEarthHTML = "Percent of this year : " + (barre) + ("<br />")
        contentHtml.write(
            str("<img src=")
            + str('"')
            + str(picture)
            + str('" ')
            + str(
                'alt="object" width='
                + str('"')
                + str(W)
                + str('"')
                + str(" height=")
                + str('"')
                + str(H)
                + str('">')
            )
        )
        contentHtml.write("<br />")
        contentHtml.write(Percentage.earthHTML)
        contentHtml.write(Percentage.BarrEarthHTML)
        contentHtml.close()


def perihelion(object, years1, years):
    indexFile = open("/var/www/html/main.html", "a")
    with open("/var/www/html/orbital.json", "r") as O:
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
                    + "-" * int((50 / 100) * (100 - percent))
                    + "]"
                )
                print("Percent of this year : " + (barre))
                print("\n")
                Percentage.objectHTML = (
                    (str(orbit[object][0]["info"]) + str(" : ") + str(object))
                    + ("<br />")
                    + str(("Day of the year : ") + str("Day ") + str(new))
                    + ("<br />")
                    + str(
                        ("Year progress : ")
                        + str(Percentage.objectResult)
                        + str("%")
                        + ("<br />")
                    )
                )
                percent = Percentage.objectResult
                barre = (
                    "["
                    + "#" * int((50 / 100) * percent)
                    + "_" * int((50 / 100) * (100 - percent))
                    + "]"
                )
                Percentage.barrobject = "Percent of this year : " + (barre) + str("\n")
                Percentage.barrobjectHTML = (
                    "Percent of this year : " + (barre) + ("<br />")
                )
                indexFile.write("<br />")
                indexFile.write("<br />")
                indexFile.write(
                    str("<img src=")
                    + str('"')
                    + str(picture)
                    + str('" ')
                    + str(
                        'alt="object" width='
                        + str('"')
                        + str(W)
                        + str('"')
                        + str(" height=")
                        + str('"')
                        + str(H)
                        + str('">')
                    )
                )

                indexFile.write("<br />")
                indexFile.write(Percentage.objectHTML)
                indexFile.write(Percentage.barrobjectHTML)
                indexFile.close()


Earth()
perihelion("Mercury", 88, 88)
perihelion("Venus", 215, 215)
perihelion("Earth", 364, 364)
perihelion("Moon", 28, 28)
perihelion("Mars", 688, 688)
perihelion("Jupiter", 4328, 4328)
perihelion("Saturn", 10719, 10719)
perihelion("Uranus", 30769, 30769)
perihelion("Neptune", 60639, 60639)
perihelion("Pluto", 90591, 90591)
perihelion("Tesla", 559, 559)
perihelion("Ceres", 1684, 1684)
perihelion("Haumea", 103775, 103775)
perihelion("Makemake", 112330, 112330)
perihelion("Eris", 203651, 203651)
goblin("2015 TG387 The Gobelin")
perihelion("Encke", 1204, 1204)
perihelion("Faye", 2660, 2660)
perihelion("Hale-Bopp", 729117, 866718)
perihelion("Halley", 27564, 27564)


endHTML = str("</p>") + str("\n") + str("</font>") + str("\n") + str("</body>")

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

contentHtml = open("/var/www/html/main.html", "a")
contentHtml.write("<br />")
contentHtml.write("<br />")
contentHtml.write(
    "Developer : Hamdy Abou El Anein - https://github.com/hamdyaea/SolarSystemPercentage"
)
contentHtml.write("<br />")
contentHtml.write("<br />")
contentHtml.write("<br />")
contentHtml.write(("Last update : ") + (dt_string) + str(" ( GMT+1 )"))
contentHtml.write(
    '<p>This page is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nd/4.0/">Creative Commons Attribution-NoDerivatives 4.0 International License</a>.</p>'
)
contentHtml.write(endHTML)
contentHtml.close()
