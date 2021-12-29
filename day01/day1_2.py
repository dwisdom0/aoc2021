
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
  for i in range(len(values)):
    try:
      cur_window = values[i] + values[i+1] + values[i+2]
      next_window = values[i+1] + values[i+2] + values[i+3]
      
      if cur_window < next_window:
        increases += 1 
    except IndexError:
      break

  print(increases)
    
    



if __name__ == '__main__':
  main()
