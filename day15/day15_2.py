import numpy as np

from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

def read_input(p):
  with open(p, 'r') as f:
    lines = f.readlines()

  risk_map = [list(l.strip()) for l in lines]
  for i, row in enumerate(risk_map):
    for j, val in enumerate(row):
      risk_map[i][j] = int(val)
  return risk_map


def build_full_map(risk_map):
  arr = np.array(risk_map, dtype=np.uint8)
  # make the top row
  top_row = np.concatenate([arr, arr+1], axis=1)
  for i in range(2,5):
    top_row = np.concatenate([top_row, arr + i], axis=1)

  # propogate it down
  full_map = np.concatenate([top_row, top_row + 1], axis=0)
  for i in range(2,5):
    full_map = np.concatenate([full_map, top_row + i], axis=0)

  # wrap values that are greater than 9
  full_map = np.where(full_map > 9, full_map - 9, full_map)
  return full_map



def score_risk(risk_map, path):
  total_risk = 0
  for j, i in path:
    total_risk += risk_map[i][j]
  # don't count the risk of the starting node
  total_risk -= risk_map[0][0]
  return total_risk


def main():
  p = 'input.txt'
  risk_map = read_input(p)
  full_map = build_full_map(risk_map)
  grid = Grid(matrix=full_map)
  start = grid.node(0,0)
  end = grid.node(-1, -1)

  finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
  path, runs = finder.find_path(start, end, grid)

  print(grid.grid_str(path=path, start=start, end=end))
  print(score_risk(full_map, path))


if __name__ == '__main__':
  main()

