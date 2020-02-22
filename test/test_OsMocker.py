from OsMocker import OsMocker
import unittest 

class test_OsMocker(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(test_OsMocker, self).__init__(*args, **kwargs)
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


    def testSeparatorForWindows(self):
        self.osMocker.setSystem('windows')
        self.assertEqual('\\', self.osMocker.sep)


    def testSeparatorForMac(self):
        self.osMocker.setSystem('mac')
        self.assertEqual('/', self.osMocker.sep)


    def testSeparatorForMac(self):
        self.osMocker.setSystem('linux')
        self.assertEqual('/', self.osMocker.sep)
        

if __name__ == '__main__':
    unittest.main()
