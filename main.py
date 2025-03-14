
import pyautogui # used to monitor mouse activity.
import tkinter # package to create pop up window
import time
from PIL import Image, ImageTk # Python Imaging Library or Pillow. Used for opening and displaying images.

def show_motivation():
    root = tkinter.Tk() # used to initialize the main window
    root.title("Keep Going!")
    canvas = tkinter.Canvas(root, width= 600, height= 400, bg= 'light blue', 
                            highlightbackground='rgb(0, 102, 204)', highlightthickness= 2)
    canvas.pack()

    Img = ImageTk.PhotoImage(Image.open("https://i.pinimg.com/736x/47/c7/92/47c79270a9a671ce17c0257f617c18d0.jpg"))
    canvas.create_image(200, 150, image = Img)

    canvas.create_text(200, 50, text= "Don't give up yet, remember you wanted to by a DSLR camera?", font=("Helvetica", 24))

    root.mainloop() # Runs the Tkinter event loop, which waits for user interaction.

# Creating a function that will look for mouse inactivity 

def mouse_inactivity():
    last_position = pyautogui.position() # Gets the current position of the mouse.
    inactivity_limit = 5 # seconds

    while true:
        time.sleep() # will pause the script for one second before checking the mouse position again
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
