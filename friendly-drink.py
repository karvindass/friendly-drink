import time # Used for time delay function
import csv # Used for csv handling

inputName = "" # Stores the name given to the program

# Used to reveal text with the time delay
def reveal(text):
    print "FD: " + text
    time.sleep(1)

# Removes excessive spaces, returns cleaned
def clean(string):
    sList = string.split()
    nString = ""
    for word in sList:
        nString += (word + " ")
    return nString[0:-1]

# Initial lines when started
def intro():
    reveal("Hey there, my name is Friendly-Drink, but I go by FD.")
    reveal("But I go by FD")
    getName()

# Gets name of user
def getName():
    reveal("What's your name?")
    inputName = raw_input('You: ')
    reveal("Hey there %s, it's nice to meet you" %inputName)

# function to get time of a location from Dataset
def getTime(locale):
    locale = clean(locale)
    searchParam = locale.lower()

    zone_id = "" # Zone ID

    reveal("Let me look up the time in %s" % locale.title())
    f0 = open('/Users/karvindassanayake/Documents/Github/friendly-drink/Datasets/timezonedb/country.csv') # Will turn to relative path in future...
    countryCode = csv.reader(f0)

    f1 = open('/Users/karvindassanayake/Documents/Github/friendly-drink/Datasets/timezonedb/zone.csv') # Will turn to relative path in future...
    zone = csv.reader(f1)

    f2 = open('/Users/karvindassanayake/Documents/Github/friendly-drink/Datasets/timezonedb/timezone.csv') # Will turn to relative path in future...
    timezone = csv.reader(f2)

    for row in zone:
        # print row[2].lower()
        if searchParam in row[2].lower():
            zone_id = row[0] # zone_id used for lookup in timezone.csv

    for row in timezone:
        # print row[4]
        if (zone_id == row[0]): # still need to account for DST
            # gets time difference and converts to num
            GMTOffset = int(row[3]) # Offset from GMT
            break
def start():
    sTime = time.time() # time from program start
    intro()
    # while True:
    qString = raw_input('> ') # Query string
    if qString.startswith("Time in"):
        getTime(qString[7:])

start()
