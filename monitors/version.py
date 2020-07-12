# -*- coding: utf-8 -*-
__version__ = "1.0.1"

import os
import sys


def get_monitors_version():
    pip_pkg_dir = os.path.join(os.path.dirname(__file__), "..", "..")
    pip_pkg_dir = os.path.abspath(pip_pkg_dir)

    return (
        'monitors {} from {} (python {})'.format(
            __version__, pip_pkg_dir, sys.version[:3],
        )
    )


def show_version():
    sys.stdout.write(get_monitors_version())
    sys.stdout.write(os.linesep)
    sys.exit()