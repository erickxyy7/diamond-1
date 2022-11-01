import unittest
import sys

sys.path.insert(0, '..')

from infix_to_postfix import expr_infix_to_postfix

class Tests(unittest.TestCase):
	
	def test_expr_infix_to_postfix(self):
		self.assertEqual(expr_infix_to_postfix(['4', '+', '5.7']), ['4', '5.7', '+'])
		self.assertEqual(expr_infix_to_postfix(['(', '4', '+', '4', ')', '*', '7']), ['4', '4', '+', '7', '*'])

unittest.main()
