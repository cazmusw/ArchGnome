import os




class ServicesManager:

    @staticmethod
    def start():
        ServicesManager.__init_pacman_cash_cleaner()
        ServicesManager.__inject_sound_optimizer()
        ServicesManager.__irqbalance_integration()
        ServicesManager.__disk_optimizer()
        ServicesManager.__ananicy_cpp_integration()
        ServicesManager.__install_microcode()

    @staticmethod
    def __init_pacman_cash_cleaner():
        os.system("sudo systemctl enable paccache.timer")

    @staticmethod
    def __inject_sound_optimizer():
        os.system("systemctl --user enable --now pipewire pipewire-pulse wireplumber")
        os.system('sudo usermod -aG realtime "$USER"')

    @staticmethod
    def __irqbalance_integration():
        os.system("sudo systemctl enable --now irqbalance")

    @staticmethod
    def __disk_optimizer():
        os.system("sudo systemctl enable fstrim.timer")

    @staticmethod
    def __ananicy_cpp_integration():
        os.system("sudo systemctl enable --now ananicy-cpp")
        os.system("sudo -u $(logname) git clone https://aur.archlinux.org/cachyos-ananicy-rules-git.git")
        os.system("cd cachyos-ananicy-rules-git && sudo -u $(logname) makepkg -sric --noconfirm")
        os.system("sudo systemctl restart ananicy-cpp")

    @staticmethod
    def __install_microcode():
        os.system("sudo mkinitcpio -P")