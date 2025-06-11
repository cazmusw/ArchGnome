import os

class MyConfigurationManager:

    @staticmethod
    def start():
        MyConfigurationManager.__clear_gnome()
        MyConfigurationManager.__change_gnome_settings_to_my()
        MyConfigurationManager.__inject_user_themes()
        MyConfigurationManager.__inject_user_extensions()


    @staticmethod
    def __clear_gnome():
        os.system("sudo pacman -R --noconfirm htop")
        os.system("sudo pacman -R --noconfirm vim")

        os.system("sudo pacman -D --noconfirm --asdeps $(pacman -Qqg gnome)")
        os.system("sudo pacman -D --noconfirm --asexplicit gnome-shell mutter gdm gnome-control-center gnome-console nautilus gnome-session gnome-settings-daemon gvfs gvfs-mtp")
        os.system("sudo pacman -Rsn --noconfirm $(pacman -Qqgdtt gnome)")


    @staticmethod
    def __inject_user_extensions():
        os.system("mv extensions ~/.local/share/gnome-shell")

    @staticmethod
    def __inject_user_themes():
        home_dir = os.path.expanduser("~")
        os.system("mv themes/ ~/.user-themes/")
        os.system(f"gsettings set org.gnome.desktop.background picture-uri-dark file://{home_dir}/.user-themes/wallpaper.jpg")


    @staticmethod
    def __change_gnome_settings_to_my():
        os.system("gsettings set org.gnome.desktop.wm.keybindings switch-input-source \"['<Alt>Shift_L']\"")
        os.system("gsettings set org.gnome.desktop.wm.keybindings switch-input-source-backward \"['<Shift>Alt_L']\"")
        os.system('gsettings set org.gnome.desktop.wm.preferences button-layout \'appmenu:minimize,maximize,close\'')
        os.system('gsettings set org.gnome.desktop.interface gtk-enable-primary-paste false')
        os.system('gsettings set org.gnome.desktop.interface font-hinting \'full\'')
        os.system('gsettings set org.gnome.desktop.session idle-delay 0')
        os.system('gsettings set org.gnome.desktop.screensaver lock-enabled false')
        os.system('gsettings set org.gnome.desktop.notifications show-in-lock-screen false')
        os.system('gsettings set org.gnome.desktop.interface clock-show-seconds true')
        os.system('gsettings set org.gnome.desktop.interface show-battery-percentage true')
        os.system('gsettings set org.gnome.desktop.interface enable-hot-corners false')
        os.system('gsettings set org.gnome.desktop.interface color-scheme \'prefer-dark\'')
        os.system("gsettings set org.gnome.desktop.input-sources sources \"[('xkb', 'us'), ('xkb', 'ru')]\"")
        os.system("gsettings set org.gnome.settings-daemon.plugins.power idle-dim false")
        os.system("gsettings set org.gnome.settings-daemon.plugins.power sleep-inactive-battery-type 'nothing'")
        os.system("gsettings set org.gnome.settings-daemon.plugins.power sleep-inactive-ac-type 'nothing'")

