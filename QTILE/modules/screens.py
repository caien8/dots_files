import os

from libqtile import widget
from libqtile import qtile
from libqtile import bar
from libqtile.config import Screen

from bars.simple_bar import bar


screens = [
    Screen(top=bar)
]
