# Сохранение БЛ интерфейса и функции по возвращению и применение интерфейса Полигона (Но почему-то багуется и не видит именно poligon_old_quit(P.S: адекватно подправлено и работает всё корректно.))
init -1000 python:

    global poligon_default_screens

    def poligon_screens_save():
        if store.persistent.poligon_default_screens is True:
            renpy.display.screen.screens[("poligon_old_quit", None)] = renpy.display.screen.screens[("quit", None)]
            renpy.display.screen.screens[("poligon_old_say", None)] = renpy.display.screen.screens[("say", None)]
            renpy.display.screen.screens[("poligon_old_nvl", None)] = renpy.display.screen.screens[("nvl", None)]
            renpy.display.screen.screens[("poligon_old_game_menu_selector", None)] = renpy.display.screen.screens[("game_menu_selector", None)]
            renpy.display.screen.screens[("poligon_old_yesno_prompt", None)] = renpy.display.screen.screens[("yesno_prompt", None)]
            renpy.display.screen.screens[("poligon_old_choice", None)] = renpy.display.screen.screens[("choice", None)]
            renpy.display.screen.screens[("poligon_old_main_menu", None)] = renpy.display.screen.screens[("main_menu", None)]
            renpy.display.screen.screens[("poligon_old_preferences", None)] = renpy.display.screen.screens[("preferences", None)]
            renpy.display.screen.screens[("poligon_old_load", None)] = renpy.display.screen.screens[("load", None)]
            renpy.display.screen.screens[("poligon_old_save", None)] = renpy.display.screen.screens[("save", None)]
            renpy.display.screen.screens[("poligon_old_text_history_screen", None)] = renpy.display.screen.screens[("text_history_screen", None)]
            renpy.display.screen.screens[("poligon_old_skip_indicator", None)] = renpy.display.screen.screens[("skip_indicator", None)]
            renpy.display.screen.screens[("poligon_old_notify", None)] = renpy.display.screen.screens[("notify", None)]

            store.persistent.poligon_default_screens = False

        else:
            pass

    def poligon_screens_activate():
        config.window_title = u"Полигон Совёнок"
        config.name = "poligon"
        config.version = "1.3"
        config.label_overrides['main_menu'] = 'poligon_main_menu'
        config.enter_transition = ImageDissolve(poligon_images + "transit/poligon_wipeleft.png", 0.4, ramplen=128)
        config.exit_transition = ImageDissolve(poligon_images + "transit/poligon_wiperight.png", 0.4, ramplen=128)
        config.intra_transition = ImageDissolve(poligon_images + "transit/poligon_wipeleft.png", 0.4, ramplen=128)
        config.main_game_transition = ImageDissolve(poligon_images + "transit/poligon_wipeleft.png", 0.4, ramplen=128)
        config.game_main_transition = Fade(2, 1, 2)
        config.end_splash_transition = Fade(1.5, 1, 2)
        config.end_game_transition = Fade(1.5, 1, 2)
        config.after_load_transition = MultipleTransition([False, ImageDissolve(poligon_images + "transit/poligon_wipeleft.png", 0.4, ramplen=128), Solid("#000"), Pause(0.25), Solid("#000"), ImageDissolve(poligon_images + "transit/poligon_wipeleft.png", 0.4, ramplen=128), True])
        config.window_show_transition = Dissolve(.2)
        config.window_hide_transition = Dissolve(.2)
        config.main_menu_music = None
        
        persistent._file_page = "poligon_FilePage_1"  
        
        renpy.display.screen.screens[("quit", None)] = renpy.display.screen.screens[("poligon_quit", None)]
        renpy.display.screen.screens[("yesno_prompt", None)] = renpy.display.screen.screens[("poligon_warning", None)]
        renpy.display.screen.screens[("say", None)] = renpy.display.screen.screens[("poligon_say", None)]
        renpy.display.screen.screens[("game_menu_selector", None)] = renpy.display.screen.screens[("poligon_pause", None)]
        renpy.display.screen.screens[("main_menu", None)] = renpy.display.screen.screens[("poligon_main_menu", None)]
        renpy.display.screen.screens[("preferences", None)] = renpy.display.screen.screens[("poligon_preferences", None)]
        renpy.display.screen.screens[("load", None)] = renpy.display.screen.screens[("poligon_load", None)]
        renpy.display.screen.screens[("save", None)] = renpy.display.screen.screens[("poligon_save", None)]
        renpy.display.screen.screens[("text_history_screen", None)] = renpy.display.screen.screens[("poligon_history", None)]
        renpy.display.screen.screens[("nvl", None)] = renpy.display.screen.screens[("poligon_nvl", None)]

        poligon_set_adv_mode()


    def poligon_screens_default():
        if store.persistent.poligon_default_screens is True:
            persistent._file_page = 1
            config.window_title = u"Бесконечное Лето"
            config.name = "Everlasting_Summer"
            config.version = "1.2"
            config.main_menu_music = "sound/music/blow_with_the_fires.ogg"
            config.enter_transition = Dissolve(.25)
            config.exit_transition = Dissolve(.25)
            config.intra_transition = Dissolve(.25)
            config.main_game_transition = Dissolve(.25)
            config.game_main_transition = Dissolve(.25)
            config.end_splash_transition = Dissolve(.25)
            config.end_game_transition = fade
            config.after_load_transition = dissolve
            config.window_show_transition = Dissolve(.25)
            config.window_hide_transition = Dissolve(.25)
            renpy.display.screen.screens[("quit", None)] = renpy.display.screen.screens[("poligon_old_quit", None)]
            renpy.display.screen.screens[("say", None)] = renpy.display.screen.screens[("poligon_old_say", None)]
            renpy.display.screen.screens[("nvl", None)] = renpy.display.screen.screens[("poligon_old_nvl", None)]
            renpy.display.screen.screens[("game_menu_selector", None)] = renpy.display.screen.screens[("poligon_old_game_menu_selector", None)]
            renpy.display.screen.screens[("yesno_prompt", None)] = renpy.display.screen.screens[("poligon_old_yesno_prompt", None)]
            renpy.display.screen.screens[("choice", None)] = renpy.display.screen.screens[("poligon_old_choice", None)]
            renpy.display.screen.screens[("main_menu", None)] = renpy.display.screen.screens[("poligon_old_main_menu", None)]
            renpy.display.screen.screens[("preferences", None)] = renpy.display.screen.screens[("poligon_old_preferences", None)]
            renpy.display.screen.screens[("load", None)] = renpy.display.screen.screens[("poligon_old_load", None)]
            renpy.display.screen.screens[("save", None)] = renpy.display.screen.screens[("poligon_old_save", None)]
            renpy.display.screen.screens[("notify", None)] = renpy.display.screen.screens[("poligon_old_notify", None)]
            renpy.display.screen.screens[("skip_indicator", None)] = renpy.display.screen.screens[("poligon_old_skip_indicator", None)]
            renpy.display.screen.screens[("text_history_screen", None)] = renpy.display.screen.screens[("poligon_old_text_history_screen", None)]

            char_define("narrator", is_nvl=False)

            store.persistent.poligon_default_screens = False


        else:
            pass



init python:

    renpy.music.register_channel("music_player", "music", False)

    # Нужно для остановки текущей музыки и вызова выбранной музыки в меню с саундтреками мода
    def poligon_play_music(track_file):
        renpy.music.stop(channel="music_player")
        renpy.music.play(track_file, channel="music_player", fadein=1.5)
    
    def poligon_stop_music():
        if renpy.music.get_playing(channel="music_player"):
            renpy.music.stop(channel="music_player", fadeout=1.0)

    def poligon_play_video(video, page):
        music = renpy.music.get_playing(channel="music")
        renpy.hide_screen("poligon_videoplayer")
        renpy.movie_cutscene(video)
        renpy.show_screen("poligon_videoplayer", transition=fade, page=page)
        if music:
            renpy.music.play(music, channel="music", loop=True, fadein=1.0)

    #Уведомление об каком-то открытии
    def poligon_notice(nmessage):
        renpy.sound.play("poligon/source/audio/sfx/gui/notification_sound.mp3", channel="sound")
        renpy.show_screen("poligon_notification", text_notify=nmessage)

    renpy.display.screen.screens[("mods", None)] = renpy.display.screen.screens[("poligon_mods", None)]
