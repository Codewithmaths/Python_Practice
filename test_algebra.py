'''test_algebra.py'''
""" pytest with make different file"""
import practice_2
def test_square():
	assert practice_2.Algebra.square(40) == 1600
	assert practice_2.Algebra.square(5) == 25
def test_cube():
	assert practice_2.Algebra.cube(40) == 64000
	assert practice_2.Algebra.cube(5) == 125
