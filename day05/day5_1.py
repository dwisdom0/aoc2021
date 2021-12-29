
def read_input(p):
  with open(p, 'r') as f:
    lines_in = f.readlines()

  # parse them into pairs of tuples
  lines = []
  for l in lines_in:
    endpoints = l.split(' -> ')
    x1 = int(endpoints[0].split(',')[0])
    y1 = int(endpoints[0].split(',')[1])
    x2 = int(endpoints[1].split(',')[0])
    y2 = int(endpoints[1].split(',')[1])
    lines.append(((x1, y1), (x2, y2)))

  return lines


def filter_vertical(lines):
  """
  return any line where x1 == x2
  """
  return [l for l in lines if l[0][0] == l[1][0]]


def filter_horizontal(lines):
  """
  return any line where y1 == y2
  """
  return [l for l in lines if l[0][1] == l[1][1]]


def get_xs(lines):
  xs = []
  for l in lines:
    xs.append(l[0][0])
    xs.append(l[1][0])
  return xs


def get_ys(lines):
  ys = []
  for l in lines:
    ys.append(l[0][1])
    ys.append(l[1][1])
  return ys


def get_board_size(lines):
  """
  Find the largest x and the largest y
  """
  x = max(get_xs(lines))
  y = max(get_ys(lines))
  return max(x, y)


def build_board(lines):
  size = get_board_size(lines)
  board = []
  for _ in range(size+1):
    board.append([0] * (size+1))
  return board


def apply_verts(board, verts):
  """
  place the vertical lines on the board
  """
  for v in verts:
    x1 = v[0][0]
    y1 = v[0][1]
    y2 = v[1][1]
    # range(larger, smaller) doesn't do anything
    # so do it both ways to make sure we have them the right
    # way around
    for y in range(y1, y2+1):
      board[y][x1] += 1
    for y in range(y2, y1+1):
      board[y][x1] += 1
  return board


def apply_horiz(board, horiz):
  """
  place the horizontal lines on the board
  """
  for h in horiz:
    x1 = h[0][0]
    x2 = h[1][0]
    y1 = h[0][1]
    # range(larger, smaller) doesn't do anything
    # so do it both ways to make sure we have them the right
    # way around
    for x in range(x1, x2+1):
      board[y1][x] += 1
    for x in range(x2, x1+1):
      board[y1][x] += 1
  return board


def score_board(board):
  score = 0
  for y, row in enumerate(board):
    for x, val in enumerate(row):
      if val > 1:
        score += 1
  return score


def main():
  p = 'input.txt'
  lines = read_input(p)
  verts = filter_vertical(lines)
  horiz = filter_horizontal(lines)
  board = build_board(lines)
  board = apply_verts(board, verts)
  board = apply_horiz(board, horiz)
  print(score_board(board))


if __name__ == '__main__':
  main()
