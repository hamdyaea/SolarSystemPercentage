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
        self.todayFull
        self.MoonResult
        self.MoonPerihelion
        self.NewMoonPerihelion
        self.MercuryResult
        self.MercuryPerihelion
        self.NewMercuryPerihelion
        self.earth
        self.BarrEarth
        self.moon
        self.barrMoon
        self.mercury
        self.barrMercury



Percentage.current_year = date.today().year
Percentage.today = int(datetime.today().strftime("%d"))
Percentage.thisMonth = int(datetime.today().strftime("%m"))


def motd():
    motd=("\n")+str("\n")+str(" __     __               _   __")+str("\n")+str(" \ \   / /              (_) / /")+str("\n")+str("  \ \_/ /__  __ _ _ __     / / ")+str("\n")+str("   \   / _ \/ _` | '__|   / /  ")+str("\n")+str("    | |  __/ (_| | |     / / _ ")+str("\n")+str("    |_|\___|\__,_|_|    /_/ (_)")+str("\n\n")
    print(motd)

def Earth():
    d0 = date(Percentage.current_year, 1, 1)
    d1 = date(Percentage.current_year, Percentage.thisMonth, Percentage.today)
    d1 = d1 + timedelta(days=1)  # Year, month, day
    d2 = date(Percentage.current_year, 12, 31)
    d3 = d2 - d0
    d3 = str(d3)
    d3 = d3[:3]
    d3 = int(d3)
    d3 = d3 + 1
    ValuePercent = d3 / 100
    delta = d1 - d0
    new = re.sub("[^0-9]", "", str(delta))
    new = str(new)
    new = new[:3]
    new = int(new)
    Percentage.EarthResult = new / ValuePercent  # 365 / 100 = 3.65
    Percentage.EarthResult = round(Percentage.EarthResult, 2)

    # Add graph progress #####
    Percentage.earth=("Planet : Earth")+str("\n")+str(("Day of the year : ") + str("Day ") + str(new))+str("\n")+str(("Year progress : ") + str(Percentage.EarthResult) + str("%"))
    print(Percentage.earth)
    # Progress bar creation
    percent = Percentage.EarthResult
    barre = (
        "["
        + "#" * int((50 / 100) * percent)
        + "-" * int((50 / 100) * (100 - percent))
        + "]"
    )
    Percentage.BarrEarth=("Percent of this year : " + (barre)+str("\n"))
    print(Percentage.BarrEarth)


def Moon():  # d0 = first perihelion , d1 = today , d2 = next perihelion
    # Rotation year before this year

    years_ago_full = datetime.now() - timedelta(
        days=1 * 365
    )  # adapt to the number of years
    years_ago_full = str(years_ago_full)
    years_ago = years_ago_full[:4]
    years_ago = int(years_ago)  # result

    # Next rotation year
    years_after_full = datetime.now() + timedelta(
        days=1 * 365
    )  # adapt to the number of years
    years_after_full = str(years_after_full)
    years_after = years_after_full[:4]
    years_after = int(years_after)  # result

    with open("Orbit.json", "r") as O:
        orbit = json.load(O)
        thisYear = orbit["Moon"][str(Percentage.current_year)]  # This year
        years_ago = orbit["Moon"][str(years_ago)][-1]
        years_after = orbit["Moon"][str(years_after)][0]
        try:
            for i in thisYear:
                d0Year = i[:4]
                d0Year = int(d0Year)
                d0Month = i[5:7]
                d0Month = int(d0Month)
                d0Day = i[8:10]
                d0Day = int(d0Day)
                d0 = date(d0Year, d0Month, d0Day)
                d1 = date(
                    Percentage.current_year, Percentage.thisMonth, Percentage.today
                )
                if (
                    d0 >= d1 - timedelta(days=30) and d0 <= d1
                ):  # i is bigger or equal today - 30 days and smaller or equal today : First day of rotation
                    Percentage.MoonPerihelion = d0

            for i in thisYear:
                d0Year = i[:4]
                d0Year = int(d0Year)
                d0Month = i[5:7]
                d0Month = int(d0Month)
                d0Day = i[8:10]
                d0Day = int(d0Day)
                d0 = date(d0Year, d0Month, d0Day)
                d1 = date(
                    Percentage.current_year, Percentage.thisMonth, Percentage.today
                )
                if (
                    d0 <= d1 + timedelta(days=30) and d0 >= d1
                ):  # i is smaller or equal today + 30 days and bigger or equalt today : Next Perihelion
                    Percentage.NewMoonPerihelion = d0
                    d1 = date(
                        Percentage.current_year, Percentage.thisMonth, Percentage.today
                    )
                    d1 = d1 + timedelta(days=1)
                    d3 = Percentage.NewMoonPerihelion - Percentage.MoonPerihelion
                    d3 = str(d3)
                    d3 = d3[:3]
                    d3 = int(d3)
                    d3 = d3 + 1
                    ValuePercent = d3 / 100
                    delta = d1 - Percentage.MoonPerihelion
                    new = re.sub("[^0-9]", "", str(delta))
                    new = str(new)
                    new = new[:2]
                    new = int(new)

                    Percentage.MoonResult = new / ValuePercent
                    Percentage.MoonResult = round(Percentage.MoonResult, 2)

                    # Add graph progress #####

                    Percentage.moon=("Satelite : Moon")+str("\n")+str(("Day of the year : ") + str("Day ") + str(new))+str("\n")+str(("Year progress : ") + str(Percentage.MoonResult) + str("%"))
                    print(Percentage.moon)

                    percent = Percentage.MoonResult
                    barre = (
                        "["
                        + "#" * int((50 / 100) * percent)
                        + "-" * int((50 / 100) * (100 - percent))
                        + "]"
                    )
                    Percentage.barrMoon=("Percent of this year : " + (barre)+str("\n"))
                    print(Percentage.barrMoon)
        except:
            try:
                for i in thisYear:
                    d0Year = i[:4]
                    d0Year = int(d0Year)
                    d0Month = i[5:7]
                    d0Month = int(d0Month)
                    d0Day = i[8:10]
                    d0Day = int(d0Day)
                    d0 = date(d0Year, d0Month, d0Day)
                    d1 = date(
                        Percentage.current_year, Percentage.thisMonth, Percentage.today
                    )
                    if (
                        d0 >= d1 - timedelta(days=30) and d0 <= d1
                    ):  # i is bigger or equal today - 30 days and smaller or equal today : First day of rotation
                        Percentage.MoonPerihelion = d0

                    d0Year = years_after[:4]
                    d0Year = int(d0Year)
                    d0Month = years_after[5:7]
                    d0Month = int(d0Month)
                    d0Day = years_after[8:10]
                    d0Day = int(d0Day)

                    d0 = date(d0Year, d0Month, d0Day)
                    d1 = date(
                        Percentage.current_year, Percentage.thisMonth, Percentage.today
                    )
                    if (
                        d0 <= d1 + timedelta(days=30) and d0 >= d1
                    ):  # i is smaller or equal today + 30 days and bigger or equalt today : Next Perihelion
                        Percentage.NewMoonPerihelion = d0
                    d1 = date(
                        Percentage.current_year, Percentage.thisMonth, Percentage.today
                    )
                    d1 = d1 + timedelta(days=1)
                    d3 = Percentage.NewMoonPerihelion - Percentage.MoonPerihelion
                    d3 = str(d3)
                    d3 = d3[:3]
                    d3 = int(d3)
                    d3 = d3 + 1
                    ValuePercent = d3 / 100
                    delta = d1 - Percentage.MoonPerihelion
                    new = re.sub("[^0-9]", "", str(delta))
                    new = str(new)
                    new = new[:2]
                    new = int(new)

                    Percentage.MoonResult = new / ValuePercent
                    Percentage.MoonResult = round(Percentage.MoonResult, 2)

                    # Add graph progress #####

                    Percentage.moon=("Satelite : Moon")+str("\n")+str(("Day of the year : ") + str("Day ") + str(new))+str("\n")+str(("Year progress : ") + str(Percentage.MoonResult) + str("%"))
                    print(Percentage.moon)

                    percent = Percentage.MoonResult
                    barre = (
                        "["
                        + "#" * int((50 / 100) * percent)
                        + "-" * int((50 / 100) * (100 - percent))
                        + "]"
                    )
                    Percentage.barrMoon=("Percent of this year : " + (barre)+str("\n"))
                    print(Percentage.barrMoon)
            except:
                d0Year = years_ago[:4]
                d0Year = int(d0Year)
                d0Month = years_ago[5:7]
                d0Month = int(d0Month)
                d0Day = years_ago[8:10]
                d0Day = int(d0Day)

                d0 = date(d0Year, d0Month, d0Day)
                d1 = date(
                    Percentage.current_year, Percentage.thisMonth, Percentage.today
                )
                if (
                    d0 <= d1 - timedelta(days=30) and d0 >= d1
                ):  # i is smaller or equal today + 30 days and bigger or equalt today : Next Perihelion
                    Percentage.NewMoonPerihelion = d0

                for i in thisYear:
                    d0Year = i[:4]
                    d0Year = int(d0Year)
                    d0Month = i[5:7]
                    d0Month = int(d0Month)
                    d0Day = i[8:10]
                    d0Day = int(d0Day)
                    d0 = date(d0Year, d0Month, d0Day)
                    d1 = date(
                        Percentage.current_year, Percentage.thisMonth, Percentage.today
                    )
                    d1 = d1 + timedelta(days=1)
                    if (
                        d0 <= d1 + timedelta(days=30) and d0 >= d1
                    ):  # i is smaller or equal today + 30 days and bigger or equalt today : Next Perihelion
                        Percentage.NewMoonPerihelion = d0
                        d1 = date(
                            Percentage.current_year,
                            Percentage.thisMonth,
                            Percentage.today,
                        )
                        d3 = Percentage.NewMoonPerihelion - Percentage.MoonPerihelion
                        d3 = str(d3)
                        d3 = d3[:3]
                        d3 = int(d3)
                        d3 = d3 + 1
                        ValuePercent = d3 / 100
                        delta = d1 - Percentage.MoonPerihelion
                        new = re.sub("[^0-9]", "", str(delta))
                        new = str(new)
                        new = new[:2]
                        new = int(new)

                        Percentage.MoonResult = new / ValuePercent
                        Percentage.MoonResult = round(Percentage.MoonResult, 2)

                        # Add graph progress #####

                        Percentage.moon=("Satelite : Moon")+str("\n")+str(("Day of the year : ") + str("Day ") + str(new))+str("\n")+str(
                            ("Year progress : ") + str(Percentage.MoonResult) + str("%")
                        )
                        print(Percentage.moon)


                        percent = Percentage.MoonResult
                        barre = (
                            "["
                            + "#" * int((50 / 100) * percent)
                            + "-" * int((50 / 100) * (100 - percent))
                            + "]"
                        )
                        Percentage.barrMoon=("Percent of this year : " + (barre)+str("\n"))
                        print(Percentage.barrMoon)


def Mercury():  # d0 = first perihelion , d1 = today , d2 = next perihelion

    # Rotation year before this year
    years_ago_full = datetime.now() - timedelta(
        days=1 * 365
    )  # adapt to the number of years
    years_ago_full = str(years_ago_full)
    years_ago = years_ago_full[:4]
    years_ago = int(years_ago)  # result

    # Next rotation year
    years_after_full = datetime.now() + timedelta(
        days=1 * 365
    )  # adapt to the number of years
    years_after_full = str(years_after_full)
    years_after = years_after_full[:4]
    years_after = int(years_after)  # result

    with open("Orbit.json", "r") as O:
        orbit = json.load(O)
        thisYear = orbit["Mercury"][str(Percentage.current_year)]  # This year
        years_ago = orbit["Mercury"][str(years_ago)][-1]
        years_after = orbit["Mercury"][str(years_after)][0]
        try:
            for i in thisYear:
                d0Year = i[:4]
                d0Year = int(d0Year)
                d0Month = i[5:7]
                d0Month = int(d0Month)
                d0Day = i[8:10]
                d0Day = int(d0Day)
                d0 = date(d0Year, d0Month, d0Day)
                d1 = date(
                    Percentage.current_year, Percentage.thisMonth, Percentage.today
                )
                d1 = d1 + timedelta(days=1)
                if (
                    d0 >= d1 - timedelta(days=90) and d0 <= d1
                ):  # i is bigger or equal today - 30 days and smaller or equal today : First day of rotation
                    Percentage.MercuryPerihelion = d0

            for i in thisYear:
                d0Year = i[:4]
                d0Year = int(d0Year)
                d0Month = i[5:7]
                d0Month = int(d0Month)
                d0Day = i[8:10]
                d0Day = int(d0Day)
                d0 = date(d0Year, d0Month, d0Day)
                d1 = date(
                    Percentage.current_year, Percentage.thisMonth, Percentage.today
                )
                d1 = d1 + timedelta(days=1)
                if (
                    d0 <= d1 + timedelta(days=90) and d0 >= d1
                ):  # i is smaller or equal today + 30 days and bigger or equalt today : Next Perihelion
                    Percentage.NewMercuryPerihelion = d0
                d1 = date(
                    Percentage.current_year, Percentage.thisMonth, Percentage.today
                )
                d3 = Percentage.NewMercuryPerihelion - Percentage.MercuryPerihelion
                d3 = str(d3)
                d3 = d3[:3]
                d3 = int(d3)
                d3 = d3 + 1
                ValuePercent = d3 / 100
                delta = d1 - Percentage.MercuryPerihelion
                new = re.sub("[^0-9]", "", str(delta))
                new = str(new)
                new = new[:2]
                new = int(new)

                Percentage.MercuryResult = new / ValuePercent
                Percentage.MercuryResult = round(Percentage.MercuryResult, 2)

                # Add graph progress #####

                Percentage.mercury=("Planet : Mercury")+str("\n")+str(("Day of the year : ") + str("Day ") + str(new))+str("\n")+str("\n")+str(("Year progress : ") + str(Percentage.MercuryResult) + str("%"))
                print(Percentage.mercury)

                percent = Percentage.MercuryResult
                barre = (
                    "["
                    + "#" * int((50 / 100) * percent)
                    + "-" * int((50 / 100) * (100 - percent))
                    + "]"
                )
                Percentage.barrMercury=("Percent of this year : " + (barre)+str("\n"))
                print(Percentage.barrMercury)
        except:
            try:
                for i in thisYear:
                    d0Year = i[:4]
                    d0Year = int(d0Year)
                    d0Month = i[5:7]
                    d0Month = int(d0Month)
                    d0Day = i[8:10]
                    d0Day = int(d0Day)
                    d0 = date(d0Year, d0Month, d0Day)
                    d1 = date(
                        Percentage.current_year, Percentage.thisMonth, Percentage.today
                    )
                    if (
                        d0 >= d1 - timedelta(days=90) and d0 <= d1
                    ):  # i is bigger or equal today - 30 days and smaller or equal today : First day of rotation
                        Percentage.MercuryPerihelion = d0

                d0Year = years_after[:4]
                d0Year = int(d0Year)
                d0Month = years_after[5:7]
                d0Month = int(d0Month)
                d0Day = years_after[8:10]
                d0Day = int(d0Day)

                d0 = date(d0Year, d0Month, d0Day)
                d1 = date(
                    Percentage.current_year, Percentage.thisMonth, Percentage.today
                )
                if (
                    d0 <= d1 + timedelta(days=90) and d0 >= d1
                ):  # i is smaller or equal today + 30 days and bigger or equalt today : Next Perihelion
                    Percentage.NewMercuryPerihelion = d0
                d1 = date(
                    Percentage.current_year, Percentage.thisMonth, Percentage.today
                )
                d1 = d1 + timedelta(days=1)
                d3 = Percentage.NewMercuryPerihelion - Percentage.MercuryPerihelion
                d3 = str(d3)
                d3 = d3[:3]
                d3 = int(d3)
                d3 = d3 + 1
                ValuePercent = d3 / 100
                delta = d1 - Percentage.MercuryPerihelion
                new = re.sub("[^0-9]", "", str(delta))
                new = str(new)
                new = new[:2]
                new = int(new)

                Percentage.MercuryResult = new / ValuePercent
                Percentage.MercuryResult = round(Percentage.MercuryResult, 2)

                # Add graph progress #####

                Percentage.mercury=("Planet : Mercury")+str("\n")+str(("Day of the year : ") + str("Day ") + str(new))+str("\n")+str(("Year progress : ") + str(Percentage.MercuryResult) + str("%"))
                print(Percentage.mercury)

                percent = Percentage.MercuryResult
                barre = (
                    "["
                    + "#" * int((50 / 100) * percent)
                    + "-" * int((50 / 100) * (100 - percent))
                    + "]"
                )
                Percentage.barrMercury=("Percent of this year : " + (barre)+str("\n"))
                print(Percentage.barrMercury)

            except:
                d0Year = years_ago[:4]
                d0Year = int(d0Year)
                d0Month = years_ago[5:7]
                d0Month = int(d0Month)
                d0Day = years_ago[8:10]
                d0Day = int(d0Day)

                d0 = date(d0Year, d0Month, d0Day)
                d1 = date(
                    Percentage.current_year, Percentage.thisMonth, Percentage.today
                )
                d1 = d1 + timedelta(days=1)
                if (
                    d0 <= d1 - timedelta(days=90) and d0 >= d1
                ):  # i is smaller or equal today + 30 days and bigger or equalt today : Next Perihelion
                    Percentage.NewMercuryPerihelion = d0

                for i in thisYear:
                    d0Year = i[:4]
                    d0Year = int(d0Year)
                    d0Month = i[5:7]
                    d0Month = int(d0Month)
                    d0Day = i[8:10]
                    d0Day = int(d0Day)
                    d0 = date(d0Year, d0Month, d0Day)
                    d1 = date(
                        Percentage.current_year, Percentage.thisMonth, Percentage.today
                    )
                    if (
                        d0 <= d1 + timedelta(days=90) and d0 >= d1
                    ):  # i is smaller or equal today + 30 days and bigger or equalt today : Next Perihelion
                        Percentage.NewMercuryPerihelion = d0
                    d1 = date(
                        Percentage.current_year, Percentage.thisMonth, Percentage.today
                    )
                    d3 = Percentage.NewMercuryPerihelion - Percentage.MercuryPerihelion
                    d3 = str(d3)
                    d3 = d3[:3]
                    d3 = int(d3)
                    d3 = d3 + 1
                    ValuePercent = d3 / 100
                    delta = d1 - Percentage.MercuryPerihelion
                    new = re.sub("[^0-9]", "", str(delta))
                    new = str(new)
                    new = new[:2]
                    new = int(new)

                    Percentage.MercuryResult = new / ValuePercent
                    Percentage.MercuryResult = round(Percentage.MercuryResult, 2)

                    # Add graph progress #####

                    Percentage.mercury = ("Planet : Mercury")+str("\n")+str(("Day of the year : ") + str("Day ") + str(new))+str("\n")+str(
                        ("Year progress : ") + str(Percentage.MercuryResult) + str("%")
                    )
                    print(Percentage.mercury)


                    percent = Percentage.MercuryResult
                    barre = (
                        "["
                        + "#" * int((50 / 100) * percent)
                        + "-" * int((50 / 100) * (100 - percent))
                        + "]"
                    )
                    Percentage.barrMercury=("Percent of this year : " + (barre)+str("\n"))
                    print(Percentage.barrMercury)
    """

    Do the same for the moon and other solar system planets, natural satelites, ISS, of all the solar system. 
    """
motd()
Earth()
Moon()
Mercury()

startHtml=(str("<!DOCTYPE html>")+str("\n")+str("<html>")+str("\n")+str("<head>")+str("\n")+str("<title>Percent Progress of the Solar System</title>")+str("\n")+str("</head>")+str("\n")+str('<body bgcolor="#000000">')+str("\n")+str('<font color="blue">')+str("\n")+str("<p>")+str("\n")+str('<img src="peri.png" alt="perihelion" width="500" height="333">'+str("\n")+str("<br />")+str("\n")+str("<br />")+str("\n")+str("<br />")))


indexFile = open("index.html",'w')
indexFile.write(startHtml)
indexFile.close()

contentHtml = open("index.html",'a')
contentHtml.write(Percentage.earth)
contentHtml.write(Percentage.BarrEarth)
contentHtml.write(Percentage.moon)
contentHtml.write(Percentage.barrMoon)
contentHtml.write(Percentage.mercury)
contentHtml.write(Percentage.barrMercury)
contentHtml.close()


