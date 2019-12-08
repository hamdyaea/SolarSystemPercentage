#!/usr/bin/env python3

# Developer : Hamdy Abou El Anein
# hamdy.aea@protonmail.com

# percentage of the year for the earth, the moon, jupiter, Saturn, etc...
# Lunar Perigee and Apogee Calculator : https://www.fourmilab.ch/earthview/pacalc.html

from datetime import date, datetime, timedelta
import re
import json
from progress.bar import Bar


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


Percentage.current_year = date.today().year
Percentage.today = int(datetime.today().strftime("%d"))
Percentage.thisMonth = int(datetime.today().strftime("%m"))


def motd():
    print("\n")
    print(" __     __               _   __")
    print(" \ \   / /              (_) / /")
    print("  \ \_/ /__  __ _ _ __     / / ")
    print("   \   / _ \/ _` | '__|   / /  ")
    print("    | |  __/ (_| | |     / / _ ")
    print("    |_|\___|\__,_|_|    /_/ (_)")
    print("\n\n")


def Earth():
    d0 = date(Percentage.current_year, 1, 1)
    d1 = date(
        Percentage.current_year, Percentage.thisMonth, Percentage.today
    )  # Year, month, day
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

    print("Planet : Earth")
    print(("Day of the year : ") + str("Day ") + str(new))
    print(("Year progress : ") + str(Percentage.EarthResult) + str("%"))
    # Progress bar creation
    bar = Bar("Percent of this year : ", max=100)
    for i in range(int(Percentage.EarthResult)):
        bar.next()
    bar.finish()
    print("\n")


def Moon():  # d0 = first perihelion , d1 = today , d2 = next perihelion
    with open("Orbit.json", "r") as O:
        orbit = json.load(O)
        thisYear = orbit["Moon"][str(Percentage.current_year)]  # This year
        """
        d0Str=orbit["Moon"][str(Percentage.current_year)][0]
        d0Year=(d0Str[:4])
        d0Year=int(d0Year)
        d0Month=(d0Str[5:7])
        d0Month=int(d0Month)
        d0Day=(d0Str[8:10])
        d0Day=int(d0Day)

        d2Str = orbit["Moon"][str(Percentage.current_year)][1]
        d2Year = (d2Str[:4])
        d2Year = int(d2Year)
        d2Month = (d2Str[5:7])
        d2Month = int(d2Month)
        d2Day = (d2Str[8:10])
        d2Day = int(d2Day)

        d0 =date(d0Year,d0Month,d0Day)
        d1 = date(Percentage.current_year, Percentage.thisMonth, Percentage.today)
        d2 = date(d2Year,d2Month,d2Day)
        d3 = d2 - d0
        """
        for i in thisYear:
            d0Year = i[:4]
            d0Year = int(d0Year)
            d0Month = i[5:7]
            d0Month = int(d0Month)
            d0Day = i[8:10]
            d0Day = int(d0Day)
            d0 = date(d0Year, d0Month, d0Day)
            d1 = date(Percentage.current_year, Percentage.thisMonth, Percentage.today)
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
            d1 = date(Percentage.current_year, Percentage.thisMonth, Percentage.today)
            if (
                d0 <= d1 + timedelta(days=30) and d0 >= d1
            ):  # i is smaller or equal today + 30 days and bigger or equalt today : Next Perihelion
                Percentage.NewMoonPerihelion = d0
        # print(Percentage.MoonPerihelion) # = d0
        # print(Percentage.NewMoonPerihelion) # = d2
        d1 = date(Percentage.current_year, Percentage.thisMonth, Percentage.today)
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

        print("Satelite : Moon")
        print(("Day of the moon rotation : ") + str("Day ") + str(new))
        print(("Moon rotation progress : ") + str(Percentage.MoonResult) + str("%"))

        # Progress bar creation
        bar = Bar("Percent of this moon rotation : ", max=100)
        for i in range(int(Percentage.MoonResult)):
            bar.next()
        bar.finish()
        print("\n")

    """
  
    i = est plus grand  ou égal qu'aujourd'hui mains 30 jours et n'est pas plus grand qu'aujourd'hui.


    Do the same for the moon and other solar system planets, natural satelites, ISS, of all the solar systme. 
    """


motd()
Earth()
Moon()
