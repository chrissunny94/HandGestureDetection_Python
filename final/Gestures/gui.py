from Tkinter import *

root = Tk()
root.resizable(width=FALSE, height=FALSE)
root.geometry('{}x{}'.format(500, 100))
root.wm_title("Project Xestos")
frame = Frame(root)
frame.pack()

bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )

def callback():
    execfile("/home/hoshank/Downloads/ppl/xestos/final/Gestures/color/hand_gesture.py")
def haar():
    execfile("/home/hoshank/Downloads/ppl/xestos/final/Gestures/Haar/hand_detect.py")

def finger():
    execfile("/home/hoshank/Downloads/ppl/xestos/final/finger gesture detection/gesture.py")

fingerdetect = Button(frame, text="Open Finger Detect", fg="red",command=finger)
fingerdetect.pack( side = LEFT)

color = Button(frame, text="Open Color Detect", fg="brown",command=callback)
color.pack( side = LEFT )

haar = Button(frame, text="Open Haar ", fg="blue",command=haar)
haar.pack( side = LEFT )

help = Button(bottomframe, text="Help", fg="black")
help.pack( side = BOTTOM)

root.mainloop()