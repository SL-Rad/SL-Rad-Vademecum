# Non funziona, capire come indicare l'immagine

import matplotlib.pyplot as plt
import numpy as np


def show_slice_window(slice, level, window):
    """
    Function to display an image slice
    Input is a numpy 2D array
    """
    max = level + window/2
    min = level - window/2
    slice = slice.clip(min, max)
    plt.figure()
    plt.imshow(slice.T, cmap="gray", origin="lower")
    plt.savefig('L'+str(level)+'W'+str(window))
