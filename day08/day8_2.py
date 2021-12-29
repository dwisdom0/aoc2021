def read_input(p):
  with open(p, 'r') as f:
    lines = f.readlines()
  in_out = [l.strip().split(' | ') for l in lines]
  return in_out


def parse_in_out(in_out):
  ins = in_out[0].split(' ')
  outs = in_out[1].split(' ')
  return ins, outs


def solve_connections(ins):
  # find 1
  # length == 2
  for i in ins:
    if len(i) == 2:
      one = set(i)

  # find 4
  # length == 4
  for i in ins:
    if len(i) == 4:
      four = set(i)

  # find 7
  # length == 3
  for i in ins:
    if len(i) == 3:
      seven = set(i)

  # find 8
  # length == 7
  for i in ins:
    if len(i) == 7:
      eight = set(i)

  connections = {}
  connections['a'] = seven - one

  # find b, e, and f
  # b appears in 6 digits
  # e appears in 4 digits
  # f appears in 9 digits
  seen = {}
  for i in ins:
    for side in i:
      if side in seen:
        seen[side] += 1
      else:
        seen[side] = 1
  for side in seen:
    if seen[side] == 6:
      connections['b'] = set(side)
    elif seen[side] == 4:
      connections['e'] = set(side)
    elif seen[side] == 9:
      connections['f'] = set(side)


  # d = 4 - 1 - b
  connections['d'] = four - one - connections['b']

  # c = 4 - b - d - f
  connections['c'] = four - connections['b'] - connections['d'] - connections['f']

  # g = 8 - a - b - c - d - e - f
  connections['g'] = eight - \
                     connections['a'] - \
                     connections['b'] - \
                     connections['c'] - \
                     connections['d'] - \
                     connections['e'] - \
                     connections['f']

  # Some weirdness to get the single elemets out of the sets
  to_return = {}
  for k in connections:
    to_return[k], = connections[k]

  # Invert the dictionary to use it for deocding
  to_return = {value: key for key, value in to_return.items()}

  return to_return


def sides2digit(sides):
  """
  convert an alphabetical list of sides
  to the digit they represent (as a string)
  """
  d = {}
  d['abcefg'] = '0'
  d['cf'] = '1'
  d['acdeg'] = '2'
  d['acdfg'] = '3'
  d['bcdf'] = '4'
  d['abdfg'] = '5'
  d['abdefg'] = '6'
  d['acf'] = '7'
  d['abcdefg'] = '8'
  d['abcdfg'] = '9'
  return d[sides]


def decode(outs, connections):
  clear_texts = []
  for o in outs:
    clear = ''
    for side in o:
      ct = connections[side]
      clear += ct
    clear_texts.append(''.join(sorted(clear)))

  return clear_texts


def solve_output(outs, connections):
  clear_texts = decode(outs, connections)

  digits = ''
  for ct in clear_texts:
    digits += sides2digit(ct)

  return int(digits)


def main():
  p = 'input.txt'
  in_outs = read_input(p)
  total = 0
  for in_out in in_outs:
    ins, outs = parse_in_out(in_out)
    connections = solve_connections(ins)
    total += solve_output(outs, connections)

  print(total)


if __name__ == '__main__':
  main()
