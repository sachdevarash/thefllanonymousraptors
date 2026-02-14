from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

hub = PrimeHub()
left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.E)
drive_base = DriveBase(left_motor, right_motor, wheel_diameter=88, axle_track=128)
front_motor = Motor(Port.D)
back_motor = Motor(Port.C)
distance_sensor = UltrasonicSensor(Port.B)
right_color_sensor = ColorSensor(Port.F)
use_gyro=True
##
##smashing the silo function
##
def silo():
    back_motor.run_angle(-300,100)
    wait(100)
    back_motor.run_angle(-300,-100)
    wait(100)
    back_motor.run_angle(-500,100)
    wait(100)
    back_motor.run_angle(-300,-100)
    wait(100)
    back_motor.run_angle(-500,100)
    wait(100)
    back_motor.run_angle(-500,-100)
    wait(100)
    back_motor.run_angle(-500,100)
    wait(100)
    back_motor.run_angle(-500,-100)
    wait(100)
    back_motor.run_angle(-500,100)
    wait(100)
    back_motor.run_angle(-500,-100)

drive_base.straight(750)#750 before
####
#silo()
#front_motor.run_angle(200,90)

#Getting to forge and etc
# drive_base.turn(100)
#drive_base.straight(120) #110
# drive_base.turn(100)
#drive_base.straight(360) #370 before
#solving etc

#hit the who lived there
drive_base.turn(-50)

#back out of there and get to neutral position
drive_base.straight(-80)#-50
drive_base.turn(30)

#move forward and hit forge
drive_base.turn(90)
wait(100)
drive_base.straight(30)#20
wait(100)
drive_base.turn(-75) 
wait(100)
drive_base.turn(15) #prev 20
wait(100)
front_motor.run_angle(200,-200)
wait(100)
drive_base.straight(15)
wait(100)
drive_base.turn(70)
wait(100)
front_motor.run_angle(200,200)
wait(100)

#second shot at forge
drive_base.turn(-175)

#come back to base
wait(100)
drive_base.turn(-90)
drive_base.straight(300)
