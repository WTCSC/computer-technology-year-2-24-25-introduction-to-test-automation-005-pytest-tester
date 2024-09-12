import pytest
import math_it_up

"""
This file contains the tests for the math_it_up module, which contains the
following functions:

- math_it_up.is_even
- math_it_up.is_odd
- math_it_up.mean
- math_it_up.median
- math_it_up.mode

The `is_even` and `is_odd` functions accept a single argument, a number, and
return True if the number is even or odd, respectively.

The `mean` function accepts a single argument, a list of numbers, and returns
the mean of the numbers.

The `median` function accepts a single argument, a list of numbers, and returns
the median of the numbers.

The `mode` function accepts a single argument, a list of numbers, and returns
the mode of the numbers.

To run the tests, run `pytest` from the command line in the same directory as
this file.
"""

@pytest.fixture
def sample_data():
  """
  Sample
  """
  return [6, -42, 86, 0, 56, 86]

def test_is_even():
  """
  Tests for the `is_even` function
  """
  assert math_it_up.is_even(0)
  assert math_it_up.is_even(6)
  assert math_it_up.is_even(-42)

  assert not math_it_up.is_even(1)
  assert not math_it_up.is_even(9)
  assert not math_it_up.is_even(-71)

def test_is_odd():
  """
  Tests for the `is_odd` function
  """
  assert not math_it_up.is_odd(0)
  assert not math_it_up.is_odd(6)
  assert not math_it_up.is_odd(-42)

  assert math_it_up.is_odd(1)
  assert math_it_up.is_odd(9)
  assert math_it_up.is_odd(-71)

def test_mean(sample_data):
  """
  Tests for the `mean` function
  """
  assert math_it_up.mean(sample_data) == 32

def test_median(sample_data):
  """
  Tests for the `median` function
  """
  assert math_it_up.median(sample_data) == 31

def test_mode(sample_data):
  """
  Tests for the `mode` function
  """
  assert 86 in math_it_up.mode(sample_data)