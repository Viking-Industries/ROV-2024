import math
import pygame, tkinter as tk
import cv2
from PIL import Image, ImageTk

pygame.init()
pygame.joystick.init()


controller = pygame.joystick.Joystick(0)
controller.init()

deadzone = 0.1

motor1 = 0
motor2 = 0
motor3 = 0
motor4 = 0
motormax = 90

strength = 0
direction = None

while True:
    x = controller.get_axis(0)
    y = controller.get_axis(1) * -1
    twist = controller.get_axis(2)

    if abs(x) < deadzone:
        x = 0
    if abs(y) < deadzone:
        y = 0
    if abs(twist) < deadzone:
        twist = 0

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

    if direction == "fd" or direction == "bw":
        strength = abs(y)
    elif direction == "l" or direction == "r":
        strength = abs(x)
    else: 
        strength = math.sqrt(x**2 + y**2) * (1/math.sqrt(2))

    if strength > 1.0:
        strength = 1.0

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

    print(motor1, motor2, motor3, motor4)    