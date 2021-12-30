import plotly.express as px

from collections import Counter

from tqdm import tqdm

def read_input(p):
  with open(p, 'r') as f:
    lines = f.readlines()

  x_range = lines[0].split('x=')[1].split(',')[0]
  x1, x2 = x_range.split('..')
  x1 = int(x1)
  x2 = int(x2)
  y_range = lines[0].split('y=')[1].strip()
  y1, y2 = y_range.split('..')
  y1 = int(y1)
  y2 = int(y2)
  return (x1, x2), (y1, y2)


def plot_path(path, x1, x2, y1, y2):
  xs = [p[0] for p in path]
  ys = [p[1] for p in path]
  fig = px.scatter(x=xs, y=ys)
  fig.add_vline(x1)
  fig.add_vline(x2)
  fig.add_hline(y1)
  fig.add_hline(y2)
  fig.show()


def min_x0_to_reach(x1,x2):
  """
  Find the minimum initial x velocity needed to make it to the target
  """
  # sum of 1 to the number must be between x1 and x2, inclusive
  for i in range(x1):
    sum_i = (i * (i + 1)) / 2
    if sum_i >= x1 and sum_i <= x2:
      return i


def simulate_launch(x0, y0, x1, x2, y1, y2):
  path = [[0,0]]
  past_target = False
  pos = [0, 0]
  new_pos = []
  xv = x0
  yv = y0
  while not past_target:
    new_x = pos[0] + max([xv, 0])
    new_y = pos[1] + yv
    xv -= 1
    yv -= 1
    path.append([new_x, new_y])
    pos[0] = new_x
    pos[1] = new_y
    # x2 is the right limit of the target
    # y1 is the bottom limit of the target
    if pos[0] > x2 or pos[1] < y1:
      past_target = True

  return path


def hits_target(path, x1, x2, y1, y2):
  """
  Check whether the path intersects with the target area
  """
  for x, y in path:
    if x >= x1 and x <= x2 and y >= y1 and y <= y2:
      return True
  return False


def count_hits(x1, x2, y1, y2):
  start_x = min_x0_to_reach(x1, x2)
  init_hits = []

  for x0 in tqdm(range(start_x, x2+1), ascii=True):
    for y0 in range(y1, 1000):
      path = simulate_launch(x0, y0, x1, x2, y1, y2)
      if hits_target(path, x1, x2, y1, y2):
        init_hits.append((x0, y0))
  hits = Counter(init_hits)
  return hits


def main():
  p = 'input.txt'
  (x1, x2), (y1, y2) = read_input(p)
  hits = count_hits(x1, x2, y1, y2)
  #print(hits)
  print(len(hits))


if __name__ == '__main__':
  main()
