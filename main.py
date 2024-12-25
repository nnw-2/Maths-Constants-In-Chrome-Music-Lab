#Only intended to work by using the music lab settings Length : 10 bars , Beats per bar : 7 , Beats split into : 4 , Range : 3 octave.
#How many boxes to work with - height : 23    width : 280
import time
from pynput.keyboard import Key , Controller , Listener
import sys
import numpy as np
import random
keyboard = Controller()

constant = input("e i pi or ratio?")

#want to make 2 bar sections 2 chorus : 4 bars, 3 random : 6 bars. v1 c v2 c v3
verse1 = np.zeros(shape=(23,56) , dtype=int)
verse2 = np.zeros(shape=(23,56) , dtype=int)
verse3 = np.zeros(shape=(23,56) , dtype=int)
chorus = np.zeros(shape=(23,56) , dtype=int)

#the original shapes
#https://musiclab.chromeexperiments.com/Song-Maker/song/5547182859616256

e_shape = np.array([[0,1,1,1,0],
                    [1,0,0,0,1],
                    [1,1,1,1,0],
                    [1,0,0,0,0],
                    [0,1,1,1,1]]
                                )
e_shape2 = np.array([[0,0,1,1,1,1,1,1,0,0],
                    [0,0,1,1,1,1,1,1,0,0],
                    [1,1,0,0,0,0,0,0,1,1],
                    [1,1,0,0,0,0,0,0,1,1],
                    [1,1,1,1,1,1,1,1,0,0],
                    [1,1,1,1,1,1,1,1,0,0],
                    [1,1,0,0,0,0,0,0,0,0],
                    [1,1,0,0,0,0,0,0,0,0],
                    [0,0,1,1,1,1,1,1,1,1],
                    [0,0,1,1,1,1,1,1,1,1]]
                                )
i_shape = np.array([[1],
                    [0],
                    [1],
                    [1],
                    [1]]
                        )
i_shape2 = np.array([[1,1],
                    [1,1],
                    [0,0],
                    [1,1],
                    [1,1],
                    [1,1],
                    [1,1],
                    [1,1],
                    [1,1],
                    [1,1],
                    [1,1]]
                        )
pi_shape = np.array([[1,1,1,1,1,1,1,1],
                    [0,0,1,0,0,1,0,0],
                    [0,0,1,0,0,1,0,0],
                    [0,0,1,0,0,1,0,0],
                    [0,0,1,0,0,1,0,0],
                    [0,0,1,0,0,0,1,0]]
                                    )
pi_shape2 = np.array([[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0],
                    [0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0],
                    [0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0],
                    [0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0],
                    [0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0],
                    [0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0],
                    [0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0],
                    [0,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0],
                    [0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0],]
                                                        )
ratio = np.array([[0,0,0,0,0,1,1,0,0],
                [0,1,0,0,1,0,0,1,0],
                [1,0,0,0,1,0,0,0,1],
                [1,0,0,0,1,0,0,0,1],
                [1,0,0,0,1,0,0,0,1],
                [0,1,0,0,1,0,0,1,0],
                [0,0,1,1,1,1,1,0,0],
                [0,0,0,0,1,0,0,0,0],
                [0,0,0,0,1,0,0,0,0],
                [0,0,0,0,1,0,0,0,0],
                [0,0,0,0,1,0,0,0,0]]
                                    )
ratio2 = np.array([[0,0,0,1,0,0,0],
                [0,1,1,1,1,1,0],
                [1,0,0,1,0,0,1],
                [1,0,0,1,0,0,1],
                [1,0,0,1,0,0,1],
                [0,1,1,1,1,1,0],
                [0,0,0,1,0,0,0]]
                                )
match constant:
    case "e":
        pattern = {0: e_shape,
                    1: e_shape2,
                                2:np.array([])
                                }
        
    case "i":
        pattern = {0:i_shape,
                    1:i_shape2,
                                2:np.array([])
                                }
        
    case "pi":
        pattern = {0:pi_shape,
                    1:pi_shape2,
                                2:np.array([])
                                }
        
    case "ratio":
        pattern = {0:ratio,
                    1:ratio2,
                                2:np.array([])
                                }
        
    case _:
        sys.exit()

def on_press(key):
    if 'char' in dir(key):     #check if char method exists,
        if key.char == 's':
            listener.stop()
def check_press():
    global listener
    with Listener(on_press = on_press) as listener:
        listener.join()

def final_array(pattern):
    return np.append(adding_to_arrays(verse1  , pattern , random.randint(6,12)),np.append(adding_to_arrays(chorus , pattern , random.randint(6,12)),np.append(adding_to_arrays(verse2 , pattern , random.randint(6,12)),np.append(adding_to_arrays(chorus , pattern , random.randint(6,12)),adding_to_arrays(verse3 , pattern , random.randint(6,12)),axis=1),axis=1),axis=1),axis=1)


def adding_to_arrays(array, pattern, num_to_add):
        for _ in range(num_to_add):
            pat = pattern[random.randint(0,1)]
            starting_point = (random.randint(0, len(array) - 1), random.randint(0, len(array[0]) - 1))
            rows, cols = pat.shape
            rows_remaining = len(array) - starting_point[0]
            cols_remaining = len(array[0]) - starting_point[1]
            
            # Slice the pattern to match the remaining space in the array
            pattern_slice = pat[:rows_remaining, :cols_remaining]
            
            array[starting_point[0]:starting_point[0] + rows, starting_point[1]:starting_point[1] + cols] = pattern_slice
        return array

check_press()

#do the stuff after here

fin_arr = final_array(pattern)
step = -1
start = 0
stop = len(fin_arr)
for col in range(0,len(fin_arr[0])):
    step *= -1
    keyboard.press(Key.right)
    keyboard.release(Key.right)
    if step == 1:
        for row in range(start,stop,step):
            time.sleep(0.005)
            if fin_arr[row][col] == 1:
                keyboard.press(Key.enter)
                keyboard.release(Key.enter)
            keyboard.press(Key.down)
            keyboard.release(Key.down)
    else:
        for row in range(stop-1,start-1,step):
            time.sleep(0.005)
            if fin_arr[row][col] == 1:
                keyboard.press(Key.enter)
                keyboard.release(Key.down)
            keyboard.press(Key.up)
            keyboard.release(Key.up)
