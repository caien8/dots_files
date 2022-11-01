import os
import re
import socket
import subprocess
from typing import List

from modules.keys import *
from modules.groups import *
from modules.layouts import *
from modules.mouse import *
from modules.hooks import *
from modules.screens import *

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
wmname = "Qtile"

widget_defaults = dict(
        font='Cascadia Code',
        fontsize=13,
        padding=3
)

auto_fullscreen = True
focus_on_window_activation = "smart"  # or focus
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True
