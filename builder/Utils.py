import os

def __install_yay():
    os.system("sudo -u $(logname) git -C /tmp clone https://aur.archlinux.org/yay.git")
    os.system("cd /tmp/yay && sudo -u $(logname) makepkg -si --noconfirm")

def __install_pacman_package(package_names: list):
    for package in package_names:
        os.system(f"sudo pacman -S --noconfirm {package}")
        print(f"Installed: {package}")


def __install_aur_package(package_names: list):
    for package in package_names:
        os.system(f"sudo -u $(logname) yay -S --noconfirm --sudoloop {package}")
        print(f"Installed: {package}")