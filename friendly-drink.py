import time # Used for time delay function
import csv # Used for csv handling

# Dictionary containing information about user
userData = {}
# userName - stores the name given to the program

# Used to reveal text with the time delay
def reveal(text):
    time.sleep(1)
    print "FD: " + text

# Removes excessive spaces, returns cleaned
def clean(string):
    sList = string.split()
    nString = ""
    for word in sList:
        nString += (word + " ")
    return nString[0:-1] # skips last space

# Initial lines when started
def intro():
    reveal("Hey there, my name is Friendly-Drink, but I go by FD.")
    reveal("But I go by FD")
    getName()

# Gets name of user
def getName():
    reveal("What's your name?")
    userData['userName'] = raw_input('> ') # input stored in user data dictionary
    reveal("Hey there %s, it's nice to meet you" % userData['userName'])

# function to print time of a location from user input using Dataset
def getTime(locale):
    locale = clean(locale)
    searchParam = locale.lower()

    reveal("Let me look up the time in %s" % locale.title())
    f0 = open('../friendly-drink/Datasets/timezonedb/country.csv')
    countryTable = csv.reader(f0)

    f1 = open('../friendly-drink/Datasets/timezonedb/zone.csv')
    zone = csv.reader(f1)

    f2 = open('../friendly-drink/Datasets/timezonedb/timezone.csv')
    timezone = csv.reader(f2)

    for row in zone:
        if searchParam in row[2].lower():
            zone_id = row[0] # zone_id used for lookup in timezone.csv
            countryCode = row[1] # countryCode

    if 'zone_id' not in locals():
        print "I can't find that place"
        return

    for row in countryTable:
        if row[0] == countryCode:
            countryName = row[1] # Full name of country is saved

    for row in timezone:
        if (zone_id == row[0]): # still need to account for DST
            # gets time difference and converts to num
            GMTOffset = int(row[3]) # Offset from GMT
            break

    checkTime = time.time() + GMTOffset # gets time in desired locale
    print "The time in %s, %s is:" % (searchParam.title(), countryName)
    print time.strftime("%H:%M:%S, %a, %d %b %Y ", time.gmtime(checkTime))

def start():
    sTime = time.time() # time from program start
    intro()
    while True:
        qString = raw_input('> ') # Query string
        if qString.startswith("Time in"):
            getTime(qString[7:])
        elif qString == "end":
            break

start()
