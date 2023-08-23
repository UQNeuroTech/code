
from neurosity import NeurositySDK
from micromelon import RoverController, motors, leds, sounds, TUNES

# Neurosity initialization
neurosity = NeurositySDK({
    "device_id": "YOUR_NEUROSITY_DEVICE_ID"
})
neurosity.login({
    "email": "YOUR_NEUROSITY_EMAIL",
    "password": "YOUR_NEUROSITY_PASSWORD"
})

# Micromelon initialization
robot = RoverController()
robot.connectBLE("YOUR_ROBOT_ID")

def focus_callback(data):
    speed = data['probability'] * 100
    motors.set_speed(speed)
    
    # LED intensity proportional to focus
    led_intensity = int(data['probability'] * 255)
    leds.setAll(led_intensity, 0, 0)  # Red color intensity based on focus
    
    # Play accelerating sound for increased focus
    if speed > 50:
        sounds.playTune(TUNES.UP)

unsubscribe_focus = neurosity.focus(focus_callback)
