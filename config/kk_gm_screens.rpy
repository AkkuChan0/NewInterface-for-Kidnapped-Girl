screen kk_ingame_menu(title=None, scroll=None, yinitial=0.0):

    zorder 1

    add "kk_game_menu" ypos 159

    vbox:
        area(12, 298, 220, 388)
        textbutton _("Скрыть"):
            style "button" text_style "kk_mm_textbutton" text_size 30 xcenter 0.5
            action [Return(), With(dissolve)]
        textbutton _("Сохранить"):
            style "button" text_style "kk_mm_textbutton" text_size 30 xcenter 0.5
            action [ShowMenu("kk_game_save"), With(dissolve)]
        textbutton _("Загрузить"):
            style "button" text_style "kk_mm_textbutton" text_size 30 xcenter 0.5
            action [ShowMenu("kk_game_load"), With(dissolve)]
        textbutton _("Настройки"):
            style "button" text_style "kk_mm_textbutton" text_size 30 xcenter 0.5
            action [ShowMenu("kk_game_preferences"), With(dissolve)]
        textbutton _("Главное меню"):
            style "button" text_style "kk_mm_textbutton" text_size 29 xcenter 0.5
            action MainMenu()
        textbutton _("Выйти из игры"):
            style "button" text_style "kk_mm_textbutton" text_size 28 xcenter 0.5
            action Quit(confirm=True)

    key "mouseup_3" action [Return(), With(dissolve)]
    key "K_ESCAPE" action [Return(), With(dissolve)]


screen kk_game_preferences:

    tag menu

    use kk_ingame_menu

    add "kk_nvl_box" xcenter 0.5 ypos 87
    text _("НАСТРОЙКИ") size 60 xpos 325 ypos 134 color "#fff" font kk_inter_thin_font drop_shadow [ (1, 1), (2, 1) ] drop_shadow_color "000"


    text _("Режим экрана") xpos 539-86 ypos 230+36 color "#fff" font kk_inter_thin_font size 36 drop_shadow [ (1, 1), (2, 1) ] drop_shadow_color "000"
    textbutton _("Оконный"):
        style "radio_button" text_style "kk_mm_textbutton" text_size 32 text_drop_shadow [ (1, 1), (2, 1) ] text_drop_shadow_color "000"
        xpos 556-86 ypos 286+36
        action Preference("display", "window")
    textbutton _("Полный"):
        style "radio_button" text_style "kk_mm_textbutton" text_size 32 text_drop_shadow [ (1, 1), (2, 1) ] text_drop_shadow_color "000"
        xpos 556-86 ypos 333+36
        action Preference("display", "fullscreen")

    text _("Пропуск") xpos 909-86 ypos 230+36 color "#fff" font kk_inter_thin_font size 36 drop_shadow [ (1, 1), (2, 1) ] drop_shadow_color "000"
    textbutton _("Всего текста"):
        style "radio_button" text_style "kk_mm_textbutton" text_size 32 text_drop_shadow [ (1, 1), (2, 1) ] text_drop_shadow_color "000"
        xpos 928-86 ypos 286+36
        action Preference("skip", "all")
    textbutton _("Прочитанного"):
        style "radio_button" text_style "kk_mm_textbutton" text_size 32 text_drop_shadow [ (1, 1), (2, 1) ] text_drop_shadow_color "000"
        xpos 928-86 ypos 333+36
        action Preference("skip", "seen")


    text _("Скорость текста") xpos 539-86 ypos 450+36 color "#fff" font kk_inter_thin_font size 36 drop_shadow [ (1, 1), (2, 1) ] drop_shadow_color "000"
    bar value Preference("text speed") xpos 539-86 ypos 505+36 xmaximum 500

    text _("Скорость авточтения") xpos 539-86 ypos 577+36 color "#fff" font kk_inter_thin_font size 36 drop_shadow [ (1, 1), (2, 1) ] drop_shadow_color "000"
    bar value Preference("auto-forward time") xpos 539-86 ypos 632+36 xmaximum 500

    text _("Громкость музыки") xpos 1213-150 ypos 450+36 color "#fff" font kk_inter_thin_font size 36 drop_shadow [ (1, 1), (2, 1) ] drop_shadow_color "000"
    bar value Preference("music volume") xpos 1213-150 ypos 505+36 xmaximum 500

    text _("Громкость звуков") xpos 1213-150 ypos 577+36 color "#fff" font kk_inter_thin_font size 36 drop_shadow [ (1, 1), (2, 1) ] drop_shadow_color "000"
    bar value Preference("sound volume") xpos 1213-150 ypos 632+36 xmaximum 500

    text _("Громкость озвучки") xpos 1213-150 ypos 704+36 color "#fff" font kk_inter_thin_font size 36 drop_shadow [ (1, 1), (2, 1) ] drop_shadow_color "000"
    bar value Preference("voice volume") xpos 1213-150 ypos 759+36 xmaximum 500


    textbutton _("Настройки New Interface").upper():
        style "button" text_style "kk_mm_textbutton" text_size 30 text_drop_shadow [ (1, 1), (2, 1) ] text_drop_shadow_color "000"
        xpos 539-86 ypos 907+36
        action [Hide("menu"), ShowMenu("kk_interface_settings"), With(dissolve)]

    textbutton "Language".upper():
        style "button" text_style "kk_mm_textbutton" text_size 30 text_drop_shadow [ (1, 1), (2, 1) ] text_drop_shadow_color "000"
        xpos 1213-150 ypos 907+36
        action [ShowMenu("kk_language_game"), With(dissolve)]


screen kk_language_game():

    tag menu

    use kk_ingame_menu

    add "kk_nvl_box" xcenter 0.5 ypos 87
    text "LANGUAGE" size 60 xpos 325 ypos 134 color "#fff" font kk_inter_thin_font drop_shadow [ (1, 1), (2, 1) ] drop_shadow_color "000"

    vbox:
        xpos 420 ypos 228
        spacing 15
        textbutton _("English") style "button" text_style "kk_mm_textbutton" text_size 36 action SetVariable("kk_lang", "english"), Show("smooth_language", transition=dissolve2)
        textbutton _("Русский") style "button" text_style "kk_mm_textbutton" text_size 36 action SetVariable("kk_lang", None), Show("smooth_language", transition=dissolve2)
        textbutton _("Chinese") style "button" text_style "kk_mm_textbutton" text_size 36 action SetVariable("kk_lang", "chinese"), Show("smooth_language", transition=dissolve2)
        textbutton _("Thai") style "button" text_style "kk_mm_textbutton" text_size 36 action SetVariable("kk_lang", "thai"), Show("smooth_language", transition=dissolve2)
        textbutton _("Polish") style "button" text_style "kk_mm_textbutton" text_size 36 action SetVariable("kk_lang", "polish"), Show("smooth_language", transition=dissolve2)
        textbutton _("German") style "button" text_style "kk_mm_textbutton" text_size 36 action SetVariable("kk_lang", "german"), Show("smooth_language", transition=dissolve2)



screen kk_game_save():

    tag menu

    use kk_ingame_menu

    add "kk_nvl_box" xcenter 0.5 ypos 87
    text _("СОХРАНИТЬ") size 60 xpos 325 ypos 134 color "#fff" font kk_inter_thin_font drop_shadow [ (1, 1), (2, 1) ] drop_shadow_color "000"
    
    use kk_game_file_slots(_("Сохранить"))


screen kk_game_load():

    tag menu

    use kk_ingame_menu

    add "kk_nvl_box" xcenter 0.5 ypos 87
    text _("ЗАГРУЗИТЬ") size 60 xpos 325 ypos 134 color "#fff" font kk_inter_thin_font drop_shadow [ (1, 1), (2, 1) ] drop_shadow_color "000"
    
    use kk_game_file_slots(_("Загрузить"))


screen kk_game_file_slots(title):


    default page_name_value = FilePageNameInputValue(pattern=_("{} страница"), auto=_("Автосохранения"), quick=_("Быстрые сохранения"))

    fixed:

        ## Это гарантирует, что ввод будет принимать enter перед остальными
        ## кнопками.
        order_reverse True

        ## Номер страницы, который может быть изменён посредством клика на
        ## кнопку.
        button:
            style "page_label"

            key_events True
            xcenter 0.5 ycenter 0.26
            action page_name_value.Toggle()

            input:
                style "page_label_text" font kk_inter_thin_font
                value page_name_value

        ## Таблица слотов.
        grid gui.file_slot_cols gui.file_slot_rows:
            style_prefix "slot"

            xcenter 0.5 ycenter 0.59

            spacing gui.slot_spacing

            for i in range(gui.file_slot_cols * gui.file_slot_rows):

                $ slot = i + 1

                button:

                    vbox:

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %d %B %Y, %H:%M"), empty=_("Пустой слот")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                    key "save_delete" action FileDelete(slot)

                    if title == "Сохранить":
                        action FileSave(slot)
                    else:
                        action FileLoad(slot)

        ## Кнопки для доступа к другим страницам.
        hbox:
            style_prefix "page"

            xcenter 0.5 ycenter 0.9

            spacing gui.page_spacing

            textbutton _("<")  text_idle_color "#fff" text_font kk_inter_thin_font action FilePagePrevious()

            if config.has_autosave:
                textbutton _("{#auto_page}А") text_idle_color "#fff" text_hover_color "#FF69B4" text_font kk_inter_thin_font action FilePage("auto")

            if config.has_quicksave:
                textbutton _("{#quick_page}Б") text_idle_color "#fff" text_hover_color "#FF69B4"  text_font kk_inter_thin_font action FilePage("quick")

            ## range(1, 10) задаёт диапазон значений от 1 до 9.
            for page in range(1, 10):
                textbutton str(page) text_font kk_inter_thin_font text_idle_color "#fff" text_hover_color "#FF69B4"  action FilePage(page)

            textbutton _(">") text_idle_color "#fff" text_hover_color "#FF69B4"  text_font kk_inter_thin_font action FilePageNext()






screen kk_quick_menu:

    tag kk_qm


screen kk_say:

    add "kk_small_shit" xpos 283 ypos 842
    add "kk_db" xcenter 0.5 ypos 842

    if who:
        text who id "who" xpos 387 ypos 880 color "#add19a" font kk_inter_thin_font drop_shadow [ (1, 1), (2, 1) ] drop_shadow_color "000" size 38
    text what id "what" xpos 471 ypos 925 color "#fff" font kk_inter_light_font drop_shadow [ (1, 1), (2, 1) ] drop_shadow_color "000" size 30 xmaximum 962

    imagebutton:
        idle "kk_int_history"
        hover "kk_int_history" at kk_imagebutton
        xpos 302 ypos 884
        action [ShowMenu("kk_history"), With(dissolve)]

    imagebutton:
        idle "kk_int_hide"
        hover "kk_int_hide" at kk_imagebutton
        xpos 304 ypos 949
        action [HideInterface(), With(dissolve)]

    imagebutton:
        idle "kk_int_menu"
        hover "kk_int_menu" at kk_imagebutton
        xpos 302 ypos 1018
        action ShowMenu("kk_game_preferences", transition=dissolve)  

    vbox:
        area (1045, 867, 552, 22)
        text kk_get_nowmusic().upper() color "#fff" font kk_inter_thin_font size 24 drop_shadow [ (1, 1), (2, 1) ] drop_shadow_color "000" xcenter 0.5

    key "mouseup_3" action ShowMenu("kk_game_preferences", transition=dissolve)
    key "K_ESCAPE" action ShowMenu("kk_game_preferences", transition=dissolve)


screen kk_nvl:

    add "kk_nvl_box" xcenter 0.5 ypos 87
    vbox:
        xpos -290 ypos 159
        spacing 55
        for who, what, who_id, what_id, window_id in dialogue:
            if who:
                text who id who_id color "#add19a" font kk_inter_thin_font size 34 
            text what id what_id color "#fff" font kk_inter_thin_font drop_shadow [ (1, 1), (2, 1) ] drop_shadow_color "000" size 30 xmaximum 1160

        if items:
            vbox:
                id "menu"
                for caption, action, chosen in items:
                    if action:
                        button:
                            style "nvl_menu_choice_button"
                            action action
                            text caption style "nvl_menu_choice"
                    else:
                        text caption style "nvl_dialogue"

    key "mouseup_3" action ShowMenu("kk_game_preferences", transition=dissolve)
    key "K_ESCAPE" action ShowMenu("kk_game_preferences", transition=dissolve)


screen kk_history():

    predict False
    add "kk_nvl_box" xcenter 0.5 ypos 87
    text _("ИСТОРИЯ") size 60 xpos 325 ypos 134 color "#fff" font kk_inter_thin_font drop_shadow [ (1, 1), (2, 1) ] drop_shadow_color "000"

    viewport id "history_scroll":
        mousewheel True
        area(390, 228, 1100, 772)
        yinitial 1.0
        vbox:
            style_prefix "kk_history_text"
            spacing 2
            for h in _history_list:
                if h.who:
                    text h.who xalign -0.2 style "kk_history_text" color "#add19a" drop_shadow [ (1, 1), (2, 1) ] drop_shadow_color "000" 
                    textbutton h.what style "button" text_style "kk_mm_textbutton" text_size 30 action RollbackToIdentifier(h.rollback_identifier)
                else:
                    textbutton h.what style "button" text_style "kk_mm_textbutton" text_size 30 action RollbackToIdentifier(h.rollback_identifier)

    if not _history_list:
        hbox:
            area(427, 228, 1066, 772)
            text "История диалогов пуста." style "kk_history_text" xcenter 0.5 ycenter 0.5
    vbar value YScrollValue(viewport="history_scroll") xpos 1540 ypos 159 ymaximum 846


screen kk_choice(items):
    #style_prefix "choice"

    vbox:
        ycenter 0.4
        spacing 20
        for i in items:
            add "kk_choice_button" ypos 1.2 xalign 0.0
            textbutton i.caption style "button" text_style "kk_mm_textbutton" text_size 30 xpos 0.05 action i.action


screen kk_notify(message, _time=4):

    zorder 100
    style_prefix "kk_notify"

    frame at kk_notify_appear:
        text "[message!tq]" color "#fff" font kk_inter_thin_font size 32 xmaximum 800

    timer _time action Hide('kk_notify')


transform kk_notify_appear:
    on show:
        alpha 0 xpos -0.08
        ease .3 alpha 1.0 xpos 0.0
    on hide:
        ease .5 alpha 0.0 xpos -0.2


style kk_notify_frame is empty
style kk_notify_text is gui_text

style kk_notify_frame:
    ypos gui.notify_ypos

    background Frame("kk_notify_box", Borders(40, 15, 130, 15), tile=False)
    padding gui.notify_frame_borders.padding

style kk_notify_text:
    properties gui.text_properties("notify")