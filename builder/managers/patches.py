import os


class PatchManager:

    @staticmethod
    def start():
        PatchManager.__patch_timeout()
        PatchManager.__patch_build_system()
        PatchManager.__patch_nvidia_to_cpu_access()
        PatchManager.__patch_zram_config()


    @staticmethod
    def __patch_zram_config():
        os.system("sudo sh -c 'echo zram-size = ram >> /etc/systemd/zram-generator.conf'")
        os.system("sudo sh -c 'echo compression-algorithm = zstd >> /etc/systemd/zram-generator.conf'")
        os.system("sudo sh -c 'echo swap-priority = 100 >> /etc/systemd/zram-generator.conf'")
        os.system("sudo sh -c 'echo fs-type = swap >> /etc/systemd/zram-generator.conf'")
        os.system("sudo systemctl daemon-reload")
        os.system("sudo systemctl start systemd-zram-setup@zram0.service")


    @staticmethod
    def __patch_nvidia_to_cpu_access():
        os.system("sudo sh -c 'echo options nvidia NVreg_UsePageAttributeTable=1 >> /etc/modprobe.d/nvidia-pat.conf'")


    @staticmethod
    def __patch_timeout():
        os.system(r"sudo sed -i 's/\[options\]/\[options\]\nDisableDownloadTimeout/g' /etc/pacman.conf")

    @staticmethod
    def __patch_build_system():
        os.system("mv configs/.makepkg.conf ~/")