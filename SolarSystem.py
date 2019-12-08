#!/usr/bin/env python3

# Developer : Hamdy Abou El Anein
# hamdy.aea@protonmail.com

# percentage of the year for the earth, the moon, jupiter, Saturn, etc...
# Lunar Perigee and Apogee Calculator : https://www.fourmilab.ch/earthview/pacalc.html
# Mercury and others : https://in-the-sky.org/newscalyear.php

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
        self.MercuryResult
        self.MercuryPerihelion
        self.NewMercuryPerihelion


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

    # Rotation year before this year
    years_ago_full = datetime.now() - timedelta(days=1 * 365) # adapt to the number of years
    years_ago_full = str(years_ago_full)
    years_ago = years_ago_full[:4]
    years_ago = int(years_ago)  # result

    # Next rotation year
    years_after_full = datetime.now() + timedelta(days=1 * 365) # adapt to the number of years
    years_after_full = str(years_after_full)
    years_after = years_after_full[:4]
    years_after = int(years_after)  # result

    with open("Orbit.json", "r") as O:
        orbit = json.load(O)
        thisYear = orbit["Moon"][str(Percentage.current_year)]  # This year
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

            d1 = date(Percentage.current_year, Percentage.thisMonth, Percentage.today)
            d3 = Percentage.NewMoonPerihelion - Percentage.MoonPerihelion
        except:
            for i in thisYear:
                d0Year = years_ago
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
                d0Year = years_after
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

def Mercury():  # d0 = first perihelion , d1 = today , d2 = next perihelion

    # Rotation year before this year
    years_ago_full = datetime.now() - timedelta(days=1 * 365)  # adapt to the number of years
    years_ago_full = str(years_ago_full)
    years_ago = years_ago_full[:4]
    years_ago = int(years_ago)  # result

    # Next rotation year
    years_after_full = datetime.now() + timedelta(days=1 * 365)  # adapt to the number of years
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
                if (
                        d0 <= d1 + timedelta(days=90) and d0 >= d1
                ):  # i is smaller or equal today + 30 days and bigger or equalt today : Next Perihelion
                    Percentage.NewMercuryPerihelion = d0
                d1 = date(Percentage.current_year, Percentage.thisMonth, Percentage.today)
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

                print("Planet : Mercury")
                print(("Day of the year : ") + str("Day ") + str(new))
                print(("Year progress : ") + str(Percentage.MercuryResult) + str("%"))

                # Progress bar creation
                bar = Bar("Percent of this year : ", max=100)
                for i in range(int(Percentage.MercuryResult)):
                    bar.next()
                bar.finish()
                print("\n")
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
                d1 = date(Percentage.current_year, Percentage.thisMonth, Percentage.today)
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

                print("Planet : Mercury")
                print(("Day of the year : ") + str("Day ") + str(new))
                print(("Year progress : ") + str(Percentage.MercuryResult) + str("%"))

                # Progress bar creation
                bar = Bar("Percent of this year : ", max=100)
                for i in range(int(Percentage.MercuryResult)):
                    bar.next()
                bar.finish()
                print("\n")
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
                    d1 = date(Percentage.current_year, Percentage.thisMonth, Percentage.today)
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

                    print("Planet : Mercury")
                    print(("Day of the year : ") + str("Day ") + str(new))
                    print(("Year progress : ") + str(Percentage.MercuryResult) + str("%"))

                    # Progress bar creation
                    bar = Bar("Percent of this year : ", max=100)
                    for i in range(int(Percentage.MercuryResult)):
                        bar.next()
                    bar.finish()
                    print("\n")
    """

    Do the same for the moon and other solar system planets, natural satelites, ISS, of all the solar system. 
    """


motd()
Earth()
Moon()
Mercury()