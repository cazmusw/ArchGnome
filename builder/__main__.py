import packages
import Utils

from managers.mysetup import MyConfigurationManager
from managers.patches import PatchManager
from managers.services import ServicesManager
from managers.jetbrains import JetbrainsManager

def main():

    print("Instalation started...")

    Utils.__install_pacman_package(packages.REFLECTOR)
    Utils.__optimize_mirrors()

    Utils.__install_yay()

    MyConfigurationManager.start()

    Utils.__install_pacman_package(packages.BASE_PACKAGES)
    Utils.__install_pacman_package(packages.MY_DRIVERS)
    Utils.__install_pacman_package(packages.MY_PROGRAMS)


    Utils.__install_aur_package(packages.AUR_PACKAGES)

    PatchManager.start()
    ServicesManager.start()
    JetbrainsManager.start()

    Utils.__after_install_clear()

    print("Installation End")


if __name__ == "__main__":
    main()