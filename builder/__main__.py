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

    #Disk cleaner
    DownloadManager.__disk_optimizer()
    #Optimize system
    DownloadManager.__irqbalance_integration()
    DownloadManager.__init_build_optimizer()


    input("Остановочная точка, далее потребуется подтверждать установку, будьте у экрана")

    #Task manager
    DownloadManager.__ananicy_cpp_integration()
    #Установка аур и его пакетов
    DownloadManager.__install_yay()
    if downloadPrograms:
        DownloadManager.__install_aur_package(packages.AUR_PACKAGES)
    DownloadManager.__install_sound_optimizer()
    DownloadManager.__pacman_cash_cleaner()


    #Post install
    DownloadManager.__change_gnome_settings_to_my()
    DownloadManager.__inject_user_extensions()
    DownloadManager.__inject_user_themes()

    DownloadManager.__jetbrains_bypass()

    print("Installation End")


if __name__ == "__main__":
    main()