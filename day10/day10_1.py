from collections import deque

def read_input(p):
  with open(p, 'r') as f:
    lines = f.readlines()

  lines = [l.strip() for l in lines]
  return lines


def find_corrupt(l):
  """
  push openning parens, pop for each closing paren
  and make sure it matches
  """
  s = deque()
  open_parens = ['(', '[', '{', '<']
  paren_map = {'(':')', '[':']', '{':'}' , '<':'>'}
  for paren in l:
    if paren in open_parens:
      s.append(paren)
    else:
      check = s.pop()
      if paren != paren_map[check]:
        return paren
  return False


def score_corruptions(cors):
  score_map = {')':3, ']':57, '}':1197, '>':25137}
  total = 0
  for c in cors:
    if c:
      total += score_map[c]
  return total


def main():
  p = 'input.txt'
  lines = read_input(p)
  cors = []
  for l in lines:
    cors.append(find_corrupt(l))
  score = score_corruptions(cors)
  print(score)


if __name__ == '__main__':
  main()
  
