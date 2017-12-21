# -*- coding: utf-8 -*-

import sys
from pycoinmon.common import Colors
if sys.version_info >= (3, 0):
    import io
else:
    import StringIO as io


ascii_title = """
                ___     ___    __     ___      ___ ___      ___     ___
   ___  __ __  /'___\  / __`\ /\_\  /' _ `\  /' __` __`\   / __`\ /' _ `\\
  / _ \/ // / /\ \__/ /\ \_\ \\\\/\ \ /\ \/\ \ /\ \/\ \/\ \ /\ \_\ \/\ \/\ \\
 / .__/\_, /  \ \____\\\\ \____/ \ \ \\\\ \_\ \_\\\\ \_\ \_\ \_\\\\ \____/\ \_\ \_\\
/_/   /___/    \/____/ \/___/   \/_/ \/_/\/_/ \/_/\/_/\/_/ \/___/  \/_/\/_/

"""


def process_title(title):
    buf = io.StringIO(title)
    lines = buf.readlines()
    lines = lines[1:-1]
    colored_lines = []
    colored_title = ""

    for line in lines:
        colored_lines.append(Colors.BLUE + line[:13] + Colors.YELLOW + line[14:])

    for line in colored_lines:
        colored_title += line

    return colored_title + Colors.ENDLINE
