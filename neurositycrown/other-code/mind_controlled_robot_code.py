
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

last_focus_prob = 0
last_calm_prob = 0

def focus_callback(data):
    global last_focus_prob
    last_focus_prob = data['probability']
    
    if last_focus_prob > 0.5 and last_calm_prob <= 0.5:
        # Move the robot forward
        motors.move_forward()
        leds.setAll(0, 0, 255)  # Blue color for forward movement
        sounds.playTune(TUNES.UP)
    elif last_focus_prob > 0.5 and last_calm_prob > 0.5:
        motors.stop()
        leds.setAll(255, 255, 255)  # White color for neutral state

def calm_callback(data):
    global last_calm_prob
    last_calm_prob = data['probability']
    
    if last_calm_prob > 0.5 and last_focus_prob <= 0.5:
        # Move the robot backward
        motors.move_backward()
        leds.setAll(0, 255, 0)  # Green color for calm movement
        sounds.playTune(TUNES.DOWN)
    elif last_focus_prob > 0.5 and last_calm_prob > 0.5:
        motors.stop()
        leds.setAll(255, 255, 255)  # White color for neutral state

unsubscribe_focus = neurosity.focus(focus_callback)
unsubscribe_calm = neurosity.calm(calm_callback)
