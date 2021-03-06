# -*- coding: utf-8 -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import click
import sys

from .application import App


@click.command()
def upload():
    app = App()
    app.upload_emx_file()


@click.group()
def main(args=None):
    """Command line utility"""


main.add_command(upload)


if __name__ == "__main__":
    sys.exit(main())
