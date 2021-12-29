
# dataclass wasn't added until 3.7
# and I'm writing this on 3.6.9
class Packet:
  def __init__(self, version, p_type, data):
    self.version = version
    self.p_type = p_type
    self.data = data

  def __repr__(self):
    return f'version: {self.version}, p_type: {self.p_type}, data: {self.data}'


def read_input(p):
  with open(p, 'r') as f:
    lines = f.readlines()

  dec_data = int(lines[0], 16)
  bin_data = bin(dec_data)[2:]

  return bin_data

def parse_next_packet(bin_data):
  """
  There's no way to know how long the next packet will be
  unless we parse the entire data section of the packet
  """

def main():
  p = 'input.txt'
  bin_data = read_input(p)
  #print(bin_data)
  p = Packet(1,2,'asdf')
  print(p)


if __name__ == '__main__':
  main()
