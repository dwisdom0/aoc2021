import numpy as np
from day9_1 import *

def test_low_point_corner():
  grid = np.array([np.array([5,5,5]),
                   np.array([5,1,5]),
                   np.array([5,5,5])])
  assert is_low_point(grid, 0, 0) == False
  assert is_low_point(grid, 0, 2) == False
  assert is_low_point(grid, 2, 0) == False
  assert is_low_point(grid, 2, 2) == False


def test_low_point_center():
  grid = np.array([np.array([5,5,5]),
                   np.array([5,1,5]),
                   np.array([5,5,5])])
  assert is_low_point(grid, 1, 1) == True


def test_risk():
  grid = np.array([np.array([5,5,5]),
                   np.array([5,1,5]),
                   np.array([5,5,5])])
  assert total_risk(grid) == 2


def test_given_board():
  grid = np.array([np.array([2,1,9,9,9,4,3,2,1,0]),
                   np.array([3,9,8,7,8,9,4,9,2,1]),
                   np.array([9,8,5,6,7,8,9,8,9,2]),
                   np.array([8,7,6,7,8,9,6,7,8,9]),
                   np.array([9,8,9,9,9,6,5,6,7,8])])
  assert total_risk(grid) == 15


def test_random_board():
  rng = np.random.default_rng(12345)
  grid = 10 * rng.random((20,20))
  grid = grid.astype(np.uint8)
  # creates this grid
  # [[2 3 7 6 3 3 5 1 6 9 2 9 6 0 4 8 6 3 7 2] 2, 0, 3
  #  [0 1 3 4 2 8 1 1 0 5 8 6 9 7 8 9 5 9 4 2] 0, 0
  #  [4 6 3 9 2 3 2 3 0 6 2 0 6 1 3 4 1 2 4 4] 0, 1, 1
  #  [2 2 2 2 4 2 4 2 8 1 8 1 7 6 2 7 2 0 6 5] 2, 2, 2, 0
  #  [6 1 2 6 0 8 4 6 3 1 0 2 8 9 4 3 2 9 0 4] 1, 0, 0
  #  [1 2 7 2 5 3 5 3 2 2 0 4 8 9 0 9 1 7 8 1] 1, 2, 3, 0, 1, 1 (misses the first 1 here)
  #  [3 3 3 5 0 4 8 0 4 4 7 9 7 2 6 3 7 6 9 8] 0, 3, 
  #  [0 2 8 6 3 0 7 0 0 9 7 8 4 1 5 4 1 1 2 9]
  #  [9 7 7 7 5 1 8 8 7 9 9 5 7 6 1 3 0 8 0 5]
  #  [1 1 1 8 4 3 9 5 3 3 6 1 7 8 4 4 1 4 7 4]
  #  [6 0 2 2 9 0 2 0 6 6 3 0 4 1 4 3 2 8 6 4]
  #  [3 1 6 5 9 9 8 8 4 3 4 5 8 1 6 9 2 2 8 6]
  #  [9 6 9 8 6 1 2 8 3 6 4 4 0 8 3 3 0 6 7 5]
  #  [4 7 0 5 7 3 8 4 1 9 4 7 0 8 1 1 2 4 4 4]
  #  [0 5 7 9 5 9 9 2 0 1 7 2 1 9 6 9 3 1 1 9]
  #  [1 8 2 8 0 3 4 9 8 3 4 7 6 8 6 5 9 3 3 3]
  #  [4 0 4 3 2 2 7 3 9 4 6 3 8 2 2 2 1 7 4 1]
  #  [5 4 5 7 0 4 0 9 6 1 9 1 3 0 3 7 1 7 4 8]
  #  [1 9 7 0 4 0 7 3 7 8 1 8 3 3 6 9 6 2 0 1]
  #  [2 0 0 9 1 3 9 5 6 2 6 1 3 9 7 4 4 7 3 4]]
  #

  assert is_low_point(grid, 5, 0) == True
