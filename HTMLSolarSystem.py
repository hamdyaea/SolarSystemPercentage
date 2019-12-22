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
        self.JupiterResult
        self.JupiterPerihelion
        self.NewJupiterPerihelion
        self.SaturnResult
        self.SaturnPerihelion
        self.NewSaturnPerihelion
        self.UranusResult
        self.UranusPerihelion
        self.NewUranusPerihelion
        self.NeptuneResult
        self.NeptunePerihelion
        self.NewNeptunePerihelion
        self.PlutoResult
        self.PlutoPerihelion
        self.NewPlutoPerihelion
        self.Pluto
        self.barrPluto
        self.PlutoHTML
        self.barrPlutoHTML
        self.HalleyResult
        self.HalleyPerihelion
        self.NewHalleyPerihelion
        self.Halley
        self.barrHalley
        self.HalleyHTML
        self.barrHalleyHTML
        self.TeslaResult
        self.TeslaPerihelion
        self.NewTeslaPerihelion
        self.Tesla
        self.barrTesla
        self.TeslaHTML
        self.barrTeslaHTML
        self.CeresResult
        self.CeresPerihelion
        self.NewCeresPerihelion
        self.Ceres
        self.barrCeres
        self.CeresHTML
        self.barrCeresHTML
        self.HaumeaResult
        self.HaumeaPerihelion
        self.NewHaumeaPerihelion
        self.Haumea
        self.barrHaumea
        self.HaumeaHTML
        self.barrHaumeaHTML
        self.MakemakeResult
        self.MakemakePerihelion
        self.NewMakemakePerihelion
        self.Makemake
        self.barrMakemake
        self.MakemakeHTML
        self.barrMakemakeHTML
        self.ErisResult
        self.ErisPerihelion
        self.NewErisPerihelion
        self.Eris
        self.barrEris
        self.ErisHTML
        self.barrErisHTML


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
    d3 = d3.split()
    d3 = int(d3[0])
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
                    d0 >= d1 - timedelta(days=25) and d0 <= d1
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
                    d0 <= d1 + timedelta(days=25) and d0 >= d1
                ):  # i is smaller or equal today + 30 days and bigger or equalt today : Next Perihelion
                    Percentage.NewMoonPerihelion = d0
                    # print(Percentage.NewMoonPerihelion)
                d1 = date(
                    Percentage.current_year, Percentage.thisMonth, Percentage.today
                )
                d1 = d1 + timedelta(days=1)
                d3 = Percentage.NewMoonPerihelion - Percentage.MoonPerihelion
                d3 = str(d3)
                d3 = d3.split()
                d3 = int(d3[0])
                d3 = d3 + 1
                ValuePercent = d3 / 100
                delta = d1 - Percentage.MoonPerihelion
                delta = str(delta)
                delta = delta.split()
                delta = delta[0]
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
                    + str(("Year progress : ") + str(Percentage.MoonResult) + str("%"))
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
                Percentage.barrMoon = "Percent of this year : " + (barre) + str("\n")
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
                        d0 >= d1 - timedelta(days=25) and d0 <= d1
                    ):  # i is bigger or equal today - 30 days and smaller or equal today : First day of rotation
                        Percentage.MoonPerihelion = d0
                        # print(Percentage.MoonPerihelion)
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
                        d0 <= d1 + timedelta(days=25) and d0 >= d1
                    ):  # i is smaller or equal today + 30 days and bigger or equalt today : Next Perihelion
                        Percentage.NewMoonPerihelion = d0
                        # print(Percentage.NewMoonPerihelion)
                        d1 = date(
                            Percentage.current_year,
                            Percentage.thisMonth,
                            Percentage.today,
                        )
                        d1 = d1 + timedelta(days=1)
                        d3 = Percentage.NewMoonPerihelion - Percentage.MoonPerihelion
                        d3 = str(d3)
                        d3 = d3[:3]
                        d3 = int(d3)
                        d3 = d3 + 1
                        ValuePercent = d3 / 100
                        delta = d1 - Percentage.MoonPerihelion
                        #
                        delta = str(delta)
                        delta = delta.split()
                        delta = delta[0]
                        new = re.sub("[^0-9]", "", str(delta))
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
                    d0 >= d1 - timedelta(days=25) and d0 <= d1
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
                        d0 <= d1 + timedelta(days=25) and d0 >= d1 or d0 == d1
                    ):  # i is smaller or equal today + 30 days and bigger or equalt today : Next Perihelion
                        Percentage.NewMoonPerihelion = d0
                    d1 = date(
                        Percentage.current_year, Percentage.thisMonth, Percentage.today,
                    )
                    d3 = Percentage.NewMoonPerihelion - Percentage.MoonPerihelion
                    d3 = str(d3)
                    d3 = d3.split()
                    d3 = int(d3[0])
                    d3 = d3 + 1
                    ValuePercent = d3 / 100
                    delta = d1 - Percentage.MoonPerihelion
                    delta = str(delta)
                    delta = delta.split()
                    delta = delta[0]
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
                d3 = d3.split()
                d3 = int(d3[0])
                d3 = d3 + 1
                ValuePercent = d3 / 100
                delta = d1 - Percentage.MercuryPerihelion
                delta = str(delta)
                delta = delta.split()
                delta = delta[0]
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
                d3 = d3.split()
                d3 = int(d3[0])
                d3 = d3 + 1
                ValuePercent = d3 / 100
                delta = d1 - Percentage.MercuryPerihelion
                delta = str(delta)
                delta = delta.split()
                delta = delta[0]
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
                    d3 = d3.split()
                    d3 = int(d3[0])
                    d3 = d3 + 1
                    ValuePercent = d3 / 100
                    delta = d1 - Percentage.MercuryPerihelion
                    delta = str(delta)
                    delta = delta.split()
                    delta = delta[0]
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
                d3 = d3.split()
                d3 = int(d3[0])
                d3 = d3 + 1
                ValuePercent = d3 / 100
                delta = d1 - Percentage.VenusPerihelion
                delta = str(delta)
                delta = delta.split()
                delta = delta[0]
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
                Percentage.barrVenus = "Percent of this year : " + (barre) + str("\n")
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
                        d3 = d3.split()
                        d3 = int(d3[0])
                        d3 = d3 + 1
                        ValuePercent = d3 / 100
                        delta = d1 - Percentage.VenusPerihelion
                        delta = str(delta)
                        delta = delta.split()
                        delta = delta[0]
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
                            d3 = d3.split()
                            d3 = int(d3[0])
                            d3 = d3 + 1
                            ValuePercent = d3 / 100
                            delta = d1 - Percentage.VenusPerihelion
                            delta = str(delta)
                            delta = delta.split()
                            delta = delta[0]
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
            thisYear = orbit["Mars"][str(Percentage.current_year - 1)]
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
                d3 = d3.split()
                d3 = int(d3[0])
                d3 = d3 + 1
                ValuePercent = d3 / 100
                delta = d1 - Percentage.MarsPerihelion
                delta = str(delta)
                delta = delta.split()
                delta = delta[0]
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
                Percentage.barrMars = "Percent of this year : " + (barre) + str("\n")
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
                        d3 = d3.split()
                        d3 = int(d3[0])
                        d3 = d3 + 1
                        ValuePercent = d3 / 100
                        delta = d1 - Percentage.MarsPerihelion
                        delta = str(delta)
                        delta = delta.split()
                        delta = delta[0]
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
                            ("Year progress : ") + str(Percentage.MarsResult) + str("%")
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
                                Percentage.NewMarsPerihelion - Percentage.MarsPerihelion
                            )
                            d3 = str(d3)
                            d3 = d3.split()
                            d3 = int(d3[0])
                            d3 = d3 + 1
                            ValuePercent = d3 / 100
                            delta = d1 - Percentage.MarsPerihelion
                            delta = str(delta)
                            delta = delta.split()
                            delta = delta[0]
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


def Jupiter():  # d0 = first perihelion , d1 = today , d2 = next perihelion

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
        thisYear = orbit["Jupiter"]  # This year
        # years_ago = orbit["Jupiter"][str(years_ago)][-1]
        # years_after = orbit["Jupiter"][str(years_after)][0]
        for i in thisYear:
            d0Year = i[:4]
            d0Year = int(d0Year)
            d0Month = i[5:7]
            d0Month = int(d0Month)
            d0Day = i[8:10]
            d0Day = int(d0Day)
            d0 = date(d0Year, d0Month, d0Day)
            d1 = date(Percentage.current_year, Percentage.thisMonth, Percentage.today)
            d1 = d1 + timedelta(days=1)
            if (
                d0 >= d1 - timedelta(days=4400) and d0 <= d1
            ):  # i is bigger or equal today - 30 days and smaller or equal today : First day of rotation
                Percentage.JupiterPerihelion = d0

        for i in thisYear:
            d0Year = i[:4]
            d0Year = int(d0Year)
            d0Month = i[5:7]
            d0Month = int(d0Month)
            d0Day = i[8:10]
            d0Day = int(d0Day)
            d0 = date(d0Year, d0Month, d0Day)
            d1 = date(Percentage.current_year, Percentage.thisMonth, Percentage.today)
            d1 = d1 + timedelta(days=1)
            if (
                d0 <= d1 + timedelta(days=4400) and d0 >= d1
            ):  # i is smaller or equal today + 30 days and bigger or equalt today : Next Perihelion
                Percentage.NewJupiterPerihelion = d0
                d1 = date(
                    Percentage.current_year, Percentage.thisMonth, Percentage.today
                )
                d3 = Percentage.NewJupiterPerihelion - Percentage.JupiterPerihelion
                d3 = str(d3)
                d3 = d3.split()
                d3 = int(d3[0])
                d3 = d3 + 1
                ValuePercent = d3 / 100
                delta = d1 - Percentage.JupiterPerihelion
                delta = str(delta)
                delta = delta.split()
                delta = delta[0]
                new = re.sub("[^0-9]", "", str(delta))
                new = str(new)
                new = new[:4]
                new = int(new)
                Percentage.JupiterResult = new / ValuePercent
                Percentage.JupiterResult = round(Percentage.JupiterResult, 2)

                # Add graph progress #####

                print("Planet : Jupiter")
                print(("Day of the year : ") + str("Day ") + str(new))
                print(("Year progress : ") + str(Percentage.JupiterResult) + str("%"))

                percent = Percentage.JupiterResult
                barre = (
                    "["
                    + "#" * int((50 / 100) * percent)
                    + "-" * int((50 / 100) * (100 - percent))
                    + "]"
                )
                print("Percent of this year : " + (barre))
                print("\n")
                Percentage.JupiterHTML = (
                    ("Planet : Jupiter")
                    + ("<br />")
                    + str(("Day of the year : ") + str("Day ") + str(new))
                    + ("<br />")
                    + str(
                        ("Year progress : ")
                        + str(Percentage.JupiterResult)
                        + str("%")
                        + ("<br />")
                    )
                )
                percent = Percentage.JupiterResult
                barre = (
                    "["
                    + "#" * int((50 / 100) * percent)
                    + "_" * int((50 / 100) * (100 - percent))
                    + "]"
                )
                Percentage.barrJupiter = "Percent of this year : " + (barre) + str("\n")
                Percentage.barrJupiterHTML = (
                    "Percent of this year : " + (barre) + ("<br />")
                )


def Saturn():  # d0 = first perihelion , d1 = today , d2 = next perihelion

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
        thisYear = orbit["Saturn"]  # This year
        # years_ago = orbit["Saturn"][str(years_ago)][-1]
        # years_after = orbit["Saturn"][str(years_after)][0]
        for i in thisYear:
            d0Year = i[:4]
            d0Year = int(d0Year)
            d0Month = i[5:7]
            d0Month = int(d0Month)
            d0Day = i[8:10]
            d0Day = int(d0Day)
            d0 = date(d0Year, d0Month, d0Day)
            d1 = date(Percentage.current_year, Percentage.thisMonth, Percentage.today)
            d1 = d1 + timedelta(days=1)
            if (
                d0 >= d1 - timedelta(days=11000) and d0 <= d1
            ):  # i is bigger or equal today - 30 days and smaller or equal today : First day of rotation
                Percentage.SaturnPerihelion = d0

        for i in thisYear:
            d0Year = i[:4]
            d0Year = int(d0Year)
            d0Month = i[5:7]
            d0Month = int(d0Month)
            d0Day = i[8:10]
            d0Day = int(d0Day)
            d0 = date(d0Year, d0Month, d0Day)
            d1 = date(Percentage.current_year, Percentage.thisMonth, Percentage.today)
            d1 = d1 + timedelta(days=1)
            if (
                d0 <= d1 + timedelta(days=11000) and d0 >= d1
            ):  # i is smaller or equal today + 30 days and bigger or equalt today : Next Perihelion
                Percentage.NewSaturnPerihelion = d0
                d1 = date(
                    Percentage.current_year, Percentage.thisMonth, Percentage.today
                )
                d3 = Percentage.NewSaturnPerihelion - Percentage.SaturnPerihelion
                d3 = str(d3)
                d3 = d3.split()
                d3 = int(d3[0])
                d3 = d3 + 1
                ValuePercent = d3 / 100
                delta = d1 - Percentage.SaturnPerihelion
                delta = str(delta)
                delta = delta.split()
                delta = delta[0]
                new = re.sub("[^0-9]", "", str(delta))
                new = str(new)
                new = new[:4]
                new = int(new)
                Percentage.SaturnResult = new / ValuePercent
                Percentage.SaturnResult = round(Percentage.SaturnResult, 2)

                # Add graph progress #####

                print("Planet : Saturn")
                print(("Day of the year : ") + str("Day ") + str(new))
                print(("Year progress : ") + str(Percentage.SaturnResult) + str("%"))

                percent = Percentage.SaturnResult
                barre = (
                    "["
                    + "#" * int((50 / 100) * percent)
                    + "-" * int((50 / 100) * (100 - percent))
                    + "]"
                )
                print("Percent of this year : " + (barre))
                print("\n")
                Percentage.SaturnHTML = (
                    ("Planet : Saturn")
                    + ("<br />")
                    + str(("Day of the year : ") + str("Day ") + str(new))
                    + ("<br />")
                    + str(
                        ("Year progress : ")
                        + str(Percentage.SaturnResult)
                        + str("%")
                        + ("<br />")
                    )
                )
                percent = Percentage.SaturnResult
                barre = (
                    "["
                    + "#" * int((50 / 100) * percent)
                    + "_" * int((50 / 100) * (100 - percent))
                    + "]"
                )
                Percentage.barrSaturn = "Percent of this year : " + (barre) + str("\n")
                Percentage.barrSaturnHTML = (
                    "Percent of this year : " + (barre) + ("<br />")
                )


def Uranus():  # d0 = first perihelion , d1 = today , d2 = next perihelion

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
        thisYear = orbit["Uranus"]  # This year
        # years_ago = orbit["Uranus"][str(years_ago)][-1]
        # years_after = orbit["Uranus"][str(years_after)][0]
        for i in thisYear:
            d0Year = i[:4]
            d0Year = int(d0Year)
            d0Month = i[5:7]
            d0Month = int(d0Month)
            d0Day = i[8:10]
            d0Day = int(d0Day)
            d0 = date(d0Year, d0Month, d0Day)
            d1 = date(Percentage.current_year, Percentage.thisMonth, Percentage.today)
            d1 = d1 + timedelta(days=1)
            if (
                d0 >= d1 - timedelta(days=32850) and d0 <= d1
            ):  # i is bigger or equal today - 30 days and smaller or equal today : First day of rotation
                Percentage.UranusPerihelion = d0

        for i in thisYear:
            d0Year = i[:4]
            d0Year = int(d0Year)
            d0Month = i[5:7]
            d0Month = int(d0Month)
            d0Day = i[8:10]
            d0Day = int(d0Day)
            d0 = date(d0Year, d0Month, d0Day)
            d1 = date(Percentage.current_year, Percentage.thisMonth, Percentage.today)
            d1 = d1 + timedelta(days=1)
            if (
                d0 <= d1 + timedelta(days=32850) and d0 >= d1
            ):  # i is smaller or equal today + 30 days and bigger or equalt today : Next Perihelion
                Percentage.NewUranusPerihelion = d0
                d1 = date(
                    Percentage.current_year, Percentage.thisMonth, Percentage.today
                )
                d3 = Percentage.NewUranusPerihelion - Percentage.UranusPerihelion
                d3 = str(d3)
                d3 = d3.split()
                d3 = int(d3[0])
                d3 = d3 + 1
                ValuePercent = d3 / 100
                delta = d1 - Percentage.UranusPerihelion
                delta = str(delta)
                delta = delta.split()
                delta = delta[0]
                new = re.sub("[^0-9]", "", str(delta))
                new = str(new)
                new = new[:4]
                new = int(new)
                Percentage.UranusResult = new / ValuePercent
                Percentage.UranusResult = round(Percentage.UranusResult, 2)

                # Add graph progress #####

                print("Planet : Uranus")
                print(("Day of the year : ") + str("Day ") + str(new))
                print(("Year progress : ") + str(Percentage.UranusResult) + str("%"))

                percent = Percentage.UranusResult
                barre = (
                    "["
                    + "#" * int((50 / 100) * percent)
                    + "-" * int((50 / 100) * (100 - percent))
                    + "]"
                )
                print("Percent of this year : " + (barre))
                print("\n")
                Percentage.UranusHTML = (
                    ("Planet : Uranus")
                    + ("<br />")
                    + str(("Day of the year : ") + str("Day ") + str(new))
                    + ("<br />")
                    + str(
                        ("Year progress : ")
                        + str(Percentage.UranusResult)
                        + str("%")
                        + ("<br />")
                    )
                )
                percent = Percentage.UranusResult
                barre = (
                    "["
                    + "#" * int((50 / 100) * percent)
                    + "_" * int((50 / 100) * (100 - percent))
                    + "]"
                )
                Percentage.barrUranus = "Percent of this year : " + (barre) + str("\n")
                Percentage.barrUranusHTML = (
                    "Percent of this year : " + (barre) + ("<br />")
                )


def Neptune():  # d0 = first perihelion , d1 = today , d2 = next perihelion

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
        thisYear = orbit["Neptune"]  # This year
        # years_ago = orbit["Neptune"][str(years_ago)][-1]
        # years_after = orbit["Neptune"][str(years_after)][0]
        for i in thisYear:
            d0Year = i[:4]
            d0Year = int(d0Year)
            d0Month = i[5:7]
            d0Month = int(d0Month)
            d0Day = i[8:10]
            d0Day = int(d0Day)
            d0 = date(d0Year, d0Month, d0Day)
            d1 = date(Percentage.current_year, Percentage.thisMonth, Percentage.today)
            d1 = d1 + timedelta(days=1)
            if (
                d0 >= d1 - timedelta(days=62000) and d0 <= d1
            ):  # i is bigger or equal today - 30 days and smaller or equal today : First day of rotation
                Percentage.NeptunePerihelion = d0

        for i in thisYear:
            d0Year = i[:4]
            d0Year = int(d0Year)
            d0Month = i[5:7]
            d0Month = int(d0Month)
            d0Day = i[8:10]
            d0Day = int(d0Day)
            d0 = date(d0Year, d0Month, d0Day)
            d1 = date(Percentage.current_year, Percentage.thisMonth, Percentage.today)
            d1 = d1 + timedelta(days=1)
            if (
                d0 <= d1 + timedelta(days=62000) and d0 >= d1
            ):  # i is smaller or equal today + 30 days and bigger or equalt today : Next Perihelion
                Percentage.NewNeptunePerihelion = d0
                d1 = date(
                    Percentage.current_year, Percentage.thisMonth, Percentage.today
                )
                d3 = Percentage.NewNeptunePerihelion - Percentage.NeptunePerihelion
                d3 = str(d3)
                d3 = d3.split()
                d3 = int(d3[0])
                d3 = d3 + 1
                ValuePercent = d3 / 100
                delta = d1 - Percentage.NeptunePerihelion
                delta = str(delta)
                delta = delta.split()
                delta = delta[0]
                new = re.sub("[^0-9]", "", str(delta))
                new = str(new)
                new = new[:4]
                new = int(new)
                Percentage.NeptuneResult = new / ValuePercent
                Percentage.NeptuneResult = round(Percentage.NeptuneResult, 2)

                # Add graph progress #####

                print("Planet : Neptune")
                print(("Day of the year : ") + str("Day ") + str(new))
                print(("Year progress : ") + str(Percentage.NeptuneResult) + str("%"))

                percent = Percentage.NeptuneResult
                barre = (
                    "["
                    + "#" * int((50 / 100) * percent)
                    + "-" * int((50 / 100) * (100 - percent))
                    + "]"
                )
                print("Percent of this year : " + (barre))
                print("\n")
                Percentage.NeptuneHTML = (
                    ("Planet : Neptune")
                    + ("<br />")
                    + str(("Day of the year : ") + str("Day ") + str(new))
                    + ("<br />")
                    + str(
                        ("Year progress : ")
                        + str(Percentage.NeptuneResult)
                        + str("%")
                        + ("<br />")
                    )
                )
                percent = Percentage.NeptuneResult
                barre = (
                    "["
                    + "#" * int((50 / 100) * percent)
                    + "_" * int((50 / 100) * (100 - percent))
                    + "]"
                )
                Percentage.barrNeptune = "Percent of this year : " + (barre) + str("\n")
                Percentage.barrNeptuneHTML = (
                    "Percent of this year : " + (barre) + ("<br />")
                )


def Pluto():  # d0 = first perihelion , d1 = today , d2 = next perihelion

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
        thisYear = orbit["Pluto"]  # This year
        # years_ago = orbit["Pluto"][str(years_ago)][-1]
        # years_after = orbit["Pluto"][str(years_after)][0]
        for i in thisYear:
            d0Year = i[:4]
            d0Year = int(d0Year)
            d0Month = i[5:7]
            d0Month = int(d0Month)
            d0Day = i[8:10]
            d0Day = int(d0Day)
            d0 = date(d0Year, d0Month, d0Day)
            d1 = date(Percentage.current_year, Percentage.thisMonth, Percentage.today)
            d1 = d1 + timedelta(days=1)
            if (
                d0 >= d1 - timedelta(days=99000) and d0 <= d1
            ):  # i is bigger or equal today - 30 days and smaller or equal today : First day of rotation
                Percentage.PlutoPerihelion = d0

        for i in thisYear:
            d0Year = i[:4]
            d0Year = int(d0Year)
            d0Month = i[5:7]
            d0Month = int(d0Month)
            d0Day = i[8:10]
            d0Day = int(d0Day)
            d0 = date(d0Year, d0Month, d0Day)
            d1 = date(Percentage.current_year, Percentage.thisMonth, Percentage.today)
            d1 = d1 + timedelta(days=1)
            if (
                d0 <= d1 + timedelta(days=99000) and d0 >= d1
            ):  # i is smaller or equal today + 30 days and bigger or equalt today : Next Perihelion
                Percentage.NewPlutoPerihelion = d0
                d1 = date(
                    Percentage.current_year, Percentage.thisMonth, Percentage.today
                )
                d3 = Percentage.NewPlutoPerihelion - Percentage.PlutoPerihelion
                d3 = str(d3)
                d3 = d3.split()
                d3 = int(d3[0])
                d3 = d3 + 1
                ValuePercent = d3 / 100
                delta = d1 - Percentage.PlutoPerihelion
                delta = str(delta)
                delta = delta.split()
                delta = delta[0]
                new = re.sub("[^0-9]", "", str(delta))
                new = str(new)
                new = new[:4]
                new = int(new)
                Percentage.PlutoResult = new / ValuePercent
                Percentage.PlutoResult = round(Percentage.PlutoResult, 2)

                # Add graph progress #####

                print("Dwarf planet : Pluto")
                print(("Day of the year : ") + str("Day ") + str(new))
                print(("Year progress : ") + str(Percentage.PlutoResult) + str("%"))

                percent = Percentage.PlutoResult
                barre = (
                    "["
                    + "#" * int((50 / 100) * percent)
                    + "-" * int((50 / 100) * (100 - percent))
                    + "]"
                )
                print("Percent of this year : " + (barre))
                print("\n")
                Percentage.PlutoHTML = (
                    ("Dwarf planet : Pluto")
                    + ("<br />")
                    + str(("Day of the year : ") + str("Day ") + str(new))
                    + ("<br />")
                    + str(
                        ("Year progress : ")
                        + str(Percentage.PlutoResult)
                        + str("%")
                        + ("<br />")
                    )
                )
                percent = Percentage.PlutoResult
                barre = (
                    "["
                    + "#" * int((50 / 100) * percent)
                    + "_" * int((50 / 100) * (100 - percent))
                    + "]"
                )
                Percentage.barrPluto = "Percent of this year : " + (barre) + str("\n")
                Percentage.barrPlutoHTML = (
                    "Percent of this year : " + (barre) + ("<br />")
                )


def Halley():  # d0 = first perihelion , d1 = today , d2 = next perihelion

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
        thisYear = orbit["Halley"]  # This year
        # years_ago = orbit["Halley"][str(years_ago)][-1]
        # years_after = orbit["Halley"][str(years_after)][0]
        for i in thisYear:
            d0Year = i[:4]
            d0Year = int(d0Year)
            d0Month = i[5:7]
            d0Month = int(d0Month)
            d0Day = i[8:10]
            d0Day = int(d0Day)
            d0 = date(d0Year, d0Month, d0Day)
            d1 = date(Percentage.current_year, Percentage.thisMonth, Percentage.today)
            d1 = d1 + timedelta(days=1)
            if (
                d0 >= d1 - timedelta(days=28000) and d0 <= d1
            ):  # i is bigger or equal today - 30 days and smaller or equal today : First day of rotation
                Percentage.HalleyPerihelion = d0

        for i in thisYear:
            d0Year = i[:4]
            d0Year = int(d0Year)
            d0Month = i[5:7]
            d0Month = int(d0Month)
            d0Day = i[8:10]
            d0Day = int(d0Day)
            d0 = date(d0Year, d0Month, d0Day)
            d1 = date(Percentage.current_year, Percentage.thisMonth, Percentage.today)
            d1 = d1 + timedelta(days=1)
            if (
                d0 <= d1 + timedelta(days=28000) and d0 >= d1
            ):  # i is smaller or equal today + 30 days and bigger or equalt today : Next Perihelion
                Percentage.NewHalleyPerihelion = d0
                d1 = date(
                    Percentage.current_year, Percentage.thisMonth, Percentage.today
                )
                d3 = Percentage.NewHalleyPerihelion - Percentage.HalleyPerihelion
                d3 = str(d3)
                d3 = d3.split()
                d3 = int(d3[0])
                d3 = d3 + 1
                ValuePercent = d3 / 100
                delta = d1 - Percentage.HalleyPerihelion
                delta = str(delta)
                delta = delta.split()
                delta = delta[0]
                new = re.sub("[^0-9]", "", str(delta))
                new = str(new)
                new = new[:4]
                new = int(new)
                Percentage.HalleyResult = new / ValuePercent
                Percentage.HalleyResult = round(Percentage.HalleyResult, 2)

                # Add graph progress #####

                print("Comet : Halley")
                print(("Day of the year : ") + str("Day ") + str(new))
                print(("Year progress : ") + str(Percentage.HalleyResult) + str("%"))

                percent = Percentage.HalleyResult
                barre = (
                    "["
                    + "#" * int((50 / 100) * percent)
                    + "-" * int((50 / 100) * (100 - percent))
                    + "]"
                )
                print("Percent of this year : " + (barre))
                print("\n")
                Percentage.HalleyHTML = (
                    ("Comet : Halley")
                    + ("<br />")
                    + str(("Day of the year : ") + str("Day ") + str(new))
                    + ("<br />")
                    + str(
                        ("Year progress : ")
                        + str(Percentage.HalleyResult)
                        + str("%")
                        + ("<br />")
                    )
                )
                percent = Percentage.HalleyResult
                barre = (
                    "["
                    + "#" * int((50 / 100) * percent)
                    + "_" * int((50 / 100) * (100 - percent))
                    + "]"
                )
                Percentage.barrHalley = "Percent of this year : " + (barre) + str("\n")
                Percentage.barrHalleyHTML = (
                    "Percent of this year : " + (barre) + ("<br />")
                )


def Tesla():  # d0 = first perihelion , d1 = today , d2 = next perihelion

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
        thisYear = orbit["Tesla"]  # This year
        # years_ago = orbit["Tesla"][str(years_ago)][-1]
        # years_after = orbit["Tesla"][str(years_after)][0]
        for i in thisYear:
            d0Year = i[:4]
            d0Year = int(d0Year)
            d0Month = i[5:7]
            d0Month = int(d0Month)
            d0Day = i[8:10]
            d0Day = int(d0Day)
            d0 = date(d0Year, d0Month, d0Day)
            d1 = date(Percentage.current_year, Percentage.thisMonth, Percentage.today)
            d1 = d1 + timedelta(days=1)
            if (
                d0 >= d1 - timedelta(days=568) and d0 <= d1
            ):  # i is bigger or equal today - 30 days and smaller or equal today : First day of rotation
                Percentage.TeslaPerihelion = d0

        for i in thisYear:
            d0Year = i[:4]
            d0Year = int(d0Year)
            d0Month = i[5:7]
            d0Month = int(d0Month)
            d0Day = i[8:10]
            d0Day = int(d0Day)
            d0 = date(d0Year, d0Month, d0Day)
            d1 = date(Percentage.current_year, Percentage.thisMonth, Percentage.today)
            d1 = d1 + timedelta(days=1)
            if (
                d0 <= d1 + timedelta(days=568) and d0 >= d1
            ):  # i is smaller or equal today + 30 days and bigger or equalt today : Next Perihelion
                Percentage.NewTeslaPerihelion = d0
                d1 = date(
                    Percentage.current_year, Percentage.thisMonth, Percentage.today
                )
                d3 = Percentage.NewTeslaPerihelion - Percentage.TeslaPerihelion
                d3 = str(d3)
                d3 = d3.split()
                d3 = int(d3[0])
                d3 = d3 + 1
                ValuePercent = d3 / 100
                delta = d1 - Percentage.TeslaPerihelion
                delta = str(delta)
                delta = delta.split()
                delta = delta[0]
                new = re.sub("[^0-9]", "", str(delta))
                new = str(new)
                new = new[:4]
                new = int(new)
                Percentage.TeslaResult = new / ValuePercent
                Percentage.TeslaResult = round(Percentage.TeslaResult, 2)

                # Add graph progress #####

                print("Spacecraft : Tesla")
                print(("Day of the year : ") + str("Day ") + str(new))
                print(("Year progress : ") + str(Percentage.TeslaResult) + str("%"))

                percent = Percentage.TeslaResult
                barre = (
                    "["
                    + "#" * int((50 / 100) * percent)
                    + "-" * int((50 / 100) * (100 - percent))
                    + "]"
                )
                print("Percent of this year : " + (barre))
                print("\n")
                Percentage.TeslaHTML = (
                    ("Spacecraft : Tesla")
                    + ("<br />")
                    + str(("Day of the year : ") + str("Day ") + str(new))
                    + ("<br />")
                    + str(
                        ("Year progress : ")
                        + str(Percentage.TeslaResult)
                        + str("%")
                        + ("<br />")
                    )
                )
                percent = Percentage.TeslaResult
                barre = (
                    "["
                    + "#" * int((50 / 100) * percent)
                    + "_" * int((50 / 100) * (100 - percent))
                    + "]"
                )
                Percentage.barrTesla = "Percent of this year : " + (barre) + str("\n")
                Percentage.barrTeslaHTML = (
                    "Percent of this year : " + (barre) + ("<br />")
                )


def Ceres():  # d0 = first perihelion , d1 = today , d2 = next perihelion

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
        thisYear = orbit["Ceres"]  # This year
        # years_ago = orbit["Ceres"][str(years_ago)][-1]
        # years_after = orbit["Ceres"][str(years_after)][0]
        for i in thisYear:
            d0Year = i[:4]
            d0Year = int(d0Year)
            d0Month = i[5:7]
            d0Month = int(d0Month)
            d0Day = i[8:10]
            d0Day = int(d0Day)
            d0 = date(d0Year, d0Month, d0Day)
            d1 = date(Percentage.current_year, Percentage.thisMonth, Percentage.today)
            d1 = d1 + timedelta(days=1)
            if (
                d0 >= d1 - timedelta(days=1683) and d0 <= d1
            ):  # i is bigger or equal today - 30 days and smaller or equal today : First day of rotation
                Percentage.CeresPerihelion = d0

        for i in thisYear:
            d0Year = i[:4]
            d0Year = int(d0Year)
            d0Month = i[5:7]
            d0Month = int(d0Month)
            d0Day = i[8:10]
            d0Day = int(d0Day)
            d0 = date(d0Year, d0Month, d0Day)
            d1 = date(Percentage.current_year, Percentage.thisMonth, Percentage.today)
            d1 = d1 + timedelta(days=1)
            if (
                d0 <= d1 + timedelta(days=1683) and d0 >= d1
            ):  # i is smaller or equal today + 30 days and bigger or equalt today : Next Perihelion
                Percentage.NewCeresPerihelion = d0
                d1 = date(
                    Percentage.current_year, Percentage.thisMonth, Percentage.today
                )
                d3 = Percentage.NewCeresPerihelion - Percentage.CeresPerihelion
                d3 = str(d3)
                d3 = d3.split()
                d3 = int(d3[0])
                d3 = d3 + 1
                ValuePercent = d3 / 100
                delta = d1 - Percentage.CeresPerihelion
                delta = str(delta)
                delta = delta.split()
                delta = delta[0]
                new = re.sub("[^0-9]", "", str(delta))
                new = str(new)
                new = new[:4]
                new = int(new)
                Percentage.CeresResult = new / ValuePercent
                Percentage.CeresResult = round(Percentage.CeresResult, 2)

                # Add graph progress #####

                print("Dwarf planet : Ceres")
                print(("Day of the year : ") + str("Day ") + str(new))
                print(("Year progress : ") + str(Percentage.CeresResult) + str("%"))

                percent = Percentage.CeresResult
                barre = (
                    "["
                    + "#" * int((50 / 100) * percent)
                    + "-" * int((50 / 100) * (100 - percent))
                    + "]"
                )
                print("Percent of this year : " + (barre))
                print("\n")
                Percentage.CeresHTML = (
                    ("Dwarf planet : Ceres")
                    + ("<br />")
                    + str(("Day of the year : ") + str("Day ") + str(new))
                    + ("<br />")
                    + str(
                        ("Year progress : ")
                        + str(Percentage.CeresResult)
                        + str("%")
                        + ("<br />")
                    )
                )
                percent = Percentage.CeresResult
                barre = (
                    "["
                    + "#" * int((50 / 100) * percent)
                    + "_" * int((50 / 100) * (100 - percent))
                    + "]"
                )
                Percentage.barrCeres = "Percent of this year : " + (barre) + str("\n")
                Percentage.barrCeresHTML = (
                    "Percent of this year : " + (barre) + ("<br />")
                )


def Haumea():  # d0 = first perihelion , d1 = today , d2 = next perihelion

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
        thisYear = orbit["Haumea"]  # This year
        # years_ago = orbit["Haumea"][str(years_ago)][-1]
        # years_after = orbit["Haumea"][str(years_after)][0]
        for i in thisYear:
            d0Year = i[:4]
            d0Year = int(d0Year)
            d0Month = i[5:7]
            d0Month = int(d0Month)
            d0Day = i[8:10]
            d0Day = int(d0Day)
            d0 = date(d0Year, d0Month, d0Day)
            d1 = date(Percentage.current_year, Percentage.thisMonth, Percentage.today)
            d1 = d1 + timedelta(days=1)
            if (
                d0 >= d1 - timedelta(days=103774) and d0 <= d1
            ):  # i is bigger or equal today - 30 days and smaller or equal today : First day of rotation
                Percentage.HaumeaPerihelion = d0

        for i in thisYear:
            d0Year = i[:4]
            d0Year = int(d0Year)
            d0Month = i[5:7]
            d0Month = int(d0Month)
            d0Day = i[8:10]
            d0Day = int(d0Day)
            d0 = date(d0Year, d0Month, d0Day)
            d1 = date(Percentage.current_year, Percentage.thisMonth, Percentage.today)
            d1 = d1 + timedelta(days=1)
            if (
                d0 <= d1 + timedelta(days=103774) and d0 >= d1
            ):  # i is smaller or equal today + 30 days and bigger or equalt today : Next Perihelion
                Percentage.NewHaumeaPerihelion = d0
                d1 = date(
                    Percentage.current_year, Percentage.thisMonth, Percentage.today
                )
                d3 = Percentage.NewHaumeaPerihelion - Percentage.HaumeaPerihelion
                d3 = str(d3)
                d3 = d3.split()
                d3 = int(d3[0])
                d3 = d3 + 1
                ValuePercent = d3 / 100
                delta = d1 - Percentage.HaumeaPerihelion
                delta = str(delta)
                delta = delta.split()
                delta = delta[0]
                new = re.sub("[^0-9]", "", str(delta))
                new = str(new)
                new = new[:4]
                new = int(new)
                Percentage.HaumeaResult = new / ValuePercent
                Percentage.HaumeaResult = round(Percentage.HaumeaResult, 2)

                # Add graph progress #####

                print("Dwarf planet : Haumea")
                print(("Day of the year : ") + str("Day ") + str(new))
                print(("Year progress : ") + str(Percentage.HaumeaResult) + str("%"))

                percent = Percentage.HaumeaResult
                barre = (
                    "["
                    + "#" * int((50 / 100) * percent)
                    + "-" * int((50 / 100) * (100 - percent))
                    + "]"
                )
                print("Percent of this year : " + (barre))
                print("\n")
                Percentage.HaumeaHTML = (
                    ("Dwarf planet : Haumea")
                    + ("<br />")
                    + str(("Day of the year : ") + str("Day ") + str(new))
                    + ("<br />")
                    + str(
                        ("Year progress : ")
                        + str(Percentage.HaumeaResult)
                        + str("%")
                        + ("<br />")
                    )
                )
                percent = Percentage.HaumeaResult
                barre = (
                    "["
                    + "#" * int((50 / 100) * percent)
                    + "_" * int((50 / 100) * (100 - percent))
                    + "]"
                )
                Percentage.barrHaumea = "Percent of this year : " + (barre) + str("\n")
                Percentage.barrHaumeaHTML = (
                    "Percent of this year : " + (barre) + ("<br />")
                )


def Makemake():  # d0 = first perihelion , d1 = today , d2 = next perihelion

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
        thisYear = orbit["Makemake"]  # This year
        # years_ago = orbit["Makemake"][str(years_ago)][-1]
        # years_after = orbit["Makemake"][str(years_after)][0]
        for i in thisYear:
            d0Year = i[:4]
            d0Year = int(d0Year)
            d0Month = i[5:7]
            d0Month = int(d0Month)
            d0Day = i[8:10]
            d0Day = int(d0Day)
            d0 = date(d0Year, d0Month, d0Day)
            d1 = date(Percentage.current_year, Percentage.thisMonth, Percentage.today)
            d1 = d1 + timedelta(days=1)
            if (
                d0 >= d1 - timedelta(days=112330) and d0 <= d1
            ):  # i is bigger or equal today - 30 days and smaller or equal today : First day of rotation
                Percentage.MakemakePerihelion = d0

        for i in thisYear:
            d0Year = i[:4]
            d0Year = int(d0Year)
            d0Month = i[5:7]
            d0Month = int(d0Month)
            d0Day = i[8:10]
            d0Day = int(d0Day)
            d0 = date(d0Year, d0Month, d0Day)
            d1 = date(Percentage.current_year, Percentage.thisMonth, Percentage.today)
            d1 = d1 + timedelta(days=1)
            if (
                d0 <= d1 + timedelta(days=112330) and d0 >= d1
            ):  # i is smaller or equal today + 30 days and bigger or equalt today : Next Perihelion
                Percentage.NewMakemakePerihelion = d0
                d1 = date(
                    Percentage.current_year, Percentage.thisMonth, Percentage.today
                )
                d3 = Percentage.NewMakemakePerihelion - Percentage.MakemakePerihelion
                d3 = str(d3)
                d3 = d3.split()
                d3 = int(d3[0])
                d3 = d3 + 1
                ValuePercent = d3 / 100
                delta = d1 - Percentage.MakemakePerihelion
                delta = str(delta)
                delta = delta.split()
                delta = delta[0]
                new = re.sub("[^0-9]", "", str(delta))
                new = str(new)
                new = new[:4]
                new = int(new)
                Percentage.MakemakeResult = new / ValuePercent
                Percentage.MakemakeResult = round(Percentage.MakemakeResult, 2)

                # Add graph progress #####

                print("Dwarf planet : Makemake")
                print(("Day of the year : ") + str("Day ") + str(new))
                print(("Year progress : ") + str(Percentage.MakemakeResult) + str("%"))

                percent = Percentage.MakemakeResult
                barre = (
                    "["
                    + "#" * int((50 / 100) * percent)
                    + "-" * int((50 / 100) * (100 - percent))
                    + "]"
                )
                print("Percent of this year : " + (barre))
                print("\n")
                Percentage.MakemakeHTML = (
                    ("Dwarf planet : Makemake")
                    + ("<br />")
                    + str(("Day of the year : ") + str("Day ") + str(new))
                    + ("<br />")
                    + str(
                        ("Year progress : ")
                        + str(Percentage.MakemakeResult)
                        + str("%")
                        + ("<br />")
                    )
                )
                percent = Percentage.MakemakeResult
                barre = (
                    "["
                    + "#" * int((50 / 100) * percent)
                    + "_" * int((50 / 100) * (100 - percent))
                    + "]"
                )
                Percentage.barrMakemake = (
                    "Percent of this year : " + (barre) + str("\n")
                )
                Percentage.barrMakemakeHTML = (
                    "Percent of this year : " + (barre) + ("<br />")
                )


def Eris():  # d0 = first perihelion , d1 = today , d2 = next perihelion

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
        thisYear = orbit["Eris"]  # This year
        # years_ago = orbit["Eris"][str(years_ago)][-1]
        # years_after = orbit["Eris"][str(years_after)][0]
        for i in thisYear:
            d0Year = i[:4]
            d0Year = int(d0Year)
            d0Month = i[5:7]
            d0Month = int(d0Month)
            d0Day = i[8:10]
            d0Day = int(d0Day)
            d0 = date(d0Year, d0Month, d0Day)
            d1 = date(Percentage.current_year, Percentage.thisMonth, Percentage.today)
            d1 = d1 + timedelta(days=1)
            if (
                d0 >= d1 - timedelta(days=203661) and d0 <= d1
            ):  # i is bigger or equal today - 30 days and smaller or equal today : First day of rotation
                Percentage.ErisPerihelion = d0

        for i in thisYear:
            d0Year = i[:4]
            d0Year = int(d0Year)
            d0Month = i[5:7]
            d0Month = int(d0Month)
            d0Day = i[8:10]
            d0Day = int(d0Day)
            d0 = date(d0Year, d0Month, d0Day)
            d1 = date(Percentage.current_year, Percentage.thisMonth, Percentage.today)
            d1 = d1 + timedelta(days=1)
            if (
                d0 <= d1 + timedelta(days=203661) and d0 >= d1
            ):  # i is smaller or equal today + 30 days and bigger or equalt today : Next Perihelion
                Percentage.NewErisPerihelion = d0
                d1 = date(
                    Percentage.current_year, Percentage.thisMonth, Percentage.today
                )
                d3 = Percentage.NewErisPerihelion - Percentage.ErisPerihelion
                d3 = str(d3)
                d3 = d3.split()
                d3 = int(d3[0])
                d3 = d3 + 1
                ValuePercent = d3 / 100
                delta = d1 - Percentage.ErisPerihelion
                delta = str(delta)
                delta = delta.split()
                delta = delta[0]
                new = re.sub("[^0-9]", "", str(delta))
                new = str(new)
                new = new[:4]
                new = int(new)
                Percentage.ErisResult = new / ValuePercent
                Percentage.ErisResult = round(Percentage.ErisResult, 2)

                # Add graph progress #####

                print("Dwarf planet : Eris")
                print(("Day of the year : ") + str("Day ") + str(new))
                print(("Year progress : ") + str(Percentage.ErisResult) + str("%"))

                percent = Percentage.ErisResult
                barre = (
                    "["
                    + "#" * int((50 / 100) * percent)
                    + "-" * int((50 / 100) * (100 - percent))
                    + "]"
                )
                print("Percent of this year : " + (barre))
                print("\n")
                Percentage.ErisHTML = (
                    ("Dwarf planet : Eris")
                    + ("<br />")
                    + str(("Day of the year : ") + str("Day ") + str(new))
                    + ("<br />")
                    + str(
                        ("Year progress : ")
                        + str(Percentage.ErisResult)
                        + str("%")
                        + ("<br />")
                    )
                )
                percent = Percentage.ErisResult
                barre = (
                    "["
                    + "#" * int((50 / 100) * percent)
                    + "_" * int((50 / 100) * (100 - percent))
                    + "]"
                )
                Percentage.barrEris = "Percent of this year : " + (barre) + str("\n")
                Percentage.barrErisHTML = (
                    "Percent of this year : " + (barre) + ("<br />")
                )

def Encke():  # d0 = first perihelion , d1 = today , d2 = next perihelion

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
        thisYear = orbit["Encke"]  # This year
        # years_ago = orbit["Encke"][str(years_ago)][-1]
        # years_after = orbit["Encke"][str(years_after)][0]
        for i in thisYear:
            d0Year = i[:4]
            d0Year = int(d0Year)
            d0Month = i[5:7]
            d0Month = int(d0Month)
            d0Day = i[8:10]
            d0Day = int(d0Day)
            d0 = date(d0Year, d0Month, d0Day)
            d1 = date(Percentage.current_year, Percentage.thisMonth, Percentage.today)
            d1 = d1 + timedelta(days=1)
            if (
                    d0 >= d1 - timedelta(days=1203) and d0 <= d1
            ):  # i is bigger or equal today - 30 days and smaller or equal today : First day of rotation
                Percentage.EnckePerihelion = d0

        for i in thisYear:
            d0Year = i[:4]
            d0Year = int(d0Year)
            d0Month = i[5:7]
            d0Month = int(d0Month)
            d0Day = i[8:10]
            d0Day = int(d0Day)
            d0 = date(d0Year, d0Month, d0Day)
            d1 = date(Percentage.current_year, Percentage.thisMonth, Percentage.today)
            d1 = d1 + timedelta(days=1)
            if (
                    d0 <= d1 + timedelta(days=1203) and d0 >= d1
            ):  # i is smaller or equal today + 30 days and bigger or equalt today : Next Perihelion
                Percentage.NewEnckePerihelion = d0
                d1 = date(
                    Percentage.current_year, Percentage.thisMonth, Percentage.today
                )
                d3 = Percentage.NewEnckePerihelion - Percentage.EnckePerihelion
                d3 = str(d3)
                d3 = d3.split()
                d3 = int(d3[0])
                d3 = d3 + 1
                ValuePercent = d3 / 100
                delta = d1 - Percentage.EnckePerihelion
                delta = str(delta)
                delta = delta.split()
                delta = delta[0]
                new = re.sub("[^0-9]", "", str(delta))
                new = str(new)
                new = new[:4]
                new = int(new)
                Percentage.EnckeResult = new / ValuePercent
                Percentage.EnckeResult = round(Percentage.EnckeResult, 2)

                # Add graph progress #####

                print("Comet : Encke")
                print(("Day of the year : ") + str("Day ") + str(new))
                print(("Year progress : ") + str(Percentage.EnckeResult) + str("%"))

                percent = Percentage.EnckeResult
                barre = (
                        "["
                        + "#" * int((50 / 100) * percent)
                        + "-" * int((50 / 100) * (100 - percent))
                        + "]"
                )
                print("Percent of this year : " + (barre))
                print("\n")
                Percentage.EnckeHTML = (
                        ("Comet : Encke")
                        + ("<br />")
                        + str(("Day of the year : ") + str("Day ") + str(new))
                        + ("<br />")
                        + str(
                    ("Year progress : ")
                    + str(Percentage.EnckeResult)
                    + str("%")
                    + ("<br />")
                )
                )
                percent = Percentage.EnckeResult
                barre = (
                        "["
                        + "#" * int((50 / 100) * percent)
                        + "_" * int((50 / 100) * (100 - percent))
                        + "]"
                )
                Percentage.barrEncke = "Percent of this year : " + (barre) + str("\n")
                Percentage.barrEnckeHTML = (
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
Jupiter()
Saturn()
Uranus()
Neptune()
Pluto()
Halley()
Tesla()
Ceres()
Haumea()
Makemake()
Eris()
Encke()

startHtml = (
    str("<!DOCTYPE html>")
    + str("\n")
    + str("<html>")
    + str("\n")
    + str("<head>")
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
endHTML = str("</p>") + str("\n") + str("</font>") + str("\n") + str("</body>")

indexFile = open("/var/www/html/main.html", "w")
indexFile.write(startHtml)
indexFile.close()

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

contentHtml = open("/var/www/html/main.html", "a")
# contentHtml.write(Percentage.motdResultHTML)
contentHtml.write(
    '<img src="http://astrometry.ch/pictures/terre.png" alt="earth" width="100" height="100">'
)
contentHtml.write("<br />")
contentHtml.write(Percentage.earthHTML)
contentHtml.write(Percentage.BarrEarthHTML)
contentHtml.write("<br />")
contentHtml.write("<br />")
contentHtml.write(
    '<img src="http://astrometry.ch/pictures/lune.jpg" alt="moon" width="130" height="100">'
)
contentHtml.write("<br />")
contentHtml.write(Percentage.moonHTML)
contentHtml.write(Percentage.barrMoonHTML)
contentHtml.write("<br />")
contentHtml.write("<br />")
contentHtml.write(
    '<img src="http://astrometry.ch/pictures/mercury.png" alt="mercury" width="100" height="100">'
)
contentHtml.write("<br />")
contentHtml.write(Percentage.mercuryHTML)
contentHtml.write(Percentage.barrMercuryHTML)
contentHtml.write("<br />")
contentHtml.write("<br />")
contentHtml.write(
    '<img src="http://astrometry.ch/pictures/venus.jpg" alt="venus" width="100" height="100">'
)
contentHtml.write("<br />")
contentHtml.write(Percentage.VenusHTML)
contentHtml.write(Percentage.barrVenusHTML)
contentHtml.write("<br />")
contentHtml.write("<br />")
contentHtml.write(
    '<img src="http://astrometry.ch/pictures/mars.jpg" alt="mars" width="100" height="100">'
)
contentHtml.write("<br />")
contentHtml.write(Percentage.MarsHTML)
contentHtml.write(Percentage.barrMarsHTML)
contentHtml.write("<br />")
contentHtml.write("<br />")
contentHtml.write(
    '<img src="http://astrometry.ch/pictures/jupiter.jpg" alt="jupiter" width="100" height="100">'
)
contentHtml.write("<br />")
contentHtml.write(Percentage.JupiterHTML)
contentHtml.write(Percentage.barrJupiterHTML)
contentHtml.write("<br />")
contentHtml.write("<br />")
contentHtml.write(
    '<img src="http://astrometry.ch/pictures/saturn.jpg" alt="saturn" width="130" height="100">'
)
contentHtml.write("<br />")
contentHtml.write(Percentage.SaturnHTML)
contentHtml.write(Percentage.barrSaturnHTML)
contentHtml.write("<br />")
contentHtml.write("<br />")
contentHtml.write(
    '<img src="http://astrometry.ch/pictures/uranus.jpg" alt="uranus" width="100" height="100">'
)
contentHtml.write("<br />")
contentHtml.write(Percentage.UranusHTML)
contentHtml.write(Percentage.barrUranusHTML)
contentHtml.write("<br />")
contentHtml.write("<br />")
contentHtml.write(
    '<img src="http://astrometry.ch/pictures/neptune.jpg" alt="neptune" width="100" height="100">'
)
contentHtml.write("<br />")
contentHtml.write(Percentage.NeptuneHTML)
contentHtml.write(Percentage.barrNeptuneHTML)
contentHtml.write("<br />")
contentHtml.write("<br />")
contentHtml.write(
    '<img src="http://astrometry.ch/pictures/pluto.jpg" alt="pluto" width="100" height="100">'
)
contentHtml.write("<br />")
contentHtml.write(Percentage.PlutoHTML)
contentHtml.write(Percentage.barrPlutoHTML)
contentHtml.write("<br />")
contentHtml.write("<br />")
contentHtml.write(
    '<img src="http://astrometry.ch/pictures/halley.jpg" alt="halley" width="100" height="100">'
)
contentHtml.write("<br />")
contentHtml.write(Percentage.HalleyHTML)
contentHtml.write(Percentage.barrHalleyHTML)
contentHtml.write("<br />")
contentHtml.write("<br />")
contentHtml.write(
    '<img src="http://astrometry.ch/pictures/tesla.jpg" alt="tesla" width="130" height="100">'
)
contentHtml.write("<br />")
contentHtml.write(Percentage.TeslaHTML)
contentHtml.write(Percentage.barrTeslaHTML)
contentHtml.write("<br />")
contentHtml.write("<br />")
contentHtml.write(
    '<img src="http://astrometry.ch/pictures/ceres.jpg" alt="ceres" width="130" height="100">'
)
contentHtml.write("<br />")
contentHtml.write(Percentage.CeresHTML)
contentHtml.write(Percentage.barrCeresHTML)
contentHtml.write("<br />")
contentHtml.write("<br />")
contentHtml.write(
    '<img src="http://astrometry.ch/pictures/makemake.jpg" alt="makemake" width="100ay be" height="100">'
)
contentHtml.write("<br />")
contentHtml.write(Percentage.MakemakeHTML)
contentHtml.write(Percentage.barrMakemakeHTML)
contentHtml.write("<br />")
contentHtml.write("<br />")
contentHtml.write(
    '<img src="http://astrometry.ch/pictures/haumea.jpg" alt="haumea" width="100" height="100">'
)
contentHtml.write("<br />")
contentHtml.write(Percentage.HaumeaHTML)
contentHtml.write(Percentage.barrHaumeaHTML)
contentHtml.write("<br />")
contentHtml.write("<br />")
contentHtml.write(
    '<img src="http://astrometry.ch/pictures/eris.jpg" alt="eris" width="100" height="100">'
)
contentHtml.write("<br />")
contentHtml.write(Percentage.ErisHTML)
contentHtml.write(Percentage.barrErisHTML)
contentHtml.write("<br />")
contentHtml.write("<br />")
contentHtml.write(
    '<img src="http://astrometry.ch/pictures/encke.jpg" alt="eris" width="100" height="100">'
)
contentHtml.write("<br />")
contentHtml.write(Percentage.EnckeHTML)
contentHtml.write(Percentage.barrEnckeHTML)
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
