from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.hubs import PrimeHub
from CSAI_Bridge import AIFeatures, Feature
from pybricks.tools import wait

rotation = Motor(Port.A)
jumping = Motor(Port.B)
hub = PrimeHub()

ai = AIFeatures()

was_up = False

rotation.dc(-20)

while True:
    if not ai.update():
        continue

    person = ai.getPerson()

    if person:
        x, y = ai.getCoords(Feature.NOSE)
        is_up = y > 0
    else:
        is_up = False

    if is_up and not was_up:
        hub.speaker.beep(1000, 50)
        jumping.run_angle(500, 30, wait=True)
        jumping.run_angle(-500, 30, wait=True)

    was_up = is_up