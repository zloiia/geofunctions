import unittest
def load_src(name, fpath):
    import os, imp
    return imp.load_source(name, os.path.join(os.path.dirname(__file__), fpath))

load_src('functions','../functions.py')
from functions import *

class TestSequenceFunctions(unittest.TestCase):
	def setUp(self):
		pass

	def test_floatToList(self):
		self.assertEqual(fromFloatToList(55.547000), (55,32,82))


if __name__=='__main__':
	unittest.main()