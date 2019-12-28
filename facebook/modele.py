#!/usr/bin/env python3

from keys import *
import facebook



graph = facebook.GraphAPI(access_token=[token], version="3.0")

graph.put_photo(image=open("/var/www/html/pictures/lune.jpg", 'rb'), message='Look at the moon !')