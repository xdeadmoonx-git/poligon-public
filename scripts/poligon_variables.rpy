init -700 python:

    # persistent.poligon_first_start = "reset"
    # persistent.poligon_update_patch_4 = None

    # if persistent.poligon_update_patch_3 is None:
    #     if persistent.poligon_characters:
    #         del persistent.poligon_characters
    #     if persistent.poligon_arts:
    #         del persistent.poligon_arts
    #     if persistent.poligon_music:
    #         del persistent.poligon_music
    #     if persistent.poligon_bg:
    #         del persistent.poligon_bg
    #     if persistent.poligon_videoplayers:
    #         del persistent.poligon_videoplayers
    #     persistent.poligon_update_patch_3 = True
    #     persistent.poligon_first_start = "reset"
    #     renpy.save_persistent()
    
    # if persistent.poligon_update_patch_4 is None:
    #     if persistent.poligon_characters["semen"]:

    #         old_descs = [ persistent.poligon_characters["semen"].get("descs", None) ]
            
    #         del persistent.poligon_characters["semen"]["descs"]

    #         persistent.poligon_characters["semen"]["descs"] = {
    #             "chapter_1": [],
    #             "chapter_2": []
    #         }

    #         for i in old_descs:
    #             persistent.poligon_characters["semen"]["descs"]["chapter_1"].append(i)

    #     persistent.poligon_update_patch_4 = True
    #     renpy.save_persistent()


    if persistent.poligon_first_start is None or persistent.poligon_first_start == "reset":
        persistent.poligon_characters = {
            # Персонажи первой главы
            "violetta": {
                "name": "Виолетта Коллайдер",
                "descs": [],
                "image": "poligon_violettamini",
                "unlocked": False,
                "descs_2_unlocked": False
            },
            "semen": {
                "name": "Семён Персунов",
                # "descs": [],
                "descs": {
                    "chapter_1": [],
                    "chapter_2": [],
                },
                "image": "poligon_semenmini",
                "unlocked": False,
                "descs_2_unlocked": False,
                "descs_3_unlocked": False,
                "descs_4_unlocked": False
                },
            "uvao": {
                "name": "Юля",
                "descs": [],
                "image": "poligon_uvaomini",
                "unlocked": False,
                "descs_2_unlocked": False,
                "descs_3_unlocked": False,
                "descs_4_unlocked": False,
                "descs_5_unlocked": False,
                "descs_6_unlocked": False
            },
            "maxon": {
                "name": "Максим Каспийский",
                "descs": [],
                "image": "poligon_maxonmini",
                "unlocked": False,
                "descs_2_unlocked": False,
                "descs_3_unlocked": False
            }
        }

        persistent.poligon_music = {
            "menu_theme": {
                "name": "Marakya - Menu Theme",
                "file": "poligon/source/audio/music/menu_theme.ogg",
                "unlocked": True
            },
            # Музыка первой главы
            "a_terrible_dream": {
                "name": "Ayofangs - A Terrible Dream",
                "file": "poligon/source/audio/music/a_terrible_dream.ogg",
                "unlocked": False
            },
            "anatomy_of_fear": {
                "name": "Ayofangs - Anatomy of Fear",
                "file": "poligon/source/audio/music/anatomy_of_fear.ogg",
                "unlocked": False
            },
            "cloudy": {
                "name": "Ayofangs - Cloudy",
                "file": "poligon/source/audio/music/cloudy.ogg",
                "unlocked": False
            },
            "here_and_now": {
                "name": "Ayofangs - Here and Now",
                "file": "poligon/source/audio/music/here_and_now.ogg",
                "unlocked": False
            },
            "innocence": {
                "name": "SUNO AI - Innocence",
                "file": "poligon/source/audio/music/innocence.ogg",
                "unlocked": False
            },
            "mysterious_person": {
                "name": "Ayofangs - Mysterious Person",
                "file": "poligon/source/audio/music/mysterious_person.ogg",
                "unlocked": False
            },
            "out_of_the_darkness": {
                "name": "Ayofangs - Out of the Darkness",
                "file": "poligon/source/audio/music/out_of_the_darkness.ogg",
                "unlocked": False
            },
            "progulka": {
                "name": "Ayofangs - PROGULKA",
                "file": "poligon/source/audio/music/progulka.ogg",
                "unlocked": False
            },
            "pyrale": {
                "name": "Ayofangs - Pyrale",
                "file": "poligon/source/audio/music/pyrale.ogg",
                "unlocked": False
            },
            "reject_yourself": {
                "name": "That Guy From 2015 - Reject Yourself",
                "file": "poligon/source/audio/music/reject_yourself.ogg",
                "unlocked": False
            },
            "the_forester": {
                "name": "Marakya - The Forester",
                "file": "poligon/source/audio/music/the_forester.ogg",
                "unlocked": False
            },
            "the_stars_are_brighter_than_usual": {
                "name": "Marakya - The Stars Are Brighter Than Usual",
                "file": "poligon/source/audio/music/the_stars_are_brighter_than_usual.ogg",
                "unlocked": False
            },
            "time_for_reflection": {
                "name": "Marakya - Time for Reflection",
                "file": "poligon/source/audio/music/time_for_reflection.ogg",
                "unlocked": False
            },
            "unusual_girl": {
                "name": "That Guy From 2015 - Unusual Girl",
                "file": "poligon/source/audio/music/unusual_girl.ogg",
                "unlocked": False
            },
            "voltage": {
                "name": "Marakya – Voltage",
                "file": "poligon/source/audio/music/voltage.ogg",
                "unlocked": False
            },
            "who_are_you": {
                "name": "Ayofangs - Who Are You",
                "file": "poligon/source/audio/music/who_are_you.ogg",
                "unlocked": False
            },
            "a_speckled_sheet": {
                "name": "Ayofangs - A Speckled Sheet",
                "file": "poligon/source/audio/music/a_speckled_sheet.ogg",
                "unlocked": False
            },
            "there_is_only_hope": {
                "name": "Marakya - There Is Only Hope",
                "file": "poligon/source/audio/music/there_is_only_hope.ogg",
                "unlocked": False
            },
            "nochnik": {
                "name": "Ayofangs - Nochnik",
                "file": "poligon/source/audio/music/nochnik.ogg",
                "unlocked": False
            },
            "credits": {
                "name": "Ayofangs - Last Seconds",
                "file": "poligon/source/audio/music/credits.ogg",
                "unlocked": False
            }
            ##################
        }

        persistent.poligon_arts = {
            # Арты первой главы
            "gluki_Yuli_1_arh": {
                "menu_file": "poligon_gluki_Yuli_1_arh",
                "show_file": "cg poligon_gluki_Yuli_1", 
                "unlocked": False
                },
            "gluki_Yuli_2_arh": {
                "menu_file": "poligon_gluki_Yuli_2_arh",
                "show_file": "cg poligon_gluki_Yuli_2", 
                "unlocked": False
                },
            "kasha_arh": {
                "menu_file": "poligon_kasha_arh",
                "show_file": "cg poligon_kasha",
                "unlocked": False
                },
            "int_car_arh": {
                "menu_file": "poligon_int_car_arh",
                "show_file": "cg poligon_int_car",
                "unlocked": False
                },
            "int_car_lightness_arh": {
                "menu_file": "poligon_int_car_lightness_arh",
                "show_file": "cg poligon_int_car_lightness",
                "unlocked": False
                },
            "ext_forest_olen_2_arh": {
                "menu_file": "poligon_ext_forest_olen_2_arh",
                "show_file": "cg poligon_ext_forest_olen_2",
                "unlocked": False
                },
            "folder_close_arh": {
                "menu_file": "poligon_folder_close_arh",
                "show_file": "cg poligon_folder_close",
                "unlocked": False
            },
            "folder_open_arh": {
                "menu_file": "poligon_folder_open_arh",
                "show_file": "cg poligon_folder_open",
                "unlocked": False
            },
            "plakat_arh": {
                "menu_file": "poligon_plakat_arh",
                "show_file": "cg poligon_plakat",
                "unlocked": False
            },
            "radio_arh": {
                "menu_file": "poligon_radio_arh",
                "show_file": "cg poligon_radio",
                "unlocked": False
            },
            "ranka_1_arh": {
                "menu_file": "poligon_ranka_1_arh",
                "show_file": "cg poligon_ranka_1",
                "unlocked": False
            },
            "ranka_2_arh": {
                "menu_file": "poligon_ranka_2_arh",
                "show_file": "cg poligon_ranka_2",
                "unlocked": False
            },
            "ranka_3_arh": {
                "menu_file": "poligon_ranka_3_arh",
                "show_file": "cg poligon_ranka_3",
                "unlocked": False
            },
            "reznya_arh": {
                "menu_file": "poligon_reznya_arh",
                "show_file": "cg poligon_reznya",
                "unlocked": False
            },
            "yulya_eye_arh": {
                "menu_file": "poligon_yulya_eye_arh",
                "show_file": "cg poligon_yulya_eye",
                "unlocked": False
            },
            "viola_close_watch_arh": {
                "menu_file": "poligon_viola_close_watch_arh",
                "show_file": "cg poligon_viola_close_watch",
                "unlocked": False
            },
            "viola_road_day_arh": {
                "menu_file": "poligon_viola_road_day_arh",
                "show_file": "cg poligon_viola_road_day",
                "unlocked": False
            },
            "viola_road_sunset_arh": {
                "menu_file": "poligon_viola_road_sunset_arh",
                "show_file": "cg poligon_viola_road_sunset",
                "unlocked": False
            },
            "lab_ceiling_viola_arh": {
                "menu_file": "poligon_lab_ceiling_viola_arh",
                "show_file": "cg poligon_lab_ceiling_viola",
                "unlocked": False
            },
            "viola_tekstura_arh": {
                "menu_file": "poligon_viola_tekstura_arh",
                "show_file": "cg poligon_viola_tekstura",
                "unlocked": False
            },
            "viola_smile_arh": {
                "menu_file": "poligon_viola_smile_arh",
                "show_file": "cg poligon_viola_smile",
                "unlocked": False
            },
            "yulya_mirror_yourself_arh": {
                "menu_file": "poligon_yulya_mirror_yourself_arh",
                "show_file": "cg poligon_yulya_mirror_yourself",
                "unlocked": False
            },
            "lab_ceiling_moth_arh": {
                "menu_file": "poligon_lab_ceiling_moth_arh",
                "show_file": "cg poligon_lab_ceiling_moth",
                "unlocked": False
            },
            "yulya_forest_arh": {
                "menu_file": "poligon_yulya_forest_arh",
                "show_file": "cg poligon_yulya_forest",
                "unlocked": False
            },
            "yulya_forest_2_arh": {
                "menu_file": "poligon_yulya_forest_2_arh",
                "show_file": "cg poligon_yulya_forest_2",
                "unlocked": False
            },
            "yulya_maksim_library_arh": {
                "menu_file": "poligon_yulya_maksim_library_arh",
                "show_file": "cg poligon_yulya_maksim_library",
                "unlocked": False
            },
            "yulya_orphanage_arh": {
                "menu_file": "poligon_yulya_orphanage_arh",
                "show_file": "cg poligon_yulya_orphanage",
                "unlocked": False
            },
            "memories_arh": {
                "menu_file": "poligon_memories_arh",
                "show_file": "cg poligon_memories",
                "unlocked": False
            },
            "yulya_viola_car_sunset_arh": {
                "menu_file": "poligon_yulya_viola_car_sunset_arh",
                "show_file": "cg poligon_yulya_viola_car_sunset",
                "unlocked": False
            }
            ##############################
        }

        persistent.poligon_bg = {
            # Фоновые изображения первой главы
            "library_arh": {
                "menu_file": "poligon_library_arh",
                "show_file": "bg poligon_library", 
                "unlocked": False
                },
            "ext_hospital_day_arh": {
                "menu_file": "poligon_ext_hospital_day_arh",
                "show_file": "bg poligon_ext_hospital_day",
                "unlocked": False
                },
            "corridor_orphanage_night_arh": {
                "menu_file": "poligon_corridor_orphanage_night_arh",
                "show_file": "bg poligon_corridor_orphanage_night", 
                "unlocked": False
                },
            "yulya_room_arh": {
                "menu_file": "poligon_yulya_room_arh",
                "show_file": "bg poligon_yulya_room",
                "unlocked": False
                },
            "fire_son_arh": {
                "menu_file": "poligon_fire_son_arh",
                "show_file": "bg poligon_fire_son",
                "unlocked": False
                },
            "hallucination_background_arh": {
                "menu_file": "poligon_hallucination_background_arh",
                "show_file": "bg poligon_hallucination_background",
                "unlocked": False
                },
            "hallucination_red_background_arh": {
                "menu_file": "poligon_hallucination_red_background_arh",
                "show_file": "bg poligon_hallucination_red_background",
                "unlocked": False
                },
            "int_hospital_cabinet_arh": {
                "menu_file": "poligon_int_hospital_cabinet_arh",
                "show_file": "bg poligon_int_hospital_cabinet",
                "unlocked": False
            },
            "int_hospital_day_arh": {
                "menu_file": "poligon_int_hospital_day_arh",
                "show_file": "bg poligon_int_hospital_day",
                "unlocked": False
            },
            "hooks_blood_arh": {
                "menu_file": "poligon_hooks_blood_arh",
                "show_file": "bg poligon_hooks_blood",
                "unlocked": False
            },
            "lab_ceiling_arh": {
                "menu_file": "poligon_lab_ceiling_arh",
                "show_file": "bg poligon_lab_ceiling",
                "unlocked": False
            },
            "lab_room_arh": {
                "menu_file": "poligon_lab_room_arh",
                "show_file": "bg poligon_lab_room",
                "unlocked": False
            },
            "ext_forest_streamlet_night_arh": {
                "menu_file": "poligon_ext_forest_streamlet_night_arh",
                "show_file": "bg poligon_ext_forest_streamlet_night",
                "unlocked": False
            },
            "ext_forest_streamlet_sunset_arh": {
                "menu_file": "poligon_ext_forest_streamlet_sunset_arh",
                "show_file": "bg poligon_ext_forest_streamlet_sunset",
                "unlocked": False
            },
            "ext_orphanage_car_arh": {
                "menu_file": "poligon_ext_orphanage_car_arh",
                "show_file": "bg poligon_ext_orphanage_car",
                "unlocked": False
            },
            "int_aidpost_sunset_folders_arh": {
                "menu_file": "poligon_int_aidpost_sunset_folders_arh",
                "show_file": "bg poligon_int_aidpost_sunset_folders",
                "unlocked": False
            },
            "ext_forest_olen_1_arh": {
                "menu_file": "poligon_ext_forest_olen_1_arh",
                "show_file": "bg poligon_ext_forest_olen_1",
                "unlocked": False
            },
            "palata_yuli_arh": {
                "menu_file": "poligon_palata_yuli_arh",
                "show_file": "bg poligon_palata_yuli",
                "unlocked": False
            },
            "train_dark_arh": {
                "menu_file": "poligon_train_dark_arh",
                "show_file": "bg poligon_train_dark",
                "unlocked": False
            },
            "stena_arh": {
                "menu_file": "poligon_stena_arh",
                "show_file": "bg poligon_stena",
                "unlocked": False
            },
            "yulya_room_night_arh": {
                "menu_file": "poligon_yulya_room_night_arh",
                "show_file": "bg poligon_yulya_room_night",
                "unlocked": False
            },
            "train_station_dark_arh": {
                "menu_file": "poligon_train_station_dark_arh",
                "show_file": "bg poligon_train_station_dark",
                "unlocked": False
            }
            ########################
        }


        persistent.poligon_videoplayers = {
            # Видеоплееры первой главы
                "introduction": {
                    "file": "poligon_videoplayer_cassette_introduction",
                    "video": "poligon/source/videos/UVAO_anim.webm",
                    "unlocked": False
                },
                "cave": {
                    "file": "poligon_videoplayer_cassette_cave",
                    "video": "poligon/source/videos/cave.webm",
                    "unlocked": False
                },
                "UVAO": {
                    "file": "poligon_videoplayer_cassette_uvao",
                    "video": "poligon/source/videos/ep2.webm",
                    "unlocked": False
                }
            #############################
            }

        persistent.poligon_first_start = True


    poligon_about_chapters = {
        "UVAO": {
            "text":"Погрузитесь в больное прошлое девочки, чья судьба была предрешена с самого детства, но вот - надежда, за которой следует плата. Узнайте, какой ценой даются научные “открытия”, и что остается, когда эксперимент окончен.",
            "image":"poligon_select_chapters_uvao_in_select"
        }
    }

    show_image = None
    select_chapter = None
    button_SH = True
    pause_click = False
    video = None
    videoplayer_page = None
    semen_chapter_2_new = None
