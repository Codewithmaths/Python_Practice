# # test_practice_2.py
""" pytest testing  """
# import practice_2
# import pytest
# def test_add():
#     assert practice_2.Add.add(2, 3) == 5
#     assert practice_2.Add.add(-1, 1) == 0
#     assert practice_2.Add.add(0, 0) == 0
# def test_subtract():
#     assert practice_2.Sub.subtract(5, 3) == 2
#     assert practice_2.Sub.subtract(0, 0) == 0
#     assert practice_2.Sub.subtract(-1, -1) == 0


# def test_addition():
#     assert 1+1 == 2
# def test_subtraction():
#     assert 3-1 == 2


# def add(a, b):
#     """
#     Function to add two numbers.
#     >>> add(2, 3)
#     5
#     >>> add(-1, 1)
#     0
#     """
#     return a + b
# def subtract(a, b):
#     """
#     Function to subtract two numbers.
#     >>> subtract(5, 2)
#     3
#     >>> subtract(10, 5)
#     4
#     """
#     return a - b


# # test_reversal2.py
# import pytest
# def reverse_text(text):
#     if not isinstance(text, str):
#         raise ValueError('Expected a string')
#     return text[::-1]
# def test_reverse_text_non_string():
#     with pytest.raises(ValueError):
#         reverse_text(1234)


""" pytest with fixture"""
# import pytest
# from practice_2 import calculator
# @pytest.fixture
# def calc():
#     return calculator()
# def test_add(calc):
#     assert calc.add(2,3)==5
# def test_sub(calc):
#     assert calc.sub(7,2)==5
# def test_multiply(calc):
#     assert calc.multipy(2,3)==6
# def test_divide(calc):
#     assert calc.divide(8,2)==4
# def test_divide_by_zero(calc):
#     with pytest.raises(ValueError):
#         calc.divide(10,0)

"""pytest testing with marker"""
# import practice_2
# import pytest
# @pytest.mark.algebra # marker
# def test_square():
# 	assert practice_2.Algebra.square(40) == 1600
# 	assert practice_2.Algebra.square(5) == 25
# @pytest.mark.algebra
# def test_cube():
# 	assert practice_2.Algebra.cube(40) == 64000
# 	assert practice_2.Algebra.cube(5) == 125
# @pytest.mark.geometry
# def test_is_triangle():
# 	assert practice_2.Geometry.is_triangle(120, 40, 20) == True
# 	assert practice_2.Geometry.is_triangle(45, 67, 99) == False
# @pytest.mark.geometry
# def test_is_quadrilateral():
# 	assert practice_2.Geometry.is_quadrilateral(350, 5, 5, 0) == True
# 	assert practice_2.Geometry.is_quadrilateral(11, 22, 33, 44) == False

'''test_practice_2.py  " pytest with class" '''
# import practice_2
# class Test_Algebra: # making a class for testing the two tests belonging to the Algebra class
# 	def test_square(self):
# 		assert practice_2.Algebra.square(40) == 1600
# 		assert practice_2.Algebra.square(5) == 25
# 	def test_cube(self): # making a class for testing the two tests belonging to the Geometry class
# 		assert practice_2.Algebra.cube(40) == 64000
# 		assert practice_2.Algebra.cube(5) == 125
# class Test_Geometry:
# 	def test_is_triangle(self):
# 		assert practice_2.Geometry.is_triangle(120, 40, 20) == True
# 		assert practice_2.Geometry.is_triangle(45, 67, 99) == False
# 	def test_is_quadrilateral(self):
# 		assert practice_2.Geometry.is_quadrilateral(350, 5, 5, 0) == True
# 		assert practice_2.Geometry.is_quadrilateral(11, 22, 33, 44) == False

""" Nose Test """
# def test_addition():
#     assert 1+1 == 2
# def test_subtraction():
#     assert 2-1 == 1


# test_database.py
# import nose
# def setup():
#     pass
# def teardown():
#     pass
# @nose.with_setup(setup, teardown)
# def test_query():
#     pass

""" Testing Unittest """
# import unittest

# def add(a, b):
#     return a + b

# class TestAddFunction(unittest.TestCase):
#     def test_add_positive_numbers(self):
#         self.assertEqual(add(1, 2), 3)

#     def test_add_negative_numbers(self):
#         self.assertEqual(add(-1, -2), -3)

#     def test_add_mixed_numbers(self):
#         self.assertEqual(add(1, -2), -1)
#         self.assertEqual(add(-1, 2), 1)

# if __name__ == '__main__':
#     unittest.main()

import unittest

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        pass

    # Returns True if the string contains 4 a.
    def test_strings_a(self):
        self.assertEqual('a'*4, 'aaaa')

    # Returns True if the string is in upper case.
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_strip(self):
        s = 'geeksforgeeks'
        self.assertEqual(s.strip('geek'), 'sforgeeks')

    # Returns true if the string splits and matches
    # the given output.
    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
