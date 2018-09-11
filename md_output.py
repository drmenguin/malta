################################################################################
##                          TOWNS AND CITIES OF MALTA                         ##
##                          drmenguin - GPLv3 License                         ##
################################################################################

import sys

# First check that Python 3 is used.
if sys.version_info < (3,0):
    sys.exit("""Sorry, requires Python 3.x, not Python 2.x""")

# Try to import Google Geocoder for Longitude/Latitudes.
try:
    from geopy.geocoders import GoogleV3
except ImportError:
    sys.exit("""This module requires the package geopy. Please install and try again.""")

# Load wikipedia list of cities/towns.
towns = open("towns.txt", "r").read().splitlines()

# Prepare to write to file (Markdown table format)
out = open("output.md", "w")
out.write("| *City or Town* | *What Google Maps API Recognised* | * Coordinates * |\n")
out.write("|:--------------:|:---------------------------------:|:---------------:|\n")

# Use Google API to find Latitude/Longitude for each town
# Needs Google API key, get a free trial key here:
# https://cloud.google.com/maps-platform/
geocoder = GoogleV3(api_key="ENTER_YOUR_KEY_HERE", timeout=None)
for town in towns[8:]:
    town_object = geocoder.geocode(town)
    if town_object:
        town_string = "| " +  town + " " \
                      + "| " + str(town_object.address) + " " \
                      + "| " + str(town_object.latitude) + ", " \
                      + str(town_object.longitude) + " |\n"
        print(town, "("+town_object.address+")", town_object.latitude, town_object.longitude)
        out.write(town_string)

# Close file
out.close()



