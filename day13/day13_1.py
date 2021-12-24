import numpy as np

def read_input(p):
  with open(p, 'r') as f:
    lines = f.readlines()

  points = []
  folds = []
  for l in lines:
    if l.startswith('fold'):
      folds.append(l.split()[-1])
    elif l == '\n':
      pass
    else:
      p1, p2 = l.split(',')
      p1 = int(p1.strip())
      p2 = int(p2.strip())
      points.append([p1,p2])

  points = np.array(points)
  x_size = np.max(points[:, 0]) + 1
  y_size = np.max(points[:, 1]) + 1

  paper = np.zeros((y_size, x_size), bool)
  for x, y in points:
    paper[y, x] = True

  return paper, folds


def parse_fold(fold):
  up = True
  if 'x' in fold:
    up = False
  line = int(fold.split('=')[-1])

  return up, line


# I misread the input so I implemented the upward fold
# even though I don't use it
def fold_up(paper, fold_line):
  for i, row in enumerate(paper[fold_line+1:]):
    for j, dot in enumerate(row):
      if dot:
        row_idx = fold_line - i - 1
        paper[row_idx][j] = True

  return paper[:fold_line]


def fold_left(paper, fold_line):
  for i, row in enumerate(paper):
    for j, dot in enumerate(row[fold_line+1:]):
      if dot:
        col_idx = fold_line - j - 1
        paper[i, col_idx] = True
  return paper[:, :fold_line]


def main():
  p = 'input.txt'
  paper, folds = read_input(p)
  print(folds[0])
  first_up, first_fold_line = parse_fold(folds[0])
  print(f'dots before folding: {np.sum(paper)}')
  if not first_up:
    print('folding left')
    paper = fold_left(paper, first_fold_line)

  print(f'dots after folding: {np.sum(paper)}')


if __name__ == '__main__':
  main()
