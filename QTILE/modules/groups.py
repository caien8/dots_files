from libqtile.config import Key, Group, Screen, ScratchPad, DropDown
from libqtile.command import lazy
from .keys import *


groups = []

# FOR QWERTY KEYBOARDS
group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0",]

group_labels = [" 1 ", " 2 ", " 3 ", " 4 ", " 5 ", " 6 ", " 7 ", " 8 ", " 9 ", " 0 ",]
#group_labels = [" ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ",]
#group_labels = ["dev", "www", "sys", "doc", "vim", "chat", "mus", "vid", "gfx", "vbox",]

group_layouts = ["monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall",]
#group_layouts = ["monadtall", "matrix", "monadtall", "bsp", "monadtall", "matrix", "monadtall", "bsp", "monadtall", "monadtall",]

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
        ))

for i in groups:
    keys.extend([

#CHANGE WORKSPACES
        Key([mod], i.name, lazy.group[i.name].toscreen()),
        Key(["mod1"], "Tab", lazy.screen.next_group()),
        Key(["mod1", "shift"], "Tab", lazy.screen.prev_group()),

        # Add key command for ScratchPad DropDown
        #Key([mod], "space", lazy.group["scratchpad"].dropdown_toggle("term")),

# MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND STAY ON WORKSPACE
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
# MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND FOLLOW MOVED WINDOW TO WORKSPACE
        #Key([mod, "shift"], i.name, lazy.window.togroup(i.name) , lazy.group[i.name].toscreen()),
    ])

# Append ScratchPad to group list
groups.append(
    ScratchPad("scratchpad", [
                   # define a drop down terminal.ScratchPad
                   DropDown("term", terminal, opacity=0.8, height=0.5, width=0.6, x=0.2, y=0.2),
                   DropDown("mixer", "pavucontrol", width=0.4, x=0.3, y=0.1),
                   DropDown('khal', "kitty -t ikhal -e ikhal", x=0.6785, width=0.32, height=0.997, opacity=0.9),
               ]),
)

## ScratchPad KeyBindings
keys.extend([
        # DropDown Term
        Key([mod], "t", lazy.group["scratchpad"].dropdown_toggle("term")),
        Key([mod], "u", lazy.group["scratchpad"].dropdown_toggle("mixer")),
        Key([mod], "i", lazy.group["scratchpad"].dropdown_toggle("khal")),
])
