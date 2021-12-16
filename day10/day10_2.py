import numpy as np
from collections import deque


def read_input(p):
  with open(p, 'r') as f:
    lines = f.readlines()

  lines = [l.strip() for l in lines]
  return lines


def is_corrupt(l):
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
        return True
  return False



def drop_corrupt(lines):
  return [l for l in lines if not is_corrupt(l)]


def complete_line(line):
  s = deque()
  open_parens = ['(', '[', '{', '<']
  paren_map = {'(':')', '[':']', '{':'}' , '<':'>'}
  for paren in line:
    if paren in open_parens:
      s.append(paren)
    # If it's a closing paren, we know it's correct
    # since we dropped all the corrupted lines already
    # so just pop the open paren and keep going
    else:
      _ = s.pop()

  # complete the line
  completion = ''
  for _ in range(len(s)):
    open_paren = s.pop()
    completion += paren_map[open_paren]

  return completion

def score_completions(completions):
  score_map = {')':1, ']':2, '}':3, '>':4}
  scores = []
  for completion in completions:
    score = 0
    for paren in completion:
      score *= 5
      score += score_map[paren]
    scores.append(score)
  return int(np.median(scores))

def main():
  p = 'input.txt'
  lines = read_input(p)
  lines = drop_corrupt(lines)
  completions = []
  for l in lines:
    completions.append(complete_line(l))
  score = score_completions(completions)
  print(score)


if __name__ == '__main__':
  main()
  
