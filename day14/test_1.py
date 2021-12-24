from day14_1 import *

def test_bigrams():
  polymer = ['N', 'N', 'C', 'B']
  bigrams = extract_bigrams(polymer)
  correct_bigrams = ['NN', 'NC', 'CB']
  assert bigrams == correct_bigrams


def test_one_step():
  polymer = ['N', 'N', 'C', 'B']
  rules = {'CH':'B',
           'HH':'N',
           'CB':'H',
           'NH':'C',
           'HB':'C',
           'HC':'B',
           'HN':'C',
           'NN':'C',
           'BH':'H',
           'NC':'B',
           'NB':'B',
           'BN':'B',
           'BB':'N',
           'BC':'B',
           'CC':'N',
           'CN':'C'}
  new_polymer = apply_rules(polymer, rules)
  correct_polymer = ['N', 'C', 'N', 'B', 'C', 'H', 'B']
  assert new_polymer == correct_polymer

