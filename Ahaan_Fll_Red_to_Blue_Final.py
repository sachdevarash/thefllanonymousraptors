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

drive_base.use_gyro(True)

drive_base.reset(distance=0, angle=0)  # sets angle to 90°
# Move arm up
motor_B.run_angle(250,-180)
# Move to mission 1
# Step 1
drive_base.straight(270)
# Move arm down to remove sand
# Step 2
motor_B.run_angle(250,450)
# Move backwards
# Step 3
drive_base.straight(-100)
# Move arm up to mave out of the way
motor_B.run_angle(250,-180)

# Turn -90 Degrees
# Step 4
right_motor.run_angle(speed=250, rotation_angle=315)
# Move forward for alignment
# Step 5
drive_base.straight(10)

# Turn 90 degrees
# Step 6
left_motor.run_angle(speed=250, rotation_angle=315)

# Push red slidey thingy
# Step 7
drive_base.straight(200)
# Move arm up
motor_B.run_angle(250,-180)
 # Move backwards
 # Step 8
drive_base.straight(-150)
# Leave Mission 1

drive_base.turn(90)
# Move away from mission
drive_base.straight(-125)

# Turn to move to mission 2
# Step 9
drive_base.turn(-90)
# Start moving to mission 2
# Step 10
drive_base.straight(450)
# turn to mission 2
# Step 11
drive_base.turn(-90)
# Move into mission 2
# Step 12
drive_base.straight(-275)
# Turn towards the gear in mission 2
drive_base.turn(-5)
# drive_base.turn(180)
# drive_base.straight(90)
# drive_base.turn(105)
# drive_base.straight(-210)
drive_base.turn(-5)
def run_motor_a(speed,angle):
    motor_A.run_angle(speed,0-angle*3.857)
# turn motor to turn gear
# Step 13
run_motor_a(500,-180)
drive_base.straight(-50)
# drive_base.turn(-20)
drive_base.straight(-50)
run_motor_a(500,650)


#  go home
# Step 14
drive_base.straight(70)
# Step 15
drive_base.turn(110)
# Step 16
drive_base.straight(850)





    





