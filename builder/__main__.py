import os
import packages
import DownloadManager





def main():

    downloadDrivers = input("Скачать драйвера") == 'y'
    downloadPrograms = input("Скачать мои программы") == 'y'


    print("Installation Start")

    DownloadManager.__clear_gnome()

    DownloadManager.__udpdate_system()

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


    #Установка аур и его пакетов
    DownloadManager.__install_yay()
    DownloadManager.__install_pacman_package(packages.AUR_PACKAGES)

    print("Installation End")


if __name__ == "__main__":
    main()