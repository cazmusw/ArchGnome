import os
import packages

def main():

    print("Installation Start")

    __clear_gnome()

    os.system("sudo pacman -Sy")

    #Включение мультибиблиотек
    __patch_multilib()
    os.system("sudo pacman -Syu")

    #Мультизагрузка
    os.system("sudo sed -i 's/#ParallelDownloads = 4/ParallelDownloads = 4/g' /etc/pacman.conf")

    #Мультизагрузка
    os.system("sudo sed -i 's/\[options\]/\[options\]\nDisableDownloadTimeout/g' /etc/pacman.conf")

    #Устанавливаем первые пакеты для дальнейшей быстрой установки
    __install_pacman_package(packages.FAST_PACKAGES)
    __optimize_mirrors()

    #Устанавливаем пакеты базовые
    __install_pacman_package(packages.BASE_PACKAGES)

    #Установка аур и его пакетов
    __install_yay()
    __install_pacman_package(packages.AUR_PACKAGES)




if __name__ == "__main__":
    main()

def __clear_gnome():
    os.system("sudo pacman -D --noconfirm --asdeps $(pacman -Qqg gnome)")
    os.system("sudo pacman -D --noconfirm --asexplicit gnome-shell mutter gdm gnome-control-center gnome-console nautilus gnome-session gnome-settings-daemon gvfs gvfs-mtp")
    os.system("sudo pacman -Rsn --noconfirm $(pacman -Qqgdtt gnome)")


def __patch_multilib():
    os.system(r"sudo sed -i 's/^#\[multilib\]/[multilib]/' /etc/pacman.conf")
    os.system(r"sudo sed -i '/^\[multilib\]$/,/^\[/ s/^#\(Include = \/etc\/pacman\.d\/mirrorlist\)/\1/' /etc/pacman.conf")

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