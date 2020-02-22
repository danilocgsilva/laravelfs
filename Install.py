from src.Install import Install
from shutil import copy
import os

install = Install()
install.setOs(os)
installingPath = install.getExecutablePath()

install_source = os.path.join('install_assets', install.getProgramEntry())
install_destiny = os.path.join(install.getExecutablePath(), install.getProgramEntry())

copy(install_source, install_destiny)