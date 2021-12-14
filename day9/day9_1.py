import numpy as np


def read_input(p):
  with open(p, 'r') as f:
    lines = f.readlines()
  lines = [np.array(list(l.strip()), dtype=np.uint8) for l in lines]
  return np.array(lines)


def is_low_point(grid, i, j):
  point = grid[i][j]
  neighbors = []

  if i > 0:
    neighbors.append(grid[i-1][j])

  if j > 0:
    neighbors.append(grid[i][j-1])

  try:
    neighbors.append(grid[i+1][j])
  except IndexError:
    pass
  try:
    neighbors.append(grid[i][j+1])
  except IndexError:
    pass

  if point < min(neighbors):
    return True
  return False


def total_risk(grid):
  risk = 0
  for i, row in enumerate(grid):
    for j, val in enumerate(row):
      if is_low_point(grid, i, j):
        risk += val + 1
  return risk


def main():
  p = 'input.txt'
  grid = read_input(p)
  print(total_risk(grid))


if __name__ == '__main__':
  main()
