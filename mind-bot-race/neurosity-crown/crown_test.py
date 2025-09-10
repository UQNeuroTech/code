from neurosity import NeurositySDK
import os

NEUROSITY_EMAIL = 'reubenr202@gmail.com'
NEUROSITY_PASSWORD = 'neuro123'
NEUROSITY_DEVICE_ID = 'e88770a76231aac1ca98f41e7c9094cd'

neurosity = NeurositySDK({
    # "device_id": os.getenv("NEUROSITY_DEVICE_ID"),
    "device_id": NEUROSITY_DEVICE_ID,
})

neurosity.login({
    "email": NEUROSITY_EMAIL,
    "password": NEUROSITY_PASSWORD
})

def callback(data):
    # print("data", data)
    
    # Switch light off/on
    print("Right Arm:", data.probability)

# unsubscribe = neurosity.brainwaves_raw(callback)
unsubscribe = neurosity.kinesis_predictions("rightArm", callback)

