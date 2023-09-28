from neurosity import NeurositySDK
import os

from micromelon import *
import time

NEUROSITY_EMAIL = 'reubenr202@gmail.com'
NEUROSITY_PASSWORD = 'neuro123'
NEUROSITY_DEVICE_ID = 'e88770a76231aac1ca98f41e7c9094cd'

# Distance (in cm) that the micromelon moves forward when you activate kenisis
forwardDistance = 2

# Track the last time that kenesis was activated
last_trigger = time.time()

def main():

    # Initialize Neurosity Crown object
    neurosity = NeurositySDK({
    "device_id": NEUROSITY_DEVICE_ID,
    })

    # Log into the Neurosity API
    neurosity.login({
    "email": NEUROSITY_EMAIL,
    "password": NEUROSITY_PASSWORD
    })

    # Initialise micromelon rover
    roverInit()

    unsubscribe = neurosity.kinesis("rightArm", callback)
    # unsubscribe = neurosity.kinesis("leftArm", callback)

    # unsubscribe = neurosity.brainwaves_raw(callback)
    # unsubscribe = neurosity.focus(callback)


def callback(data):
    # Switch light off/on
    print(data['metric'], data['label'], ":", data['confidence'])

    # global Motors

    global last_trigger
    
    # time.sleep(1)
    # Motors.moveDistance(int(forwardDistance))
    current_trigger = time.time()

    diff = current_trigger - last_trigger
    print("diff:", diff)

    if ((diff > 3) & (data['confidence'] > 0.9)):
        Motors.moveDistance(int(forwardDistance))
        last_trigger = current_trigger

def roverInit():
    """Initialize the Micromelon rover"""
    rc = RoverController()

    rc.connectBLE(116)
    rc.startRover()

main()

