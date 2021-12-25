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
  grid = Grid(matrix=risk_map)
  start = grid.node(0,0)
  end = grid.node(-1, -1)

  finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
  path, runs = finder.find_path(start, end, grid)

  print(grid.grid_str(path=path, start=start, end=end))
  print(score_risk(risk_map, path))


if __name__ == '__main__':
  main()

