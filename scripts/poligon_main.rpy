init:

    $ mods["poligon_start_mod"]=u"Полигон Совёнок"
    $ poligon_define_assets('poligon', poligon_sprites_folder='source/images/sprites')
    $ poligon_define_es_assets('images/bg')

    $ config.developer = True

label poligon_start_mod:
    $ renpy.block_rollback()
    window hide
    $ renpy.transition(Dissolve(2))
    python:
        store.persistent.poligon_default_screens = True
        renpy.game.context().force_checkpoint = True
        poligon_screens_save()
        poligon_screens_activate()
        poligon_say_set = "night"

    $ default_mouse = "poligon_mouse"

    jump poligon_main_menu

label poligon_main_menu:

    $ renpy.block_rollback()
    $ poligon_set_adv_mode()
    $ nvl_clear()
    window hide
    with dissolve

    stop ambience fadeout 1
    stop music fadeout 1

    play music poligon_menu_theme fadein 2.5

    scene poligon_mainmenu_background with Fade(1.5, 2, 1.5)
    show expression (ShortParticles(
        "poligon/source/images/gui/particle/dust_particle_1.png",
        "poligon/source/images/gui/particle/dust_particle_2.png",
        "poligon/source/images/gui/particle/dust_particle_3.png",
        "poligon/source/images/gui/particle/dust_particle_4.png",
        "poligon/source/images/gui/particle/dust_particle_5.png",
        "poligon/source/images/gui/particle/dust_particle_6.png",
        "poligon/source/images/gui/particle/dust_vignette.png",
        0.2
    ))
    call screen main_menu with Dissolve (.5)




label poligon_start_label:
    $ renpy.block_rollback()
    stop music fadeout 1.5
    stop ambience fadeout 1.5
    stop sound_loop fadeout 1.5
    scene bg black with dissolve
    $ renpy.pause (2, hard=True)
    $ poligon_say_time = "day"
    if select_chapter == "UVAO":
        jump poligon_chapter_1_prolog


label poligon_exit:

    $ renpy.block_rollback()
    python:
        store.persistent.poligon_default_screens = True
        poligon_screens_default()

    stop music fadeout 4
    stop sound_loop fadeout 4
    stop music_player fadeout 4
    stop ambience fadeout 4
    stop sound_loop fadeout 4
    scene black
    with Fade(1.5, 2, 1.5)

    $ default_mouse = "default"
    python:
        config.label_overrides['main_menu'] = 'main_menu'
    $ renpy.show("black")
    $ renpy.call("_start_store")
    $ renpy.start_predict_screen("main_menu")
    $ renpy.display.interface.with_none(overlay=False)
    $ renpy.music.play(config.main_menu_music, if_changed=True)
    $ renpy.stop_predict_screen("main_menu")
    $ renpy.transition(config.end_splash_transition)
    $ renpy.game.context().force_checkpoint = True
    $ renpy.free_memory()
    $ renpy.call("_main_menu")

label poligon_video_play:
    hide screen poligon_videoplayer
    $ renpy.movie_cutscene(video)
    scene black
    jump poligon_main_menu

