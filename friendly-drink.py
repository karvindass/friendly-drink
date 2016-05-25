import time # Used for time delay function

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

def start():
    sTime = time.time() # time from program start
    intro()
    # while True:
    qString = raw_input('> ') # Query string
    if qString.startswith("Time in"):
        getTime(qString[7:])

start()
