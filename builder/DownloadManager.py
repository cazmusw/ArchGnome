import os


def __install_microcode():
    os.system("sudo mkinitcpio -P")

def __install_sound_optimizer():
    os.system("systemctl --user enable --now pipewire pipewire-pulse wireplumber")
    os.system('sudo usermod -aG realtime "$USER"')

def __pacman_cash_cleaner():
    os.system("sudo systemctl enable paccache.timer")


def __ananicy_cpp_integration():
    os.system("sudo systemctl enable --now ananicy-cpp")
    os.system("git clone https://aur.archlinux.org/cachyos-ananicy-rules-git.git")
    os.system("cd cachyos-ananicy-rules-git && sudo -u nobody makepkg -sric --noconfirm")
    os.system("sudo systemctl restart ananicy-cpp")

def __disk_optimizer():
    os.system("sudo systemctl enable fstrim.timer")

def __irqbalance_integration():
    os.system("sudo systemctl enable --now irqbalance")

def __gnome_optimizer():
    os.system("systemctl --user mask org.gnome.SettingsDaemon.Wacom.service")
    os.system("systemctl --user mask org.gnome.SettingsDaemon.PrintNotifications.service")
    os.system("systemctl --user mask org.gnome.SettingsDaemon.ScreensaverProxy.service")
    os.system("systemctl --user mask org.gnome.SettingsDaemon.Sharing.service")
    os.system("systemctl --user mask org.gnome.SettingsDaemon.Smartcard.service")

def __init_build_optimizer():
    os.system("mv ~/ArchGnome/configs/.makepkg.conf ~/")


def __updater_system():
    os.system("sudo pacman -Sy --noconfirm")
    os.system("sudo systemctl enable --now archlinux-keyring-wkd-sync.timer")

def __clear_gnome():
    os.system("sudo pacman -D --noconfirm --asdeps $(pacman -Qqg gnome)")
    os.system("sudo pacman -D --noconfirm --asexplicit gnome-shell mutter gdm gnome-control-center gnome-console nautilus gnome-session gnome-settings-daemon gvfs gvfs-mtp")
    os.system("sudo pacman -Rsn --noconfirm $(pacman -Qqgdtt gnome)")

    os.system("sudo pacman -R --noconfirm htop")
    os.system("sudo pacman -R --noconfirm vim")

def __disable_timeout():
    os.system(r"sudo sed -i 's/\[options\]/\[options\]\nDisableDownloadTimeout/g' /etc/pacman.conf")


def __patch_multilib():
    os.system(r"sudo sed -i 's/^#\[multilib\]/[multilib]/' /etc/pacman.conf")
    os.system(r"sudo sed -i '/^\[multilib\]$/,/^\[/ s/^#\(Include = \/etc\/pacman\.d\/mirrorlist\)/\1/' /etc/pacman.conf")
    os.system("sudo pacman -Sl --noconfirm multilib")
    os.system("sudo pacman -Sy --noconfirm")

def __optimize_mirrors():
    os.system("sudo reflector --verbose --country 'Russia' -l 25 --sort rate --save /etc/pacman.d/mirrorlist")

def __install_yay():
    os.system("git -C /tmp clone https://aur.archlinux.org/yay.git")
    os.system("cd /tmp/yay && sudo -u nobody makepkg -si --noconfirm")

def __install_pacman_package(package_names: list):
    for package in package_names:
        os.system(f"sudo pacman -S --noconfirm {package}")
        print(f"Installed: {package}")


def __install_aur_package(package_names: list):
    for package in package_names:
        os.system(f"sudo -u nobody yay -S --noconfirm {package}")
        print(f"Installed: {package}")