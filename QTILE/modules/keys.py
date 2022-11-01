import os
from libqtile.lazy import lazy
from libqtile.config import Key, KeyChord
from libqtile.utils import guess_terminal
from libqtile.dgroups import simple_key_binder
from modules.colors import onedark_darker

c6 = onedark_darker["color6"]
c5 = onedark_darker["color5"]

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
        ),

]


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
