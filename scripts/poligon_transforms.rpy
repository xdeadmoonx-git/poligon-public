
init:


    # О, вот это тоже классно, на заметку.
    transform poligon_settings_button_anim:
        on hover:
            easein 0.1 yoffset -2 zoom 1.1
        on idle:
            easein 0.1 yoffset 2 zoom 1.0
    #######################################

    transform poligon_settings_button_anim_characters:
        on hover:
            easein 0.1 yoffset -0.5 zoom 1.05
        on idle:
            easein 0.1 yoffset 0.5 zoom 1.0

    transform poligon_load_anim:
        zoom 0.4 alpha 0
        ease 0.5 zoom 1.0 alpha 1
        on hover:
            easein 0.1 yoffset -2 zoom 1.2
        on idle:
            easein 0.1 yoffset 2 zoom 1.0

    transform poligon_mods_info_anim:
        on show:
            zoom 0.4 alpha 0
            linear 0.5 zoom 1.0 alpha 1
        on hide:
            zoom 1.0 alpha 1
            linear 0.5 zoom 0.4 alpha 0

    transform poligon_settings_button_anim_in:
        alpha 0.0
        linear .5 alpha 1.0
        on hover:
            easein 0.1 yoffset -0.5 zoom 1.05
        on idle:
            easein 0.1 yoffset 0.5 zoom 1.0

    transform poligon_settings_button_anim_characters_in:
        alpha 0.0
        linear .5 alpha 1.0
        on hover:
            easein 0.1 yoffset -2 zoom 1.1
        on idle:
            easein 0.1 yoffset 2 zoom 1.0

    transform poligon_fade_in:
        alpha 0.0
        linear .3 alpha 1.0

    transform poligon_fade_out:
        alpha 1.0
        linear .1 alpha 0.0

    transform poligon_blur:
        ease .1 blur 10.0

    transform poligon_menu_anim(yoff, yof, xz):
        on hover:
            easein 0.1 yoffset yoff zoom xz
        on idle:
            easein 0.1 yoffset yof zoom 1.0

    transform poligon_notice_anim(xo):
        xoffset xo
        ease 0.5 xoffset 0
        pause 5.0
        ease 0.5 xoffset xo

    transform poligon_videoplayer_anim(xoff, xof, yoff, yof, xz):
        on hover:
            easein 0.1 xoffset xoff yoffset yoff zoom xz
        on idle:
            easein 0.1 xoffset xof yoffset yof zoom 1.0

    transform poligon_chapters_about_in(xa,ya,xoff,yoff,xon):
        xalign xa
        yalign ya
        xoffset xoff yoffset yoff
        ease 1.2 xoffset xon

    transform poligon_chapters_about_in_button(xa,ya,xoff,yoff,xon):
        xalign xa
        yalign ya
        xoffset xoff yoffset yoff
        ease 1.2 xoffset xon
        on hover:
            easein 0.1 yoffset -2 zoom 1.1
        on idle:
            easein 0.1 yoffset 2 zoom 1.0

    transform poligon_artsbg_hover:
        on idle:
            linear 0.133 zoom 1.0
        on hover:
            linear 0.133 zoom 1.0155

    transform poligon_move(xease):
        subpixel True
        parallel:
            xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
            ease 0.16 zoom 1.04 xpos 0.5 ypos 0.49
        parallel:
            ease xease xpos 0.5 ypos 0.49
            ease xease xpos 0.48 ypos 0.51
            ease xease xpos 0.5 ypos 0.49
            ease xease xpos 0.52 ypos 0.51
            repeat
    
    transform poligon_yoffset_ease(y, yy, e):
        yoffset y subpixel True
        ease e yoffset yy

    transform poligon_headshake(zooming, zoom1, zoom2, zoom3, rotate1, rotate2, xxoffset, yyoffset, blur1, blur2, blur3, blur4, blur5, blur6):
        subpixel True
        zoom zooming xalign 0.5 yalign 0.5
        parallel:
            ease 0.2 blur blur1
            ease 4 blur blur2
            ease 1.5 blur blur3
            ease 0.2 blur blur4
            ease 3 blur blur5
            ease 4 blur blur6
            repeat
        parallel:
            ease 1.8 zoom zoom1
            ease 2.2 zoom zoom2
            ease 1.6 zoom zoom3
            repeat
        parallel:
            ease 1.5 rotate rotate1
            ease 2.0 rotate rotate2
            ease 1.5 rotate 0
            repeat
        parallel:
            ease 1.3 xoffset -xxoffset - 4 yoffset -yyoffset - 1
            ease 1.5 xoffset xxoffset + 8 yoffset yyoffset + 4
            ease 1.4 xoffset -xxoffset - 1 yoffset yyoffset + 6
            ease 1.6 xoffset 0 yoffset 0
            repeat

    transform poligon_heartbeat(m):
        truecenter
        subpixel True
        block:

            linear 0.33 zoom 1.00 + 0.06 * m xalign 0.5  + 0.012 * m blur 3

            linear 0.37 zoom 1.00 xalign 0.5 blur 0

            pause 0.40

            linear 0.29 zoom 1.00 + 0.04 * m xalign 0.5  - 0.012 * m blur 2

            linear 0.33 zoom 1.00 xalign 0.5 blur 0

            pause 0.70

            repeat

    transform poligon_credits_fade_in_out(pause_duration=3.0):
        alpha 0.0
        linear 1.2 alpha 1.0
        pause pause_duration
        linear 1.2 alpha 0.0

    transform poligon_credits_fade_in(pause_duration=3.0):
        alpha 0.0
        linear 1.2 alpha 1.0
        pause pause_duration
        alpha 0.0

    transform poligon_credits_move_up:
        ypos 0.5
        linear 1.5 ypos 0.2

    transform poligon_credits_delayed_appear(delay):
        alpha 0.0
        pause delay
        linear 1.2 alpha 1.0

    transform poligon_smoke_move:
        xpos -4000
        yalign 0.5
        ease 30 xpos 2500
        repeat


init python:

    poligon_smoke_images = [ "poligon_smoke_{}".format(i) for i in range(1, 5) ]
    poligon_smoke_anim_args = sum([[img, 30] for img in poligon_smoke_images], [])

    poligon_smoke_red_images = [ "poligon_smoke_red_{}".format(i) for i in range(1, 5) ]
    poligon_smoke_red_anim_args = sum([[img, 30] for img in poligon_smoke_red_images], [])

    renpy.image("poligon_smoke", Animation(*poligon_smoke_anim_args, loop=True))
    renpy.image("poligon_smoke_red", Animation(*poligon_smoke_red_anim_args, loop=True))