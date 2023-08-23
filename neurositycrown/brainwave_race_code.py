
from neurosity import NeurositySDK
from micromelon import RoverController, motors, leds, sounds, TUNES
import os

NEUROSITY_EMAIL = 'reubenr202@gmail.com'
NEUROSITY_PASSWORD = 'neuro123'
NEUROSITY_DEVICE_ID = 'e88770a76231aac1ca98f41e7c9094cd'

#load_dotenv()

neurosity = NeurositySDK({
    "device_id": os.getenv("NEUROSITY_DEVICE_ID"),
    "device_id": NEUROSITY_DEVICE_ID,
})

neurosity.login({
    "email": NEUROSITY_EMAIL,
    "password": NEUROSITY_PASSWORD
})

# Micromelon initialization
robot = RoverController()
robot.connectBLE("83")

def focus_callback(data):
    speed = data['probability'] * 60
    motors.write(speed)
    print(data['probability'])
    
    # LED intensity proportional to focus
    led_intensity = int(data['probability'] * 255)
    leds.setAll(led_intensity, 0, 0)  # Red color intensity based on focus
    
    # Play accelerating sound for increased focus
    if speed > 15:
        sounds.playTune(TUNES.UP)

unsubscribe_focus = neurosity.focus(focus_callback)
