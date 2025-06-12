import os

def __install_yay():
    input("You need to enter password. Press enter to continue...")
    os.system("git -C /tmp clone https://aur.archlinux.org/yay.git")
    os.system("cd /tmp/yay && makepkg -si --noconfirm")

def __patch_multilib():
    os.system(r"sudo sed -i 's/^#\[multilib\]/[multilib]/' /etc/pacman.conf")
    os.system(r"sudo sed -i '/^\[multilib\]$/,/^\[/ s/^#\(Include = \/etc\/pacman\.d\/mirrorlist\)/\1/' /etc/pacman.conf")
    os.system("sudo pacman -Sl --noconfirm multilib")
    os.system("sudo pacman -Sy --noconfirm")

def __after_install_clear():
    os.system("sudo pacman -Syu --noconfirm")
    os.system("sudo pacman -Scc --noconfirm")

def __optimize_mirrors():
    os.system("sudo reflector --verbose --country 'Russia' -l 25 --sort rate --save /etc/pacman.d/mirrorlist")

def __install_pacman_package(package_names: list):
    for package in package_names:
        os.system(f"sudo pacman -S --noconfirm {package}")
        print(f"Installed: {package}")


def __install_aur_package(package_names: list):
    input("You need to enter password. Press enter to continue...")
    for package in package_names:
        os.system(f"yay -S --noconfirm --sudoloop {package}")
        print(f"Installed: {package}")