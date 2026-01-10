# ---importint stuff---
# make traveled distance smaller if nessecary
from pybricks.hubs import PrimeHub
from pybricks.parameters import Port, Direction, Stop
from pybricks.pupdevices import UltrasonicSensor, Motor
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# --- GLOBAL INITIALIZATION ---

DRIVE_FAST_SPEED_CM_PER_SEC = 30
DRIVE_APPROACH_SPEED_CM_PER_SEC = 8
DRIVE_MISSION_SPEED_CM_PER_SEC = 15
ARM_SPEED = 70


# BUILDING 8
# Robot stops when it gets closer than 6 cm.
BUILDING8_DISTANCE_THRESHOLD_CM = 6
BUILDING8_INITIAL_DISTANCE_CM = 30

def create_robot_once():
    hub = PrimeHub()
   
    distance_sensor = UltrasonicSensor(Port.B)

    left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
    right_motor = Motor(Port.E)

    # ORIGINAL ARM MOTOR
    arm_motor_1 = Motor(Port.D, Direction.CLOCKWISE, [[28, 36], [12, 20]])
    arm_motor_1.brake()

    # NEW SECOND ARM MOTOR
    arm_motor_2 = Motor(Port.C, Direction.COUNTERCLOCKWISE, [28, 36]) # Assuming Port C and a different direction/gearing
    arm_motor_2.brake()

    drive_base = DriveBase(
        left_motor, right_motor, wheel_diameter=88, axle_track=142)
    drive_base.settings(
        straight_speed=DRIVE_FAST_SPEED_CM_PER_SEC*10)
    drive_base.use_gyro(True)
   
    # CHANGED: Return both arm motors
    return drive_base, arm_motor_1, arm_motor_2, distance_sensor

   

# --- TOP-LEVEL FUNCTIONS ---

# CHANGED: Renamed function parameter for clarity
def initialize_distance_sensor(distance_sensor):
    """Initializes sensors. Distance sensor does not require baseline readings."""
    # This function uses the argument 'distance_sensor'
    print("Distance Sensor Initialized.")
    # Distance sensor does not require a complex initial reading.
    return None


def complete_cleanup():
    """Completes final missing tasks."""
    print("Mission complete. Cleaning up.")
    wait(1000)

# The following functions now rely on the global variables set below.
def set_position():
    arm_motor_1.run_angle(50, 164)
    arm_motor_2.run_angle(50, 45)
    drive_base.straight(40)
    drive_base.turn(-45)

def move_forward_until_collision():
    drive_base.straight(300)
    arm_motor_2.run_angle(50, -45)
    drive_base.straight(210)

def do_mission():
    # Changed: Using ARM_SPEED constant, though the original was using 10.
    # Sticking to the original '10' since ARM_SPEED is 70.
    arm_motor_2.run_angle(50, 50)
    arm_motor_1.run_angle(200, -160)
    arm_motor_2.run_angle(50, -60)
    arm_motor_1.run_angle(50, 160)
    drive_base.straight(-140)
    drive_base.straight(70)
    drive_base.turn(45)
    drive_base.straight(-100)
    drive_base.turn(-90)


def return_to_base():
    drive_base.straight(-600)


# FIX 1: Only call create_robot_once() once to avoid OSError: EBUSY
drive_base, arm_motor_1, arm_motor_2, distance_sensor = create_robot_once()

# REMOVED: Redundant and error-causing call to create_robot_once()
#create_robot_once()

# FIX 2: Call initialize_distance_sensor() with the required argument
initialize_distance_sensor(distance_sensor)

complete_cleanup()

set_position()

move_forward_until_collision()

do_mission()

return_to_base()