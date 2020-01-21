import unittest

cimport {name}.{name} as c{name}

class Cimpor_{name}_Tester(unittest.TestCase): 

    def test_cimport_getit(self):
        self.assertEqual(c{name}.getit(), 21)
