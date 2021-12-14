def read_input(p):
  with open(p, 'r') as f:
    lines = f.readlines()
  outputs = [l.split(' | ')[1].strip() for l in lines]
  individual_outputs = []
  for o in outputs:
    individual_outputs += o.split(' ')
  return individual_outputs


def count_1478(outs):
  """
  1: 2 segments
  4: 4 segments
  7: 3 segments
  8: 7 segments
  """
  total = 0
  for o in outs:
    if len(o) in [2,3,4,7]:
      total += 1
  return total


def main():
  p = 'input.txt'
  outputs = read_input(p)
  print(count_1478(outputs))


if __name__ == '__main__':
  main()
