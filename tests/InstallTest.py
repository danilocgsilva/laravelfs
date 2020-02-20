import unittest
import sys
from OsMocker import OsMocker
sys.path.append('..')
from Install import Install

class InstallTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(InstallTest, self).__init__(*args, **kwargs)
        self.install = Install()
        self.osMocker = OsMocker()


    def testGetInstallingPathForWindows(self):

        self.osMocker.setSystem('windows')
        self.install.setOs(self.osMocker)

        windowsPath = "C:/Windows"
        self.assertEqual(windowsPath, self.install.getInstallingPath())


    def testGetInstallingPathForMac(self):

        self.osMocker.setSystem('mac')
        self.install.setOs(self.osMocker)

        macPath = "/usr/local/bin"
        self.assertEqual(macPath, self.install.getInstallingPath())


    def testGetInstallingPathForLinux(self):

        self.osMocker.setSystem('linux')
        self.install.setOs(self.osMocker)

        linuxPath = "/usr/local/bin"

        print(linuxPath)
        print(self.install.getInstallingPath())

        self.assertEqual(linuxPath, self.install.getInstallingPath())





if __name__ == '__main__':
    unittest.main()
