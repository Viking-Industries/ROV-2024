import math
deadzone = 0.1

motor1 = 0
motor2 = 0
motor3 = 0
motor4 = 0
motormax = 65

strength = 0
direction = None

# Create a function "motorvalues" that returns the correct motor values for each movement direction.

def motorvalues(controller):
    # set up variables
    global motor1, motor2, motor3, motor4
    # x and y are obtained from the controller's horizontal and vertical axis position
    # twist is the axis when you twist the joystick
    x = controller.get_axis(0)
    y = controller.get_axis(1) * -1
    twist = controller.get_axis(2)

    # only runs if the throttle button is pressed
    # Sometimes if the joystick isn't moving it might give a ~0.1 value on the x/y axis, this fixes it.
    
    if controller.get_button(0) == 1:
        if abs(x) < deadzone:
            x = 0
        if abs(y) < deadzone:
            y = 0
        if abs(twist) < deadzone:
            twist = 0
        
        # this determines the direction of the joystick depending on x and y values
        if y > 0 and -0.25 < x < 0.25:
            direction = "fd"
        elif y < 0 and -0.25 < x < 0.25:
            direction = "bw"
        elif -0.25 < y < 0.25 and x < 0:
            direction = "l"
        elif -0.25 < y < 0.25 and x > 0:
            direction = "r"
        elif y > 0.25 and x < -0.25:
            direction = "fl"
        elif y > 0.25 and x > 0.25:
            direction = "fr"
        elif y < -0.25 and x < -0.25:
            direction = "bl"
        elif y < -0.25 and x > 0.25:
            direction = "br"
        else:
            direction = None

        # the strength multiplier is determined by taking how far you push the joystick (value between 0 and 1)
        if direction == "fd" or direction == "bw":
            strength = abs(y)
        elif direction == "l" or direction == "r":
            strength = abs(x)
        else: 
            # slightly different for diagonals, because the joystick doesn't have a circular bounding area but a square
            # a little bit of Pythagorean theorem 
            strength = math.sqrt(x**2 + y**2) * (1/math.sqrt(2))
        
        if strength > 1.0:
            strength = 1.0

        # based on the direction and strength, the correct configuration for the motors is determined
        # this outputs a number from -65 to 65 for each horizontal motor in the vectored thrust orientation
        if direction == "fd":
            motor1 = int(motormax * strength)
            motor2 = int(motormax * strength)
            motor3 = -int(motormax * strength)
            motor4 = -int(motormax * strength)
        elif direction == "bw":
            motor1 = -int(motormax * strength)
            motor2 = -int(motormax * strength)
            motor3 = int(motormax * strength)
            motor4 = int(motormax * strength)
        elif direction == "l":
            motor1 = -int(motormax * strength)
            motor2 = int(motormax * strength)
            motor3 = -int(motormax * strength)
            motor4 = int(motormax * strength)
        elif direction == "r":
            motor1 = int(motormax * strength)
            motor2 = -int(motormax * strength)
            motor3 = int(motormax * strength)
            motor4 = -int(motormax * strength)
        elif direction == "fl":
            motor1 = 0
            motor2 = int(motormax * strength)
            motor3 = -int(motormax * strength)
            motor4 = 0
        elif direction == "fr":
            motor1 = int(motormax * strength)
            motor2 = 0
            motor3 = 0
            motor4 = -int(motormax * strength)
        elif direction == "bl":
            motor1 = -int(motormax * strength)
            motor2 = 0
            motor3 = 0
            motor4 = int(motormax * strength)
        elif direction == "br":
            motor1 = 0
            motor2 = -int(motormax * strength)
            motor3 = int(motormax * strength)
            motor4 = 0
        elif twist < 0 and direction == None:
            motor1 = -int(motormax * abs(twist))
            motor2 = int(motormax * abs(twist))
            motor3 = int(motormax * abs(twist))
            motor4 = -int(motormax * abs(twist))
        elif twist > 0 and direction == None:
            motor1 = int(motormax * abs(twist))
            motor2 = -int(motormax * abs(twist))
            motor3 = -int(motormax * abs(twist))
            motor4 = int(motormax * abs(twist))
        else:
            motor1 = motor2 = motor3 = motor4 = 0
    else:
        motor1 = motor2 = motor3 = motor4 = 0

    return motor1, motor2, motor3, motor4

u1 = 0
u2 = 0
u3 = 0
u4 = 0

# creates a function "verticalmotors" to return the values for the vertical thrusters based on three buttons
def verticalmotors(controller):
    global u1, u2, u3, u4

    # this button resets the up motor values 
    if controller.get_button(1) == 1:
        u1 = 0
        u2 = 0
        u3 = 0
        u4 = 0
    # this button decreases the up motors by 2
    if controller.get_button(2) == 1:
        u1 -= 2
        u2 -= 2
        u3 -= 2
        u4 -= 2
    # this button increases the up motors by 2
    elif controller.get_button(4) == 1:
        u1 += 2
        u2 += 2
        u3 += 2
        u4 += 2

    # tilt buttons
    if controller.get_button(5) == 1:
        u1 += 2
        u2 += 2
        u3 -= 2
        u4 -= 2
    elif controller.get_button(3) == 1:
        u1 -= 2
        u2 -= 2
        u3 += 2
        u4 += 2

    # sets max. and min boundaries
    if u1 > 90:
        u1 = 90
    elif u1 < -90:
        u1 = -90

    if u2 > 90:
        u2 = 90
    elif u2 < -90:
        u2 = -90

    if u3 > 90:
        u3 = 90
    elif u3 < -90:
        u3 = -90

    if u4 > 90:
        u4 = 90
    elif u4 < -90:
        u4 = -90

    if u1 > 90:
        u1 = 90
    elif u1 < -90:
        u1 = -90

    return u1, u2, u3, u4 

