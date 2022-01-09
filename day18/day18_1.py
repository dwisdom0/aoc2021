from collections import namedtuple, deque


Pair = namedtuple(
  'Pair',
  'left right parent'
)


def read_number(number):
  s = deque()
  for c in number:
    if c == '[':
      s.append(c)
    elif c == ',':
      pass
    elif c == ']':

    else:
      s.append(c)

def read_input(p):
  with open(p, 'r') as f:
    lines = f.readlines()
  return [l.strip() for l in lines]


def main():
  p = 'input.txt'
  input_numbers = read_input(p)
  
