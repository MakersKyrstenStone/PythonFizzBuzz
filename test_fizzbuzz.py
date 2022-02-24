import unittest

from fizzbuzz import generate

class TestFizzBuzz(unittest.TestCase):
  def test_lists_values_up_to_one(self):
    self.assertEqual(generate(1), '1')

  def test_lists_values_up_to_two(self):
    self.assertEqual(generate(2), '1, 2')
  
  def test_list_values_up_to_three(self):
    self.assertEqual(generate(3), '1, 2, Fizz')
  
  def test_list_values_up_to_five(self):
    self.assertEqual(generate(5), '1, 2, Fizz, 4, Buzz')
  
  def test_list_values_up_to_fifteen(self):
    self.assertEqual(generate(15), '1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz')
  