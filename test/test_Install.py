import unittest
import sys
from OsMocker import OsMocker
sys.path.append('..')
from src.Install import Install
from src.InstallException import InstallException

class test_Install(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(test_Install, self).__init__(*args, **kwargs)
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

    
    def testGetProgramEntryForMac(self):

        self.osMocker.setSystem('mac')
        self.install.setOs(self.osMocker)

        expectedEntryProgram = 'laravelfs'

        self.assertEqual(expectedEntryProgram, self.install.getProgramEntry())


    def testGetProgramEntryForLinux(self):

        self.osMocker.setSystem('linux')
        self.install.setOs(self.osMocker)

        expectedEntryProgram = 'laravelfs'

        self.assertEqual(expectedEntryProgram, self.install.getProgramEntry())
        

    def testGetProgramEntryForWindows(self):

        self.osMocker.setSystem('windows')
        self.install.setOs(self.osMocker)

        expectedEntryProgram = 'laravelfs.cmd'

        self.assertEqual(expectedEntryProgram, self.install.getProgramEntry())


    def testThrowExceptionIfTriesUseGetExecutablePathWithoutSettingOs(self):
        with self.assertRaises(InstallException):
            executablePath = self.install.getExecutablePath()


    def testThrowExceptionIfTriesUseGetProgramEntryWithoutSettingOs(self):
        with self.assertRaises(InstallException):
            executablePath = self.install.getProgramEntry()




if __name__ == '__main__':
    unittest.main()
