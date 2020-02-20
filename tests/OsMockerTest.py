from OsMocker import OsMocker
import unittest 

class OsMockerTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(OsMockerTest, self).__init__(*args, **kwargs)
        self.osMocker = OsMocker()


    def testSetSystemNotAllowedSystem(self):
        with self.assertRaises(Exception):
            self.assertRaises(Exception, self.osMocker.setSystem('not_exists'))


    def testReturnCorrectNameForWindows(self):
        self.osMocker.setSystem('windows')
        self.assertEqual('nt', self.osMocker.name)


    def testReturnCorrectNameForMac(self):
        self.osMocker.setSystem('mac')
        self.assertEqual('darwin', self.osMocker.name)


    def testReturnCorrectNameForLinux(self):
        self.osMocker.setSystem('linux')
        self.assertEqual('posix', self.osMocker.name)
        

if __name__ == '__main__':
    unittest.main()
