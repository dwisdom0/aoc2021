
def read_input(p):
  with open(p, 'r') as f:
    lines = f.readlines()
  directions = []
  values = []
  for l in lines:
    split_line = l.split(' ')
    directions.append(split_line[0])
    values.append(int(split_line[1]))
  return directions, values
  

def main():
  directions, values = read_input('input.txt')
  aim = 0
  pos = 0
  depth = 0
  for d, v in zip(directions, values):
    if d == 'forward':
      pos += v
      depth += aim * v
    elif d == 'down':
      aim += v
    elif d == 'up':
      aim -= v
    else:
      raise ValueError(f'unexpected direction {d}')
  
  print(f'pos: {pos}')
  print(f'depth: {depth}')
  print(f'pos * depth: {pos*depth}')

if __name__ == '__main__':
  main()
