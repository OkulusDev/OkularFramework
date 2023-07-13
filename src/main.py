#!/usr/bin/python3
"""Okular Framework - is a program for interacting with the Internet, for conducting penetration testing, working with Linux and OSINT
Copyright (C) 2022, 2023 Okulus Dev (Alexeev Bronislav)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>."""
import sys

# Внешние библиотеки
from colorama import init, Fore, Style

# Внутренние модули
from modules import installer
from modules import net

LICENSE = '''Okular Framework  Copyright (C) 2022, 2023  OkularDev
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions.
'''


def main():
	"""Функция, запускаемая при старте самого файла"""
	init()
	print('''
                   \\_|_/
                --  \\*/  -- 
                   _/|\\_
                   /\\|/\\
                  /\\/|\\/\\
                 /\\/\\|/\\/\\
               _/   _|_   \\_
               -     -     -

        OKULUS FRAMEWORK   --> By OkulusDev <--
   Твой проводник в мир интернета и белого хакинга
		''')

	# Проверяем, есть ли аргументы командной строки
	if len(sys.argv) > 1:
		# Проверяем команду

		if sys.argv[1] == '--help':
			# Команда вызова справки
			print('Справка Okular Framework')
			print('''
    --help - вызов данной справки комманд
    --install/-i - установка программ
    --interactive-mode/-im - интерактивный режим псевдо командной строки
				''')
		elif sys.argv[1] == '--install' or sys.argv[1] == '-i':
			print('[+] Запускаем программу установки утилит для Debian/Ubuntu-based дистрибутивов')
			installer.install_pkgs()
		elif sys.argv[1] == '--changemac' or sys.argv[1] == '-cm':
			print('[+] Запускаем скрипт для изменения MAC-адреса')
		else:
			print(f'[!] Команда {sys.argv[1]} не найдена')
	else:
		print('[!] Введите аргумент. Для вызова справки запустите с флагом --help')


if __name__ == '__main__':
	"""Запускаем функцию main"""
	print(LICENSE)
	main()
