import tkinter as tk
from pyfirmata import Arduino, util
import time

# Define the board port (e.g., '/dev/ttyUSB0' on Linux or 'COM3' on Windows)
port = 'COM5'  # Change this to your port

# Initialize Arduino board
board = Arduino(port)

# Define pins for ULN2003 driver
in1_pin = board.get_pin('d:9:o')
in2_pin = board.get_pin('d:10:o')
in3_pin = board.get_pin('d:11:o')
in4_pin = board.get_pin('d:12:o')

# Define control sequences for the stepper motor
steps = [
    [1, 0, 0, 1],
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1]
]

# Function to rotate the motor
def step_motor(direction, delay):
    for step in range(8):
        for pin in range(4):
            board.digital[pin+2].write(steps[step][pin])
        time.sleep(delay)

# Create Tkinter GUI
def rotate_motor():
    direction = direction_var.get()
    delay = float(delay_entry.get())
    step_motor(direction, delay)

root = tk.Tk()
root.title("Stepper Motor Control")

# Direction selection
direction_label = tk.Label(root, text="Direction:")
direction_label.grid(row=0, column=0, padx=5, pady=5)
direction_var = tk.StringVar(value="cw")
direction_option_menu = tk.OptionMenu(root, direction_var, "cw", "ccw")
direction_option_menu.grid(row=0, column=1, padx=5, pady=5)

# Delay input
delay_label = tk.Label(root, text="Delay (s):")
delay_label.grid(row=1, column=0, padx=5, pady=5)
delay_entry = tk.Entry(root)
delay_entry.grid(row=1, column=1, padx=5, pady=5)

# Button to start motor rotation
rotate_button = tk.Button(root, text="Rotate Motor", command=rotate_motor)
rotate_button.grid(row=2, columnspan=2, padx=5, pady=5)

root.mainloop()