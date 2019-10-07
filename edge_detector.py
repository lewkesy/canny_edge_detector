from gaussian_filter import gaussian
from gradient import gradient
from nonmax_suppression import maximum
from double_thresholding import thresholding
from connect import connect
import numpy as np
from PIL import Image
from matplotlib.pyplot import imshow, show, subplot, gray, title, axis

if __name__ == '__main__':
    from sys import argv
    if len(argv) < 2:
        print ("Usage: python %s <image>")
        exit()
    im = np.array(Image.open(argv[1]))
    subplot(1, 3, 1)
    imshow(im)
    axis('off')
    title('Original')

    if len(im.shape) == 3:
	    im = im[:, :, 0]
    gim = gaussian(im)
    grim, gphase = gradient(gim)
    gmax = maximum(grim, gphase)
    weak, strong = thresholding(gmax, minRate=0.1, maxRate=0.2)
    edge = connect(weak, strong, rate=0.2)
    
    gray()
    subplot(1, 3, 2)
    imshow(grim/grim.max())
    axis('off')
    title('nms')

    subplot(1, 3, 3)
    imshow(edge/edge.max())
    axis('off')
    title('Edges')

    show()
