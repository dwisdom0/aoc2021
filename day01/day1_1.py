
def read_input(p):
  """
  reads the input text file
  splits on newlines
  """
  with open(p, 'r') as f:
    values = f.readlines()
  real_values = []
  for v in values:
    real_values.append(int(v))
  return real_values
  
def main():
  values = read_input('input.txt')
  increases = 0
  for i, v in enumerate(values, start=1):
    if i == len(values):
      break
    if v < values[i]:
      increases += 1 

  print(increases)
    
    



if __name__ == '__main__':
  main()
