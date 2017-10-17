#!/usr/bin/python
# coding=utf-8

# Simple Steam profile checker Telegram bot
# Copyright (c) 2017 EasyCoding Team
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from setuptools import setup, find_packages

setup(
    name='stmbot',
    version='0.1',
    packages=find_packages(),
    package_dir={
        'stmbot': 'stmbot',
    },
    url='https://github.com/xvitaly/stmbot',
    license='GPLv3',
    entry_points={
        'console_scripts': [
            'stmbot = stmbot.scripts.runbot:main',
        ],
    },
    install_requires=['pytelegrambotapi'],
    author='Vitaly Zaitsev',
    author_email='vitaly@easycoding.org',
    description='Simple Steam profile checker bot'
)
