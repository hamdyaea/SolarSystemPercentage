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
        self.earthHTML
        self.BarrEarth
        self.BarrEarthHTML
        self.moon
        self.barrMoon
        self.moonHTML
        self.barrMoonHTML
        self.mercury
        self.barrMercury
        self.mercuryHTML
        self.barrMercuryHTML
        self.motdResult
        self.motdResultHTML
        self.Venus
        self.barrVenus
        self.VenusHTML
        self.barrVenusHTML
        self.VenusResult
        self.VenusPerihelion
        self.NewVenusPerihelion
        self.MarsResult
        self.MarsPerihelion
        self.NewMarsPerihelion


Percentage.current_year = date.today().year
Percentage.today = int(datetime.today().strftime("%d"))
Percentage.thisMonth = int(datetime.today().strftime("%m"))


def motd():
    Percentage.motdResult = (
        ("\n")
        + str("\n")
        + str(" __     __               _   __")
        + str("\n")
        + str(" \ \   / /              (_) / /")
        + str("\n")
        + str("  \ \_/ /__  __ _ _ __     / / ")
        + str("\n")
        + str("   \   / _ \/ _` | '__|   / /  ")
        + str("\n")
        + str("    | |  __/ (_| | |     / / _ ")
        + str("\n")
        + str("    |_|\___|\__,_|_|    /_/ (_)")
        + str("\n\n")
    )
    Percentage.motdResultHTML = (
        ("<br />")
        + str(" __     __               _   __")
        + ("<br />")
        + str(" \ \   / /              (_) / /")
        + ("<br />")
        + str("  \ \_/ /__  __ _ _ __     / / ")
        + ("<br />")
        + str("   \   / _ \/ _` | '__|   / /  ")
        + ("<br />")
        + str("    | |  __/ (_| | |     / / _ ")
        + ("<br />")
        + str("    |_|\___|\__,_|_|    /_/ (_)")
        + ("<br />")
        + ("<br />")
    )
    print(Percentage.motdResult)


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
    Percentage.earth = (
        ("Planet : Earth")
        + str("\n")
        + str(("Day of the year : ") + str("Day ") + str(new))
        + str("\n")
        + str(("Year progress : ") + str(Percentage.EarthResult) + str("%"))
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
    # Progress bar creation
    percent = Percentage.EarthResult
    barre = (
        "["
        + "#" * int((50 / 100) * percent)
        + "_" * int((50 / 100) * (100 - percent))
        + "]"
    )
    Percentage.BarrEarth = "Percent of this year : " + (barre) + str("\n")
    print(Percentage.BarrEarth)
    Percentage.BarrEarthHTML = "Percent of this year : " + (barre) + ("<br />")


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

    with open("/var/www/html/Orbit.json", "r") as O:
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

                    Percentage.moon = (
                        ("Satelite : Moon")
                        + str("\n")
                        + str(("Day of the year : ") + str("Day ") + str(new))
                        + str("\n")
                        + str(
                            ("Year progress : ") + str(Percentage.MoonResult) + str("%")
                        )
                    )
                    print(Percentage.moon)
                    Percentage.moonHTML = (
                        ("Satelite : Moon")
                        + ("<br />")
                        + str(("Day of the year : ") + str("Day ") + str(new))
                        + ("<br />")
                        + str(
                            ("Year progress : ")
                            + str(Percentage.MoonResult)
                            + str("%")
                            + ("<br />")
                        )
                    )
                    percent = Percentage.MoonResult
                    barre = (
                        "["
                        + "#" * int((50 / 100) * percent)
                        + "_" * int((50 / 100) * (100 - percent))
                        + "]"
                    )
                    Percentage.barrMoon = (
                        "Percent of this year : " + (barre) + str("\n")
                    )
                    print(Percentage.barrMoon)
                    Percentage.barrMoonHTML = (
                        "Percent of this year : " + (barre) + ("<br />")
                    )
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

                    Percentage.moon = (
                        ("Satelite : Moon")
                        + str("\n")
                        + str(("Day of the year : ") + str("Day ") + str(new))
                        + str("\n")
                        + str(
                            ("Year progress : ") + str(Percentage.MoonResult) + str("%")
                        )
                    )
                    print(Percentage.moon)
                    Percentage.moonHTML = (
                        ("Satelite : Moon")
                        + ("<br />")
                        + str(("Day of the year : ") + str("Day ") + str(new))
                        + ("<br />")
                        + str(
                            ("Year progress : ")
                            + str(Percentage.MoonResult)
                            + str("%")
                            + ("<br />")
                        )
                    )
                    percent = Percentage.MoonResult
                    barre = (
                        "["
                        + "#" * int((50 / 100) * percent)
                        + "_" * int((50 / 100) * (100 - percent))
                        + "]"
                    )
                    Percentage.barrMoon = (
                        "Percent of this year : " + (barre) + str("\n")
                    )
                    print(Percentage.barrMoon)
                    Percentage.barrMoonHTML = (
                        "Percent of this year : " + (barre) + ("<br />")
                    )
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
                    d0 >= d1 - timedelta(days=30) and d0 <= d1
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

                        Percentage.moon = (
                            ("Satelite : Moon")
                            + str("\n")
                            + str(("Day of the year : ") + str("Day ") + str(new))
                            + str("\n")
                            + str(
                                ("Year progress : ")
                                + str(Percentage.MoonResult)
                                + str("%")
                            )
                        )
                        print(Percentage.moon)
                        Percentage.moonHTML = (
                            ("Satelite : Moon")
                            + ("<br />")
                            + str(("Day of the year : ") + str("Day ") + str(new))
                            + ("<br />")
                            + str(
                                ("Year progress : ")
                                + str(Percentage.MoonResult)
                                + str("%")
                                + ("<br />")
                            )
                        )

                        percent = Percentage.MoonResult
                        barre = (
                            "["
                            + "#" * int((50 / 100) * percent)
                            + "_" * int((50 / 100) * (100 - percent))
                            + "]"
                        )
                        Percentage.barrMoon = (
                            "Percent of this year : " + (barre) + str("\n")
                        )
                        print(Percentage.barrMoon)
                        Percentage.barrMoonHTML = (
                            "Percent of this year : " + (barre) + ("<br />")
                        )


def Mercury():  # d0 = first perihelaperihelion

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

    with open("/var/www/html/Orbit.json", "r") as O:
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

                Percentage.mercury = (
                    ("Planet : Mercury")
                    + str("\n")
                    + str(("Day of the year : ") + str("Day ") + str(new))
                    + str("\n")
                    + str("\n")
                    + str(
                        ("Year progress : ") + str(Percentage.MercuryResult) + str("%")
                    )
                )
                print(Percentage.mercury)
                Percentage.mercuryHTML = (
                    ("Planet : Mercury")
                    + ("<br />")
                    + str(("Day of the year : ") + str("Day ") + str(new))
                    + ("<br />")
                    + str(
                        ("Year progress : ") + str(Percentage.MercuryResult) + str("%")
                    )
                )
                percent = Percentage.MercuryResult
                barre = (
                    "["
                    + "#" * int((50 / 100) * percent)
                    + "_" * int((50 / 100) * (100 - percent))
                    + "]"
                )
                Percentage.barrMercury = "Percent of this year : " + (barre) + str("\n")
                print(Percentage.barrMercury)
                Percentage.barrMercuryHTML = (
                    "Percent of this year : " + (barre) + ("<br />") + ("<br />")
                )
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

                Percentage.mercury = (
                    ("Planet : Mercury")
                    + str("\n")
                    + str(("Day of the year : ") + str("Day ") + str(new))
                    + str("\n")
                    + str(
                        ("Year progress : ") + str(Percentage.MercuryResult) + str("%")
                    )
                )
                print(Percentage.mercury)
                Percentage.mercuryHTML = (
                    ("Planet : Mercury")
                    + ("<br />")
                    + str(("Day of the year : ") + str("Day ") + str(new))
                    + ("<br />")
                    + str(
                        ("Year progress : ")
                        + str(Percentage.MercuryResult)
                        + str("%")
                        + ("<br />")
                    )
                )

                percent = Percentage.MercuryResult
                barre = (
                    "["
                    + "#" * int((50 / 100) * percent)
                    + "_" * int((50 / 100) * (100 - percent))
                    + "]"
                )
                Percentage.barrMercury = "Percent of this year : " + (barre) + str("\n")
                print(Percentage.barrMercury)
                Percentage.barrMercuryHTML = (
                    "Percent of this year : " + (barre) + ("<br />")
                )

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
                    d0 >= d1 - timedelta(days=90) and d0 <= d1
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

                    Percentage.mercury = (
                        ("Planet : Mercury")
                        + str("\n")
                        + str(("Day of the year : ") + str("Day ") + str(new))
                        + str("\n")
                        + str(
                            ("Year progress : ")
                            + str(Percentage.MercuryResult)
                            + str("%")
                        )
                    )
                    print(Percentage.mercury)
                    Percentage.mercuryHTML = (
                        ("Planet : Mercury")
                        + ("<br />")
                        + str(("Day of the year : ") + str("Day ") + str(new))
                        + ("<br />")
                        + str(
                            ("Year progress : ")
                            + str(Percentage.MercuryResult)
                            + str("%")
                            + ("<br />")
                        )
                    )
                    percent = Percentage.MercuryResult
                    barre = (
                        "["
                        + "#" * int((50 / 100) * percent)
                        + "_" * int((50 / 100) * (100 - percent))
                        + "]"
                    )
                    Percentage.barrMercury = (
                        "Percent of this year : " + (barre) + str("\n")
                    )
                    print(Percentage.barrMercury)
                    Percentage.barrMercuryHTML = (
                        "Percent of this year : " + (barre) + ("<br />")
                    )

def Venus():  # d0 = first perihelion , d1 = today , d2 = next perihelion

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

    with open("/var/www/html/Orbit.json", "r") as O:
        orbit = json.load(O)
        thisYear = orbit["Venus"][str(Percentage.current_year)]  # This year
        years_ago = orbit["Venus"][str(years_ago)][-1]
        years_after = orbit["Venus"][str(years_after)][0]
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
                        d0 >= d1 - timedelta(days=250) and d0 <= d1
                ):  # i is bigger or equal today - 30 days and smaller or equal today : First day of rotation
                    Percentage.VenusPerihelion = d0

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
                        d0 <= d1 + timedelta(days=250) and d0 >= d1
                ):  # i is smaller or equal today + 30 days and bigger or equalt today : Next Perihelion
                    Percentage.NewVenusPerihelion = d0
                d1 = date(
                    Percentage.current_year, Percentage.thisMonth, Percentage.today
                )
                d3 = Percentage.NewVenusPerihelion - Percentage.VenusPerihelion
                d3 = str(d3)
                d3 = d3[:3]
                d3 = int(d3)
                d3 = d3 + 1
                ValuePercent = d3 / 100
                delta = d1 - Percentage.VenusPerihelion
                new = re.sub("[^0-9]", "", str(delta))
                new = str(new)
                new = new[:3]
                new = int(new)

                Percentage.VenusResult = new / ValuePercent
                Percentage.VenusResult = round(Percentage.VenusResult, 2)

                # Add graph progress #####

                print("Planet : Venus")
                print(("Day of the year : ") + str("Day ") + str(new))
                print(("Year progress : ") + str(Percentage.VenusResult) + str("%"))

                percent = Percentage.VenusResult
                barre = (
                        "["
                        + "#" * int((50 / 100) * percent)
                        + "-" * int((50 / 100) * (100 - percent))
                        + "]"
                )
                print("Percent of this year : " + (barre))
                print("\n")
                Percentage.VenusHTML = (
                        ("Planet : Venus")
                        + ("<br />")
                        + str(("Day of the year : ") + str("Day ") + str(new))
                        + ("<br />")
                        + str(
                    ("Year progress : ")
                    + str(Percentage.VenusResult)
                    + str("%")
                    + ("<br />")
                )
                )
                percent = Percentage.VenusResult
                barre = (
                        "["
                        + "#" * int((50 / 100) * percent)
                        + "_" * int((50 / 100) * (100 - percent))
                        + "]"
                )
                Percentage.barrVenus = (
                        "Percent of this year : " + (barre) + str("\n")
                )
                Percentage.barrVenusHTML = (
                        "Percent of this year : " + (barre) + ("<br />")
                )
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
                            d0 >= d1 - timedelta(days=250) and d0 <= d1
                    ):  # i is bigger or equal today - 30 days and smaller or equal today : First day of rotation
                        Percentage.VenusPerihelion = d0

                        d0Year = years_after[:4]
                        d0Year = int(d0Year)
                        d0Month = years_after[5:7]
                        d0Month = int(d0Month)
                        d0Day = years_after[8:10]
                        d0Day = int(d0Day)

                        d0 = date(d0Year, d0Month, d0Day)

                        d1 = date(
                            Percentage.current_year,
                            Percentage.thisMonth,
                            Percentage.today,
                        )
                    if (
                            d0 <= d1 + timedelta(days=250) and d0 >= d1
                    ):  # i is smaller or equal today + 30 days and bigger or equalt today : Next Perihelion
                        Percentage.NewVenusPerihelion = d0
                        d1 = date(
                            Percentage.current_year,
                            Percentage.thisMonth,
                            Percentage.today,
                        )
                        d1 = d1 + timedelta(days=1)
                        d3 = Percentage.NewVenusPerihelion - Percentage.VenusPerihelion
                        d3 = str(d3)
                        d3 = d3[:3]
                        d3 = int(d3)
                        d3 = d3 + 1
                        ValuePercent = d3 / 100
                        delta = d1 - Percentage.VenusPerihelion
                        new = re.sub("[^0-9]", "", str(delta))
                        new = str(new)
                        new = new[:3]
                        new = int(new)

                        Percentage.VenusResult = new / ValuePercent
                        Percentage.VenusResult = round(Percentage.VenusResult, 2)

                        # Add graph progress #####

                        print("Planet : Venus")
                        print(("Day of the year : ") + str("Day ") + str(new))
                        print(
                            ("Year progress : ")
                            + str(Percentage.VenusResult)
                            + str("%")
                        )

                        percent = Percentage.VenusResult

                        barre = (
                                "["
                                + "#" * int((50 / 100) * percent)
                                + "_" * int((50 / 100) * (100 - percent))
                                + "]"
                        )
                        print("Percent of this year : " + (barre))
                        print("\n")
                        Percentage.VenusHTML = (
                                ("Planet : Venus")
                                + ("<br />")
                                + str(("Day of the year : ") + str("Day ") + str(new))
                                + ("<br />")
                                + str(
                            ("Year progress : ")
                            + str(Percentage.VenusResult)
                            + str("%")
                            + ("<br />")
                        )
                        )
                        percent = Percentage.VenusResult
                        barre = (
                                "["
                                + "#" * int((50 / 100) * percent)
                                + "_" * int((50 / 100) * (100 - percent))
                                + "]"
                        )
                        Percentage.barrVenus = (
                                "Percent of this year : " + (barre) + str("\n")
                        )
                        Percentage.barrVenusHTML = (
                                "Percent of this year : " + (barre) + ("<br />")
                        )
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
                        d0 >= d1 - timedelta(days=700) and d0 <= d1
                ):  # i is smaller or equal today + 30 days and bigger or equalt today : Next Perihelion
                    Percentage.NewVenusPerihelion = d0

                    for i in thisYear:
                        d0Year = i[:4]
                        d0Year = int(d0Year)
                        d0Month = i[5:7]
                        d0Month = int(d0Month)
                        d0Day = i[8:10]
                        d0Day = int(d0Day)
                        d0 = date(d0Year, d0Month, d0Day)
                        d1 = date(
                            Percentage.current_year,
                            Percentage.thisMonth,
                            Percentage.today,
                        )
                        if (
                                d0 <= d1 + timedelta(days=250) and d0 >= d1
                        ):  # i is smaller or equal today + 30 days and bigger or equalt today : Next Perihelion
                            Percentage.NewVenusPerihelion = d0
                            d1 = date(
                                Percentage.current_year,
                                Percentage.thisMonth,
                                Percentage.today,
                            )
                            d3 = (
                                    Percentage.NewVenusPerihelion
                                    - Percentage.VenusPerihelion
                            )
                            d3 = str(d3)
                            d3 = d3[:3]
                            d3 = int(d3)
                            d3 = d3 + 1
                            ValuePercent = d3 / 100
                            delta = d1 - Percentage.VenusPerihelion
                            new = re.sub("[^0-9]", "", str(delta))
                            new = str(new)
                            new = new[:3]
                            new = int(new)

                            Percentage.VenusResult = new / ValuePercent
                            Percentage.VenusResult = round(Percentage.VenusResult, 2)

                            # Add graph progress #####

                            print("Planet : Venus")
                            print(("Day of the year : ") + str("Day ") + str(new))
                            print(
                                ("Year progress : ")
                                + str(Percentage.VenusResult)
                                + str("%")
                            )

                            percent = Percentage.VenusResult
                            barre = (
                                    "["
                                    + "#" * int((50 / 100) * percent)
                                    + "_" * int((50 / 100) * (100 - percent))
                                    + "]"
                            )
                            print("Percent of this year : " + (barre))
                            print("\n")
                            Percentage.VenusHTML = (
                                    ("Planet : Venus")
                                    + ("<br />")
                                    + str(("Day of the year : ") + str("Day ") + str(new))
                                    + ("<br />")
                                    + str(
                                ("Year progress : ")
                                + str(Percentage.VenusResult)
                                + str("%")
                                + ("<br />")
                            )
                            )
                            percent = Percentage.VenusResult
                            barre = (
                                    "["
                                    + "#" * int((50 / 100) * percent)
                                    + "_" * int((50 / 100) * (100 - percent))
                                    + "]"
                            )
                            Percentage.barrVenus = (
                                    "Percent of this year : " + (barre) + str("\n")
                            )
                            Percentage.barrVenusHTML = (
                                    "Percent of this year : " + (barre) + ("<br />")
                            )

def Mars():  # d0 = first perihelion , d1 = today , d2 = next perihelion

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

    with open("/var/www/html/Orbit.json", "r") as O:
        orbit = json.load(O)
        try:
            thisYear = orbit["Mars"][str(Percentage.current_year)]  # This year
        except:
            thisYear = orbit["Mars"][str(Percentage.current_year-1)]
        years_ago = orbit["Mars"][str(years_ago)][-1]
        years_after = orbit["Mars"][str(years_after)][0]
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
                        d0 >= d1 - timedelta(days=700) and d0 <= d1
                ):  # i is bigger or equal today - 30 days and smaller or equal today : First day of rotation
                    Percentage.MarsPerihelion = d0

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
                        d0 <= d1 + timedelta(days=700) and d0 >= d1
                ):  # i is smaller or equal today + 30 days and bigger or equalt today : Next Perihelion
                    Percentage.NewMarsPerihelion = d0
                d1 = date(
                    Percentage.current_year, Percentage.thisMonth, Percentage.today
                )
                d3 = Percentage.NewMarsPerihelion - Percentage.MarsPerihelion
                d3 = str(d3)
                d3 = d3[:3]
                d3 = int(d3)
                d3 = d3 + 1
                ValuePercent = d3 / 100
                delta = d1 - Percentage.MarsPerihelion
                new = re.sub("[^0-9]", "", str(delta))
                new = str(new)
                new = new[:3]
                new = int(new)

                Percentage.MarsResult = new / ValuePercent
                Percentage.MarsResult = round(Percentage.MarsResult, 2)

                # Add graph progress #####

                print("Planet : Mars")
                print(("Day of the year : ") + str("Day ") + str(new))
                print(("Year progress : ") + str(Percentage.MarsResult) + str("%"))

                percent = Percentage.MarsResult
                barre = (
                        "["
                        + "#" * int((50 / 100) * percent)
                        + "-" * int((50 / 100) * (100 - percent))
                        + "]"
                )
                print("Percent of this year : " + (barre))
                print("\n")
                Percentage.MarsHTML = (
                        ("Planet : Mars")
                        + ("<br />")
                        + str(("Day of the year : ") + str("Day ") + str(new))
                        + ("<br />")
                        + str(
                    ("Year progress : ")
                    + str(Percentage.MarsResult)
                    + str("%")
                    + ("<br />")
                )
                )
                percent = Percentage.MarsResult
                barre = (
                        "["
                        + "#" * int((50 / 100) * percent)
                        + "_" * int((50 / 100) * (100 - percent))
                        + "]"
                )
                Percentage.barrMars = (
                        "Percent of this year : " + (barre) + str("\n")
                )
                Percentage.barrMarsHTML = (
                        "Percent of this year : " + (barre) + ("<br />")
                )
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
                            d0 >= d1 - timedelta(days=700) and d0 <= d1
                    ):  # i is bigger or equal today - 30 days and smaller or equal today : First day of rotation
                        Percentage.MarsPerihelion = d0
                        d0Year = years_after[:4]
                        d0Year = int(d0Year)
                        d0Month = years_after[5:7]
                        d0Month = int(d0Month)
                        d0Day = years_after[8:10]
                        d0Day = int(d0Day)

                        d0 = date(d0Year, d0Month, d0Day)

                        d1 = date(
                            Percentage.current_year,
                            Percentage.thisMonth,
                            Percentage.today,
                        )
                    if (
                            d0 <= d1 + timedelta(days=700) and d0 >= d1
                    ):  # i is smaller or equal today + 30 days and bigger or equalt today : Next Perihelion
                        Percentage.NewMarsPerihelion = d0
                        d1 = date(
                            Percentage.current_year,
                            Percentage.thisMonth,
                            Percentage.today,
                        )
                        d1 = d1 + timedelta(days=1)
                        d3 = Percentage.NewMarsPerihelion - Percentage.MarsPerihelion
                        d3 = str(d3)
                        d3 = d3[:3]
                        d3 = int(d3)
                        d3 = d3 + 1
                        ValuePercent = d3 / 100
                        delta = d1 - Percentage.MarsPerihelion
                        new = re.sub("[^0-9]", "", str(delta))
                        new = str(new)
                        new = new[:3]
                        new = int(new)

                        Percentage.MarsResult = new / ValuePercent
                        Percentage.MarsResult = round(Percentage.MarsResult, 2)

                        # Add graph progress #####

                        print("Planet : Mars")
                        print(("Day of the year : ") + str("Day ") + str(new))
                        print(
                            ("Year progress : ")
                            + str(Percentage.MarsResult)
                            + str("%")
                        )

                        percent = Percentage.MarsResult

                        barre = (
                                "["
                                + "#" * int((50 / 100) * percent)
                                + "_" * int((50 / 100) * (100 - percent))
                                + "]"
                        )
                        print("Percent of this year : " + (barre))
                        print("\n")
                        Percentage.MarsHTML = (
                                ("Planet : Mars")
                                + ("<br />")
                                + str(("Day of the year : ") + str("Day ") + str(new))
                                + ("<br />")
                                + str(
                            ("Year progress : ")
                            + str(Percentage.MarsResult)
                            + str("%")
                            + ("<br />")
                        )
                        )
                        percent = Percentage.MarsResult
                        barre = (
                                "["
                                + "#" * int((50 / 100) * percent)
                                + "_" * int((50 / 100) * (100 - percent))
                                + "]"
                        )
                        Percentage.barrMars = (
                                "Percent of this year : " + (barre) + str("\n")
                        )
                        Percentage.barrMarsHTML = (
                                "Percent of this year : " + (barre) + ("<br />")
                        )
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
                        d0 >= d1 - timedelta(days=700) and d0 <= d1
                ):  # i is smaller or equal today + 30 days and bigger or equalt today : Next Perihelion
                    Percentage.NewMarsPerihelion = d0

                    for i in thisYear:
                        d0Year = i[:4]
                        d0Year = int(d0Year)
                        d0Month = i[5:7]
                        d0Month = int(d0Month)
                        d0Day = i[8:10]
                        d0Day = int(d0Day)
                        d0 = date(d0Year, d0Month, d0Day)
                        d1 = date(
                            Percentage.current_year,
                            Percentage.thisMonth,
                            Percentage.today,
                        )
                        if (
                                d0 <= d1 + timedelta(days=700) and d0 >= d1
                        ):  # i is smaller or equal today + 30 days and bigger or equalt today : Next Perihelion
                            Percentage.NewMarsPerihelion = d0
                            d1 = date(
                                Percentage.current_year,
                                Percentage.thisMonth,
                                Percentage.today,
                            )
                            d3 = (
                                    Percentage.NewMarsPerihelion
                                    - Percentage.MarsPerihelion
                            )
                            d3 = str(d3)
                            d3 = d3[:3]
                            d3 = int(d3)
                            d3 = d3 + 1
                            ValuePercent = d3 / 100
                            delta = d1 - Percentage.MarsPerihelion
                            new = re.sub("[^0-9]", "", str(delta))
                            new = str(new)
                            new = new[:3]
                            new = int(new)

                            Percentage.MarsResult = new / ValuePercent
                            Percentage.MarsResult = round(Percentage.MarsResult, 2)

                            # Add graph progress #####

                            print("Planet : Mars")
                            print(("Day of the year : ") + str("Day ") + str(new))
                            print(
                                ("Year progress : ")
                                + str(Percentage.MarsResult)
                                + str("%")
                            )

                            percent = Percentage.MarsResult
                            barre = (
                                    "["
                                    + "#" * int((50 / 100) * percent)
                                    + "_" * int((50 / 100) * (100 - percent))
                                    + "]"
                            )
                            print("Percent of this year : " + (barre))
                            print("\n")
                            Percentage.MarsHTML = (
                                    ("Planet : Mars")
                                    + ("<br />")
                                    + str(("Day of the year : ") + str("Day ") + str(new))
                                    + ("<br />")
                                    + str(
                                ("Year progress : ")
                                + str(Percentage.MarsResult)
                                + str("%")
                                + ("<br />")
                            )
                            )
                            percent = Percentage.MarsResult
                            barre = (
                                    "["
                                    + "#" * int((50 / 100) * percent)
                                    + "_" * int((50 / 100) * (100 - percent))
                                    + "]"
                            )
                            Percentage.barrMars = (
                                    "Percent of this year : " + (barre) + str("\n")
                            )
                            Percentage.barrMarsHTML = (
                                    "Percent of this year : " + (barre) + ("<br />")
                            )







    """

    Do the same for the moon and other solar system planets, natural satelites, ISS, of all the solar system. 
    """


motd()
Earth()
Moon()
Mercury()
Venus()
Mars()

startHtml = (
    str("<!DOCTYPE html>")
    + str("\n")
    + str("<html>")
    + str("\n")
    + str("<head>")
    + str("\n")
    + str("<title>Percent Progress of the Solar System</title>")
    + str("\n")
    + str("<style>")
    + str("\n")
    + str("body {")
    + str("\n")
    + str("background-image: url('nightsky.jpg');")
    +str("\n")
    +str("<basefont face = 'Monospace'>")
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
    + str("<font face = 'Monospace' size ='6' color='white'>")+str("\n")
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
endHTML = str("</p>") + str("\n") + str("</font>") + str("\n") + str("</body>")

indexFile = open("/var/www/html/index.html", "w")
indexFile.write(startHtml)
indexFile.close()

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

contentHtml = open("/var/www/html/index.html", "a")
# contentHtml.write(Percentage.motdResultHTML)
contentHtml.write(Percentage.earthHTML)
contentHtml.write(Percentage.BarrEarthHTML)
contentHtml.write("<br />")
contentHtml.write("<br />")
contentHtml.write(Percentage.moonHTML)
contentHtml.write(Percentage.barrMoonHTML)
contentHtml.write("<br />")
contentHtml.write("<br />")
contentHtml.write(Percentage.mercuryHTML)
contentHtml.write(Percentage.barrMercuryHTML)
contentHtml.write("<br />")
contentHtml.write("<br />")
contentHtml.write(Percentage.VenusHTML)
contentHtml.write(Percentage.barrVenusHTML)
contentHtml.write("<br />")
contentHtml.write("<br />")
contentHtml.write(Percentage.MarsHTML)
contentHtml.write(Percentage.barrMarsHTML)
contentHtml.write("<br />")
contentHtml.write("<br />")
contentHtml.write("Developer : Hamdy Abou El Anein - https://github.com/hamdyaea/SolarSystemPercentage")
contentHtml.write("<br />")
contentHtml.write("<br />")
contentHtml.write("<br />")
contentHtml.write(("Last update : ") + (dt_string))
contentHtml.write(endHTML)
contentHtml.close()
