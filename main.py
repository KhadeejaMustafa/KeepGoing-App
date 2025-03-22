
import pyautogui # used to monitor mouse activity.
import tkinter # package to create pop up window
import time
from PIL import Image, ImageTk # Python Imaging Library or Pillow. Used for opening and displaying images.
import keyboard # to handle termination of program through escape key

def show_motivation():
    root = tkinter.Tk() # used to initialize the main window
    root.title("Keep Going!")

    # creating a background image for the canvas
    bg_image = Image.open("bg_pattern.jpg")
    bg_image = bg_image.resize((750, 770))
    background_img = ImageTk.PhotoImage(bg_image)

    # creates Canvas
    canvas = tkinter.Canvas(root, width= 750, height= 770, highlightbackground = '#ffffe6', highlightthickness= 4)
    canvas.pack()
    # adding the background image
    canvas.create_image(0, 0, image = background_img, anchor= tkinter.NW)
    
 
    Img = Image.open("cameraimg.jpg")
    Img = Img.resize((395,395))
    motivation_img = ImageTk.PhotoImage(Img)

    canvas.create_image(375,385, image=motivation_img, anchor = 'center')

    canvas.create_text(370, 70, text= "Just a reminder. You were doing this to buy a new DSLR Camera, So keep going!", font=("Georgia", 18, "bold"), justify= 'center', fill='#60401f', width= 710)

    root.mainloop() # Runs the Tkinter event loop, which waits for user interaction.

# Creating a function that will look for mouse inactivity 

def mouse_inactivity():
    last_position = pyautogui.position() # Gets the current position of the mouse.
    inactivity_limit = 5 # seconds

    while True:

        if keyboard.is_pressed("esc"):
            print("Exiting the program..")
            break

        time.sleep(1) # will pause the script for one second before checking the mouse position again
        current_position = pyautogui.position() # Gets the current position of the mouse.
        if last_position == current_position: # if these mouse position has not changed, then turn the inactivity_limit into a value smaller than zero
            inactivity_limit -= 1
            if inactivity_limit == 0:
             show_motivation()
             inactivity_limit = 5
        else: 
            last_position = current_position
            inactivity_limit = 5

mouse_inactivity()
