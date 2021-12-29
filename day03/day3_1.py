def read_data():
  p = 'input.txt'
  with open(p, 'r') as f:
    lines = f.readlines()
  d = {}
  for i in range(12):
    d[i] = [int(l[i]) for l in lines]
  return d
  

def main():
  d = read_data()
  gamma_bits = ''
  epsilon_bits = ''
  
  for i in range(12):
    gb = int(round(sum(d[i])/len(d[i])))
    eb = int(not gb)
    gamma_bits += str(gb)
    epsilon_bits += str(eb)
  
  g = int(gamma_bits, 2) 
  e = int(epsilon_bits, 2)
  print(gamma_bits)
  print(epsilon_bits)
  print(g)
  print(e)
  print(g*e)
  
      


if __name__ == '__main__':
  main()
  
