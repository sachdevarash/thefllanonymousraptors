#Author: Nolan
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase
from pybricks.hubs import PrimeHub

#line up at last black line
#crunches are ok
#driving on the mission is :):):):):):):)
#mjolnir up
#middle finger down ;p
#scream

motor_d = Motor(Port.D)
motor_c = Motor(Port.C)

right_motor = Motor(Port.A,Direction.COUNTERCLOCKWISE)
left_motor = Motor(Port.E)

wheel_diameter = 88
axle_track = 130
drive_base = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)


# 1 straight to surface brushing
drive_base.straight(700)
# 2 turn left to face surface brushing
drive_base.turn(90)
# 3 forward to surface brushing
drive_base.straight(15)
drive_base.settings(turn_rate=100)
# 4 turn left and knock down dirt cover
drive_base.turn(90)
# 5 turn right and knock down other dirt cover
drive_base.turn(-180)
# 6turn left to original position
drive_base.turn(90)
drive_base.settings(turn_rate=250)
# 7 back up
drive_base.straight(-70)
# 8 aligns for brush
drive_base.turn(45)
# 9 goes forward for no reason hah
drive_base.straight(47)
# 10 align more
drive_base.turn(-25)
# 11 back up 
drive_base.straight(-80)
# 12 go forward to brush
drive_base.straight(160)
# 13 pick up brush
motor_d.run_angle(500,200)
# 14 back up with brush
drive_base.straight(-60)
# 15 turn to face map reveal
drive_base.turn(-93)
# 16 arm down slightly
motor_d.run_angle(500,-50)
# 17 go to first map cover
drive_base.straight(85)
# 18 yeet first map cover
drive_base.turn(230)
# 19 back up to second map cover
drive_base.straight(-65)
# 20 hammer down
motor_c.run_angle(300,-240)
# 21 pusssh
drive_base.straight(-145)
# 22 lift arm
motor_c.run_angle(1000,910)
# 23 align with final map cover
drive_base.turn(90)
# 24 arm down
motor_c.run_angle(500,-410)
# 25 move final map cover
drive_base.turn(-90)
# 26 arm up
motor_c.run_angle(1000,910)
# 27 turn to final step 
drive_base.turn(80)
# 28 go off map reveal
drive_base.straight(110)
# 29 turn and align with base
drive_base.turn(-140)
# 30 go to base
drive_base.straight(700)
# 31 turn to fit in base
drive_base.turn(-90)
# 32 drop brush
motor_d.run_angle(1000,-150)
