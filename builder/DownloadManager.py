import os


def __install_microcode():
    os.system("sudo mkinitcpio -P")

def __udpdate_system():
    os.system("sudo pacman -Sy --noconfirm")

def __clear_gnome():
    os.system("sudo pacman -D --noconfirm --asdeps $(pacman -Qqg gnome)")
    os.system("sudo pacman -D --noconfirm --asexplicit gnome-shell mutter gdm gnome-control-center gnome-console nautilus gnome-session gnome-settings-daemon gvfs gvfs-mtp")
    os.system("sudo pacman -Rsn --noconfirm $(pacman -Qqgdtt gnome)")

    os.system("sudo pacman -R --noconfirm htop")
    os.system("sudo pacman -R --noconfirm vim")

def __disable_timeout():
    os.system("sudo sed -i 's/\[options\]/\[options\]\nDisableDownloadTimeout/g' /etc/pacman.conf")


def __patch_multilib():
    os.system(r"sudo sed -i 's/^#\[multilib\]/[multilib]/' /etc/pacman.conf")
    os.system(r"sudo sed -i '/^\[multilib\]$/,/^\[/ s/^#\(Include = \/etc\/pacman\.d\/mirrorlist\)/\1/' /etc/pacman.conf")
    os.system("sudo pacman -Syu --noconfirm")

def __optimize_mirrors():
    os.system("sudo reflector --verbose --country 'Russia' -l 25 --sort rate --save /etc/pacman.d/mirrorlist")

def __install_yay():
    os.system("git -C /tmp clone https://aur.archlinux.org/yay.git")
    os.system("cd /tmp/yay && makepkg -si")

def __install_pacman_package(package_names: list):
    for package in package_names:
        os.system(f"sudo pacman -S --noconfirm {package}")
        print(f"Installed: {package}")


def __install_aur_package(package_names: list):
    for package in package_names:
        os.system(f"yay -S --noconfirm {package}")
        print(f"Installed: {package}")