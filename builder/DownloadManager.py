import os


def __install_microcode():
    os.system("sudo mkinitcpio -P")

def __install_sound_optimizer():
    os.system("systemctl --user enable --now pipewire pipewire-pulse wireplumber")
    os.system('sudo usermod -aG realtime "$USER"')

def __pacman_cash_cleaner():
    os.system("sudo systemctl enable paccache.timer")


def __inject_user_extensions():
    os.system("mv ~/ArchGnome/extensions ~/.local/share/gnome-shell")

def __inject_user_themes():
    os.system("mv ~/ArchGnome/themes/ ~/.user-themes/")
    os.system("gsettings set org.gnome.desktop.background picture-uri file://~/.user-themes/background.jpg")



def __change_gnome_settings_to_my():
    #Расскладка переключение
    os.system("gsettings set org.gnome.desktop.wm.keybindings switch-input-source \"['<Alt>Shift_L']\"")
    os.system("gsettings set org.gnome.desktop.wm.keybindings switch-input-source-backward \"['<Shift>Alt_L']\"")
    #Вернём кнопки на родину
    os.system('gsettings set org.gnome.desktop.wm.preferences button-layout \'appmenu:minimize,maximize,close\'')

    #Улучшаем визуал
    os.system('gsettings set org.gnome.desktop.interface gtk-enable-primary-paste false')
    os.system('gsettings set org.gnome.desktop.interface font-hinting \'full\'')

    #Авто выход с сесий не нужен
    os.system('gsettings set org.gnome.desktop.session idle-delay 0')
    os.system('gsettings set org.gnome.desktop.screensaver lock-enabled false')

    #Уведы не нужны
    os.system('gsettings set org.gnome.desktop.notifications show-in-lock-screen false')
    #Формат часов
    os.system('gsettings set org.gnome.desktop.interface clock-show-seconds true')
    #Процент заряда, для ноутбуков
    os.system('gsettings set org.gnome.desktop.interface show-battery-percentage true')
    #Горячие углы не нужны
    os.system('gsettings set org.gnome.desktop.interface enable-hot-corners false')
    #Белая тема - жуть
    os.system('gsettings set org.gnome.desktop.interface color-scheme \'prefer-dark\'')
    #Добавляем русский
    os.system("gsettings set org.gnome.desktop.input-sources sources \"[('xkb', 'us'), ('xkb', 'ru')]\"")
    #Для ноутов отключаем авто стоп экранов
    os.system("gsettings set org.gnome.settings-daemon.plugins.power idle-dim false")
    os.system("gsettings set org.gnome.settings-daemon.plugins.power sleep-inactive-battery-type 'nothing'")
    os.system("gsettings set org.gnome.settings-daemon.plugins.power sleep-inactive-ac-type 'nothing'")


def __ananicy_cpp_integration():
    os.system("sudo systemctl enable --now ananicy-cpp")
    os.system("git clone https://aur.archlinux.org/cachyos-ananicy-rules-git.git")
    os.system("cd cachyos-ananicy-rules-git && makepkg -sric --noconfirm")
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

    os.system("sudo pacman -R --noconfirm htop")
    os.system("sudo pacman -R --noconfirm vim")

    os.system("sudo pacman -D --noconfirm --asdeps $(pacman -Qqg gnome)")
    os.system("sudo pacman -D --noconfirm --asexplicit gnome-shell mutter gdm gnome-control-center gnome-console nautilus gnome-session gnome-settings-daemon gvfs gvfs-mtp")
    os.system("sudo pacman -Rsn --noconfirm $(pacman -Qqgdtt gnome)")


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
    os.system("cd /tmp/yay && makepkg -si --noconfirm")

def __install_pacman_package(package_names: list):
    for package in package_names:
        os.system(f"sudo pacman -S --noconfirm {package}")
        print(f"Installed: {package}")


def __install_aur_package(package_names: list):
    for package in package_names:
        os.system(f"yay -S --noconfirm --sudoloop {package}")
        print(f"Installed: {package}")