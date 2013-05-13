#!/usr/bin/python
import unittest

class Test(unittest.TestCase):
    def test_basic_addition(self):
        self.failUnlessEqual(1+1,2)
        
    
if __name__ == "__main__":
    unittest.main() # run all tests
