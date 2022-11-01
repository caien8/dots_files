import os
from libqtile import qtile
from libqtile.bar import Bar
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

from modules.colors import onedark_darker
from modules.keys import terminal
from modules.groups import *


# Remove portions of windows group_names
def parse_func(text):
  for string in ["Brave", "Firefox", "Code"]:
        if string in text:
            text = string
        else:
            text = text
  return text

bar = Bar([
        Sep(
            linewidth = 0,
            padding = 2,
            foreground = onedark_darker["color4"],
            background = onedark_darker["color4"]
        ),
        Image(
            filename = "~/.config/qtile/icons/archlinux_blue.png",
            scale = "False",
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal)},
            background = onedark_darker["color4"],
        ),
        #### MEMORY ####
        Sep(
            linewidth = 2,
            padding = 2,
            foreground = onedark_darker["colorback"],
            background = onedark_darker["colorback"]
        ),
        TextBox(
            text = '  ',
            font = "Font Awesome 6 Free Solid",
            fontsize = 15,
            padding = 2,
            foreground = onedark_darker["colorback"],
            background = onedark_darker["color5"],
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e htop')},
            update_interval = 1
        ),
        Memory(
            foreground = onedark_darker["color5"],
            background = onedark_darker["colorback"],
            #mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e htop')},
            fmt = 'Mem:{}',
            #format = '{MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}',
            format = '[{MemUsed:.0f}]{mm}',
            padding = 5,
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e htop')},
            update_interval = 1
        ),
        ###### CPU ######
        TextBox(
            text = '  ',
            font = "Font Awesome 6 Free Solid",
            fontsize = 15,
            padding = 2,
            foreground = onedark_darker["colorback"],
            background = onedark_darker["color3"],
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e gotop')},
        ),
        CPU(
            background = onedark_darker["colorback"],
            foreground = onedark_darker["color3"],
            fmt = 'Cpu:{}',
            #format = '{freq_current}GHz {load_percent}%',
            format = '[{load_percent}]%',
            padding = 5,
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e htop')},
            update_interval = 2
        ),
        #### TEMPERATURE ########
        TextBox(
            text = '    ',
            font = "Font Awesome 6 Free Solid",
            fontsize = 18,
            padding = 2,
            foreground = onedark_darker["colorback"],
            background = onedark_darker["color4"],
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e htop')},
        ),
        ThermalSensor(
            foreground = onedark_darker["color4"],
            background = onedark_darker["colorback"],
            threshold = 70,
            fmt = 'Temp:{}',
            format ='[{temp:.0f}{unit}]',
            padding = 5,
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e htop')},
            update_interval = 0
        ),
        #### NETWORK ########
        TextBox(
            text = '  ',
            font = "Font Awesome 6 Free Solid",
            fontsize = 15,
            padding = 2,
            foreground = onedark_darker["colorback"],
            background = onedark_darker["color2"],
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn("dmenu_run")},
        ),
        Net(
            interface = "wlan0",
            format = '{down}{up}',
            prefix = 'M',
            foreground = onedark_darker["color2"],
            background = onedark_darker["colorback"],
            padding = 5,
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn("dmenu_run")},
            update_interval = 1,
            
        ),
        #### WINDOW NAME ########
        WindowName(
            foreground = onedark_darker["color5"],
            background = onedark_darker["colorback"],
            padding = 5,
            format = '[{name}]',
            # empty_group_string = '[]',
            parse_text = parse_func,
        ),
        #### GROUPBOX ####
        GroupBox(
            font = "JetBrainsMono Nerd Font Bold",
            fontsize = 12,
            fmt = '{}',
            borderwidth = 2,
            background = onedark_darker["colorback"],
            active = onedark_darker["color1"],
            inactive = onedark_darker["color2"],
            rounded = False,
            Block_highlight_text_color = onedark_darker["color3"],
            highlight_method = 'block',
            #highlight_color = onedark_darker["colorback"],  #  line block colour
            this_current_screen_border = onedark_darker["color4"],
            this_screen_border = onedark_darker["color7"],
            urgent_alert_method = 'block',
            urgent_border = onedark_darker["color10"],
            urgent_text = onedark_darker["color14"],
            disable_drag = True,
        ),
        ########################################################
        ##### LEFT BAR #####
        ########################################################
        Spacer(background=onedark_darker["colorback"]),
        #### WINDOW COUNT ####
        TextBox(
            text = '  ',
            font = "Font Awesome 6 Free Solid",
            fontsize = 15,
            background = onedark_darker["color9"],
            foreground = onedark_darker["color4"],
            padding = 2
        ),
        WindowCount(
            format = '{num}',
            background = onedark_darker["color9"],
            foreground = onedark_darker["color4"],
            show_zero = True,
        ),
        ###### LAYOUTS ######
        Sep(
            linewidth = 10,
            padding = 4,
            foreground = onedark_darker["colorback"],
            background = onedark_darker["colorback"]

        ),
        CurrentLayoutIcon(
            custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
            foreground = onedark_darker["colorback"],
            background = onedark_darker["color14"],
            padding = 0,
            scale = 0.7
        ),
        CurrentLayout(
            foreground = onedark_darker["color14"],
            background = onedark_darker["colorback"],
            padding = 5,
        ),
        #### BATTERY ####
        TextBox(
            text = '  ',
            font = "Font Awesome 6 Free Solid",
            fontsize = 15,
            padding = 2,
            foreground = onedark_darker["colorback"],
            background = onedark_darker["color6"]
        ),
        Battery(
            padding = 1,
            background = onedark_darker["colorback"],
            foreground = onedark_darker["color6"],
            charge_char = 'AC',
            discharge_char = '',
            empty_char = 'ﮣ',
            full_char = 'ﭹ',
            fmt = 'Bat:{}',
            format = '{char}[{percent:2.0%}]', #{hour:d}:{min:02d} {watt:.2f} W'
            #low_background = none,
            low_forground = '#ff0000',
            update_interval = 1,
        ),
        Battery(
            padding = 2,
            background = onedark_darker["colorback"],
            foreground = onedark_darker["color6"],
            format = "{hour:d}:{min:02d}",
            update_interval = 20
        ),
        #### VOLUME ####
        TextBox(
            text = '  ',
            font = "Font Awesome 6 Free Solid",
            fontsize = 15,
            padding = 2,
            foreground = onedark_darker["colorback"],
            background = onedark_darker["color7"]
        ),
        PulseVolume(
            background = onedark_darker["colorback"],
            foreground = onedark_darker["color7"],
            fmt = 'Vol:[{}]',
            device = 'default',
            channel = 'Master',
            limit_max_volume = True,
            padding = 5,
            update_interval = 0,
            mute_command = 'pactl set-sink-mute @DEFAULT_SINK@ toggle',
            volume_up_command = 'pactl set-sink-volume @DEFAULT_SINK@ +5%',
            volume_down_command = 'pactl set-sink-volume @DEFAULT_SINK@ -5%',
        ),
        #### CLOCK ####
        TextBox(
            text = '  ',
            font = "Font Awesome 6 Free Solid",
            fontsize = 15,
            padding = 2,
            foreground = onedark_darker["colorback"],
            background = onedark_darker["color10"]
        ),
        Clock(
            foreground = onedark_darker["color10"],
            background = onedark_darker["colorback"],
            format = "%a%d,%b[%I:%M]%P",
            mouse_callbacks = {"Button1": lazy.group['scratchpad'].dropdown_toggle('khal')},
            padding = 5,
        ),

        Systray(
            background = onedark_darker["colorback"],
            padding = 2
        ),

    ], 
    size=20,
    opacity = 0.8
)
