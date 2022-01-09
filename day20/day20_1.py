
def read_input(p):
  with open(p, 'r') as f:
    enhancer = f.readline().strip()
    _ = f.readline()
    image = f.readlines()
  image = [i.strip().replace('#', '1').replace('.', '0') for i in image]
  image = [list(i) for i in image]
  enhancer = enhancer.replace('#', '1').replace('.', '0')

  return enhancer, image


def get_conv_in_order(image, i, j):
  conv = ''
  idxs = [[i-1, j-1],
          [i-1, j],
          [i-1, j+1],
          [i, j-1],
          [i, j],
          [i, j+1],
          [i+1, j-1],
          [i+1, j],
          [i+1, j+1]]

  for i_idx, j_idx in idxs:
    try:
      conv += image[i_idx][j_idx]
    except IndexError:
      conv += '0'

  return conv


def pad_image_inplace(image):
  for row in image:
    row.insert(0, '0')
    row.append('0')

  new_width = len(image[0])
  image.insert(0, ['0'] * new_width)
  image.append(['0'] * new_width)


def convolve_3x3(image):
  """
  convolve the image with a 3x3 matrix of 1's
  interpret the convolution as a binary number
  """
  new_image = []
  pad_image_inplace(image)
  for i, row in enumerate(image):
    new_row = []
    for j, val in enumerate(row):
      b_str = get_conv_in_order(image, i, j)
      new_row.append(int(b_str, 2))
    new_image.append(new_row)

  return new_image


def enhance(image, enhancement):
  """
  take an image of ints and replace each one
  with the corresponding entry in the enhancement list
  """
  new_image = []
  for i, row in enumerate(image):
    new_row = []
    for j, val in enumerate(row):
      new_row.append(enhancement[val])
    new_image.append(new_row)
  return new_image


def enhance_algo(image, enhancement):
  image = convolve_3x3(image)
  image = enhance(image, enhancement)
  return image


def score_image(image):
  total = 0
  for i, row in enumerate(image):
    for j, val in enumerate(row):
      if val == '1':
        total += 1
  return total


def main():
  p = 'input.txt'
  enhancer, image = read_input(p)
  image = enhance_algo(image, enhancer)
  print(len(image), len(image[0]))
  image = enhance_algo(image, enhancer)
  print(len(image), len(image[0]))
  print(score_image(image))
  # 5570 was too high



if __name__ == '__main__':
  main()
