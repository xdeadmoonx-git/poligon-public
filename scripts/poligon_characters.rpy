init python:

    def poligon_reg_char(id, name, who_color, what_color="#fff", pref="", suf="", kind_mode="adv"):
        gl = globals()

        if kind_mode == "nvl":
            char_kind = nvl
        else:
            char_kind = adv

        gl[id] = Character(name, 
        color=who_color, what_color=what_color, 
        drop_shadow=[(2, 2)], drop_shadow_color="#000", what_drop_shadow=[(2, 2)], what_drop_shadow_color="#000",
        what_prefix=pref, what_suffix=suf,
        screen="poligon_say",
        kind=char_kind,
        ctc=None, ctc_position="fixed"
        )

    poligon_characters = [
        # Персонажи первой главы
        ("ptho", None, "#FFFFFF", "#ffffff", "«", "»"),
        ("semen", "Семен", "#E1DD7D"),
        ("uvao", "Юля", "#e56102"),
        ("vilka", "Виола", "#a5a5ff"),
        ("maxon", "Максим", "#a5a5ff"),
        ("vodila", "Водитель", "#8b4513"),
        ("noname", "???", "#fff"),
        ("povar", "Повариха", "#c9ba2e"),
        ("olga", "Ольга Дмитриевна", "#00ea32"),
        ("pedagog","Воспитатель","#fcab72"),
        ("marina","Марина В.","#fcab72"),
        ("doctor_1","Старый врач","#cffafa"),
        ("doctor_2","Доктор","#7afafa"),
        ("doсtor_3","Доктор","#7afafa"),
        ("prodavez","Продавщица","#a0d9fa"),
        ("golos","Голос","#f00"),
        ("Medsis","Медсетра","#f1f7ad"),
        ("jenshina","Женщина","#a5a5ff"),
        ("radio","Радио","#995a2c"),
        ("solder","Солдат","#b8b8b8"),
        ("rmaxon", "Максим", "#f00")
        ############
    ]

    def poligon_set_nvl_mode():
        for char in poligon_characters:
            poligon_reg_char(*char, kind_mode="nvl")
        globals()['narrator'] = Character(
            None,
            kind=nvl,
            what_style="narrator_%s" % time_of_day,
            ctc=None,
            ctc_position="fixed"
        )

    def poligon_set_adv_mode():
        for char in poligon_characters:
            poligon_reg_char(*char, kind_mode="adv")
        globals()['narrator'] = Character(
            None,
            kind=adv,
            what_style="narrator_%s" % time_of_day,
            ctc=None,
            ctc_position="fixed"
        )
    


screen poligon_radio_text(message, xx, yy, tsize, cps, style):
    zorder 100
    frame:
        style style 
        align (0.5, 0.8)
        xoffset xx
        yoffset yy
        xmaximum 1550
        text message:
            slow_cps cps
            style style size tsize
