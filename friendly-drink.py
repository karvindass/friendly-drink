import time # Used for time delay function

inputName = "" # Stores the name given to the program

# Used to reveal text with the time delay
def reveal(text):
    print "FD: " + text
    time.sleep(1)

# Initial lines when started
def start():
    reveal("Hey there, my name is Friendly-Drink, but I go by FD.")
    reveal("But I go by FD")

# Gets name of user
def getName():
    reveal("What's your name?")
    inputName = raw_input('You: ')
    reveal("Hey there %s, it's nice to meet you" %inputName)

start()
getName()
