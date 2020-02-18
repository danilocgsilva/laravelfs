import unittest
import sys
sys.path.append('..')
from Install import Install

class InstallTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(InstallTest, self).__init__(*args, **kwargs)
        self.install = Install()

if __name__ == '__main__':
    unittest.main()
