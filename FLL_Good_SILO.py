from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from pybricks.tools import hub_menu

#Setup the hub and sensors
hub = PrimeHub()
left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.E)
drive_base = DriveBase(left_motor, right_motor, wheel_diameter=88, axle_track=128)
front_motor = Motor(Port.D)
back_motor = Motor(Port.C)
distance_sensor = UltrasonicSensor(Port.B)
right_color_sensor = ColorSensor(Port.F)

#missionsilo()
#Step 1
drive_base.straight(-350)
back_motor.run_angle(-800,300)
wait(100)
back_motor.run_angle(-800,-300)
wait(100)
back_motor.run_angle(-800,300)
wait(100)
back_motor.run_angle(-800,-300)
wait(100)
back_motor.run_angle(-800,300)
wait(100)
back_motor.run_angle(-800,-300)
wait(100)
#Step 2
wait(200)
drive_base.straight(300)
