import pygame, tkinter as Tk

pygame.init()
pygame.joystick.init()


stick = pygame.joystick.Joystick(0)
stick.init()


from joystick import motorvalues
def main():
     root = Tk()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    motors = motorvalues(stick)

    print(motors[0], motors[1])
    print(motors[2], motors[3])






# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = True

#     motors = motorvalues(stick)

#     print(motors[0], motors[1])
#     print(motors[2], motors[3])