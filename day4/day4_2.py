def read_data():
  p = 'input.txt'
  with open(p, 'r') as f:
    lines = f.readlines()

  lines = [l.replace('\n', '') for l in lines]
  nums = lines[0].split(',') 
  nums = [int(n) for n in nums]
  boards = []
  new_board = []
  for i, l in enumerate(lines[2:]):
    if l == '' :
      boards.append(new_board)
      new_board = []
      continue

    new_row = [int(x) for x in l.split()]
    new_board.append(new_row)

  return nums, boards

def build_masks(boards):
  masks = []
  for b in boards:
    masks.append([[0]*5,
                  [0]*5,
                  [0]*5,
                  [0]*5,
                  [0]*5])
  return masks
    
def is_bingo(mask):
  bingo = [1]*5
  # check rows
  for r in mask:
    if r == bingo:
      return True
  # check cols
  for j in range(5):
    col = [mask[i][j] for i in range(5)]
    if col == bingo:
      return True

  return False

 
def call_num(num, boards, masks):
  for b, m in zip(boards, masks):
    for i, r in enumerate(b):
      for j, val in enumerate(r):
        if val == num:
          m[i][j] = 1
  return masks


def score_board(board, mask, last_num):
  total = 0
  for i, r in enumerate(mask):
    for j, bit in enumerate(r):
      if bit == 0:
        total += board[i][j] 
  return total * last_num
  

def main():
  nums, boards = read_data()
  masks = build_masks(boards)
  win_mask = [0] * len(masks)

  done = False
  for num in nums:
    if done:
      break
    masks = call_num(num, boards, masks)
    for i, mask in enumerate(masks):
      if is_bingo(mask):
        win_mask[i] = 1

      if sum(win_mask) == len(win_mask):
        print(score_board(boards[i], mask, num))
        done = True
        break
      
    
if __name__ == '__main__':
  main()
        
      
    
    
    
