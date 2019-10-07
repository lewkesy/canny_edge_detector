import numpy as np
from scipy.signal import convolve2d as conv2
from IPython import embed
def gradient(im):
    # Sobel operator
    op1 = np.array([[1, 0, -1],
                 [2, 0, -2],
                 [1, 0, -1]])
    op2 = np.array([[-1, -2, -1],
                 [ 0,  0,  0],
                 [ 1,  2,  1]])

    Gx = conv2(im, op1, mode='same', boundary='symm')
    Gy = conv2(im, op2, mode='same', boundary='symm')

    G = np.sqrt(Gx**2 + Gy**2)
    # embed()
    # G[np.where(G < np.max(G) * 0.2)] = 0
    Theta = np.arctan2(Gy, Gx)
    # print(G)
    return G, Theta
