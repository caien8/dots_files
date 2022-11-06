import os
import re
import socket
import subprocess
from typing import List
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.dgroups import simple_key_binder
from libqtile.config import Key, Group, Screen, ScratchPad, DropDown, KeyChord, Match, Click, Drag
from libqtile.command import lazy
from libqtile import layout, hook, widget, qtile, bar
from libqtile.widget.sep import Sep
from libqtile.widget.image import Image
from libqtile.widget.textbox import TextBox
from libqtile.widget.clock import Clock
from libqtile.widget.cpu import CPU
from libqtile.widget import ThermalSensor
from libqtile.widget.pulse_volume import PulseVolume
from libqtile.widget.battery import Battery
from libqtile.widget import CurrentLayoutIcon
from libqtile.widget.currentlayout import CurrentLayout
from libqtile.widget.groupbox import GroupBox
from libqtile.widget.memory import Memory
from libqtile.widget.net import Net
from libqtile.widget.spacer import Spacer
from libqtile.widget.systray import Systray
from libqtile.widget.window_count import WindowCount
from libqtile.widget.windowname import WindowName

##############  DOOM-ONE  ######################
doom_one =  {
    'colorback' : '#282c34',
    'colorfore' : '#bbc2cf',
    'color1' : '#1c1f24',
    'color2' : '#ff6c6b',
    'color3' : '#98be65',
    'color4' : '#da8548',
    'color5' : '#51afef',
    'color6' : '#c678dd',
    'color7' : '#5699af',
    'color8' : '#202328',
    'color9' : '#5b6268',
    'color10' : '#da8548',
    'color11' : '#4db5bd',
    'color12' : '#ecbe7b',
    'color13' : '#3071db',
    'color14' : '#a9a1e1',
    'color15' : '#46d9ff',
    'color16' : '#dfdfdf',
}
###############  DRACULA   ########################
dracula = {
        'colorback': '#282a36',
        'colorfore': '#f8f8f2',
        'color1': '#000000',
        'color2': '#ff5555',
        'color3': '#50fa7b',
        'color4': '#f1fa8c',
        'color5': '#bd93f9',
        'color6': '#ff79c6',
        'color7': '#8be9fd',
        'color8': '#bfbfbf',
        'color9': '#4d4d4d',
        'color10': '#ff6e67',
        'color11': '#5af78e',
        'color12': '#f4f99d',
        'color13': '#caa9fa',
        'color14': '#ff92d0',
        'color15': '#9aedfe',
        'color16': '#e6e6e6',
}
##############  MONOKAI_PRO  ##########################
monokai_pro = {
    'colorback': '#2D2A2E',
    'colorfore': '#FCFCFA',
    'color1': '#403E41',
    'color2': '#FF6188',
    'color3': '#A9DC76',
    'color4': '#FFD866',
    'color5': '#FC9867',
    'color6': '#AB9DF2',
    'color7' : '#78DCE8',
    'color8': '#FCFCFA',
    'color9': '#727072',
    'color10': '#FF6188',
    'color11': '#A9DC76',
    'color12': '#FFD866',
    'color13': '#FC9867',
    'color14': '#AB9DF2',
    'color15': '#78DCE8',
    'color16': '#FCFCFA',
}
###############  NORD   ##################################
nord = {
    'colorback' : '#2E3440',
    'colorfore' : '#D8DEE9',
    'color1' : '#3B4252',
    'color2' : '#BF616A',
    'color3' : '#A3BE8C',
    'color4' : '#EBCB8B',
    'color5' : '#81A1C1',
    'color6' : '#B48EAD',
    'color7' : '#88C0D0',
    'color8' : '#E5E9F0',
    'color9' : '#4C566A',
    'color10' : '#BF616A',
    'color11' : '#A3BE8C',
    'color12' : '#EBCB8B',
    'color13' : '#81A1C1',
    'color14' : '#B48EAD',
    'color15' : '#8FBCBB',
    'color16' : '#ECEFF4',
}
#############  OCEANIC_NEXT   #########################
oceanic_next = {
    'colorback' : '#1b2b34',
    'colorfore' : '#d8dee9',
    'color1' : '#29414f',
    'color2' : '#ec5f67',
    'color3' : '#99c794',
    'color4' : '#fac863',
    'color5' : '#6699cc',
    'color6' : '#c594c5',
    'color7' : '#5fb3b3',
    'color8' : '#65737e',
    'color9' : "#405860",
    'color10' : '#ec5f67',
    'color11' : '#99c794',
    'color12' : '#fac863',
    'color13' : '#6699cc',
    'color14' : '#c594c5',
    'color15' : '#5fb3b3',
    'color16' : '#adb5c0',
}
################ PALENIGHT  #########################
palenight = {
    'colorback' : '#292d3e',
    'colorfore' : '#d0d0d0',
    'color1' : '#292d3e',
    'color2' : '#f07178',
    'color3' : '#c3e88d',
    'color4' : '#ffcb6b',
    'color5' : '#82aaff',
    'color6' : '#c792ea',
    'color7' : '#89ddff',
    'color8' : '#d0d0d0',
    'color9' : '#434758',
    'color10' : '#ff8b92',
    'color11' : '#ddffa7',
    'color12' : '#ffe585',
    'color13' : '#9cc4ff',
    'color14' : '#e1acff',
    'color15' : '#a3f7ff',
    'color16' : '#ffffff',
}
###########  TOMORROW_NIGHT   ########################
tomorrow_night = {
    'colorBack' : "#1d1f21",
    'colorFore' : "#c5c8c6",
    'color1' : "#1d1f21",
    'color2' : "#cc6666",
    'color3' : "#b5bd68",
    'color4' : "#e6c547",
    'color5' : "#81a2be",
    'color6' : "#b294bb",
    'color7' : "#70c0ba",
    'color8' : "#373b41",
    'color9' : "#666666",
    'color10' : "#ff3334",
    'color11' : "#9ec400",
    'color12' : "#f0c674",
    'color13' : "#81a2be",
    'color14' : "#b77ee0",
    'color15' : "#54ced6",
    'color16' : "#282a2e",
}
#################  TOKYONIGHT   ################################
tokyonight = {
   'colorback' : "#1a1b26",
    'colorfore' : "#a9b1d6",
    'color1' : "#32344a",
    'color2' : "#f7768e",
    'color3' : "#9ece6a",
    'color4' : "#e0af68",
    'color5' : "#7aa2f7",
    'color6' : "#ff007c",
    'color7' : "#449dab",
    'color8' : "#787c99",
    'color9' : "#444b6a",
    'color10' : "#ff7a93",
    'color11' : "#b9f27c",
    'color12' : "#ff9e64",
    'color13' : "#7aa2f7",
    'color14' : "#bb9af7",
    'color15' : "#0db9d7",
    'color16' : "#acb0d0",
}
###### ONEDARK_DARKER ######
onedark_darker = {
	'colorback' : "#1f2329",
	'colorfore' : "#a0a8b7",
	'color1' : "#0e1013",
    'color2' : "#e55561",
    'color3' : "#8ebd6b",
    'color4' : "#e2b86b",
    'color5' : "#4fa6ed",
    'color6' : "#bf68d9",
    'color7' : "#48b0bd",
    'color8' : "#535965",
    'color9' : "#181b20",
    'color10' : "#e86671",
    'color11' : "#98c379",
    'color12' : "#e5c07b",
    'color13' : "#61afef",
    'color14' : "#c678dd",
    'color15' : "#2b6f77",
    'color16' : "#a0a8b7",
}

theme = onedark_darker
c6 = theme["color6"]
c5 = theme["color5"]

home = os.path.expanduser("~")                      # Allow using "home +" to expand ~
mod = "mod4"
terminal = guess_terminal(preference = "kitty")
myBrowser = "brave"                               # My browser
myFM = "thunar"                                     # My file manager
text_editor = "code"
music_player = "spotify"
emulator = "virtualbox"

keys = [
    ####### THE ESSENTIALS ########
    # LAUNCH TERMINAL
    Key([mod], "Return", lazy.spawn(terminal), desc='Launches My Terminal'),
    # LAUNCH BROWSER
    Key([mod], "w", lazy.spawn(myBrowser), desc='Launches my browser'),
    # LAUNCH FILEMANAGER
    Key([mod], "f", lazy.spawn(myFM), desc='Launches my file manager'),
    # LAUNCH TEXT-EDITOR 
    Key([mod], "v", lazy.spawn(text_editor), desc='Launches my text editor'),
    # LAUNCH ROFI
    Key([mod], "r", lazy.spawn("rofi -modi drun,run -show drun"), desc='Run Launcher'),
    # LAUNCH DMENU
    Key([mod], "d", lazy.spawn(f"dmenu_run -l 9 -nf {c6} -sb {c5}"), desc = 'Launch dmenu'),
    # LAUNCH MUSIC PLAYER 
    Key([mod], "s", lazy.spawn(music_player), desc='Launches my music_player'),
    # LAUNCH EMULATOR 
    Key([mod], "a", lazy.spawn(emulator), desc='Launches my emulator'),
    # KILL WINDOW
    Key([mod], "c", lazy.window.kill(), desc="Kill focused window"),
    # RESTART QTILE
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    # SHUTDOWN QTILE
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    # SPAWN COMMAND-PROMPT
    Key([mod], "p", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    # LAUNCH POWERMENU
    Key([mod], "Delete",
        lazy.spawn("rofi -theme ~/.config/rofi/configPower.rasi -show power-menu -modi power-menu:~/.scripts/rofi-power-menu"),
        desc='Launch the powermenu'
        ),
    # LOCK SCREEN
    Key([mod, "shift"], "x",
        lazy.spawn("betterlockscreen -l dimblur"),
        desc='Lock screen'
        ),
    # Screenshot
    Key([], "Print",
        lazy.spawn("flameshot screen --path " + home + "/Pictures/Screenshots"),
        desc='Print entire screen'
        ),
    Key([mod], "Print",
        lazy.spawn("flameshot gui --path " + home + "/Pictures/Screenshots"),
        desc='Select print screen'
        ),
    ####### WINDOWS #######
    # TOOGLE WINDOWS
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),    
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "space", lazy.layout.flip(), desc="Switch window positions"),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Floating controls
    Key([mod], "bracketleft", lazy.group.prev_window(), lazy.window.bring_to_front(), desc='Move focus to prev floating window'),
    Key([mod], "bracketright", lazy.group.next_window(), lazy.window.bring_to_front(), desc='Move focus to next floating window'),
    # CHANGE WINDOW SIZE
    Key([mod, "control"], "h",
        lazy.layout.shrink(),
        lazy.layout.decrease_nmaster(),
        desc='Shrink window (MonadTall), decrease number in master pane (Tile)'
        ),
    Key([mod, "control"], "l",
        lazy.layout.grow(),
        lazy.layout.increase_nmaster(),
        desc='Expand window (MonadTall), increase number in master pane (Tile)'
        ),
    Key([mod], "n",
        lazy.layout.normalize(),
        desc='normalize window size ratios'
        ),
    Key([mod], "m",
        lazy.layout.maximize(),
        desc='toggle window between minimum and maximum sizes'
        ),
    Key([mod, "shift"], "f",
        lazy.window.toggle_floating(),
        desc='toggle floating'
        ),
    Key([mod], "o",
        lazy.window.toggle_fullscreen(),
        desc='toggle fullscreen'
        ),
    ####### LAYOUTS ########
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "Tab",
        lazy.layout.rotate(),
        lazy.layout.flip(),
        desc='Switch which side main pane occupies (XmonadTall)'
        ),
    Key([mod, "control"], "Tab",
        lazy.layout.toggle_split(),
        desc='Toggle between split and unsplit sides of stack'
        ),
    Key([mod, "shift", "control"], "h", lazy.layout.swap_column_left()),
    Key([mod, "shift", "control"], "l", lazy.layout.swap_column_right()),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),
    ###### WINDOW ######
    # Switch focus to specific monitor
    # Key([mod], "w", lazy.to_screen(0), desc='Keyboard focus to monitor 1'),
    # Key([mod], "e", lazy.to_screen(1), desc='Keyboard focus to monitor 2'),
    # Switch focus of monitors
    Key([mod], "period", lazy.next_screen(), desc='Move focus to next monitor'),
    Key([mod], "comma", lazy.prev_screen(), desc='Move focus to prev monitor'),
    ###### GROUPS ######
    # Switch Groups
    Key([mod], "End", lazy.screen.next_group(), desc='Move focus to next group'),
    Key([mod], "Home", lazy.screen.prev_group(), desc='Move focus to prev group'),
    ###### EXTRA CONTROLS ######
    # Key([], "XF86AudioRaiseVolume",lazy.spawn("amixer set Master 3%+")),
    # Key([], "XF86AudioLowerVolume",lazy.spawn("amixer set Master 3%-")),
    # Key([], "XF86AudioMute",lazy.spawn("amixer set Master toggle")),
        # Brightness controls
    Key([], "XF86MonBrightnessUp",
        lazy.spawn("brightnessctl set +5%"),
        desc="Increase screen brightness"
        ),
    Key([], "XF86MonBrightnessDown",
        lazy.spawn("brightnessctl set 5%-"),
        desc="Decrease screen brightness"
        ),
    # Volume controls
    Key([], "XF86AudioRaiseVolume",
        lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%"),
        desc="Raise volume"
        ),
    Key([], "XF86AudioLowerVolume",
        lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -10%"),
        desc="Lower volume"
        ),
    Key([], "XF86AudioMute",
        lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle"),
        desc="Mute speakers"
        ),
    Key([], "XF86AudioMicMute",
        lazy.spawn("pactl set-source-mute @DEFAULT_SOURCE@ toggle"),
        desc="Mute microphone"
        ),
    Key([], "XF86AudioPlay",
        lazy.spawn("playerctl play-pause"),
        desc="Play/Pause audio"
        ),
    Key([], "XF86AudioNext",
        lazy.spawn("playerctl next"),
        desc="Next track"
        ),
    Key([], "XF86AudioPrev",
        lazy.spawn("playerctl previous"),
        desc="Previous track"
        ),]
        
def show_keys(keys):
    """
    print current keybindings in a pretty way for a rofi/dmenu window.
    """
    key_help = ""
    keys_ignored = (
        "XF86AudioMute",  #
        "XF86AudioLowerVolume",  #
        "XF86AudioRaiseVolume",  #
        "XF86AudioPlay",  #
        "XF86AudioNext",  #
        "XF86AudioPrev",  #
        "XF86AudioStop",
    )
    text_replaced = {
        "mod4": "[S]",  #
        "control": "[Ctl]",  #
        "mod1": "[Alt]",  #
        "shift": "[Shf]",  #
        "twosuperior": "²",  #
        "less": "<",  #
        "ampersand": "&",  #
        "Escape": "Esc",  #
        "Return": "Enter",  #
    }
    for k in keys:
        if k.key in keys_ignored:
            continue

        mods = ""
        key = ""
        desc = k.desc.title()
        for m in k.modifiers:
            if m in text_replaced.keys():
                mods += text_replaced[m] + " + "
            else:
                mods += m.capitalize() + " + "

        if len(k.key) > 1:
            if k.key in text_replaced.keys():
                key = text_replaced[k.key]
            else:
                key = k.key.title()
        else:
            key = k.key

        key_line = "{:<25} {}".format(mods + key, desc + "\n")
        key_help += key_line

        # debug_print(key_line)  # debug only

    return key_help

# this must be done AFTER all the keys have been defined
keys.extend(
    [Key([mod], "F1", lazy.spawn("sh -c 'echo \"" + show_keys(keys) +
         "\" | rofi -theme ~/.config/rofi/configTall.rasi -dmenu -i -mesg \"Keyboard shortcuts\"'"), desc="Print keyboard bindings")]
)

############ GROUPS ##############
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
                   DropDown("term", terminal, opacity=0.99, height=0.5, width=0.6, x=0.2, y=0.2),
                   DropDown("mixer", "pavucontrol", width=0.4, x=0.3, y=0.1),
                   DropDown('khal', "kitty -e ikhal", x=0.6785, width=0.32, height=0.997, opacity=0.9),
               ]),
)
## ScratchPad KeyBindings
keys.extend([
        # DropDown Term
        Key([mod], "t", lazy.group["scratchpad"].dropdown_toggle("term")),
        Key([mod], "u", lazy.group["scratchpad"].dropdown_toggle("mixer")),
        Key([mod], "i", lazy.group["scratchpad"].dropdown_toggle("khal")),
])

############# LAYOUTS ###############
layout_theme = {
    "margin": 2,
    "border_width": 4,
    "border_focus": theme["color4"],
    "border_normal": theme["colorback"],
}
layouts = [
    layout.MonadTall( **layout_theme),
    #layout.MonadWide(**layout_theme),
    layout.MonadThreeCol(**layout_theme),
    layout.Bsp(**layout_theme),
    #layout.Stack(stacks=2, **layout_theme),
    #layout.Columns(**layout_theme),
    #layout.RatioTile(**layout_theme),
    layout.Tile(shift_windows=True, **layout_theme),
    #layout.VerticalTile(**layout_theme),
    #layout.Matrix(**layout_theme),
    layout.Zoomy(**layout_theme),
    #layout.MonadTall(margin=8, border_width=2, border_focus="#5e81ac", border_normal="#4c566a"),
    #layout.Max(**layout_theme),
    #layout.Stack(num_stacks=2),
    #layout.RatioTile(**layout_theme),
    layout.TreeTab(
         font = "UbunutuMono Nerd Font",
         fontsize = 10,
         sections = ["FIRST", "SECOND", "THIRD", "FOURTH"],
         section_fontsize = 10,
         border_width = 2,
         bg_color = theme["colorback"],
         active_bg = "#c678dd",
         active_fg = "#000000",
         inactive_bg = "#a9a1e1",
         inactive_fg = "#1c1f24",
         padding_left = 0,
         padding_x = 0,
         padding_y = 5,
         section_top = 10,
         section_bottom = 20,
         level_shift = 8,
         vspace = 3,
         panel_width = 200
         ),
    layout.Floating(**layout_theme)
]
floating_types = ["notification", "toolbar", "splash", "dialog", "Conky"]
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class='confirmreset'),  # gitk
        Match(wm_class='makebranch'),  # gitk
        Match(wm_class='maketag'),  # gitk
        Match(wm_class='ssh-askpass'),  # ssh-askpass
        Match(title='branchdialog'),  # gitk
        Match(title='pinentry'),  # GPG key password entry
        Match(wm_class='confirm'),
        Match(wm_class='dialog'),
        Match(wm_class='download'),
        Match(wm_class='error'),
        Match(wm_class='file_progress'),
        Match(wm_class='notification'),
        Match(wm_class='splash'),
        Match(wm_class='toolbar'),
        Match(wm_class='Arandr'),
        Match(wm_class='feh'),
        Match(wm_class='Galculator'),
        Match(wm_class='archlinux-logout'),
        Match(wm_class='Conky'),
        Match(wm_class='blueman-manager'),
        Match(wm_class='nm-connection-editor'),
        Match(wm_class='xarchiver'),
    ],
    border_width = 2,
    border_focus = theme["color5"],
)

############# WIDGETS ##############
# Remove portions of windows group_names
def parse_func(text):
  for string in ["Brave", "Firefox", "Code"]:
        if string in text:
            text = string
        else:
            text = text
  return text

widget_defaults = dict(
        # font='Cascadia Code',
        font="UbunutuMono Nerd Font Mono Bold",
        fontsize=12,
        padding=2,
        background= theme["colorback"],
)
screens = [
    Screen(top=bar.Bar([
        ###### LOGO ######
        Sep(
            linewidth = 2,
            padding = 2,
            foreground = theme["color4"],
            background = theme["color4"]
        ),
        Image(
            filename = "~/.config/qtile/icons/archlinux_blue.png",
            scale = "False",
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal)},
            #background = theme["color4"],
        ),
        #Sep(
        #    linewidth = 0,
        #    padding = 2,
        #    foreground = theme["colorback"],
        #    background = theme["colorback"]
        #),
        ###### GROUPBOX ######
        TextBox(
            text = "",
            padding = 2,
            foreground = theme["color4"],
            background = theme["colorback"],
        ),
        GroupBox(
            font = "JetBrains Nerd Font Mono Bold",
            fontsize = 12,
            padding = 1.5,
            fmt = '{}',
            borderwidth = 1,
            background = theme["colorback"],
            active = theme["color6"],
            inactive = theme["color5"],
            rounded = False,
            #Block_highlight_text_color = theme["color3"],
            highlight_method = 'line',
            highlight_color = theme["colorback"],  #  line block colour
            this_current_screen_border = theme["color4"],
            this_screen_border = theme["color7"],
            urgent_alert_method = 'line',
            urgent_border = theme["color10"],
            urgent_text = theme["color14"],
            disable_drag = True,
        ),
         TextBox(
            text = "",
            padding = 2,
            foreground = theme["color4"],
            background = theme["colorback"],
        ),
        ###### LAYOUTS ######
        CurrentLayoutIcon(
            custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
            foreground = theme["color14"],
            background = theme["colorback"],
            padding = 0,
            scale = 0.7
        ),
        CurrentLayout(
            foreground = theme["color14"],
            background = theme["colorback"],
            padding = 5,
        ),
        ###### WINDOW COUNT ######
        Sep(
            linewidth = 2,
            padding = 4,
            foreground = theme["color8"],
            background = theme["colorback"]
        ),
        TextBox(
            text = '',
            font = "Font Awesome 6 Free Solid",
            fontsize = 15,
            background = theme["color9"],
            foreground = theme["color4"],
            padding = 2
        ),
        WindowCount(
            format = '{num}',
            background = theme["colorback"],
            foreground = theme["color4"],
            show_zero = True,
        ),
        ###### WINDOW NAME ######
        Sep(
            linewidth = 2,
            padding = 4,
            foreground = theme["color8"],
            background = theme["colorback"]
        ),
        TextBox(
            text = "",
            font = "Font Awesome 6 Free Solid",
            fontsize = 15,
            padding = 2,
            foreground = theme["color2"],
            background = theme["colorback"]
        ),
        WindowName(
            foreground = theme["color5"],
            background = theme["colorback"],
            padding = 5,
            format = ': {name}',
            # empty_group_string = '[ ]',
            parse_text = parse_func,
        ),
        #########################################################
        ######### LEFT #########
        #########################################################
        #widget.Spacer(),
        #Sep(
        #    linewidth = 0,
        #    padding = 6,
        #    foreground = theme["color1"],
        #    background = theme["color1"],
        #),

        ###### NETWORK ######
        Sep(
            linewidth = 2,
            padding = 4,
            foreground = theme["color8"],
            background = theme["colorback"]
        ),
        TextBox(
            text = '',
            font = "Font Awesome 6 Free Solid",
            fontsize = 15,
            padding = 1,
            foreground = theme["color2"],
            background = theme["colorback"],
        ),
        Net(
            interface = "wlan0",
            format = "{down}{up}",
            prefix = 'M',
            foreground = theme["color2"],
            background = theme["colorback"],
            padding = 2,
            update_interval = 1,
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('networkmanager_dmenu -l 9 -nf red -sb red')},
        ),
        ##### CPU ######
        Sep(
            linewidth = 2,
            padding = 4,
            foreground = theme["color8"],
            background = theme["colorback"]
        ),
        TextBox(
            text = '',
            font = "Font Awesome 6 Free Solid",
            fontsize = 15,
            padding = 2,
            foreground = theme["color3"],
            background = theme["colorback"],
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e gotop')},
        ),
        CPU(
            background = theme["colorback"],
            foreground = theme["color3"],
            fmt = 'Cpu:{}',
            update_interval = 1,
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e gotop')},
            #format = '{freq_current}GHz {load_percent}%',
            format = '[{load_percent}]%',
            padding = 2,
        ),
        ###### TEMPERATURE ######
        Sep(
            linewidth = 2,
            padding = 4,
            foreground = theme["color8"],
            background = theme["colorback"]
        ),
        TextBox(
            text = '',
            font = "Font Awesome 6 Free Solid",
            fontsize = 15,
            padding = 2,
            foreground = theme["color4"],
            background = theme["colorback"],
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e htop')},
        ),
        ThermalSensor(
            foreground = theme["color4"],
            background = theme["colorback"],
            update_interval = 0,
            threshold = 70,
            fmt = 'Temp:{}',
            format='[{temp:.0f}{unit}]',
            padding = 2,
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e htop')},
        ),
        ##### MEMORY ######
        Sep(
            linewidth = 2,
            padding = 4,
            foreground = theme["color8"],
            background = theme["colorback"]
        ),
        TextBox(
            text = '',
            font = "Font Awesome 6 Free Solid",
            fontsize = 15,
            padding = 2,
            foreground = theme["color5"],
            background = theme["colorback"],
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e htop')},
        ),
        Memory(
            foreground = theme["color5"],
            background = theme["colorback"],
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e htop')},
            fmt = 'Mem:{}',
            #format = '{MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}',
            format = '[{MemUsed:.0f}]{mm}',
            padding = 2,
            update_interval = 1,
        ),
        ##### BRIGHTNESS ######
        Sep(
            linewidth = 2,
            padding = 4,
            foreground = theme["color8"],
            background = theme["colorback"]
        ),
        TextBox(
            text = '',
            font = "Font Awesome 6 Free Solid",
            fontsize = 15,
            padding = 2,
            foreground = theme["color4"],
            background = theme["colorback"]
        ),        
        widget.Backlight(
            foreground = theme["color4"],
            fmt = "Brt:[{}]",
            brightness_file = "/sys/class/backlight/amdgpu_bl0/actual_brightness",
            max_brightness_file = "/sys/class/backlight/amdgpu_bl0/max_brightness",
            fontsize = 12,
            padding = 2
        ),
        ###### VOLUME ########
        Sep(
            linewidth = 2,
            padding = 4,
            foreground = theme["color8"],
            background = theme["colorback"]
        ),
        TextBox(
            text = '',
            font = "Font Awesome 6 Free Solid",
            fontsize = 15,
            padding = 2,
            foreground = theme["color7"],
            background = theme["colorback"]
        ),
        PulseVolume(
            background = theme["colorback"],
            foreground = theme["color7"],
            fmt = 'Vol:[{}]',
            device = 'default',
            channel = 'Master',
            limit_max_volume = True,
            padding = 2,
            update_interval = 0,
            mute_command = 'pactl set-sink-mute @DEFAULT_SINK@ toggle',
            volume_up_command = 'pactl set-sink-volume @DEFAULT_SINK@ +5%',
            volume_down_command = 'pactl set-sink-volume @DEFAULT_SINK@ -5%',
        ),
        #volume,
        #widget.Volume(
        #    foreground = theme[8],
        #    background = theme[0],
        #    fmt = 'Vol: {}',
        #    padding = 5,
        #    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e alsamixer')}
        #),
        ###### BATTERY ######
        Sep(
            linewidth = 2,
            padding = 4,
            foreground = theme["color8"],
            background = theme["colorback"]
        ),
        TextBox(
            text = '',
            font = "Font Awesome 6 Free Solid",
            fontsize = 15,
            padding = 2,
            foreground = theme["color6"],
            background = theme["colorback"]
        ),
        Battery(
            padding = 1,
            background = theme["colorback"],
            foreground = theme["color6"],
            charge_char = 'AC',
            discharge_char = '',
            empty_char = 'ﮣ',
            full_char = 'ﭹ',
            fmt = 'Bat:{}',
            format = '{char}[{percent:2.0%}]', # {hour:d}:{min:02d}', # {watt:.2f} W',
            #low_background = none,
            low_forground = '#ff0000',
            update_interval = 1,
        ),
        Battery(
            padding = 2,
            background = theme["colorback"],
            foreground = theme["color6"],
            format = "{hour:d}:{min:02d}",
            update_interval = 20
        ),
        #battery,
        ##### CLOCK ######
        Sep(
            linewidth = 2,
            padding = 4,
            foreground = theme["color8"],
            background = theme["colorback"]
        ),
        TextBox(
            text = '',
            font = "Font Awesome 6 Free Solid",
            fontsize = 15,
            padding = 2,
            foreground = theme["color10"],
            background = theme["colorback"]
        ),
        Clock(
            foreground = theme["color10"],
            background = theme["colorback"],
            format = "%a%d,%b[%I:%M]%P",
            padding = 2,
        ),
        ##### SYSTRAY ######
        Sep(
            linewidth = 2,
            padding = 4,
            foreground = theme["color8"],
            background = theme["colorback"]
        ),
        Systray(
            background = theme["colorback"],
            padding = 2
        ),
        Sep(
            linewidth = 2,
            padding = 2,
            foreground = theme["colorback"],
            background = theme["colorback"]
        ),
        Sep(
            linewidth = 2,
            padding = 2,
            foreground = theme["color4"],
            background = theme["color4"]
        ),
    ], 
    opacity = 0.8,
    size = 20
    ))
]

########## MOUSE ############
# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]
dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = True
cursor_warp = False

############## HOOKS #################
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])
@hook.subscribe.client_new
def set_floating(window):
    if (window.window.get_wm_transient_for()
            or window.window.get_wm_type() in floating_types):
        window.floating = True

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
auto_fullscreen = True
focus_on_window_activation = "smart"  # or focus
reconfigure_screens = True
# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True
wmname = "Qtile"
