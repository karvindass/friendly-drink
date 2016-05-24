import time

inputName = ""

def start():
    print "Hey there, my name is Friendly-Drink, but I go by FD."
    time.sleep(1)
    print "But I go by FD"
    time.sleep(1)

def getName():
    print "What's your name?"
    inputName = raw_input('You: ')
    print()
    print "Hey there %s, it's nice to meet you" %inputName

start()
getName()
