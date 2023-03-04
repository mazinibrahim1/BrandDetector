
import cv2
import numpy as np
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import time
# Create an instance of window
def video(filepath):
   cap = cv2.VideoCapture(filepath)
# Check if camera opened successfully
   if (cap.isOpened() == False):
        print("Error opening video stream or file")
# Read until video is completed
   while (cap.isOpened()):
    
    # Capture frame-by-frame
        ret, frame = cap.read()
        if ret == True:
        # Display the resulting frame
            cv2.imshow('Frame', frame)
        # Press Q on keyboard to  exit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
    # Break the loop
        else:
            break
# When everything done, release the video capture object
   cap.release()
# Closes all the frames
   cv2.destroyAllWindows()
def end1():
    root = Toplevel()
    root.geometry("700x300")
    video(r"C:\Users\mazin\OneDrive\Desktop\brand\videoplayback.mp4")
    Label(root, text="unlabelled logos press open", font='Arial 16 bold').pack(pady=15)
    button = Button(root, text="O", command=img)
    button.pack()


def img():
    im = cv2.imread(r"C:\Users\mazin\OneDrive\Documents\wallpaper\876589.jpg", cv2.IMREAD_ANYCOLOR | cv2.IMREAD_ANYDEPTH)
    cv2.imshow("Sheep", im)
    entry= Entry(win, width= 40)
    entry.focus_set()
    entry.pack()
    string=entry.get()



def backend(filepath):
    video(filepath)
    time.sleep(2)
    while True:
    #This is to check whether to break the first loop
        isclosed=0
        cap = cv2.VideoCapture(r"C:\Users\mazin\OneDrive\Desktop\brand\loading.mp4")
        while (True):
            ret, frame = cap.read()
        # It should only show the frame when the ret is true
            if ret == True:
                cv2.imshow('frame',frame)
                if cv2.waitKey(1) == 27:
                # When esc is pressed isclosed is 1
                    isclosed=1
                    break
            else:
                break
    # To break the loop if it is closed manually
        if isclosed:
            break
    cap.release()
    cv2.destroyAllWindows()
win=Tk()
# # Set the geometry of the window
win.geometry("700x300")

# # Create a label
# Label(win, text="Click the button to open a dialog", font='Arial 16 bold').pack(pady=15)

# Function to open a file in the system
def open_file():
   filepath = filedialog.askopenfilename(title="Open a Text File", filetypes=(("mp4    files","*.mp4"), ("all files","*.*")))
   backend(filepath)

# Create a button to trigger the dialog
# button = Button(win, text="Open", command=open_file)
# button.pack()
open_file()
win.title('ml')

win.grid()
end1()
# progressbar

win.mainloop()