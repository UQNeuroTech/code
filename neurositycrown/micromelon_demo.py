from micromelon import *

rc = RoverController()

rc.connectBLE(83)
rc.startRover()

while True:
  cmd = input("Enter a command or 'quit' to exit: ")
  if cmd == "forwards":
    distance = input("How far forwards? ")
    Motors.moveDistance(int(distance))
  elif cmd == "backwards":
    distance = input("How far backwards? ")
    Motors.moveDistance(-int(distance))
  elif cmd == "left":
    angle = input("How far degrees? ")
    Motors.turnDegrees(-int(angle))
  elif cmd == "right":
    angle = input("How far degrees? ")
    Motors.turnDegrees(int(angle))
  elif cmd == "quit":
    break
  else:
    print("Unknown command: " + cmd)

rc.stopRover()
rc.end()
