import numpy as np

# function to glitch
def rollrep(arr, shift_horizontal = 0, shift_vertical = 0):

  dimensions = np.shape(arr)
  rows, columns = dimensions

  # shift_horizontal = shift_rows --> AXIS 0
  # shift_vertical = shift_columns --> AXIS 1

  # determine which axis to shift and how much to shift
  # In a two-dimensional vector, the elements of axis 0 are rows and the elements of axis 1 are columns
  if shift_horizontal != 0 and shift_vertical == 0:
    dir_axis = 0
    n_shift = shift_horizontal
  elif shift_vertical != 0 and shift_horizontal == 0:
    dir_axis = 1
    n_shift = shift_vertical
  elif shift_horizontal != 0 and shift_vertical != 0:
    dir_axis = (0,1)
    n_shift = (shift_horizontal, shift_vertical)
  else:
    print("no shift specified.")

  # determine input vector for 
  
  # roll array
  arr = np.roll(arr,axis=dir_axis, shift=n_shift)

  # add zeros
  if dir_axis == 0:
    if shift_horizontal > 0:
      arr[0:shift_horizontal,:] = 0
    elif shift_horizontal < 0:
      start = rows - shift_horizontal
      arr[start:rows+1,:] = 0
  elif dir_axis == 1:
    if shift_vertical > 0:
      arr[:,0:shift_vertical]
    elif shift_vertical < 0:
      start = columns - shift_vertical
      arr[:,start:rows+1] = 0
  elif dir_axis == (0,1):
    if shift_horizontal > 0 and shift_vertical > 0:
      arr[0:shift_horizontal,0:shift_vertical] = 0
    elif shift_horizontal > 0 and shift_vertical < 0:
      start = columns - shift_vertical
      arr[0:shift_horizontal,start:rows+1] = 0
    elif shift_horizontal < 0 and shift_vertical > 0:
      start = rows - shift_horizontal
      arr[start:rows+1,0:shift_vertical] = 0
    elif shift_horizontal < 0 and shift_vertical < 0:
      start_c = columns - shift_vertical
      start_r = rows - shift_horizontal
      arr[start_r:rows+1,0:start_c:rows+1] = 0
    
    #
  else:
    print("dir_axis paramter incorrect.")

  return arr 