from neurosity import NeurositySDK
import os

from micromelon import *
import time

NEUROSITY_EMAIL = 'reubenr202@gmail.com'
NEUROSITY_PASSWORD = 'neuro123'
NEUROSITY_DEVICE_ID = 'e88770a76231aac1ca98f41e7c9094cd'

# Distance (in cm) that the micromelon moves forward when you activate kenisis
forwardDistance = 5

# Angle (in degrees) that the micromelon turns when you activate kenisis
turnAngle = 5

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

    # Please choose which kinesis metrics you want to use:
    kinesis_type_1 = "rightARM"
    kinesis_type_2 = "leftARM"
    # kinesis_type_1 = "bitingALemon"
    # kinesis_type_2 = "blah blah" # ect. ect. (there are allot of them)

    # Assign the chosen kenisis metrics to our callback function
    unsubscribe = neurosity.kinesis(kinesis_type_1, callback)
    unsubscribe2 = neurosity.kinesis(kinesis_type_2, callback)

    # If you uncomment any of these, it will break the code:

    # unsubscribe = neurosity.brainwaves_raw(callback)
    # unsubscribe = neurosity.focus(callback)

    # ^ | Reason why I kept them here is just to demostrate
    # ^ | that you can use the Neurosity API to get other 
    # ^ | metrics - not just the 'kenisis' functionality.)
    #   | 
    #   | This includes being able to get the raw EEG data
    #   | for free!!)
    #   | 
    #   | Use Neurosity's Docs to explore: 
    #   | https://github.com/neurosity/neurosity-sdk-python 


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
        if data['label'] == 'leftArm':
            Motors.turnDegrees(-int(turnAngle))
        else:
            Motors.turnDegrees(int(turnAngle))
        
        Motors.moveDistance(int(forwardDistance))
        last_trigger = current_trigger

def roverInit():
    """Initialize the Micromelon rover"""
    rc = RoverController()

    rc.connectBLE(116)
    rc.startRover()

main()

