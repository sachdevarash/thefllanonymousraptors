from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, multitask, run_task

hub = PrimeHub()




right_motor = Motor(Port.E, Direction.CLOCKWISE)
left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
drive_base = DriveBase(left_motor, right_motor, wheel_diameter=88, axle_track=128)
motor_A = Motor(Port.C, Direction.CLOCKWISE)
motor_B = Motor(Port.D, Direction.COUNTERCLOCKWISE)

motor_A.reset_angle(0) # reset angle to 0
motor_B.reset_angle(0) # reset angle to 0



# Threshold for detecting the line (adjust based on environment)
THRESHOLD = 10  # Reflectivity value. Tune this!


drive_base.reset(distance=0, angle=0)  # sets angle to 90°
# step 1
motor_B.run_angle(250,-180)
print("1")
# step 2
drive_base.straight(270)
print("2")
# step 3
motor_B.run_angle(250,450)
print("3")
# step 4
drive_base.straight(-100)
print("4")
# step 5
drive_base.turn(-90)
print("5")
# step 6
drive_base.straight(200)
print("6")
# step 7
motor_B.run_angle(250,-180)
print("7")
# step 8
drive_base.turn(90)
print("8")
# step 9
drive_base.straight(300)
print("9")
# step 10
drive_base.straight(-100)
print("10")
# # step 11
drive_base.turn(-90)
print("11")
# # step 12
drive_base.straight(55)
print("12")
# # step 13
drive_base.turn(80)
print("13")
# # step 14
drive_base.straight(257)
print("14")
# # step 15
drive_base.turn(5)
print("15")
# # step 16
drive_base.turn(200)
print("16")
# # heh heh heh
# # step 18
drive_base.straight(-90)
print("18")
# # step 19
drive_base.turn(100)
print("19")
# # step 20
drive_base.straight(-250)
print("20")
drive_base.turn(-0)
# step 22
def run_motor_a(speed,angle):
    motor_A.run_angle(speed,0-angle*3.857)
print("22")
# step 23
run_motor_a(500,180)
drive_base.straight(-50)
drive_base.turn(-45)
run_motor_a(500,720)
print("23")

#  go home
drive_base.straight(70)
drive_base.turn(120)
drive_base.straight(850)





    





