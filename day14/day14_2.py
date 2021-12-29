import cProfile


from collections import Counter

from tqdm import tqdm
from blist import blist


def read_input(p):
  with open(p, 'r') as f:
    lines = f.readlines()

  template = list(lines[0].strip())
  rules = {}
  for l in lines[2:]:
    pair, _, insertion = l.split()
    rules[pair] = insertion

  template = blist(template)
  return template, rules


# It doesn't use any memory anymore but it's super slow
# the 16th iteration takes 9 minutes and it has to get
# all the way to 40
# supposed to be 15 seconds at most
# hmm

# I could try to profile it
# I don't really want to bother with that though
# I thought python lists had pretty cheap insertions
# but maybe not cheap enough

# As I suspected, it spends all of its time in list.insert()
# someone on stack overflow suggests using a package
# called `blist`

# Now it uses a tiny bit more memory
# and it's certainly faster
# made it to 20 out of 40 in about a minute

def apply_rules(polymer, rules):
  i = 0
  while i < len(polymer) - 1:
    to_insert = rules[polymer[i] + polymer[i+1]]
    polymer.insert(i+1, to_insert)
    i += 2
  return polymer


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
  for i in tqdm(range(40), ascii=True):
    # if i == 21:
    #   cProfile.runctx('polymer = apply_rules(polymer, rules)', globals(), locals(),
    #                   filename='profile_blist.prof')
    polymer = apply_rules(polymer, rules)
  print(score_polymer(polymer))

if __name__ == '__main__':
  main()
