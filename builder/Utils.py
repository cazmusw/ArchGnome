import os

def __install_yay():
    input("You need to enter password. Press enter to continue...")
    os.system("sudo -u $(logname) git -C /tmp clone https://aur.archlinux.org/yay.git")
    os.system("cd /tmp/yay && sudo -u $(logname) makepkg -si --noconfirm")


def __optimize_mirrors():
    os.system("sudo reflector --verbose -l 25 --sort rate --save /etc/pacman.d/mirrorlist")

def __install_pacman_package(package_names: list):
    for package in package_names:
        os.system(f"sudo pacman -S --noconfirm {package}")
        print(f"Installed: {package}")


def __install_aur_package(package_names: list):
    input("You need to enter password. Press enter to continue...")
    for package in package_names:
        os.system(f"sudo -u $(logname) yay -S --noconfirm --sudoloop {package}")
        print(f"Installed: {package}")