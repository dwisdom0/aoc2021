import numpy as np


def read_input(p):
  with open(p, 'r') as f:
    lines = f.readlines()

  lines = [list(l.strip()) for l in lines]
  return np.array(lines, dtype=np.uint8)


def gen_mask(grid):
  size = len(grid)
  mask = []
  for _ in range(size):
    mask.append([0] * size)
  return np.array(mask, dtype=np.uint8)


def flash(grid, i, j):
  i_idxs = [i-1, i, i+1]
  j_idxs = [j-1, j, j+1]
  for i_idx in i_idxs:
    for j_idx in j_idxs:
      if (i_idx > -1 and j_idx > -1) and (i_idx != i or j_idx != j):
        try:
          grid[i_idx][j_idx] += 1
        except IndexError:
          pass
  return grid


def step(grid):
  """
  simulate the grid for one step
  add 1 to every octopus
  check for flashes
  update for flashes until there aren't any more
  """
  mask = gen_mask(grid)
  grid += 1
  num_flashes = 0
  # set it to True to make a do/while loop
  any_flashes = True
  while any_flashes:
    any_flashes = False
    for i, row in enumerate(grid):
      for j, val in enumerate(row):
        if val > 9 and mask[i][j] == 0:
          mask[i][j] = 1
          grid = flash(grid, i, j)
          num_flashes += 1
          any_flashes = True
  # reset every octopus that flashed
  grid = np.where(mask == 1, 0, grid)
  return grid, num_flashes


def main():
  p = 'input.txt'
  grid = read_input(p)
  total_flashes = 0
  for _ in range(100):
    grid, num_flashes = step(grid)
    total_flashes += num_flashes

  print(total_flashes)


if __name__ == '__main__':
  main()
