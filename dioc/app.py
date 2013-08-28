# -*- coding: utf-8 -*-


"""
   dioc.app
   ~~~~~~~~

   The main dioc application.
"""


from __future__ import absolute_import

import logging
import sys

from cliff.app import App
from cliff.commandmanager import CommandManager


def main(argv=sys.argv[1:]):
    """Entry point for console."""

    import dioc

    desc = sys.modules['dioc'].__doc__.split('\n')[-2].strip()
    ver = dioc.version()
    ns = 'dioc.core'

    app = Dioc(desc, ver, ns)
    return app.run(argv)


class Dioc(App):

    log = logging.getLogger(__name__)

    def __init__(self, description, version, namespace):
        super(Dioc, self).__init__(
            description=description,
            version=version,
            command_manager=CommandManager(namespace)
        )

