import numpy as np
from scipy.signal import convolve2d as conv2

def connect(weak, strong, rate=0.2):
	pure_kernel = np.ones((3,3))
	pure_kernel[1,1] = 0

	edge_connected = conv2(strong, pure_kernel, mode='same') * weak
	for _ in range(5):
		edge_connected = conv2(edge_connected, pure_kernel, mode='same') * weak

	edge_final = strong + np.clip(edge_connected, 0, 1)
	edge = np.where(edge_final > rate, 1, 0)

	return edge