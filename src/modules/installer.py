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
import os


def install_pkgs():
	pkgs = [
		{
			'fullname': 'Network Map',
			'pkg_name': 'nmap',
			'description': 'Сканнер портов'
		},
		{
			'fullname': 'Aircrack-ng',
			'pkg_name': 'aircrack-ng',
			'description': 'Набор программ для обнаружения беспроводных сетей, перехвата через беспроводные сети трафика, аудита WEP и WPA/WPA2-PSK ключей шифрования'
		},
		{
			'fullname': 'Net Tools',
			'pkg_name': 'net-tools',
			'description': 'Набор инструментов для взаимодействия с сетью'
		}
	]

	for pkg in pkgs:
		print(f'Установка {pkg["pkg_name"]}')
		print(f'{pkg["fullname"]}: {pkg["description"]}')
		os.system(f'sudo apt install -y {pkg["pkg_name"]}')
