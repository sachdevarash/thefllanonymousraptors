#april 19





# Rohin's bot only (Nolan's bot code is on the github)
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

drive_base.use_gyro(True)
#navigate to 'who lived there'
drive_base.settings(straight_speed=300) #navigate slow to the mission
drive_base.settings(turn_rate=100)
# Step 1
drive_base.straight(70)
#Step2
drive_base.turn(-90)
# Step 3
drive_base.straight(250) #Prapti 235
# Step 4
drive_base.turn(90)
# Step 5
drive_base.straight(325)
front_motor.run_angle(200,200)
drive_base.straight(360) 


# Disable gyro for the actual missions
drive_base.use_gyro(False)


#Execute the 'who lived there' mission
drive_base.settings(turn_rate=300)
#step6
drive_base.turn(-50)

#Navigate to Forge next
#Step7
drive_base.straight(-95) 
#Step 8
drive_base.turn(90)
#Execute the forge mission
wait(100)
#Step9
drive_base.straight(17) #17 on nolan's bot. before Prapti changed it 38
wait(100)
# Step 10
drive_base.settings(turn_rate=55)#50


drive_base.turn(-80) 
wait(100)
drive_base.turn(35) #Prapti 30 last thing


#Execute Heavy lift
front_motor.run_angle(200,-250) #200= second number
wait(600) #wait for arm to settle
drive_base.settings(turn_rate=500)
#Step 11
drive_base.turn(50)
wait(100)

#return to base
front_motor.run_angle(200,150)
drive_base.turn(20)#20
drive_base.settings(turn_rate=300)
#Step 12
drive_base.straight(200)
wait(100)
#Step 13
drive_base.straight(-325)
#Step 14
drive_base.turn(80)
#Step 15
drive_base.straight(550)
