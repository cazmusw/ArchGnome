import os
import packages
import DownloadManager





def main():

    downloadDrivers = input("Скачать драйвера? (y = yes) ") == 'y'
    downloadPrograms = input("Скачать мои программы? (y = yes) ") == 'y'


    print("Installation Start")

    DownloadManager.__gnome_optimizer()
    DownloadManager.__clear_gnome()
    DownloadManager.__updater_system()

    #Включение мультибиблиотек
    DownloadManager.__patch_multilib()

    #Выключение таймаута
    DownloadManager.__disable_timeout()

    #Устанавливаем первые пакеты для дальнейшей быстрой установки
    DownloadManager.__install_pacman_package(packages.FAST_PACKAGES)
    DownloadManager.__optimize_mirrors()

    #Устанавливаем пакеты базовые
    DownloadManager.__install_pacman_package(packages.BASE_PACKAGES)

    if downloadDrivers:
        # Микрокод установка
        DownloadManager.__install_microcode()
        DownloadManager.__install_pacman_package(packages.MY_DRIVERS)

    if downloadPrograms:
        DownloadManager.__install_pacman_package(packages.MY_PROGRAMS)

    #Task manager
    DownloadManager.__ananicy_cpp_integration()
    #Disk cleaner
    DownloadManager.__disk_optimizer()
    #Optimize system
    DownloadManager.__irqbalance_integration()

    DownloadManager.__init_build_optimizer()



    #Установка аур и его пакетов
    DownloadManager.__install_yay()
    DownloadManager.__install_pacman_package(packages.AUR_PACKAGES)
    DownloadManager.__install_sound_optimizer()
    DownloadManager.__pacman_cash_cleaner()

    print("Installation End")


if __name__ == "__main__":
    main()