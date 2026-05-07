from pybricks.hubs import EssentialHub
from pybricks.pupdevices import Motor, ColorSensor, ColorLightMatrix
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

from CSAI_Bridge import AIFeatures, Feature

ai = AIFeatures()
right_arm = Motor(Port.A, Direction.COUNTERCLOCKWISE)
left_arm = Motor(Port.B, Direction.CLOCKWISE)

SPEED = 800

right_arm.run_target(SPEED, 0, wait=False)
left_arm.run_target(SPEED, 0, wait=False)

while True:
    if not ai.update() or not ai.getPerson():
        continue


    #x, y = ai.getCoords(Feature.NOSE)
    cls, conf = ai.getDetectedClass()
    n = ai.getNumClasses()
    scores = ai.getClassScore()

    if cls is 0: # both down
        right_arm.run_target(SPEED, 0, wait=False)
        left_arm.run_target(SPEED, 0, wait=False)
    elif cls is 2: # right up
        right_arm.run_target(SPEED, 170, wait=False)
        left_arm.run_target(SPEED, 0, wait=False)
    elif cls is 1: # left up
        right_arm.run_target(SPEED, 0, wait=False)
        left_arm.run_target(SPEED, 170, wait=False) 
    elif cls is 3: # both up
        right_arm.run_target(SPEED, 170, wait=False)
        left_arm.run_target(SPEED, 170, wait=False) 

    print(
        "class={} conf={} scores={} ".format(
            cls,
            conf,
            scores,
        ),
        end="\r"
    )