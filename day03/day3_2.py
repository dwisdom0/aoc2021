def read_data():
  p = 'input.txt'
  with open(p, 'r') as f:
    lines = f.readlines()

  lines = [l.replace('\n', '') for l in lines]
  return lines


def calc_o2(data):
  for i in range(len(data[0]) + 1):
    if len(data) == 1:
      return int(data[0], 2)
    
    bit = common_bit(data, i, most=True)
    data = get_next_nums(data, i, bit)
  

def calc_co2(data):
  for i in range(len(data[0]) + 1):
    if len(data) == 1:
      return int(data[0], 2)
    
    bit = common_bit(data, i, most=False)
    data = get_next_nums(data, i, bit)


def common_bit(data, i, most):
  """
  returns the most or least common bit at position `i` in
  a list of strings representing binary numbers
  """
  bs = [int(d[i]) for d in data]
  ones = sum(bs)
  zeros = len(bs) - ones

  # handle ties based on whether we're looking for O2 or CO2
  if ones == zeros:
    # O2
    if most:
      return 1
    # C02
    return 0
       
  if ones > zeros:
    most_common = 1
  else:
    most_common = 0

  if most:
    return most_common
  else:
    return int(not most_common)


def get_next_nums(data, i, bit):
  """
  returns all the numbers that have `bit` in position `i`
  """
  return [d for d in data if int(d[i]) == bit]
  
  

def main():
  data = read_data()
  o2_val = calc_o2(data)
  co2_val = calc_co2(data)
  print(o2_val)
  print(co2_val)
  print(o2_val * co2_val)

if __name__ == '__main__':
  main()
