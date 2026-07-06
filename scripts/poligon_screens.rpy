init:

    image poligon_vbar_character = im.Scale("poligon/source/images/gui/bar/vbar_track.png", 15, 895)
    image poligon_vbar_history = im.Scale("poligon/source/images/gui/bar/vbar_track.png", 15, 810)
    image poligon_vbar_about = im.Scale("poligon/source/images/gui/bar/vbar_track.png", 15, 657)
    image poligon_hbar_preferences_menu_full = im.Scale("poligon/source/images/gui/bar/bar_full.png",450,40)
    image poligon_hbar_preferences_menu_null = im.Scale("poligon/source/images/gui/bar/bar_null.png",450,40)
    image poligon_hbar_preferences_full = im.Scale("poligon/source/images/gui/bar/bar_full.png",520,40)
    image poligon_hbar_preferences_null = im.Scale("poligon/source/images/gui/bar/bar_null.png",520,40)


###### Screen для меню

screen poligon_main_menu:
    tag menu
    modal True

    imagemap:
        auto poligon_images + "gui/main_menu/social_%s.png"
        hotspot (826, 525, 197, 184) clicked OpenURL("https://vk.com/zonadejavu")
        hotspot (824, 714, 200, 184) clicked OpenURL("https://t.me/poligonsovenok")

    vbox:
        align (0.75, 0.58)
        yoffset -10
        xoffset 21
        spacing 25
        imagebutton:
            idle poligon_images + "gui/main_menu/start_button.png"
            hover poligon_images + "gui/main_menu/start_button.png"
            activate_sound poligon_start_sound hover_sound poligon_button_menu
            xoffset 25
            at poligon_menu_anim(-0.17, 0.17, 1.05)
            action ShowMenu('poligon_chapters')
        imagebutton:
            idle poligon_images + "gui/main_menu/archive_button.png"
            hover poligon_images + "gui/main_menu/archive_button.png"
            activate_sound poligon_start_sound hover_sound poligon_button_menu
            xoffset 77
            at poligon_menu_anim(-0.17, 0.17, 1.05)
            action ShowMenu('poligon_archive')
        imagebutton:
            idle poligon_images + "gui/main_menu/videoplayer_button.png"
            hover poligon_images + "gui/main_menu/videoplayer_button.png"
            hover_sound poligon_button_menu
            xoffset -10
            at poligon_menu_anim(-0.08, 0.08, 1.01)
            action ShowMenu('poligon_videoplayer')
        imagebutton:
            idle poligon_images + "gui/main_menu/load_button.png"
            hover poligon_images + "gui/main_menu/load_button.png"
            activate_sound poligon_start_sound hover_sound poligon_button_menu
            xoffset 20
            at poligon_menu_anim(-0.17, 0.17, 1.05)
            action ShowMenu('poligon_load')
        imagebutton:
            idle poligon_images + "gui/main_menu/preferences_button.png"
            hover poligon_images + "gui/main_menu/preferences_button.png"
            activate_sound poligon_start_sound hover_sound poligon_button_menu
            xoffset 26
            at poligon_menu_anim(-0.17, 0.17, 1.05)
            action ShowMenu('poligon_preferences_menu')
        imagebutton:
            idle poligon_images + "gui/main_menu/achievements_button.png"
            hover poligon_images + "gui/main_menu/achievements_button.png"
            hover_sound poligon_button_menu
            xoffset -10
            at poligon_menu_anim(-0.07, 0.07, 1.02)
            action Play("audio", "poligon/source/audio/sfx/gui/locked_error.mp3")
    imagebutton:
        align (0.75, 0.90)
        xoffset -162
        yoffset 35
        idle poligon_images + "gui/main_menu/about_button.png"
        hover poligon_images + "gui/main_menu/about_button.png"
        activate_sound poligon_start_sound hover_sound poligon_button_menu
        at poligon_menu_anim(-0.2, 0.1, 1.03)
        action ShowMenu("poligon_about")
    imagebutton:
        align (0.75, 0.90)
        xoffset 166
        yoffset 35
        idle poligon_images + "gui/main_menu/exit_button.png"
        hover poligon_images + "gui/main_menu/exit_button.png"
        activate_sound poligon_start_sound hover_sound poligon_button_menu
        at poligon_menu_anim(-0.2, 0.1, 1.03)
        action ShowMenu("poligon_quit")


screen poligon_preferences_menu:
    tag menu
    modal True

    imagebutton:
        align (0.69, 0.90)
        xoffset 55
        yoffset 35
        idle poligon_images + "gui/main_menu/exit_button.png"
        hover poligon_images + "gui/main_menu/exit_button.png"
        activate_sound poligon_start_sound hover_sound poligon_button_menu
        at poligon_menu_anim(-0.1, 0.1, 1.03)
        action Return()

    frame:
        style "poligon_scrollable_frame"
        xysize (632, 657)
        align (0.8, 0.65)

        has viewport
        mousewheel True
        draggable True
        vbox:
            spacing 5
            vbox:
                align (0.5, 0.5)

                hbox:
                    spacing 55
                    vbox:
                        text "Режим экрана" style "poligon_settings_style"
                        textbutton "В окне" style "log_button" text_style "poligon_settings_button_style" activate_sound poligon_start_sound hover_sound poligon_button_menu action Preference("display", "window") at poligon_settings_button_anim
                        textbutton "Полный экран" style "log_button" text_style "poligon_settings_button_style" activate_sound poligon_start_sound hover_sound poligon_button_menu action Preference("display", "fullscreen") at poligon_settings_button_anim
                    vbox:
                        text "Режим пропуска" style "poligon_settings_style"
                        textbutton "Всё" style "log_button" text_style "poligon_settings_button_style" activate_sound poligon_start_sound hover_sound poligon_button_menu action Preference("skip", "all") at poligon_settings_button_anim
                        textbutton "Виденное ранее" style "log_button" text_style "poligon_settings_button_style" activate_sound poligon_start_sound hover_sound poligon_button_menu action Preference("skip", "seen") at poligon_settings_button_anim

                text "Громкость музыки" style "poligon_settings_style" yoffset 10

                bar value Preference("music volume") left_bar "poligon_hbar_preferences_menu_full" right_bar "poligon_hbar_preferences_menu_null" thumb "poligon/source/images/gui/bar/htumb.png" hover_thumb "poligon/source/images/gui/bar/htumb.png" xmaximum 450 ymaximum 40 thumb_offset -10 yoffset 10 at poligon_settings_button_anim

                text "Громкость эффектов" style "poligon_settings_style" yoffset 10

                bar value Preference("sound volume") left_bar "poligon_hbar_preferences_menu_full" right_bar "poligon_hbar_preferences_menu_null" thumb "poligon/source/images/gui/bar/htumb.png" hover_thumb "poligon/source/images/gui/bar/htumb.png" xmaximum 450 ymaximum 40 thumb_offset -10 yoffset 10 at poligon_settings_button_anim

                text "Громкость фона" style "poligon_settings_style" yoffset 10

                bar value Preference("voice volume") left_bar "poligon_hbar_preferences_menu_full" right_bar "poligon_hbar_preferences_menu_null" thumb "poligon/source/images/gui/bar/htumb.png" hover_thumb "poligon/source/images/gui/bar/htumb.png" xmaximum 450 ymaximum 40 thumb_offset -10 yoffset 10 at poligon_settings_button_anim

                text "Скорость текста" style "poligon_settings_style" yoffset 10

                bar value Preference("text speed") left_bar "poligon_hbar_preferences_menu_full" right_bar "poligon_hbar_preferences_menu_null" thumb "poligon/source/images/gui/bar/htumb.png" hover_thumb "poligon/source/images/gui/bar/htumb.png" xmaximum 450 ymaximum 40 thumb_offset -10 yoffset 10 at poligon_settings_button_anim

                text "Время автоперехода" style "poligon_settings_style" yoffset 10

                bar value Preference("auto-forward time") left_bar "poligon_hbar_preferences_menu_full" right_bar "poligon_hbar_preferences_menu_null" thumb "poligon/source/images/gui/bar/htumb.png" hover_thumb "poligon/source/images/gui/bar/htumb.png" xmaximum 450 ymaximum 40 thumb_offset -10 yoffset 10 at poligon_settings_button_anim

screen poligon_about:

    tag menu
    modal True

    imagebutton:
        align (0.69, 0.90)
        xoffset 55
        yoffset 35
        idle poligon_images + "gui/main_menu/exit_button.png"
        hover poligon_images + "gui/main_menu/exit_button.png"
        activate_sound poligon_start_sound hover_sound poligon_button_menu
        at poligon_menu_anim(-0.1, 0.1, 1.03)
        action Return()

    viewport id "poligon_about":
        xysize (632, 663) 
        align (0.78, 0.65) 
        mousewheel True 
        draggable True 
        style "poligon_scrollable_frame"
        vbox:
            text _(
"""За фасадом беззаботного летнего лагеря для сирот скрывается жуткая правда. \"Совёнок\n – не место отдыха, а клетка, где пионеры – не дети, а подопытные кролики. Их жизни – грязные записи в научных журналах. Их будущее – предрешено.
\nВас ждет мрачная история, разделенная на четыре главы:

Глава 1: UVAO – Её мир — это четыре стены комнаты, где пыльные шторы колышутся от сквозняка. Она привыкла к боли, к капельницам, к жалости в глазах врачей.
Привыкла, что каждый день может стать последним. Но сегодня всё иначе. После очередного приступа ей предлагают спасение — экспериментальное лечение, шанс, о котором она не смела мечтать.
Никто не говорит ей о цене. Никто не предупреждает, что значит \"полная регенерация организма\". А когда она проснётся — уже не будет прежней. 
Что останется от неё, когда отступят боли? И кого она увидит в зеркале? 

Глава 2: Пионер – Шепотом передают историю о Пионере, загадочном призраке лагеря. Он появляется из ниоткуда, говорит с тобой, и исчезает в пустоте. 
Миф? Психоз? Или ключ к правде, который пытается достучаться до тех, кто еще может слышать? Разгадайте тайну Пионера, прежде чем она узнает о вас.

Глава 3: Тихоня – Она — обычная девушка, чья и так несладкая жизнь превратилась в настоящий кошмар. Её выбрали. Не за навыки, не за заслуги, а просто как подопытную крысу в жестоком эксперименте.  
Цель: создать идеальное живое оружие. Она должна остановить её — сбежавшую испытуемую, которая теперь представляет угрозу для всех. Но чтобы поймать монстра, ей самой придётся им стать.

Глава 4: \"Тайное не становится явным.\" Смена где сходятся все потерянные дети. Серафим, парень которому не повезло родиться в такое время, случайно узнает секрет, который не должен был знать. 
Теперь его жизнь в опасности. Он должен раскрыть правду о \"Совёнке\", прежде чем она поглотит его самого. Но помните: Каждая улика может оказаться ловушкой, а смотря в бездну, бездна смотрит в ответ.

Важно:
Этот мод не претендует на историческую достоверность. Это мрачная, фантастическая интерпретация вселенной \"Бесконечного лета\".
Все совпадения случайны.

Достижения будут добавлены в финальной главе.

Статус разработки:
Готова 1 из 4 глав.

Над модом работает команда \"Dejavu team\":
Nemirov, Markov, Lineko, Артём Кудасаев (xdeadmoonx), Павел, Ehaito, Marakya, Ayofangs, That Guy From 2015

Отдельная благодарность:
Bergen – Первоначальный код
Sagify – Анимированная заставка

Приготовьтесь к кошмару. \"Совёнок\" ждет."""
    ) style "poligon_scrollable_text"


    vbar value YScrollValue("poligon_about") bottom_bar "poligon_vbar_about" top_bar "poligon_vbar_about" thumb "poligon/source/images/gui/bar/vthumb.png" thumb_offset -12 xysize (632, 657) xoffset 510 yoffset 150 align (0.875, 0.3)

screen poligon_archive:

    tag menu
    modal True

    imagemap:
        auto poligon_images + "gui/archive/archive_%s.png"

        hotspot (642, 275, 585, 266) activate_sound poligon_start_sound hover_sound poligon_button_menu clicked If(
            pause_click == True, 
            [SetVariable("pause_click", False), Show("poligon_pause", transition=Dissolve(.2))], 
            ShowMenu("poligon_main_menu")
            )
        hotspot (333, 251, 235, 522) activate_sound poligon_start_sound hover_sound poligon_button_menu clicked [SetVariable("show_image", False), SetVariable("hovered_image", None), ShowMenu('poligon_characters')]
        hotspot (607, 653, 435, 143) activate_sound poligon_start_sound hover_sound poligon_button_menu clicked ShowMenu('poligon_arts')
        hotspot (579, 788, 413, 78) activate_sound poligon_start_sound hover_sound poligon_button_menu clicked ShowMenu('poligon_bg')
        hotspot (1056, 591, 428, 275) activate_sound poligon_start_sound hover_sound poligon_button_menu clicked [Function(renpy.music.set_pause, True, channel="music"), ShowMenu('poligon_musicplayer')]

#Немного накостылил.
screen poligon_characters:

    add "poligon_characters_background"

    tag menu
    modal True

    #Нужно, чтобы при экране с описанием персонажа, не было этих кнопок
    if button_SH == True:
        textbutton "В АРХИВ" text_style "poligon_characters_style" style "poligon_characters_style" align (0.06, 0.9555) activate_sound poligon_start_sound hover_sound poligon_button_menu action ShowMenu('poligon_archive') at poligon_settings_button_anim_in
        textbutton "В МЕНЮ" text_style "poligon_characters_style" style "poligon_characters_style" align (0.3888, 0.9555) activate_sound poligon_start_sound hover_sound poligon_button_menu action If(
            pause_click == True, 
            [SetVariable("pause_click", False), Show("poligon_pause", transition=Dissolve(.2))],
            ShowMenu('poligon_main_menu')) at poligon_settings_button_anim_in

    # Просто пробегаемся по списку, который есть для персонажей и смотрим на его доступность. Если есть, показываем.
    frame:
        style "poligon_scrollable_frame"
        xysize (670, 855)
        pos (1000,120)

        has viewport
        mousewheel True
        draggable True
        vbox:
            spacing 15
            for key, char in (persistent.poligon_characters or {}).items():
                if char["unlocked"]:
                    textbutton char["name"]:
                        text_style "poligon_characters_name_style" 
                        style "poligon_characters_style"
                        activate_sound poligon_start_sound hover_sound poligon_button_menu
                        hovered Show("hover_image", transition=Dissolve(.3), picturechar=char["image"])
                        unhovered Hide("hover_image", transition=Dissolve(.3))
                        action [Hide("hover_image", transition=Dissolve(.3)), SetVariable("button_SH", False), Show("poligon_characters_about", transition=Dissolve(.5), character=char)]
                        at poligon_settings_button_anim_characters_in


screen hover_image(picturechar):
    modal False
    add picturechar

#На персонажа, на которого мы нажали, передается аргумент в виде character=char, и мы смотрим этого персонажа, а из него вытаскиваем нужное нам описание.
screen poligon_characters_about(character):

    key "K_ESCAPE" action [SetVariable("button_SH", True), Hide("poligon_characters_about", transition=Dissolve(.5))]

    modal True

    textbutton "НАЗАД" text_style "poligon_characters_style" style "poligon_characters_style" align (0.2111, 0.9555) activate_sound poligon_start_sound hover_sound poligon_button_menu action [SetVariable("button_SH", True), Hide("poligon_characters_about", transition=Dissolve(.5))] at poligon_settings_button_anim_in

    viewport id "poligon_characters_about" xysize (852, 870) align (0.08, 0.187) mousewheel True draggable True:
        style "poligon_scrollable_frame"
        vbox:
            for text_char in character["descs"]:
                text text_char style "poligon_scrollable_text" at poligon_fade_in

    
    vbar value YScrollValue("poligon_characters_about") bottom_bar "poligon_vbar_character" top_bar "poligon_vbar_character" thumb "poligon/source/images/gui/bar/vthumb.png" thumb_offset -12 xysize (852, 895) align (0.875, 0.3)


#Тоже самое, такая же работа со списком.
screen poligon_musicplayer:

    add "poligon_player_background"
    
    tag menu
    modal True

    imagemap:
        auto poligon_images +"gui/player/player_buttons_%s.png"
        hotspot (423, 206, 340, 202) activate_sound poligon_start_sound hover_sound poligon_button_menu clicked [Function(renpy.music.set_pause, False, channel="music"), Function(poligon_stop_music), ShowMenu("poligon_archive")]
        hotspot (407, 666, 373, 226) activate_sound poligon_start_sound hover_sound poligon_button_menu clicked If(
            pause_click == True,
            [SetVariable("pause_click", False), Function(poligon_stop_music), Function(renpy.music.set_pause, False, channel="music"), Show("poligon_pause", transition=Dissolve(.2))],
            [Function(renpy.music.set_pause, False, channel="music"), Function(poligon_stop_music), ShowMenu("poligon_main_menu")]
            )

    frame:
        style "poligon_scrollable_frame"
        xysize (670, 790)
        align (0.655, 0.7333)
        xoffset 5

        has viewport
        mousewheel True
        draggable True
        vbox:
            for key, poligon_track in (persistent.poligon_music or {}).items():
                if poligon_track["unlocked"]:
                    textbutton poligon_track["name"]:
                        style "poligon_characters_name_style"
                        text_style "poligon_characters_name_style"
                        activate_sound poligon_start_sound hover_sound poligon_button_menu
                        action Function(poligon_play_music, poligon_track["file"])
                        at poligon_settings_button_anim_characters

#Тут работа со страницами. Также список с картинками, но здесь мы делаем переменную со списком артов. На экране помещается только 4 картинки, потому пробегаем цикл из 4. 
#Если разблокировано, показываем на 0(1) странице. В зависимости от кол-ва открытых артов, столько и будет страниц.
screen poligon_arts(page=0):

    key "K_ESCAPE" action ShowMenu("poligon_archive")

    tag menu
    modal True

    add "poligon_arts_background"

    imagemap:
        auto poligon_images + "gui/arts_bg/arts_bg_buttons_%s.png"
        hotspot (817, 283, 356, 221) activate_sound poligon_start_sound hover_sound poligon_button_menu clicked ShowMenu("poligon_archive")
        hotspot (804, 715, 378, 250) activate_sound poligon_start_sound hover_sound poligon_button_menu clicked If(
            pause_click == True,
            [SetVariable("pause_click", False), Show("poligon_pause", transition=Dissolve(.2))],
            ShowMenu("poligon_main_menu")
            )


    $ arts_list = [item for item in sorted(persistent.poligon_arts.items()) if item[1].get("unlocked", False)]
    $ positions = [
        (200, 170),     # Верхний левый
        (1250, 170),     # Верхний правый
        (200, 600),     # Нижний левый
        (1250, 600)      # Нижний правый
    ]
    
    
    for i in range(4):
        $ index = page * 4 + i
        if index < len(arts_list):
            $ art_key, art_data = arts_list[index]
            $ xpos, ypos = positions[i]
            imagebutton:
                xpos xpos
                ypos ypos
                idle art_data["menu_file"]
                hover art_data["menu_file"] at poligon_artsbg_hover
                activate_sound poligon_start_sound hover_sound poligon_button_menu
                focus_mask True
                action [Show("poligon_arts_view", transition=Dissolve(.5), arts_file=art_data["show_file"])]

    
    imagemap:
        auto poligon_images + "gui/arts_bg/arts_bg_arrows_%s.png"
        if page > 0:
            hotspot (716, 504, 243, 168) activate_sound poligon_start_sound hover_sound poligon_button_menu clicked Show("poligon_arts", page=page-1)
        if (page+1)*4 < len(arts_list):
            hotspot (1016, 504, 231, 173) activate_sound poligon_start_sound hover_sound poligon_button_menu clicked Show("poligon_arts", page=page+1)

#Такая же схема передачи аргумента
screen poligon_arts_view(arts_file):

    modal True

    add "poligon_arts_background" at poligon_blur
    
    #Чтобы убирать экран, надо нажимать ЛКМ, думаю очень интуитивно понятно
    key "mouseup_1" action Hide("poligon_arts_view", transition=Dissolve(.5))

    frame:
        background "#FFFFFF"
        xalign 0.5
        yalign 0.5
        padding (10,10,10,10)
        xysize (1680 + 20, 1050 + 20)

    add arts_file xysize (1680, 1050) xalign 0.5 yalign 0.5

#Тоже самое как и арты
screen poligon_bg(page=0):

    key "K_ESCAPE" action ShowMenu("poligon_archive")

    tag menu
    modal True

    add "poligon_bg_background"

    imagemap:
        auto poligon_images + "gui/arts_bg/arts_bg_buttons_%s.png"
        hotspot (817, 283, 356, 221) activate_sound poligon_start_sound hover_sound poligon_button_menu clicked ShowMenu("poligon_archive")
        hotspot (804, 715, 378, 250) activate_sound poligon_start_sound hover_sound poligon_button_menu clicked If(
            pause_click == True,
            [SetVariable("pause_click", False), Show("poligon_pause", transition=Dissolve(.2))],
            ShowMenu("poligon_main_menu")
            )


    $ bg_list = [item for item in sorted(persistent.poligon_bg.items()) if item[1].get("unlocked", False)]
    
    $ positions = [
        (200, 170),
        (1250, 170),
        (200, 600),
        (1250, 600)
    ]

    for i in range(4):
        $ index = page * 4 + i
        if index < len(bg_list):
            $ bg_key, bg_data = bg_list[index]
            $ xpos, ypos = positions[i]
            imagebutton:
                xpos xpos
                ypos ypos
                idle bg_data["menu_file"]
                hover bg_data["menu_file"] at poligon_artsbg_hover
                activate_sound poligon_start_sound hover_sound poligon_button_menu
                focus_mask True
                action [Show("poligon_bg_view", transition=Dissolve(.5), bg_file=bg_data["show_file"])]

    
    imagemap:
        auto poligon_images + "gui/arts_bg/arts_bg_arrows_%s.png"
        if page > 0:
            hotspot (716, 504, 243, 168) activate_sound poligon_start_sound hover_sound poligon_button_menu clicked Show("poligon_bg", page=page-1)
        if (page+1)*4 < len(bg_list):
            hotspot (1016, 504, 231, 173) activate_sound poligon_start_sound hover_sound poligon_button_menu clicked Show("poligon_bg", page=page+1)

#Такая же схема передачи аргумента
screen poligon_bg_view(bg_file):

    modal True

    add "poligon_bg_background" at poligon_blur
    
    key "mouseup_1" action Hide("poligon_bg_view", transition=Dissolve(.5))

    #Белая рамка
    frame:
        background "#FFFFFF"
        xalign 0.5
        yalign 0.5
        padding (10,10,10,10)
        xysize (1680 + 20, 1050 + 20)

    add bg_file xysize (1680, 1050) xalign 0.5 yalign 0.5


screen poligon_videoplayer(page=0):

    tag menu
    modal True

    add "poligon_videoplayer_background"

    imagemap:
        auto poligon_images + "gui/videoplayer/videoplayer_button_menu_%s.png"
        hotspot (17, 4, 270, 190) activate_sound poligon_start_sound hover_sound poligon_button_menu clicked ShowMenu("poligon_main_menu")

    $ poligon_videos_list = [item for item in sorted(persistent.poligon_videoplayers.items()) if item[1].get("unlocked", False)]
    $ total_pages = len(poligon_videos_list)

    if page < total_pages:
        $ key, video_data = poligon_videos_list[page]
        imagebutton:
            idle video_data["file"]
            hover video_data["file"]
            focus_mask True
            activate_sound poligon_start_sound 
            hover_sound poligon_button_menu
            xoffset -0.1
            yoffset -0.07
            at poligon_videoplayer_anim(-0.1, 0.1, -0.07, 0.07, 1.007)
            action [SetVariable("video", video_data["video"]), SetVariable("videoplayer_page", page), Start("poligon_video_play")]

    imagemap:
        auto poligon_images + "gui/videoplayer/videoplayer_arrows_%s.png"
        if page > 0:
            hotspot (114, 438, 291, 197) activate_sound poligon_start_sound hover_sound poligon_button_menu clicked Show("poligon_videoplayer", page=page-1)
        if page + 1 < total_pages:
            hotspot (1585, 436, 280, 201) activate_sound poligon_start_sound hover_sound poligon_button_menu clicked Show("poligon_videoplayer", page=page+1)



screen poligon_chapters:

    tag menu
    modal True

    add "poligon_select_chapters_background"
    add "poligon_select_chapters_unavailable_234"

    imagemap:
        auto poligon_images + "gui/chapters/select_chapters_button_menu_%s.png"
        hotspot(1206, 872, 293, 195) activate_sound poligon_start_sound hover_sound poligon_button_menu clicked ShowMenu("poligon_main_menu")

    imagemap:
        auto poligon_images + "gui/chapters/select_chapters_uvao_%s.png"
        hotspot (35, 343, 477, 513) activate_sound poligon_start_sound hover_sound poligon_button_menu clicked Show("poligon_chapters_about", poligon_chapters_about_text=poligon_about_chapters["UVAO"]["text"], poligon_chapters_about_image=poligon_about_chapters["UVAO"]["image"])

    
screen poligon_chapters_about(poligon_chapters_about_text, poligon_chapters_about_image):

    modal True
    
    add "poligon_select_chapters_background" at poligon_blur
    add "poligon_select_chapters_unavailable_234" at poligon_blur

    key "K_ESCAPE" action Hide("poligon_chapters_about", transition=Dissolve(.2))
    key "mouseup_2" action Hide("poligon_chapters_about", transition=Dissolve(.2))

    add poligon_chapters_about_image at poligon_chapters_about_in(0.05, 0.05, -1000, 150, 20)
    add "poligon_select_chapters_backtext" at poligon_chapters_about_in(0, 0, 1000, 0, 0)

    viewport id "poligon_chapters_text" xysize (957, 940) align (0.9, 0.187) xoffset 60 yoffset 50 draggable True mousewheel True:
        style "poligon_scrollable_frame"
        vbox:
            text poligon_chapters_about_text style "poligon_chapters_scrollable_text" at poligon_chapters_about_in(0, 0, 1000, 0, 0)

    textbutton "НАЧАТЬ" style "poligon_chapters_text_style" text_style "poligon_chapters_text_style" align (0.9555, 0.9555) activate_sound poligon_start_sound hover_sound poligon_button_menu action [Hide("poligon_chapters_about", transition=Dissolve(.2)), SetVariable("select_chapter", "UVAO"), Start("poligon_start_label")] at poligon_chapters_about_in_button(0.9555, 0.9555, 1000, 0, 0)
    textbutton "НАЗАД" style "poligon_chapters_text_style" text_style "poligon_chapters_text_style" align (0.7, 0.9555) activate_sound poligon_start_sound hover_sound poligon_button_menu action Hide("poligon_chapters_about", transition=Dissolve(.2)) at poligon_chapters_about_in_button(0.7, 0.9555, 1000, 0, -170)



screen credits_chapter_1:

    zorder 100
    tag credits

    default time = 0.0
    default t = 1.6

    timer 0.1 repeat True action SetScreenVariable("time", time + 0.1)


    if 0.0 <= time < 5.0:
        text "НАД ПЕРВОЙ ГЛАВОЙ РАБОТАЛИ" at poligon_credits_fade_in_out(2):
            xalign 0.5
            yalign 0.5
            size 80
            style "poligon_credits_text"

    if 4.0 <= time < 9.0:
        text "DEJAVU TEAM" at poligon_credits_fade_in(2.9):
            xalign 0.5
            yalign 0.5
            size 80
            style "poligon_credits_text"

    if 8.0 <= time < 33.0:
        text "DEJAVU TEAM" at poligon_credits_move_up:
            xalign 0.5
            yalign 0.5
            size 80
            style "poligon_credits_text"

        vbox:
            xalign 0.5
            yalign 0.65
            xoffset 90
            yoffset -50
            spacing 14


            text "Nemirov — руководитель проекта" at poligon_credits_delayed_appear(t * 1) style "poligon_credits_text" size 45
            text "Lineko — художник" at poligon_credits_delayed_appear(t * 2) style "poligon_credits_text" size 45
            text "Markov — сценарист первой главы" at poligon_credits_delayed_appear(t * 3) style "poligon_credits_text" size 45
            text "Артём Кудасаев (xdeadmoonx) — тех. часть,\nдоработка кода сценария" at poligon_credits_delayed_appear(t * 4) style "poligon_credits_text" size 45
            text "Ehaito — кодер сценария" at poligon_credits_delayed_appear(t * 5) style "poligon_credits_text" size 45
            text "Ayofangs, That Guy from 2015, Marakya — композиторы" at poligon_credits_delayed_appear(t * 6) style "poligon_credits_text" size 45
            text "Павел — редактор первой главы" at poligon_credits_delayed_appear(t * 7) style "poligon_credits_text" size 45
            

    timer 30.0 action Hide("credits_chapter_1", transition=Dissolve(2.0))
