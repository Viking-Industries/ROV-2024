import pygame, tkinter as tk
from joystick import motorvalues, verticalmotors
from PIL import ImageTk, Image
import pyautogui
import pyfirmata
pygame.init()
pygame.joystick.init()

board=pyfirmata.Arduino('COM5')

stick = pygame.joystick.Joystick(0)
stick.init()
camnum = 1

def update_numbers():
    global motors, camnum
    pygame.event.get()
    motors = motorvalues(stick)
    motor1.set(motors[0])
    motor2.set(motors[1])
    motor3.set(motors[2])
    motor4.set(motors[3])

    vmotors = verticalmotors(stick)
    umotor1.set(vmotors[0])
    umotor2.set(vmotors[1])
    umotor3.set(vmotors[2])
    umotor4.set(vmotors[3])

    if stick.get_button(8) == 1 and camnum == 1:
        camnum = 2
        pyautogui.press('right')
    elif stick.get_button(8) == 1 and camnum == 2:
        camnum = 1
        pyautogui.press('left')

    root.after(100, update_numbers)  # Update every second (1000 milliseconds)
    
def update_images():
    if motor1.get() == 0:
        paneltr.configure(image=arrowc)
    elif motor1.get() > 0:
        paneltr.configure(image=arrowtr)
    elif motor1.get() < 0:
        paneltr.configure(image=arrowbl)    

    if motor2.get() == 0:
        paneltl.configure(image=arrowc)
    elif motor2.get() > 0:
        paneltl.configure(image=arrowtl)
    elif motor2.get() < 0:
        paneltl.configure(image=arrowbr) 

    if motor3.get() == 0:
        panelbr.configure(image=arrowc)
    elif motor3.get() > 0:
        panelbr.configure(image=arrowbr)
    elif motor3.get() < 0:
        panelbr.configure(image=arrowtl)   

    if motor4.get() == 0:
        panelbl.configure(image=arrowc)
    elif motor4.get() > 0:
        panelbl.configure(image=arrowbl)
    elif motor4.get() < 0:
        panelbl.configure(image=arrowtr) 

    if umotor1.get() == 0:
        panelu1.configure(image=arrowc)
    elif umotor1.get() > 0:
        panelu1.configure(image=arrowup)
    elif umotor1.get() < 0:
        panelu1.configure(image=arrowdown)

    if umotor2.get() == 0:
        panelu2.configure(image=arrowc)
    elif umotor2.get() > 0:
        panelu2.configure(image=arrowup)
    elif umotor2.get() < 0:
        panelu2.configure(image=arrowdown)

    if umotor3.get() == 0:
        panelu3.configure(image=arrowc)
    elif umotor3.get() > 0:
        panelu3.configure(image=arrowup)
    elif umotor3.get() < 0:
        panelu3.configure(image=arrowdown)

    if umotor4.get() == 0:
        panelu4.configure(image=arrowc)
    elif umotor4.get() > 0:
        panelu4.configure(image=arrowup)
    elif umotor4.get() < 0:
        panelu4.configure(image=arrowdown)



    root.after(100, update_images)    


pin1 = board.get_pin('d:2:s')
pin2 = board.get_pin('d:3:s')
pin3 = board.get_pin('d:4:s')
pin4 = board.get_pin('d:5:s')
pin5 = board.get_pin('d:6:s')
pin6 = board.get_pin('d:7:s')
pin7 = board.get_pin('d:8:s')
pin8 = board.get_pin('d:9:s')

def motors_update():
    pin1.write(90 + motor1.get())
    pin2.write(90 + -motor2.get())
    pin3.write(90 + motor3.get())
    pin4.write(90 + -motor4.get())
    pin5.write(90 + umotor1.get())
    pin6.write(90 + umotor2.get())
    pin7.write(90 + umotor3.get())
    pin8.write(90 + umotor4.get())
    root.after(100, motors_update)

# Create the main window

root = tk.Tk()
root.title("Motor Numbers")
arrowc = ImageTk.PhotoImage(Image.open("UI/center.png"))
arrowup = ImageTk.PhotoImage(Image.open("UI/up.png"))
arrowdown = ImageTk.PhotoImage(Image.open("UI/down.png"))
arrowtl = ImageTk.PhotoImage(Image.open("UI/topleft.png"))
arrowtr = ImageTk.PhotoImage(Image.open("UI/topright.png"))
arrowbl = ImageTk.PhotoImage(Image.open("UI/bottomleft.png"))
arrowbr = ImageTk.PhotoImage(Image.open("UI/bottomright.png"))
# Variables to store the numbers
motor1 = tk.IntVar()
motor2 = tk.IntVar()
motor3 = tk.IntVar()
motor4 = tk.IntVar()

umotor1 = tk.IntVar()
umotor2 = tk.IntVar()
umotor3 = tk.IntVar()
umotor4 = tk.IntVar()


# Initial update of numbers
update_numbers()

# Create labels to display the numbers
label1 = tk.Label(root, textvariable=motor1, font=('Arial', 24), padx=20, pady=20)
label2 = tk.Label(root, textvariable=motor2, font=('Arial', 24), padx=20, pady=20)
label3 = tk.Label(root, textvariable=motor3, font=('Arial', 24), padx=20, pady=20)
label4 = tk.Label(root, textvariable=motor4, font=('Arial', 24), padx=20, pady=20)

vlabel1 = tk.Label(root, textvariable=umotor1, font=('Arial', 24), padx=20, pady=20)
vlabel2 = tk.Label(root, textvariable=umotor2, font=('Arial', 24), padx=20, pady=20)
vlabel3 = tk.Label(root, textvariable=umotor3, font=('Arial', 24), padx=20, pady=20)
vlabel4 = tk.Label(root, textvariable=umotor4, font=('Arial', 24), padx=20, pady=20)

# Grid layout for labels
label1.grid(row=0, column=1)
label2.grid(row=0, column=2)
label3.grid(row=1, column=1)
label4.grid(row=1, column=2)
vlabel1.grid(row=3, column=1)
vlabel2.grid(row=3, column=2)
vlabel3.grid(row=4, column=1)
vlabel4.grid(row=4, column=2)

# 
labelsensor = tk.Label(root, text="Water Sensor Status: Safe", font=('Arial', 24), bg="green", padx=20, pady=20)
labelsensor.grid(row=2, column=0, columnspan=4)

paneltl = tk.Label(root, image= arrowc)
paneltl.grid(row=0, column=3)

paneltr = tk.Label(root, image = arrowtr)
paneltr.grid(row=0, column=0)

panelbl = tk.Label(root, image = arrowbl)
panelbl.grid(row=1, column=3)

panelbr = tk.Label(root, image = arrowbr)
panelbr.grid(row=1, column=0)

panelu1 = tk.Label(root, image= arrowc)
panelu1.grid(row=3, column=0)

panelu2 = tk.Label(root, image= arrowc)
panelu2.grid(row=3, column=3)

panelu3 = tk.Label(root, image= arrowc)
panelu3.grid(row=4, column=0)

panelu4 = tk.Label(root, image= arrowc)
panelu4.grid(row=4, column=3)

update_images()

motors_update()
# Start the GUI main loop
root.mainloop()
