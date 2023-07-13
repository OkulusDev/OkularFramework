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
import re
import subprocess
import socket
from random import choice
import requests


def change_mac(interface: str, new_mac_address: str) -> None:
	"""Функция для изменения MAC-адреса при помощи утилиты ifconfig

	Аргументы:
	 + interface: str - название интерфейса (ex. wlan0, wlp1s0, wlp3s0, eth)
	 + new_mac_address - значение нового mac-адреса"""
	subprocess.call(["sudo", "ifconfig", interface, "down"])
	subprocess.call(["sudo", 'ifconfig', interface, 'hw', 'ether', new_mac_address])
	subprocess.call(["sudo", "ifconfig", interface, "up"])


def get_random_mac_address() -> str:
	"""Функция генерации и получения случайного mac-адреса.
	У нас есть словарь с числами от 0 до 9, и латинских букв от a до f, а также начало
	нового mac-адреса (00). После мы проходимся в итерационном цикле и добавляем 5 раз еще 
	по паре символов, а после возвращаем

	Возвращает:
	 + str - новый mac-адрес"""
	characters = list("1234567890abcdef")
	random_mac_address = "00"

	for i in range(5):
		random_mac_address += ':' + choice(characters) + choice(characters)

	return random_mac_address


def get_current_mac(interface: str):
	"""Получаем текущий MAC-адрес при помощи утилиты ifconfig"""
	output = subprocess.check_output(["ifconfig", interface])

	return re.search("\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(output)).group(0)


def launch_mac_changing(interface, ):
	print()
