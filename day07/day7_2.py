import numpy as np

from tqdm import tqdm

from copy import deepcopy

def read_input(p):
  with open(p, 'r') as f:
    line = f.readlines()

  crabs = line[0].split(',')
  return np.array(crabs, dtype=int)


def total_fuel(crabs, pos):
  """
  calculates the total fuel required to move
  all of the crabs to `pos`
  """
  # n * (n+1) / 2
  n = np.abs(crabs - pos)
  n_1 = n + 1
  return int(np.sum((n * n_1) / 2))
  #return np.sum(np.abs(crabs - pos))


def find_least_fuel(crabs):
  least_fuel = len(crabs)**10
  best_pos = 0
  for pos in tqdm(range(np.amin(crabs), np.amax(crabs) + 1), ascii=True):
    fuel = total_fuel(crabs, pos)
    if fuel < least_fuel:
      least_fuel = deepcopy(fuel)
      best_pos = deepcopy(pos)
  print(f'best_pos: {best_pos}')
  return least_fuel

def main():
  p = 'input.txt'
  crabs = read_input(p)
  print(find_least_fuel(crabs))

if __name__ == '__main__':
  main()
