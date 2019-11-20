import numpy as np
import os

dir_path = os.path.dirname(os.path.realpath(__file__))+"/numpy_saved" # path of current directory

def map_function():
    map_position = {}
    x,y=0,0
    for i in "87654321":
        for j in "abcdefgh":
            map_position[j+i] = [x,y]
            y = (y+1)%8
        x = (x+1)%8

    np.savez(dir_path+"/map_position.npz",**map_position)

