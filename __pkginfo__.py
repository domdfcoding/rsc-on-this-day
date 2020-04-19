# Copyright (C) 2019-2020 Dominic Davis-Foster <dominic@davis-foster.co.uk>
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.

# This script based on https://github.com/rocky/python-uncompyle6/blob/master/__pkginfo__.py

import pathlib

copyright = """
2019 Dominic Davis-Foster <dominic@davis-foster.co.uk>
"""

VERSION = "0.2.1"

modname = "rsc_on_this_day"
py_modules = [modname]
entry_points = {
		'console_scripts': [
				f'rsc_on_this_day=rsc_on_this_day:main',
				]
		}

license = 'GPLv3'

short_desc = 'Displays Royal Society of Chemistry "On This Day" fact'

classifiers = [
		'Development Status :: 3 - Alpha',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
		'Operating System :: OS Independent',
		'Programming Language :: Python',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		'Programming Language :: Python :: 3.8',
		'Topic :: Software Development :: Libraries :: Python Modules',
		]

author = "Dominic Davis-Foster"
author_email = "dominic@davis-foster.co.uk"
github_username = "domdfcoding"
web = github_url = f"https://github.com/{github_username}/{modname}"


# Get info from files; set: long_description
if pathlib.Path.cwd().name in {"doc-source", "manpage-builder"}:
	install_requires = (pathlib.Path.cwd().parent / "requirements.txt").read_text().split("\n")
	long_description = (pathlib.Path.cwd().parent / "README.rst").read_text() + '\n'
else:
	install_requires = pathlib.Path("requirements.txt").read_text().split("\n")
	long_description = pathlib.Path("README.rst").read_text() + '\n'
