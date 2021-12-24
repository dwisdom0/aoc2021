import pytest

from day13_1 import *



test_inputs = [

              ('test_input.txt')

              ]


@pytest.mark.parametrize('p', test_inputs)
def test_parsing(p):
  paper, folds = read_input(p)
  assert paper.shape == (15, 11)


@pytest.mark.parametrize('p', test_inputs)
def test_paper(p):
  paper, folds = read_input(p)
  right_paper = np.array([[0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
                          [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0],
                          [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
                          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]], bool)
  assert np.equal(paper, right_paper).all()


@pytest.mark.parametrize('p', test_inputs)
def test_fold_parsing(p):
  paper, folds = read_input(p)
  first_up, first_fold = parse_fold(folds[0])
  assert first_up
  assert first_fold == 7


@pytest.mark.parametrize('p', test_inputs)
def test_fold_up(p):
  paper, folds = read_input(p)
  first_up, first_fold = parse_fold(folds[0])
  paper = fold_up(paper, first_fold)
  right_answer = np.array([[1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0],
                           [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 1, 0, 0 ,0, 1],
                           [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                           [0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], bool)
  assert np.equal(paper, right_answer).all()



