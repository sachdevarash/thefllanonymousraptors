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


drive_base.straight(700)
drive_base.turn(90)
drive_base.straight(15)
drive_base.settings(turn_rate=100)
drive_base.turn(90)
drive_base.turn(-180)
drive_base.turn(90)
drive_base.settings(turn_rate=250)
drive_base.straight(-70)
drive_base.turn(45)
drive_base.straight(45)
drive_base.turn(-25)
drive_base.straight(-80)
drive_base.straight(160)
motor_d.run_angle(1000,200)
drive_base.straight(-60)
drive_base.turn(-93)
motor_d.run_angle(1000,-200)
drive_base.straight(90)
drive_base.turn(230)
drive_base.straight(-65)
motor_c.run_angle(300,-240)
drive_base.straight(-145)
motor_c.run_angle(1000,970)
drive_base.turn(80)
motor_c.run_angle(1000,-490)
drive_base.turn(-100)
drive_base.turn(70)
motor_c.run_angle(1000,970)
drive_base.straight(110)
drive_base.turn(-110)
drive_base.straight(750)