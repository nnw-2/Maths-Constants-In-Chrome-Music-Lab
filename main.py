#Only intended to work by using the music lab settings Length : 10 bars , Beats per bar : 7 , Beats split into : 4 , Range : 3 octave.
#How many boxes to work with - height : 23    width : 280
from pynput.keyboard import Key , Controller
import sys
keyboard = Controller()

constant = input("e i pi or ratio?")

#start keyboard input unpon s key being pressed
while 1:
    if keyboard.pressed("s"):
        break

#checks for s key press to end program
while 1:
    if keyboard.pressed("s"):
        sys.exit()
    