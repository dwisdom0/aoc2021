from collections import Counter


def read_input(p):
  with open(p, 'r') as f:
    lines = f.readlines()

  template = list(lines[0].strip())
  rules = {}
  for l in lines[2:]:
    pair, _, insertion = l.split()
    rules[pair] = insertion

  return template, rules


def extract_bigrams(l):
  """
  get a list of the bigrams in the polymer
  """
  bigrams = []
  for i, element in enumerate(l, start=1):
    # DoN't UsE RaNgE(lEnGtH())
    # so I'm doing this instead
    try:
      bigrams.append(element + l[i])
    except IndexError:
      break
  return bigrams


def apply_rules(polymer, rules):
  bigrams = extract_bigrams(polymer)
  new_polymer = []
  for bigram in bigrams:
    new_polymer += [bigram[0], rules[bigram]]
  new_polymer.append(polymer[-1])
  return new_polymer


def score_polymer(polymer):
  c = Counter(polymer)
  most_amt = c.most_common(1)[0][1]
  least_amt = most_amt
  for k, count in c.items():
    if count < least_amt:
      least_amt = count

  return most_amt - least_amt


def main():
  p = 'input.txt'
  polymer, rules = read_input(p)
  for _ in range(10):
    polymer = apply_rules(polymer, rules)
  print(score_polymer(polymer))

if __name__ == '__main__':
  main()
