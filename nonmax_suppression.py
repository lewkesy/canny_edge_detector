import numpy as np

def maximum(det, phase):
  # gmax = np.zeros(det.shape)
  gmax = det > 0
  h, w = det.shape
  phase = np.round(phase*4/np.pi)
  phase = np.mod(phase, 4)

  # 0 degree
  ind = np.where(phase==0)
  candidate = np.logical_and(det[ind[0], ind[1]] > det[ind[0], np.maximum(0, ind[1]-1)], det[ind[0], ind[1]] > det[ind[0], np.minimum(w-1, ind[1]+1)])
  gmax[ind[0], ind[1]] = np.logical_and(candidate, gmax[ind[0], ind[1]])
  # 180 degree
  ind = np.where(phase==2)
  candidate = np.logical_and(det[ind[0], ind[1]] > det[np.maximum(0, ind[0]-1), ind[1]], det[ind[0], ind[1]] > det[np.minimum(h-1, ind[0]+1), ind[1]])
  gmax[ind[0], ind[1]] = np.logical_and(candidate, gmax[ind[0], ind[1]])
  # 90 degree
  ind = np.where(phase==1)
  candidate = np.logical_and(det[ind[0], ind[1]] > det[np.maximum(0, ind[0]-1), np.minimum(w-1, ind[1]+1)], det[ind[0], ind[1]] > det[np.minimum(h-1, ind[0]+1), np.maximum(0, ind[1]-1)])
  gmax[ind[0], ind[1]] = np.logical_and(candidate, gmax[ind[0], ind[1]])
# 270 degree
  ind = np.where(phase==3)
  candidate = np.logical_and(det[ind[0], ind[1]] > det[np.maximum(0, ind[0]-1), np.maximum(0, ind[1]-1)], det[ind[0], ind[1]] > det[np.minimum(h-1, ind[0]+1), np.minimum(w-1, ind[1]+1)])
  gmax[ind[0], ind[1]] = np.logical_and(candidate, gmax[ind[0], ind[1]])

  det[np.where(gmax == 0)] = 0
  tmp = det>0
  return det * tmp