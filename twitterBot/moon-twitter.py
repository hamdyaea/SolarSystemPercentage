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
        self.MoonHTML
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
        self.MarsHTML
        self.barrMarsHTML
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
        thisYear = orbit["Moon"]  # This year
        # years_ago = orbit["Moon"][str(years_ago)][-1]
        # years_after = orbit["Moon"][str(years_after)][0]
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
            d1 = date(Percentage.current_year, Percentage.thisMonth, Percentage.today)
            d1 = d1 + timedelta(days=1)
            if (
                d0 <= d1 + timedelta(days=25) and d0 >= d1
            ):  # i is smaller or equal today + 30 days and bigger or equalt today : Next Perihelion
                Percentage.NewMoonPerihelion = d0
                d1 = date(
                    Percentage.current_year, Percentage.thisMonth, Percentage.today
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
                new = new[:4]
                new = int(new)
                Percentage.MoonResult = new / ValuePercent
                Percentage.MoonResult = round(Percentage.MoonResult, 2)

                # Add graph progress #####

                print("Satelite : Moon")
                print(("Day of the year : ") + str("Day ") + str(new))
                print(("Year progress : ") + str(Percentage.MoonResult) + str("%"))

                percent = Percentage.MoonResult
                barre = (
                    "["
                    + "#" * int((50 / 100) * percent)
                    + "-" * int((50 / 100) * (100 - percent))
                    + "]"
                )
                print("Percent of this year : " + (barre))
                print("\n")
                Percentage.MoonHTML = (
                    ("Satelite : Moon")
                    + str("\n")
                    + str(("Day of the year : ") + str("Day ") + str(new))
                    + str("\n")
                    + str(
                        ("Year progress : ")
                        + str(Percentage.MoonResult)
                        + str("%")
                        + str("\n")
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
                Percentage.barrMoonHTML = (
                    "Percent of this year : " + (barre) + str("\n")
                )


    """

    Do the same for the moon and other solar system planets, natural satelites, ISS, of all the solar system. 
    """


#motd()
#Earth()
Moon()
#Mercury()
#Venus()
#Mars()
#Jupiter()
#Saturn()
#Uranus()
#Neptune()


message = Percentage.MoonHTML + Percentage.barrMoonHTML + str('\n#Astronomy #Space #Espace #Astrometry')
photo = open('/var/www/html/pictures/lune.jpg', 'rb')
response = twitter.upload_media(media=photo)
twitter.update_status(status=message, media_ids=[response['media_id']])
