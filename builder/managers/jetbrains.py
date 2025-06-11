import os


class JetbrainsManager:

    @staticmethod
    def start():
        JetbrainsManager.__install_jetbrains_toolbox()
        JetbrainsManager.__inject_jetbrains_bypass()

    @staticmethod
    def __install_jetbrains_toolbox():
        os.system("apps/jetbrains-toolbox")

    @staticmethod
    def __inject_jetbrains_bypass():
        os.system("mv jetbra/ ~/.jetbra/")
        os.system("sh ~/.jetbra/scripts/jetbrains-bypass.sh")