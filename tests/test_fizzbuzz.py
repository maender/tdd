import pytest
from modules.fizzbuzz import fizzbuzz

def test_fizzbuzzWith1():
	assert fizzbuzz(1) == '1'

def test_fizzBuzzWith2():
	assert fizzbuzz(2) == '2'

def test_fizzBuzzWith3():
	assert fizzbuzz(3) == 'Fizz'

def test_fizzBuzzWith5():
	assert fizzbuzz(5) == 'Buzz'

def test_fizzBuzzWith9():
	assert fizzbuzz(9) == 'Fizz'

def test_fizzBuzzWith10():
	assert fizzbuzz(10) == 'Buzz'

def test_fizzBuzzWith15():
	assert fizzbuzz(15) == 'FizzBuzz'

def test_fizzBuzzWith30():
	assert fizzbuzz(30) == 'FizzBuzz'