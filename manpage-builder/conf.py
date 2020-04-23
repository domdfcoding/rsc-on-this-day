#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

sys.path.append(os.path.abspath('.'))
sys.path.append(os.path.abspath('..'))

from sphinx_shared import *

version = f"{modname} {__version__}"
copyright = (
		f"{__copyright__}. License GPLv3+: GNU GPL version 3 or later "
		f"<http://gnu.org/licenses/gpl.html>\n\n"
		"This is free software: you are free to change and redistribute it under certain conditions.\n\n"
		"There is NO WARRANTY, to the extent permitted by law."
		)

master_doc = 'manpage'
man_pages = [
		('manpage', slug, modname, [author], 1)
		]

# All other settings are in `sphinx_shared`
