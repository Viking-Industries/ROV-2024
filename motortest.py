import pyfirmata
from tkinter import *

def move_all(angle):
    pin1.write(angle)
    pin2.write(angle)
    pin3.write(angle)
    pin4.write(angle)
    pin5.write(angle)
    pin6.write(angle)
    pin7.write(angle)
    pin8.write(angle)
    
def move_one(angle):
    pin1.write(angle)

def move_two(angle):
    pin2.write(angle)

def move_three(angle):
    pin3.write(angle)

def move_four(angle):
    pin4.write(angle)

def move_five(angle):
    pin5.write(angle)

def move_six(angle):
    pin6.write(angle)

def move_seven(angle):
    pin7.write(angle)

def move_eight(angle):
    pin8.write(angle)
    
def move_up(angle):
    pin5.write(angle)
    pin6.write(angle)
    pin7.write(angle)
    pin8.write(angle)


def main():
    global pin1, pin2, pin3, pin4, pin5, pin6, pin7, pin8
    
    board=pyfirmata.Arduino('COM5')

    iter8 = pyfirmata.util.Iterator(board)
    iter8.start()

    pin1 = board.get_pin('d:2:s')
    pin2 = board.get_pin('d:3:s')
    pin3 = board.get_pin('d:4:s')
    pin4 = board.get_pin('d:5:s')
    
    pin5 = board.get_pin('d:6:s')
    pin6 = board.get_pin('d:7:s')
    pin7 = board.get_pin('d:8:s')
    pin8 = board.get_pin('d:9:s')

    root = Tk()
    all = Scale(root, command = move_all, to = 175, 
                  orient = HORIZONTAL, length = 400, label = 'All motors')
    all.pack(anchor = CENTER)

    one = Scale(root, command = move_one, to = 175, 
                  orient = HORIZONTAL, length = 400, label = 'Motor1')
    one.pack(anchor = CENTER)

    two = Scale(root, command = move_two, to = 175, 
                  orient = HORIZONTAL, length = 400, label = 'Motor2')
    two.pack(anchor = CENTER)

    three = Scale(root, command = move_three, to = 175, 
                  orient = HORIZONTAL, length = 400, label = 'Motor3')
    three.pack(anchor = CENTER)

    four = Scale(root, command = move_four, to = 175, 
                  orient = HORIZONTAL, length = 400, label = 'Motor4')
    four.pack(anchor = CENTER)

    five = Scale(root, command = move_five, to = 175, 
                  orient = HORIZONTAL, length = 400, label = 'Motor5')
    five.pack(anchor = CENTER)

    six = Scale(root, command = move_six, to = 175, 
                  orient = HORIZONTAL, length = 400, label = 'Motor6')
    six.pack(anchor = CENTER)

    seven = Scale(root, command = move_seven, to = 175, 
                  orient = HORIZONTAL, length = 400, label = 'Motor7')
    seven.pack(anchor = CENTER)

    eight = Scale(root, command = move_eight, to = 175, 
                  orient = HORIZONTAL, length = 400, label = 'Motor8')
    eight.pack(anchor = CENTER)

    up = Scale(root, command = move_up, to = 175, 
                  orient = HORIZONTAL, length = 400, label = 'Up Motors')
    up.pack(anchor = CENTER)

    

    root.mainloop()

main()
