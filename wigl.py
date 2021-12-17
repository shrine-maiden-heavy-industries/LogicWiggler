#!/usr/bin/env python3
# SPDX-License-Identifier: BSD-3-Clause
import sys
import os
from pathlib import Path

wigl_path = Path(sys.argv[0]).resolve()


if (wigl_path.parent / 'logic_wiggler').is_dir():
	sys.path.insert(0, str(wigl_path.parent))

from logic_wiggler import main

if __name__ == '__main__':
	sys.exit(main())

