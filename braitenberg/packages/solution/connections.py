from typing import Tuple

import numpy as np


def get_motor_left_matrix(shape: Tuple[int, int]) -> np.ndarray:
    # TODO: write your function instead of this one
    res = np.zeros(shape=shape, dtype="float32")
    # these are random values
   
    for j in range(10) :
        for i in range(350-30*j) :
           res[i+30*j+130, 320:(440+ i -7*j):] = -j/20 - 0.25
    
    # ---
    return res


def get_motor_right_matrix(shape: Tuple[int, int]) -> np.ndarray:
    # TODO: write your function instead of this one
    res = np.zeros(shape=shape, dtype="float32")
    # these are random values

    for j in range(10) :
        for i in range(350-30*j) :
           res[i+30*j+130, (200-i + 7*j):320] = -j/20 - 0.25
    # ---
    return res


#    for j in range(10) :
#        for i in range(330-20*j) :
#           res[i+20*j+150, 320:(340+i):] = -j/20 - 0.5
#
#    for j in range(10) :
#        for i in range(330-20*j) :
#           res[i+20*j+150, (300-i):320] = -j/20 - 0.25