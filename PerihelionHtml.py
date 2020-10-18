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


def start():
    startHtml = (
        str("<!DOCTYPE html>")
        + str("\n")
        + str("<html>")
        + str("\n")
        + str("<head>")
        + str("\n")
        + str('<meta charset="UTF-8">')
        + str(
            '<link rel="apple-touch-icon" sizes="57x57" href="https://astrometry.ch/pictures/apple-icon-57x57.png">'
        )
        + str(
            '<link rel="apple-touch-icon" sizes="60x60" href="https://astrometry.ch/pictures/apple-icon-60x60.png">'
        )
        + str(
            '<link rel="apple-touch-icon" sizes="72x72" href="https://astrometry.ch/pictures/apple-icon-72x72.png">'
        )
        + str(
            '<link rel="apple-touch-icon" sizes="76x76" href="https://astrometry.ch/pictures/apple-icon-76x76.png">'
        )
        + str(
            '<link rel="apple-touch-icon" sizes="114x114" href="https://astrometry.ch/pictures/apple-icon-114x114.png">'
        )
        + str(
            '<link rel="apple-touch-icon" sizes="120x120" href="https://astrometry.ch/pictures/apple-icon-120x120.png">'
        )
        + str(
            '<link rel="apple-touch-icon" sizes="144x144" href="https://astrometry.ch/pictures/apple-icon-144x144.png">'
        )
        + str(
            '<link rel="apple-touch-icon" sizes="152x152" href="https://astrometry.ch/pictures/apple-icon-152x152.png">'
        )
        + str(
            '<link rel="apple-touch-icon" sizes="180x180" href="https://astrometry.ch/pictures/apple-icon-180x180.png">'
        )
        + str(
            '<link rel="icon" type="image/png" sizes="192x192"  href="https://astrometry.ch/pictures/android-icon-192x192.png">'
        )
        + str(
            '<link rel="icon" type="image/png" sizes="32x32" href="https://astrometry.ch/pictures/favicon-32x32.png">'
        )
        + str(
            '<link rel="icon" type="image/png" sizes="96x96" href="https://astrometry.ch/pictures/favicon-96x96.png">'
        )
        + str(
            '<link rel="icon" type="image/png" sizes="16x16" href="https://astrometry.ch/pictures/favicon-16x16.png">'
        )
        + str(
            '<link rel="manifest" href="https://astrometry.ch/pictures/manifest.json">'
        )
        + str('<meta name="msapplication-TileColor"content="#ffffff">')
        + str(
            '<meta name="msapplication-TileImage" content="https://astrometry.ch/pictures/ms-icon-144x144.png">'
        )
        + str('<meta name="theme-color" content="#ffffff">')
        + str('<meta name="viewport" content="width=device-width, initial-scale=1">')
        + str("\n")
        + str("<title>Astrometry </title>")
        + str("\n")
        + str(
            '<link rel="stylesheet" href="https://astrometry.ch/css/style.css" type="text/css">'
        )
        + str("\n")
        + str("</head>")
        + str("\n")
        + str("<body>")
        + str("\n")
        + str('<div id="header">')
        + str("\n")
        + str('<div class="wrapper clearfix">')
        + str("\n")
        + str('<div id="logo">')
        + str("\n")
        + str(
            '<a href="index.html"><img src="https://astrometry.ch/pictures/astrometry1.png" alt="LOGO"></a>'
        )
        + str("\n")
        + str("</div>")
        + str("\n")
        + str('<ul id="navigation">')
        + str("\n")
        + str('<li class="selected">')
        + str("\n")
        + str('<a href="index.html">Home</a>')
        + str("\n")
        + str("</li>")
        + str("\n")
        + str("<li>")
        + str("\n")
        + str('<a href="about.html">Information</a>')
        + str("\n")
        + str("</li>")
        + str("\n")
        + str("<li>")
        + str("\n")
        + str('<a href="blog.html">Api Perihelion</a>')
        + str("\n")
        + str("</li>")
        + str("\n")
        + str("</ul>")
        + str("\n")
        + str("</div>")
        + str("\n")
        + str("</div>")
        + str("\n")
        + str('<div id="contents">')
        + str("\n")
        + str('<div id="adbox">')
        + str("\n")
        + str('<div class="wrapper clearfix">')
        + str("\n")
        + str('<div class="info">')
        + str("\n")
        + str("<marquee> <h1>Astrometry.ch </h1> </marquee>")
        + str("\n")
        + str("<marquee> <h1>Hamdy Abou El Anein </h1> </marquee>")
        + str("\n")
        + str("</div>")
        + str("\n")
        + str("</div>")
        + str("\n")
        + str("</div>")
        + str("\n")
        + str("</div>")
        + str("\n")
        + str('<div id="footer">')
        + str("\n")
        + str('<ul id="featured" class="wrapper clearfix">')
        + str("\n")
    )

    indexFile = open("/var/www/html/index.html", "w")
    indexFile.write(startHtml)
    indexFile.close()


def neowise(object):
    Percentage.Goblin_current_year = date.today().year
    Percentage.Goblin_today = int(datetime.today().strftime("%d"))
    Percentage.Goblin_thisMonth = int(datetime.today().strftime("%m"))
    indexFile = open("/var/www/html/index.html", "a")
    with open("/var/www/html/orbital.json", "r") as O:
        orbit = json.load(O)
        picture = orbit[object][0]["Picture"]
        W = orbit[object][0]["PicW"]
        H = orbit[object][0]["PicH"]
        d2 = date(2020, 7, 3)
        d1 = date(
            Percentage.Goblin_current_year,
            Percentage.Goblin_thisMonth,
            Percentage.Goblin_today,
        )
        d0 = date(8800, 7, 3)
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
        indexFile.write("<li>")
        indexFile.write("\n")
        indexFile.write(
            str('<img src="')
            + str(picture)
            + str('" alt="Img" height="')
            + str(H)
            + str('" width="')
            + str(W)
            + str('">')
        )
        indexFile.write("\n")
        indexFile.write(
            str('<h3><a href="blog.html">')
            + str(orbit[object][0]["info"])
            + str(" : ")
            + str(object)
            + str("</a></h3><br/>")
        )
        indexFile.write("\n")
        indexFile.write("<p>")
        indexFile.write("\n")
        indexFile.write(
            str("Day of the year : Day ")
            + str(new)
            + str("<br />Last perihelion : ")
            + str(orbit[object][0]["Peri"][0])
            + str("<br />Next perihelion : ")
            + str(orbit[object][0]["Peri"][1])
            + str("<br />")
            + str("Orbital period : ")
            + str(orbit[object][0]["orperiod"])
            + str("<br />Year progress : ")
            + str(Percentage.objectResult)
            + str("%")
            + str("<br />")
            + str("Percent of this year : ")
            + str(barre)
        )
        indexFile.write("\n")
        indexFile.write("</p>")
        indexFile.write("\n")
        indexFile.write("</li>")
        indexFile.write("\n")
        indexFile.close()


def atlas(object):
    Percentage.Goblin_current_year = date.today().year
    Percentage.Goblin_today = int(datetime.today().strftime("%d"))
    Percentage.Goblin_thisMonth = int(datetime.today().strftime("%m"))
    indexFile = open("/var/www/html/index.html", "a")
    with open("/var/www/html/orbital.json", "r") as O:
        orbit = json.load(O)
        picture = orbit[object][0]["Picture"]
        W = orbit[object][0]["PicW"]
        H = orbit[object][0]["PicH"]
        d2 = date(2020, 5, 31)
        d1 = date(
            Percentage.Goblin_current_year,
            Percentage.Goblin_thisMonth,
            Percentage.Goblin_today,
        )
        d0 = date(6420, 6, 6)
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
        indexFile.write("<li>")
        indexFile.write("\n")
        indexFile.write(
            str('<img src="')
            + str(picture)
            + str('" alt="Img" height="')
            + str(H)
            + str('" width="')
            + str(W)
            + str('">')
        )
        indexFile.write("\n")
        indexFile.write(
            str('<h3><a href="blog.html">')
            + str(orbit[object][0]["info"])
            + str(" : ")
            + str(object)
            + str("</a></h3><br/>")
        )
        indexFile.write("\n")
        indexFile.write("<p>")
        indexFile.write("\n")
        indexFile.write(
            str("Day of the year : Day ")
            + str(new)
            + str("<br />Last perihelion : ")
            + str(orbit[object][0]["Peri"][0])
            + str("<br />Next perihelion : ")
            + str(orbit[object][0]["Peri"][1])
            + str("<br />")
            + str("Orbital period : ")
            + str(orbit[object][0]["orperiod"])
            + str("<br />Year progress : ")
            + str(Percentage.objectResult)
            + str("%")
            + str("<br />")
            + str("Percent of this year : ")
            + str(barre)
        )
        indexFile.write("\n")
        indexFile.write("</p>")
        indexFile.write("\n")
        indexFile.write("</li>")
        indexFile.write("\n")
        indexFile.close()


def goblin(object):
    Percentage.Goblin_current_year = date.today().year + 2522
    Percentage.Goblin_today = int(datetime.today().strftime("%d"))
    Percentage.Goblin_thisMonth = int(datetime.today().strftime("%m"))
    indexFile = open("/var/www/html/index.html", "a")
    with open("/var/www/html/orbital.json", "r") as O:
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
        new = new + 11826001

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
        indexFile.write("<li>")
        indexFile.write("\n")
        indexFile.write(
            str('<img src="')
            + str(picture)
            + str('" alt="Img" height="')
            + str(H)
            + str('" width="')
            + str(W)
            + str('">')
        )
        indexFile.write("\n")
        indexFile.write(
            str('<h3><a href="blog.html">')
            + str(orbit[object][0]["info"])
            + str(" : ")
            + str(object)
            + str("</a></h3><br/>")
        )
        indexFile.write("\n")
        indexFile.write("<p>")
        indexFile.write("\n")
        indexFile.write(
            str("Day of the year : Day ")
            + str(new)
            + str("<br />Last perihelion : ")
            + str(orbit[object][0]["Peri"][0])
            + str("<br />Next perihelion : ")
            + str(orbit[object][0]["Peri"][1])
            + str("<br />")
            + str("Orbital period : ")
            + str(orbit[object][0]["orperiod"])
            + str("<br />Year progress : ")
            + str(Percentage.objectResult)
            + str("%")
            + str("<br />")
            + str("Percent of this year : ")
            + str(barre)
        )
        indexFile.write("\n")
        indexFile.write("</p>")
        indexFile.write("\n")
        indexFile.write("</li>")
        indexFile.write("\n")
        indexFile.close()


def sedna(object):
    Percentage.Goblin_current_year = date.today().year + 96
    Percentage.Goblin_today = int(datetime.today().strftime("%d"))
    Percentage.Goblin_thisMonth = int(datetime.today().strftime("%m"))
    indexFile = open("/var/www/html/index.html", "a")
    with open("/var/www/html/orbital.json", "r") as O:
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

        indexFile.write("<li>")
        indexFile.write("\n")
        indexFile.write(
            str('<img src="')
            + str(picture)
            + str('" alt="Img" height="')
            + str(H)
            + str('" width="')
            + str(W)
            + str('">')
        )
        indexFile.write("\n")
        indexFile.write(
            str('<h3><a href="blog.html">')
            + str(orbit[object][0]["info"])
            + str(" : ")
            + str(object)
            + str("</a></h3><br/>")
        )
        indexFile.write("\n")
        indexFile.write("<p>")
        indexFile.write("\n")
        indexFile.write(
            str("Day of the year : Day ")
            + str(new)
            + str("<br />Last perihelion : ")
            + str(orbit[object][0]["Peri"][0])
            + str("<br />Next perihelion : ")
            + str(orbit[object][0]["Peri"][1])
            + str("<br />")
            + str("Orbital period : ")
            + str(orbit[object][0]["orperiod"])
            + str("<br />Year progress : ")
            + str(Percentage.objectResult)
            + str("%")
            + str("<br />")
            + str("Percent of this year : ")
            + str(barre)
        )
        indexFile.write("\n")
        indexFile.write("</p>")
        indexFile.write("\n")
        indexFile.write("</li>")
        indexFile.write("\n")
        indexFile.close()


def Earth():
    indexFile = open("/var/www/html/index.html", "a")
    with open("/var/www/html/orbital.json", "r") as O:
        orbit = json.load(O)
        picture = orbit["Earth"][0]["Picture"]
        W = orbit["Earth"][0]["PicW"]
        H = orbit["Earth"][0]["PicH"]
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
        percent = Percentage.EarthResult
        barre = (
            "["
            + "#" * int((25 / 100) * percent)
            + "_" * int((25 / 100) * (100 - percent))
            + "]"
        )
        Percentage.BarrEarth = "Percent of this year : " + (barre) + str("\n\n")
        print(Percentage.earth)
        print("Last perihelion : " + str(d0))
        print("Next perihelion : " + str(d2))
        print("Orbital period : 1 year")
        print(Percentage.BarrEarth)
        indexFile.write("<li>")
        indexFile.write("\n")
        indexFile.write(
            str('<img src="')
            + str(picture)
            + str('" alt="Img" height="')
            + str(H)
            + str('" width="')
            + str(W)
            + str('">')
        )
        indexFile.write("\n")
        indexFile.write(
            str('<h3><a href="blog.html">')
            + str("Planet : Earth")
            + str("</a></h3><br/>")
        )
        indexFile.write("\n")
        indexFile.write("<p>")
        indexFile.write("\n")
        indexFile.write(
            str("Day of the year : Day ")
            + str(new)
            + str("<br />Last perihelion : ")
            + str(d0)
            + str("<br />Next perihelion : ")
            + str(d2)
            + str("<br />")
            + str("Orbital period : 1 year")
            + str("<br />Year progress : ")
            + str(Percentage.EarthResult)
            + str("%")
            + str("<br />")
            + str("Percent of this year : ")
            + str(barre)
        )
        indexFile.write("\n")
        indexFile.write("</p>")
        indexFile.write("\n")
        indexFile.write("</li>")
        indexFile.write("\n")
        indexFile.close()


def perihelion(object, years1, years):
    indexFile = open("/var/www/html/index.html", "a")
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
                print("Last perihelion : " + str(Percentage.objectPerihelion))
                print("Next perihelion : " + str(d0))
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
                indexFile.write("<li>")
                indexFile.write("\n")
                indexFile.write(
                    str('<img src="')
                    + str(picture)
                    + str('" alt="Img" height="')
                    + str(H)
                    + str('" width="')
                    + str(W)
                    + str('">')
                )
                indexFile.write("\n")
                indexFile.write(
                    str('<h3><a href="blog.html">')
                    + str(orbit[object][0]["info"])
                    + str(" : ")
                    + str(object)
                    + str("</a></h3><br/>")
                )
                indexFile.write("\n")
                indexFile.write("<p>")
                indexFile.write("\n")
                indexFile.write(
                    str("Day of the year : Day ")
                    + str(new)
                    + str("<br />Last perihelion : ")
                    + str(Percentage.objectPerihelion)
                    + str("<br />Next perihelion : ")
                    + str(d0)
                    + str("<br />")
                    + str("Orbital period : ")
                    + str(orbit[object][0]["orperiod"])
                    + str("<br />Year progress : ")
                    + str(Percentage.objectResult)
                    + str("%")
                    + str("<br />")
                    + str("Percent of this year : ")
                    + str(barre)
                )
                indexFile.write("\n")
                indexFile.write("</p>")
                indexFile.write("\n")
                indexFile.write("</li>")
                indexFile.write("\n")
                indexFile.close()


indexFile = open("/var/www/html/index.html", "a")
start()
Earth()
perihelion("Mercury", 88, 88)
perihelion("Venus", 225, 225)
perihelion("Earth", 364, 364)
indexFile = open("/var/www/html/index.html", "a")
indexFile.write("</ul>")
indexFile.write("\n")
indexFile.write('<ul id="featured" class="wrapper clearfix">')
indexFile.write("\n")
indexFile.close()
indexFile = open("/var/www/html/index.html", "a")
perihelion("Moon", 28, 28)
perihelion("Mars", 688, 688)
perihelion("Jupiter", 4328, 4328)
perihelion("Saturn", 10719, 10719)
indexFile = open("/var/www/html/index.html", "a")
indexFile.write("</ul>")
indexFile.write("\n")
indexFile.write('<ul id="featured" class="wrapper clearfix">')
indexFile.write("\n")
indexFile.close()
indexFile = open("/var/www/html/index.html", "a")
perihelion("Uranus", 30769, 30769)
perihelion("Neptune", 60639, 60639)
perihelion("Pluto", 90591, 90591)
perihelion("Tesla", 559, 559)
indexFile.write("</ul>")
indexFile.write("\n")
indexFile.write("</ul>")
indexFile.write("\n")
indexFile.write('<ul id="featured" class="wrapper clearfix">')
indexFile.write("\n")
indexFile.close()
perihelion("Ceres", 1684, 1684)
perihelion("Haumea", 103775, 103775)
perihelion("Makemake", 112330, 112330)
perihelion("Eris", 203651, 203651)
indexFile = open("/var/www/html/index.html", "a")
indexFile.write("</ul>")
indexFile.write("\n")
indexFile.write('<ul id="featured" class="wrapper clearfix">')
indexFile.write("\n")
indexFile.close()
goblin("2015 TG387 The Gobelin")
perihelion("Encke", 1204, 1204)
perihelion("Faye", 2660, 2660)
perihelion("Hale-Bopp", 729117, 866718)
indexFile = open("/var/www/html/index.html", "a")
indexFile.write("</ul>")
indexFile.write("\n")
indexFile.write('<ul id="featured" class="wrapper clearfix">')
indexFile.write("\n")
indexFile.close()
perihelion("Halley", 27564, 27564)
atlas("C/2019 Y4 ATLAS")
neowise("C/2020 F3 NEOWISE")
perihelion("99942 Apophis", 324, 324)
indexFile = open("/var/www/html/index.html", "a")
indexFile.write("</ul>")
indexFile.write("\n")
indexFile.write('<ul id="featured" class="wrapper clearfix">')
indexFile.write("\n")
indexFile.close()
perihelion("2018 VP1", 731, 731)
perihelion("2020 SO", 387, 387)
sedna("90377 Sedna")
indexFile = open("/var/www/html/index.html", "a")
indexFile.write("</ul>")
indexFile.write("\n")
indexFile.close()


indexFile = open("/var/www/html/index.html", "a")
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

indexFile.write('<div class="body">')
indexFile.write("\n")
indexFile.write('<div class="wrapper clearfix">')
indexFile.write("\n")
indexFile.write('<div id="links">')
indexFile.write("\n")
indexFile.write("<div>")
indexFile.write("\n")
indexFile.write("<h4>Social media</h4>")
indexFile.write("\n")
indexFile.write("<ul>")
indexFile.write("\n")
indexFile.write("<li>")
indexFile.write("\n")
indexFile.write(
    '<a href="https://www.facebook.com/Astrometrych-106592170853278/" target="_blank">Facebook</a>'
)
indexFile.write("\n")
indexFile.write("</li>")
indexFile.write("\n")
indexFile.write("<li>")
indexFile.write("\n")
indexFile.write(
    '<a href="https://twitter.com/intent/follow?original_referer=https%3A%2F%2Fastrometry.ch%2F&ref_src=twsrc%5Etfw&screen_name=astrometry_ch&tw_p=followbutton" target="_blank">Twitter</a>'
)
indexFile.write("\n")
indexFile.write("</li>")
indexFile.write("\n")
indexFile.write("</ul>")
indexFile.write("\n")
indexFile.write("</div>")
indexFile.write("\n")
indexFile.write("<div>")
indexFile.write("\n")
indexFile.write("<ul>")
indexFile.write("\n")
indexFile.write("<li>")
indexFile.write("\n")
indexFile.write(
    '<a href="https://github.com/hamdyaea/SolarSystemPercentage">Github of Solar system percentage</a>'
)
indexFile.write("\n")
indexFile.write("</li>")
indexFile.write("\n")
indexFile.write("<li><p>This page is licensed under a")
indexFile.write("\n")
indexFile.write(
    '<a href="https://creativecommons.org/licenses/by-nd/4.0/">Creative Commons Attribution-NoDerivatives 4.0 International License</a></p>'
)
indexFile.write("\n")
indexFile.write("</li>")
indexFile.write("\n")
indexFile.write("</ul>")
indexFile.write("\n")
indexFile.write("</div>")
indexFile.write("\n")
indexFile.write("</div>")
indexFile.write("\n")
indexFile.write('<div id="newsletter">')
indexFile.write("\n")
indexFile.write(
    "<h4>Developer - Senior linux System Engineer : Hamdy Abou El Anein</h4>"
)
indexFile.write("\n")
indexFile.write(str("<h4>Last update : ") + str(dt_string) + str(" GMT+1   </h4>"))
indexFile.write("\n")
indexFile.write("</div>")
indexFile.write("\n")
indexFile.write('<p class="footnote">')
indexFile.write("\n")
indexFile.write("astrometry.ch - Hamdy Abou El Anein")
indexFile.write("\n")
indexFile.write("</p>")
indexFile.write("\n")
indexFile.write("</div>")
indexFile.write("\n")
indexFile.write("</div>")
indexFile.write("\n")
indexFile.write("</div>")
indexFile.write("\n")
indexFile.write("</body>")
indexFile.write("\n")
indexFile.write("</html>")
indexFile.close()
