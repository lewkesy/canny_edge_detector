import numpy as np
from scipy.signal import convolve2d as conv2

def Gaussian_Filter(kernel_size=5, sigma=1.2): 
    k = (kernel_size-1)//2 
    x, y = np.meshgrid(np.linspace(-k, k, kernel_size), np.linspace(-k, k, kernel_size))
    g = np.exp(-(x * x + y * y) / (2 * sigma**2)) / (2 * np.pi * sigma ** 2)
    return np.asarray(g)

def gaussian(im):
    kernel = Gaussian_Filter()
    return conv2(im, kernel, mode='same', boundary='symm')

