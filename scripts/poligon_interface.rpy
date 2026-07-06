init:

    define config.mouse["poligon_mouse"] = [("poligon/source/images/gui/mouse/mouse.png", 0, 0)]

    image base_poligon = im.Scale("poligon/source/images/gui/warning/base_poligon.png", 1500,300)
    image box_yes = im.Scale("poligon/source/images/gui/warning/box_yes.png", 250,140)
    image box_no = im.Scale("poligon/source/images/gui/warning/box_no.png", 250,140)

    image poligon_box_notice = im.Scale("poligon/source/images/gui/notification.png", 700, 100)

screen poligon_notification(text_notify):

    zorder 100

    add "poligon_box_notice" yalign 0.04 at poligon_notice_anim(-800)
    text "[text_notify]" xoffset 33 yoffset -10 yalign 0.08 color "#FFFFFF" font poligon_fonts + "zhizn.ttf" size 28 at poligon_notice_anim(-800)
    timer 7.0 action Hide("poligon_notification")

###### Изменненный интерфейс для мода

# Меню паузы
screen poligon_pause:

    key "K_ESCAPE" action Return()

    tag menu
    modal True

    add poligon_images + "gui/pause/pause_background.png"

    button:
        style "blank_button"
        xpos 0
        ypos 0
        xfill True
        yfill True
        action Return()

    vbox:
        align (0.51, 0.5)
        spacing 40
        imagebutton:
            idle poligon_images + "gui/pause/continue_idle.png"
            hover poligon_images + "gui/pause/continue_hover.png"
            xoffset 50
            at poligon_menu_anim(-0.07, 0.07, 1.02)
            action Return()
        imagebutton:
            idle poligon_images + "gui/pause/parchive_idle.png"
            hover poligon_images + "gui/pause/parchive_hover.png"
            xoffset 185
            at poligon_menu_anim(-0.07, 0.07, 1.02)
            action [SetVariable("pause_click", True), ShowMenu("poligon_archive")]
        imagebutton:
            idle poligon_images + "gui/pause/pload_idle.png"
            hover poligon_images + "gui/pause/pload_hover.png"
            xoffset 90
            at poligon_menu_anim(-0.07, 0.07, 1.02)
            action ShowMenu("poligon_load")
        imagebutton:
            idle poligon_images + "gui/pause/save_idle.png"
            hover poligon_images + "gui/pause/save_hover.png"
            xoffset 84
            at poligon_menu_anim(-0.07, 0.07, 1.02)
            action ShowMenu("poligon_save")
        imagebutton:
            idle poligon_images + "gui/pause/ppreferences_idle.png"
            hover poligon_images + "gui/pause/ppreferences_hover.png"
            xoffset 84
            at poligon_menu_anim(-0.07, 0.07, 1.02)
            action ShowMenu("poligon_preferences")
        imagebutton:
            idle poligon_images + "gui/pause/mainmenu_idle.png"
            hover poligon_images + "gui/pause/mainmenu_hover.png"
            xoffset -5
            at poligon_menu_anim(-0.02, 0.02, 1.015)
            action Show("poligon_warning_mainmenu", transition=Dissolve(.5), messages="Вы действительно хотите выйти в главное меню?\nНесохраненные данные будут потеряны.", action_yes=[Hide("poligon_warning_mainmenu", transition=Dissolve(.1)), Start("poligon_main_menu")], action_no=Hide("poligon_warning_mainmenu", transition=Dissolve(.1)))
        imagebutton:
            idle poligon_images + "gui/pause/pexit_idle.png"
            hover poligon_images + "gui/pause/pexit_hover.png"
            xoffset 170
            at poligon_menu_anim(-0.07, 0.07, 1.02)
            action ShowMenu("poligon_quit")

    if renpy.music.get_playing(channel="music"):
        $ track_playing = renpy.music.get_playing(channel="music")
        $ name_track = None
        for key, data in persistent.poligon_music.items():
            if data.get("file") == track_playing:
                $ name_track = data.get("name")
        
        if music_list["everyday_theme"] == track_playing:
            $ name_track = "Sergey Eybog - Feeling Good"

        if name_track:
            text ["Текущая музыка:"] at poligon_yoffset_ease(-200, 0, 0.5):
                style "poligon_music_text"
                text_align 0.5 yoffset 10 xalign 0.5 font poligon_fonts + "zhizn.ttf" size 40
            text name_track at poligon_yoffset_ease(-200, 0, 0.5):
                style "poligon_music_text"
                text_align 0.5 yoffset 55 xalign 0.5 font poligon_fonts + "zhizn.ttf" size 40

# Настройки
screen poligon_preferences:

    key "K_ESCAPE" action Return()

    tag menu
    modal True

    add poligon_images + "gui/preferences/preferences_background.png"

    imagebutton:
        auto poligon_images + "gui/preferences/preferences_button_%s.png"
        activate_sound poligon_start_sound
        hover_sound poligon_button_menu
        align (0.35, 0.9)
        xoffset 50
        yoffset -30
        action Return()

    frame:
        style "poligon_scrollable_frame"
        xysize (632, 657)
        align (0.5, 0.4)
        xoffset 1
        yoffset -15
        vbox:
            text "Режим пропуска":
                style "poligon_settings_style"
                size 45
                text_align 0.5
                antialias True
                kerning 2
            
            hbox:
                spacing 50
                textbutton "Всё" text_style "poligon_settings_button_style" style "poligon_settings_button_style" text_size 45 activate_sound poligon_start_sound hover_sound poligon_button_menu action Preference("skip", "all") at poligon_settings_button_anim
                textbutton "Виденное ранее" text_style "poligon_settings_button_style" style "poligon_settings_button_style" text_size 45 activate_sound poligon_start_sound hover_sound poligon_button_menu action Preference("skip", "seen") at poligon_settings_button_anim
            
            text "Громкость музыки" style "poligon_settings_style" size 45 yoffset 30

            bar value Preference("music volume") left_bar "poligon_hbar_preferences_full" right_bar "poligon_hbar_preferences_null" thumb "poligon/source/images/gui/bar/htumb.png" hover_thumb "poligon/source/images/gui/bar/htumb.png" xmaximum 520 ymaximum 40 thumb_offset -10 yoffset 30 at poligon_settings_button_anim

            text "Громкость эффектов" style "poligon_settings_style" size 45 yoffset 30

            bar value Preference("sound volume") left_bar "poligon_hbar_preferences_full" right_bar "poligon_hbar_preferences_null" thumb "poligon/source/images/gui/bar/htumb.png" hover_thumb "poligon/source/images/gui/bar/htumb.png" xmaximum 520 ymaximum 40 thumb_offset -10 yoffset 30 at poligon_settings_button_anim

            text "Громкость фона" style "poligon_settings_style" size 45 yoffset 30

            bar value Preference("voice volume") left_bar "poligon_hbar_preferences_full" right_bar "poligon_hbar_preferences_null" thumb "poligon/source/images/gui/bar/htumb.png" hover_thumb "poligon/source/images/gui/bar/htumb.png" xmaximum 520 ymaximum 40 thumb_offset -10 yoffset 30 at poligon_settings_button_anim

            text "Скорость текста" style "poligon_settings_style" size 45 yoffset 30

            bar value Preference("text speed") left_bar "poligon_hbar_preferences_full" right_bar "poligon_hbar_preferences_null" thumb "poligon/source/images/gui/bar/htumb.png" hover_thumb "poligon/source/images/gui/bar/htumb.png" xmaximum 520 ymaximum 40 thumb_offset -10 yoffset 30 at poligon_settings_button_anim

            text "Время автоперехода" style "poligon_settings_style" size 45 yoffset 30

            bar value Preference("auto-forward time") left_bar "poligon_hbar_preferences_full" right_bar "poligon_hbar_preferences_null" thumb "poligon/source/images/gui/bar/htumb.png" hover_thumb "poligon/source/images/gui/bar/htumb.png" xmaximum 520 ymaximum 40 thumb_offset -10 yoffset 30 at poligon_settings_button_anim

#Диалоговое окно (day, sunset, night, red, white)
screen poligon_say:

    key ['h','H','р','Р'] action HideInterface()
    key ['m','M','ь','Ь'] action ShowMenu("poligon_pause")
    key "mouseup_3" action ShowMenu("poligon_pause")


    window:

        background None
        id "window"

        add poligon_images + "gui/say/dialogue_box_" + poligon_say_set + ".png":
            xpos 174
            ypos 866
            yoffset -23
            xoffset 7
        imagebutton:
            auto poligon_images + "gui/say/backward_%s_" + poligon_say_set + ".png"
            xpos 38
            ypos 924
            yoffset -25
            xoffset -11
            action ShowMenu("poligon_history")
        imagebutton:
            auto poligon_images + "gui/say/forward_%s_" + poligon_say_set + ".png"
            xpos 1768
            ypos 924
            yoffset -25
            xoffset -15
            action Skip()
        imagebutton:
            auto poligon_images + "gui/say/hide_%s_" + poligon_say_set + ".png"
            xpos 1567
            ypos 880
            xoffset 16
            yoffset -16
            action HideInterface()
        imagebutton:
            auto poligon_images + "gui/say/menu_%s_" + poligon_say_set + ".png"
            xpos 1567
            ypos 880
            xoffset 90
            yoffset -16
            action ShowMenu("poligon_pause")

        text what:
            id "what"
            font poligon_fonts + "say_what.ttf"
            xpos 193
            ypos 911
            xoffset 14
            yoffset -19
            xmaximum 1505
            size 30
            line_spacing 1
            color "#FFFFFF"
        if who:
            text who:
                id "who"
                font poligon_fonts + "say_who.ttf"
                xpos 193
                ypos 871
                xoffset 13
                yoffset -19
                size 30
                line_spacing 1


#Переопределение истории, чтобы был стиль текста из мода
#Ну и добавление своего скроллбара
screen poligon_history:

    predict False

    $ xmax = 1600
    $ xposition = 100

    $ history_text_size = 28
    $ history_name_size = 28

    button style "blank_button" xpos 0 ypos 0 xfill True yfill True action Return()

    window background Frame("images/gui/choice/day/choice_box.png") left_padding 75 right_padding 75 bottom_padding 120 top_padding 120:

        viewport id "poligon_history":
            draggable True
            mousewheel True
            scrollbars None
            yinitial 1.0

            has vbox

            for h in _history_list:

                if h.who:

                    text h.who:
                        font poligon_fonts + "say_who.ttf"
                        ypos 0
                        xpos xposition
                        xalign 0.0
                        size history_name_size
                        if "color" in h.who_args:
                            color h.who_args["color"]

                textbutton h.what style "poligon_history_text" text_style "poligon_history_text" text_size history_text_size action RollbackToIdentifier(h.rollback_identifier) xmaximum xmax xpos 100

        vbar value YScrollValue("poligon_history") bottom_bar "poligon_vbar_history" top_bar "poligon_vbar_history" thumb "poligon/source/images/gui/bar/vthumb.png" xoffset 1700

#Большое окно истории
screen poligon_nvl:

    $ poligon_nvl_size = 30

    add poligon_images + "gui/nvl_box.png"

    vbox:
        spacing 10
        
        for who, what, who_id, what_id, window_id in dialogue:
            
            window:
                id window_id
                
                has hbox:
                    xpos 150
                    ypos 75
                    spacing 10
                    
                    if who:
                        text who id who_id size poligon_nvl_size font poligon_fonts + "say_who.ttf"
                            
                    text what id what_id xmaximum 1620 size poligon_nvl_size font poligon_fonts + "say_what.ttf" color "FFFFFF"

    imagebutton auto poligon_images + "gui/say/forward_%s_" + poligon_say_set + ".png" xpos 1652 ypos 866 xoffset 70 yoffset 30 activate_sound poligon_start_sound hover_sound poligon_button_menu action Skip()
    imagebutton auto poligon_images + "gui/say/backward_%s_" + poligon_say_set + ".png" xpos 54 ypos 866 xoffset 30 yoffset 30 activate_sound poligon_start_sound hover_sound poligon_button_menu action ShowMenu("poligon_history")



#Окно выхода
screen poligon_quit:

    key "K_ESCAPE" action Return()

    tag menu
    modal True

    imagemap:
        auto poligon_images + "gui/exit/exit_%s.png"

        hotspot (882, 640, 374, 362) activate_sound poligon_start_sound hover_sound poligon_button_menu clicked Jump("poligon_exit")

        hotspot (1514, 685, 381, 326) activate_sound poligon_start_sound hover_sound poligon_button_menu clicked Return()

#Загрузки
#Немного костыльная работа со своими FilePage.
screen poligon_load:

    key "K_ESCAPE" action Return()

    tag menu
    modal True
    window:
        background "poligon_save_load_background"

        add poligon_images + "gui/zatemnenie_light.png":
            ypos -20
            xpos -20
        text "Загрузить":
            style "poligon_save_screens_style"
            size 75
            text_align 0.5
            xalign 0.1
            yalign 0.060
            xoffset -10
            antialias True
            kerning 2


        textbutton "Сохранить":
            text_style "poligon_save_screens_style"
            style "poligon_save_screens_style"
            text_size 65
            xalign 0.9
            yalign 0.07
            text_align 0.5
            at poligon_settings_button_anim
            action ShowMenu("poligon_save")


        textbutton "Загрузить?":
            text_style "poligon_save_screens_style"
            style "poligon_save_screens_style"
            activate_sound poligon_start_sound hover_sound poligon_button_menu
            ypos 950
            xalign 0.5
            action FileLoad(selected_slot)
            at poligon_settings_button_anim

        textbutton "Забыть":
            text_style "poligon_save_screens_style"
            style "poligon_save_screens_style"
            activate_sound poligon_start_sound hover_sound poligon_button_menu
            xpos 1610
            ypos 950
            action FileDelete(selected_slot)
            at poligon_settings_button_anim

        textbutton "Назад":
            text_style "poligon_save_screens_style"
            style "poligon_save_screens_style"
            activate_sound poligon_start_sound hover_sound poligon_button_menu
            xpos 60
            ypos 950
            action Return()
            at poligon_settings_button_anim

        vbox:
            spacing 40
            align (0.1, 0.2)
            xoffset -100
            yoffset 120
            
            # Делаем список с отдельными сохранениями для мода в виде простого списка, ибо страниц мало.
            for page in ["poligon_FilePage_1", "poligon_FilePage_2", "poligon_FilePage_3", "poligon_FilePage_4", "poligon_FilePage_5", "poligon_FilePage_6"]:
                textbutton str(page[-1]):
                    text_style "poligon_save_screens_style"
                    style "poligon_save_screens_style"
                    activate_sound poligon_start_sound 
                    hover_sound poligon_button_menu
                    action FilePage(page)


        grid 4 3:
            xpos 0.11
            ypos 0.2
            xmaximum 0.81
            ymaximum 0.65
            transpose False
            xfill True
            yfill True
            #Тут просто с 1000, ничего страшного :)
            for i in range(1001, 1013):
                $ display_num = i - 1000
                fixed:
                    add FileScreenshot(str(i)) at poligon_settings_button_anim:
                        xpos 10
                        ypos 10
                    button:
                        action SetVariable("selected_slot", str(i))
                        activate_sound poligon_start_sound
                        hover_sound poligon_button_menu
                        xfill False
                        yfill False
                        style "poligon_save_load_button"
                        has fixed
                        text ("%s." % display_num + FileTime(str(i), format=' %d.%m.%y, %H:%M', empty=" "+"Пусто") + "\n" +FileSaveName(str(i))) at poligon_settings_button_anim:
                            style "poligon_save_load_button_text"
                            xpos 15
                            ypos 15

                            
#Сохранение
screen poligon_save:

    key "K_ESCAPE" action Return()
    
    tag menu
    modal True

    window:
        background "poligon_save_load_background"

        add poligon_images + "gui/zatemnenie_light.png":
            ypos -20
            xpos -20
        text "Сохранить":
            style "poligon_save_screens_style"
            size 75
            text_align 0.5
            xalign 0.9
            yalign 0.060
            antialias True
            kerning 2
            at poligon_settings_button_anim

        textbutton "Загрузить":
            text_style "poligon_save_screens_style"
            style "poligon_save_screens_style"
            text_size 65
            xalign 0.1
            yalign 0.07
            text_align 0.5
            at poligon_settings_button_anim
            action ShowMenu("poligon_load")

        textbutton "Сохранить?":
            text_style "poligon_save_screens_style"
            style "poligon_save_screens_style"
            activate_sound poligon_start_sound hover_sound poligon_button_menu
            ypos 950
            xalign 0.5
            action FileSave(selected_slot)
            at poligon_settings_button_anim

        textbutton "Забыть":
            text_style "poligon_save_screens_style"
            style "poligon_save_screens_style"
            activate_sound poligon_start_sound hover_sound poligon_button_menu
            xpos 1610
            ypos 950
            action FileDelete(selected_slot)
            at poligon_settings_button_anim

        textbutton "Назад":
            text_style "poligon_save_screens_style"
            style "poligon_save_screens_style"
            activate_sound poligon_start_sound hover_sound poligon_button_menu
            xpos 60
            ypos 950
            action Return()
            at poligon_settings_button_anim

        vbox:
            spacing 40
            align (0.1, 0.2)
            xoffset -100
            yoffset 120
            
            for page in ["poligon_FilePage_1", "poligon_FilePage_2", "poligon_FilePage_3", "poligon_FilePage_4", "poligon_FilePage_5", "poligon_FilePage_6"]:
                textbutton str(page[-1]):
                    text_style "poligon_save_screens_style"
                    style "poligon_save_screens_style"
                    activate_sound poligon_start_sound 
                    hover_sound poligon_button_menu
                    action FilePage(page) 


        grid 4 3:
            xpos 0.11
            ypos 0.2
            xmaximum 0.81
            ymaximum 0.65
            transpose False
            xfill True
            yfill True
            for i in range(1001, 1013):
                $ display_num = i - 1000
                fixed:
                    add FileScreenshot(str(i)) at poligon_settings_button_anim:
                        xpos 10
                        ypos 10
                    button:
                        action SetVariable("selected_slot", str(i))
                        activate_sound poligon_start_sound
                        hover_sound poligon_button_menu
                        xfill False
                        yfill False
                        style "poligon_save_load_button"
                        has fixed
                        text ("%s." % display_num + FileTime(str(i), format=' %d.%m.%y, %H:%M', empty=" "+"Пусто") + "\n" +FileSaveName(str(i))) at poligon_settings_button_anim:
                            style "poligon_save_load_button_text"
                            xpos 15
                            ypos 15


#Респект
screen poligon_mods_info:
    text "Made with love by Dejavu Team (c) 2025" style "poligon_new_mods_style" text_align 0.5 align (0.5, 0.99) at poligon_mods_info_anim

screen poligon_mods:
    tag menu
    modal True


    $ bar_null = Frame(get_image("gui/settings/bar_null.png"),12,12)
    $ bar_full = Frame(get_image("gui/settings/bar_full.png"),12,12)
    window:
        background get_image("gui/settings/preferences_bg.jpg")
        hbox:
            align (0.5, 0.08)
            add get_image("gui/settings/star.png") yalign 0.65
            text " "+translation["mods"][_preferences.language]+" " style "settings_link" yalign 0.5 color "#FFFFFF"
            add get_image("gui/settings/star.png") yalign 0.65
        textbutton translation["Back"][_preferences.language] style "log_button" text_style "settings_link":
            align (0.015, 0.92) action ShowMenu("preferences")
        if mods:
            side "c b r" area (0.27, 0.24, 0.47, 0.70):
                viewport id "mods" draggable True mousewheel True scrollbars None yinitial 0.0:
                    has grid 1 len(mods)
                    for lbl, name in sorted(mods.iteritems()):
                        textbutton name style "log_button":
                            if name == "Полигон Совёнок":
                                text_style "poligon_mods_screens_style" ypos 0.02
                                activate_sound poligon_start_sound
                                hover_sound poligon_button_menu
                                hovered [Show("poligon_mods_info")]
                                unhovered Hide("poligon_mods_info")
                                at poligon_load_anim
                            else:
                                text_style "settings_text"
                            action (SetField(persistent, "jump_to", lbl), SetVariable(backdrop, 'prologue'), Start())
                bar value XScrollValue("mods"):
                    left_bar "images/misc/none.png" right_bar "images/misc/none.png"
                    thumb "images/misc/none.png" hover_thumb "images/misc/none.png"
                vbar value YScrollValue("mods"):
                    bottom_bar "images/misc/none.png" top_bar "images/misc/none.png"
                    thumb "images/gui/settings/vthumb.png" thumb_offset -12

#Предупреждение

# Это пришлось скостылить, ибо если вызывать через MainMenu(), то вообще ломает всё к фигам, потому увы
screen poligon_warning_mainmenu(messages, action_yes, action_no):

    modal True

    add "base_poligon" xalign 0.5 yalign 0.5

    text messages text_align 0.5 yalign 0.5 xalign 0.5 color "#fff" font poligon_fonts + "zhizn.ttf" size 50
    hbox:
        xalign 0.5 yalign 0.75
        spacing 500
        imagebutton:
            idle "box_yes" hover "box_yes" at poligon_settings_button_anim action action_yes
        imagebutton:
            idle "box_no" hover "box_no" at poligon_settings_button_anim action action_no


screen poligon_warning:

    modal True

    add "base_poligon" xalign 0.5 yalign 0.5

    text _(message) text_align 0.5 yalign 0.5 xalign 0.5 color "#fff" font poligon_fonts + "zhizn.ttf" size 50
    hbox:
        xalign 0.5 yalign 0.75
        spacing 500
        imagebutton:
            idle "box_yes" hover "box_yes" at poligon_settings_button_anim action yes_action
        imagebutton:
            idle "box_no" hover "box_no" at poligon_settings_button_anim action no_action

######