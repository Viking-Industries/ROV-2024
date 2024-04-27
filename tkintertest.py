import pygame, tkinter as tk
from joystick import motorvalues
pygame.init()
pygame.joystick.init()

stick = pygame.joystick.Joystick(0)
stick.init()

def update_numbers():
    pygame.event.get()
    motors = motorvalues(stick)
    motor1.set(motors[0])
    motor2.set(motors[1])
    motor3.set(motors[2])
    motor4.set(motors[3])

    root.after(100, update_numbers)  # Update every second (1000 milliseconds)

# Create the main window
root = tk.Tk()
root.title("Motor Numbers")

# Variables to store the numbers
motor1 = tk.IntVar()
motor2 = tk.IntVar()
motor3 = tk.IntVar()
motor4 = tk.IntVar()

# Initial update of numbers
update_numbers()

# Create labels to display the numbers
label1 = tk.Label(root, textvariable=motor1, font=('Arial', 24), padx=20, pady=20)
label2 = tk.Label(root, textvariable=motor2, font=('Arial', 24), padx=20, pady=20)
label3 = tk.Label(root, textvariable=motor3, font=('Arial', 24), padx=20, pady=20)
label4 = tk.Label(root, textvariable=motor4, font=('Arial', 24), padx=20, pady=20)

# Grid layout for labels
label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
label3.grid(row=1, column=0)
label4.grid(row=1, column=1)

# Start the GUI main loop
root.mainloop()
