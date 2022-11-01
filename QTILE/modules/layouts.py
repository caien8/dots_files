from libqtile import layout
from libqtile.config import Match

from modules.colors import onedark_darker

layout_theme = {
    "margin": 2,
    "border_width": 4,
    "border_focus": onedark_darker["color4"],
    "border_normal": onedark_darker["colorback"],
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
         bg_color = onedark_darker["colorback"],
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
    border_focus = onedark_darker["color5"],
)
