
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


def apply_lines(board, lines):
  """
  place the lines on the board
  """
  board_size = len(board)
  for l in lines:
    x1 = l[0][0]
    x2 = l[1][0]
    y1 = l[0][1]
    y2 = l[1][1]
    small_x = min(x1, x2)
    big_x = max(x1, x2)
    small_y = min(y1, y2)
    big_y = max(y1, y2)

    # four cases
    #
    # top left, bottom right
    # x1 < x2 and y1 < y2
    # x1 > x2 and y1 > x2
    #
    # top right, bottom left
    # x1 < x2 and y1 > y2
    # x1 > x2 and y2 < y2
    #
    # horizontal
    # y1 == y2
    #
    # vertical
    # x1 == x2

    # horizontal
    if y1 == y2:
      for x in range(small_x, big_x+1):
        board[y1][x] += 1

    # vertical
    elif x1 == x2:
      for y in range(small_y, big_y+1):
        board[y][x1] += 1

    # top left, bottom right
    elif (x1 > x2 and y1 > y2) or (x1 < x2 and y1 < y2):
      # small_x -> big_x
      # small_y -> big_y
      for j, x in enumerate(range(small_x, big_x+1)):
        for i, y in enumerate(range(small_y, big_y+1)):
          if i == j:
            board[y][x] += 1

    # top right, bottom left
    elif (x1 > x2 and y1 < y2) or (x1 < x2 and y1 > y2):
      # small_x -> big_x
      # big_y -> small_y
      for j, x in enumerate(range(small_x, big_x+1)):
        for i, y in enumerate(range(big_y, small_y-1, -1)):
          if i == j:
            board[y][x] += 1

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
  board = build_board(lines)
  board = apply_lines(board, lines)
  print(score_board(board))


if __name__ == '__main__':
  main()
