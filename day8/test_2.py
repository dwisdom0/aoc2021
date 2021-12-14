from day8_2 import *

def test_solver():
  in_out = ['acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab', 'cdfeb fcadb cdfeb cdbaf']
  ins, outs = parse_in_out(in_out)
  connections = solve_connections(ins)
  assert connections['d'] == 'a'
  assert connections['e'] == 'b'
  assert connections['a'] == 'c'
  assert connections['f'] == 'd'
  assert connections['g'] == 'e'
  assert connections['b'] == 'f'
  assert connections['c'] == 'g'

def test_decoder():
  in_out = ['acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab', 'cdfeb fcadb cdfeb cdbaf']
  ins, outs = parse_in_out(in_out)
  connections = solve_connections(ins)
  clear_texts = decode(outs, connections)
  assert clear_texts[0] == 'abdfg'
  assert clear_texts[1] == 'acdfg'
  assert clear_texts[2] == 'abdfg'
  assert clear_texts[3] == 'acdfg'

def test_decoder2():
  in_out = ['acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab', 'cdfeb fcadb cdfeb cdbaf']
  ins, outs = parse_in_out(in_out)
  connections = solve_connections(ins)
  digits = solve_output(outs, connections)
  assert digits == 5353


