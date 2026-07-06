# Пути через переменную, автоопределение картинок мода и бл с добавлением какой-то...красочности картинок? (P.S: Переделано автообъявление на более лучшее.)
init -1199 python:
    from os import path
    import store

    poligon_mod_folder = 'poligon/'
    poligon_main_path = poligon_mod_folder + 'source/'
    poligon_images = poligon_main_path + 'images/'
    poligon_fonts = poligon_main_path + 'fonts/'
    poligon_videos = poligon_main_path + 'videos/'
    poligon_prefix = 'poligon_'

    def poligon_define_assets(poligon_mod_folder, poligon_sprites_folder):
        for file in renpy.list_files():

            if poligon_mod_folder not in file:
                continue

            filename = path.splitext(path.basename(str(file)))[0]
            lower_file = file.lower()

            # БГ
            if '/bg/' in lower_file and lower_file.endswith(('.png', '.jpg')):
                renpy.image(
                    'bg ' + poligon_prefix + filename,
                    im.Composite((1920,1080), (0,0), file)   
                )

            # Арты
            elif '/cg/' in lower_file and lower_file.endswith(('.png', '.jpg')):
                renpy.image(
                    'cg ' + poligon_prefix + filename,
                    im.Composite((1920,1080), (0,0), file)   
                )

            # Спрайты
            elif poligon_sprites_folder in file and lower_file.endswith('.png'):
                parts = file.replace('\\', '/').split('/')
                try:
                    idx = parts.index('sprites') + 1
                    char_name = parts[idx]
                    next_part = parts[idx+1]
                    distance = next_part if next_part in ('close', 'normal', 'far') else 'normal'
                    image_name = filename
                    #image_name = f"{char_name}_{filename}"

                    renpy.image(
                        #f"{char_name} {img_name} {distance}",
                        "{char} {img} {dist}".format(
                            char = char_name,
                            img  = image_name,
                            dist = distance
                        ),
                        ConditionSwitch(
                            "poligon_sprite_set == 'sunset'",
                            im.MatrixColor(file, im.matrix.tint(0.94, 0.82, 1.0)),
                            "poligon_sprite_set == 'night'",
                            im.MatrixColor(file, im.matrix.tint(0.63, 0.78, 0.82)),
                            True, file
                        )
                    )

                except:
                    pass

            # Всё остальное
            elif lower_file.endswith(('.png', '.jpg')):
                renpy.image(poligon_prefix + filename, file)

            # Видео
            elif lower_file.endswith(('.webm', '.flv', '.vob')):
                renpy.image(
                    'videos ' + poligon_prefix + filename,
                    Movie(
                        fps=60,
                        size=(1920,1080),
                        loop=False,
                        play=file
                    )
                )

            # Аудио
            elif file.endswith(('.wav', '.mp2', '.mp3', '.ogg', '.opus')):
                globals()[poligon_prefix + filename] = file



    def poligon_define_es_assets(poligon_es_folder):
        for file in renpy.list_files():
            if poligon_es_folder in file:
                file_name = path.splitext(path.basename(file))[0]
                if file.endswith((".png", ".jpg")):
                    renpy.image(
                        "bg " + poligon_prefix + file_name,
                        im.Composite((1920,1080), (0,0), file)
                    )