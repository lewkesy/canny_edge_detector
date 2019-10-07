import numpy as np

def thresholding(im, minRate=0.15, maxRate=0.2):
    mmax = np.max(im)
    lo, hi = minRate * mmax, maxRate * mmax
    
    weak = np.where(np.logical_and(im > lo, im < hi), 1, 0)
    strong = np.where(im >= hi, 1, 0)

    return weak, strong