import numpy as np

from tqdm import tqdm

def read_input(p):
  with open(p, 'r') as f:
    lines = f.readlines()

  return lines[0].split(',')

def sim_day(fish):
  fish -= 1
  # all the 0s are now -1
  # so find the sum of all the negative entries
  new_fish = int(np.abs(np.sum(fish[np.where(np.sign(fish) == -1)])))
  # replace -1 with 6
  fish = np.where(fish == -1, 6, fish)
  # add and 8 for each new fish
  new_fish_list = np.array([8] * new_fish)
  fish = np.concatenate([fish, new_fish_list])
  return fish

def main():
  p = 'input.txt'
  fish = np.array(read_input(p), dtype=int)
  for _ in tqdm(range(80), ascii=True):
    fish = sim_day(fish)

  print(len(fish))



if __name__ == '__main__':
  main()
