import unittest
import sys
sys.path.append('..')
from FirstTest import FirstTest

class FirstTestTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(FirstTestTest, self).__init__(*args, **kwargs)
        self.firstTest = FirstTest()


    def testString(self):
        self.assertEqual('hello world', self.firstTest.testOne())


if __name__ == '__main__':
    unittest.main()
