import os


class PatchManager:

    @staticmethod
    def start():
        PatchManager.__patch_multilib()
        PatchManager.__patch_timeout()
        PatchManager.__patch_build_system()


    @staticmethod
    def __patch_multilib():
        os.system(r"sudo sed -i 's/^#\[multilib\]/[multilib]/' /etc/pacman.conf")
        os.system(r"sudo sed -i '/^\[multilib\]$/,/^\[/ s/^#\(Include = \/etc\/pacman\.d\/mirrorlist\)/\1/' /etc/pacman.conf")
        os.system("sudo pacman -Sl --noconfirm multilib")

    @staticmethod
    def __patch_timeout():
        os.system(r"sudo sed -i 's/\[options\]/\[options\]\nDisableDownloadTimeout/g' /etc/pacman.conf")

    @staticmethod
    def __patch_build_system():
        os.system("mv ~/ArchGnome/configs/.makepkg.conf ~/")