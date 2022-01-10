import itertools

def read_input(p):
  with open(p, 'r') as f:
    lines = f.readlines()

  p1_pos = int(lines[0].split(':')[-1].strip())
  p2_pos = int(lines[1].split(':')[-1].strip())

  # subtract 1 to go from 1-10 to 0-9
  p1_pos -= 1
  p2_pos -= 1

  return p1_pos, p2_pos


def create_d100():
  return itertools.cycle([x for x in range(1, 101)])


def play_turn(pos, rolls):
  """
  Play a turn by adding the three rolls to
  the current position
  and wrapping after 10
  """
  to_move = sum(rolls)
  new_pos = (pos + to_move) % 10
  return new_pos


def play_game(p1_pos, p2_pos):
  d100 = create_d100()
  p1_score = 0
  p2_score = 0
  total_rolls = 0
  while p1_score < 1000 and p2_score < 1000:
    # Player 1's turn
    rolls = []
    for _ in range(3):
      rolls.append(next(d100))
    p1_pos = play_turn(p1_pos, rolls)
    # since it's 1-10 not 0-9
    p1_score += p1_pos + 1
    total_rolls += 3

    # Player 2's turn
    rolls = []
    for _ in range(3):
      rolls.append(next(d100))
    p2_pos = play_turn(p2_pos, rolls)
    # since it's 1-10 not 0-9
    p2_score += p2_pos + 1
    total_rolls += 3

  return p1_score, p2_score, total_rolls


def main():
  p = 'input.txt'
  p1_pos, p2_pos = read_input(p)
  p1_score, p2_score, total_rolls = play_game(p1_pos, p2_pos)

  print(f'p1 score: {p1_score}')
  print(f'p2 score: {p2_score}')
  print(f'total rolls: {total_rolls}')
  print(min(p1_score, p2_score) * total_rolls)



if __name__ == '__main__':
  main()
