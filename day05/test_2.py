from day5_2 import build_board, apply_lines


def test_top_right_bottom_left():
  lines = [((10,5),(5,10))]
  board = build_board(lines)
  board = apply_lines(board, lines)
  print(board)

