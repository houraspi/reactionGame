import RPi.GPIO as GPIO
import time
import random

def rg():
    p1Score=0
    p2Score=0
    while True:
        ##set up board as how broadcomm sees the pins BCM or how humans sees the pins BOARD
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        ##set up the pin LED is attached to
        led=23
        ##set up the pin switches are attached to
        top_button=27
        bottom_button=22
        ##sets up LED as output
        GPIO.setup(led, GPIO.OUT)
        ##sets up buttons as input with pullup resistors
        GPIO.setup(top_button, GPIO.IN, GPIO.PUD_UP)
        GPIO.setup(bottom_button, GPIO.IN, GPIO.PUD_UP)
        GPIO.output(led,0)
        ##waits between 1&5 seconds
        time.sleep(random.uniform(1,5))
        ##turn led on
        GPIO.output(led,1)
        while True:
            if GPIO.input(top_button)== False:
                print("Top button is pressed, Player one wins this round!")
                p1Score+=1
                print ("Player one has ", p1Score, "points total, player two has ", p2Score, "total.")
                break
            if GPIO.input(bottom_button)== False:
                print("Bottom button pressed, Player two wins this round!")
                p2Score+=1
                print ("Player one has ", p1Score, "points total, player two has ", p2Score, "total.")
                break
        GPIO.output(led,0)
        GPIO.cleanup()
        ##edge cases. why would player one always win if they both cheat





