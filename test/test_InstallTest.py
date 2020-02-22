import unittest
import sys
from OsMocker import OsMocker
sys.path.append('..')
from src.Install import Install

class InstallTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(InstallTest, self).__init__(*args, **kwargs)
        self.install = Install()
        self.osMocker = OsMocker()


    def testGetExecutablePathForWindows(self):

        self.osMocker.setSystem('windows')
        self.install.setOs(self.osMocker)

        windowsPath = "C:\Windows"
        self.assertEqual(windowsPath, self.install.getExecutablePath())


    def testGetExecutablePathForMac(self):

        self.osMocker.setSystem('mac')
        self.install.setOs(self.osMocker)

        macPath = "/usr/local/bin"
        self.assertEqual(macPath, self.install.getExecutablePath())


    def testGetExecutablePathForLinux(self):

        self.osMocker.setSystem('linux')
        self.install.setOs(self.osMocker)

        linuxPath = "/usr/local/bin"

        print(linuxPath)
        print(self.install.getExecutablePath())

        self.assertEqual(linuxPath, self.install.getExecutablePath())





if __name__ == '__main__':
    unittest.main()
