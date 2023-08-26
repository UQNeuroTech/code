from neurosity import NeurositySDK
# from dotenv import load_dotenv
import os

from micromelon import *
import time


NEUROSITY_EMAIL = 'reubenr202@gmail.com'
NEUROSITY_PASSWORD = 'neuro123'
NEUROSITY_DEVICE_ID = 'e88770a76231aac1ca98f41e7c9094cd'

# load_dotenv()

neurosity = NeurositySDK({
    # "device_id": os.getenv("NEUROSITY_DEVICE_ID"),
    "device_id": NEUROSITY_DEVICE_ID,
})

# neurosity = NeurositySDK({"device_id": 'e88770a76231aac1ca98f41e7c9094cd'})

neurosity.login({
    "email": NEUROSITY_EMAIL,
    "password": NEUROSITY_PASSWORD
})

rover = False
forwardDistance = 2

last_trigger = time.time()




def main():

    roverInit()

    # unsubscribe = neurosity.brainwaves_raw(callback)
    # unsubscribe = neurosity.kinesis("rightArm", callback)
    unsubscribe = neurosity.kinesis("leftArm", callback)
    
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
    rc = RoverController()

    rc.connectBLE(83)
    rc.startRover()
    

    rover = True


main()

