import unittest

import {name}


class VersionTester(unittest.TestCase): 

   def test_major(self):
      self.assertEqual({name}.__version__[0], 0)

   def test_minor(self):
      self.assertEqual({name}.__version__[1], 1)

   def test_last(self):
      self.assertEqual({name}.__version__[2], 0)
