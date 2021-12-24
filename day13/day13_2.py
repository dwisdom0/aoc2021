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


def pprint_paper(paper):
  to_print = ''
  for row in paper:
    print_row = ''
    for dot in row:
      if dot:
        print_row += '#'
      else:
        print_row += ' '
    to_print += print_row + '\n'
  print(to_print)



def main():
  p = 'input.txt'
  paper, folds = read_input(p)
  for f in folds:
    up, fold_line = parse_fold(f)
    if up:
      paper = fold_up(paper, fold_line)
    else:
      paper = fold_left(paper, fold_line)

  pprint_paper(paper)



if __name__ == '__main__':
  main()
