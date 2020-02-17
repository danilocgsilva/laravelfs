from OsMocker import OsMocker
import unittest 

class OsMockerTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(OsMockerTest, self).__init__(*args, **kwargs)
        self.osMocker = OsMocker


    def testSetSystemNotAllowedSystem(self):
        self.assertRaises(Exception, self.osMocker.setSystem('not_exists'))
        

if __name__ == '__main__':
    unittest.main()
