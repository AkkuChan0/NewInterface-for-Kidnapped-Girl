screen kk_interface_settings:

    tag menu 

    add "kk_bg"
    add "kk_history_box" xpos 26 ypos 26

    text "Interface settings" style "kk_name_text" xpos 327 ypos 40

    text "Интерфейс:" style "kk_int_text" xpos 106 ypos 216

    textbutton "Включить":
        style "button" text_style "kk_int_button"
        xpos 287 ypos 189 
        action [SetVariable("persistent.kk_interface", True), Show("kk_interface_settings"), Function(kk_screens), With(dissolve)]

    textbutton "Выключить":
        style "button" text_style "kk_int_button" 
        xpos 287 ypos 245 
        action [SetVariable("persistent.kk_interface", False), Show("kk_interface_settings"), Function(kk_d_screens), With(dissolve)]

    text "Потребуется перезапуск игры" style "kk_int_text" xpos 522 ypos 216

    if persistent.kk_interface == True:
        add "kk_on" xpos 292 ypos 243
    elif persistent.kk_interface == False:
        add "kk_on" xpos 292 ypos 300

    add "kk_who_box" xpos 70 ypos 320

    textbutton "Информация о разработке":
        style "button" text_style "kk_int_button" 
        xpos 106 ypos 355 
        text_selected_idle_color "#FF69B4" text_selected_hover_color "#ffffff"
        action [ToggleScreen("kk_information"), With(dissolve)]

    # text "Настройки интерфейса:" style "kk_int_text" xpos 106 ypos 470
    # text "Размер шрифта:" style "kk_int_text" size 30 xpos 140 ypos 530

    textbutton "Выход" style "button" text_style "kk_choice_button" xpos 451 ypos 965 action [Hide("menu"), Return(), With(dissolve)]


screen kk_information:

    tag kk_info_tag

    add "kk_info_box" xpos 1011 ypos 26

    text "Информация" style "kk_name_text" xpos 1318 ypos 40

    vbox:
        
        area(1061, 160, 768, 708)

        text "Данный мод находится на этапе разработки. Множество функций на данный момент ещё не доступны.\n" style "kk_int_text"
        text "Готово на текущий момент:" style "kk_int_text"
        text "  - ADV интерфейс" style "kk_int_text"
        text "  - Экран истории с возможностью вернуться к определённой строчке" style "kk_int_text"
        text "  - Меню выборов" style "kk_int_text"
        text "  - NVL интерфейс" style "kk_int_text"
        text "  - Новое главное и игровое меню\n" style "kk_int_text"
        text "В планах:" style "kk_int_text"
        text "  - Доделать мелочи" style "kk_int_text"
        text "  - Изменить это окно (мне впадлу, если честно)" style "kk_int_text"
        text "  - Выход за рамки мода с простой заменой интерфейса\n" style "kk_int_text"
        text "Текущая версия: " + kk_version + "\n" style "kk_int_text"
        text "  Mod by AkkuChan" style "kk_int_text"


# Main Menu
screen kk_main_menu():

    add gui.main_menu_background
    add "gui/overlay/main_menu.png"
    text "NEW INTERFACE" xpos 15 ypos 15 color "#fff" font kk_inter_thin_font size 24
    text "BY AKKUCHAN" xpos 15 ypos 40 color "#fff" font kk_inter_thin_font size 24

    use kk_navigator


default _kk_start_var = None

screen kk_navigator():

    tag navigator

    textbutton _("Новая игра").upper():
        style "button" text_style "kk_mm_textbutton"
        xpos 46 ypos 369
        action [Start("_kk_start_label"), With(dissolve)]

    textbutton _("Загрузить").upper():
        style "button" text_style "kk_mm_textbutton"
        xpos 46 ypos 454
        action [ToggleScreen("kk_load_menu"), With(dissolve)]

    textbutton _("Настройки").upper():
        style "button" text_style "kk_mm_textbutton"
        xpos 46 ypos 539
        action [ToggleScreen("kk_preferences"), With(dissolve)]

    textbutton _("Экстра").upper():
        style "button" text_style "kk_mm_textbutton"
        xpos 46 ypos 633
        action [ToggleScreen("kk_bg_extra"), With(dissolve)]

    textbutton _("Выход").upper():
        style "button" text_style "kk_mm_textbutton"
        xpos 46 ypos 901
        action Quit(confirm=True)


label _kk_start_label:

    stop music fadeout 2.0
    stop sound fadeout 2.0
    window hide
    scene black
    with dissolve

    if _kk_start_var:
        $ _temp = _kk_start_var
        $ _kk_start_var = None
        $ renpy.jump(_temp)

    jump start

screen kk_load_menu():

    tag menu

    add "gui/game_menu.png"
    add "gui/overlay/game_menu.png"
    text _("ЗАГРУЗИТЬ") xpos 160 ypos 50 color "#fff" font kk_inter_thin_font size 60
    use kk_navigator
    
    use kk_file_slots(_("Загрузить"))


screen kk_file_slots(title):



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
            xcenter 0.61 ycenter 0.13
            action page_name_value.Toggle()

            input:
                style "page_label_text" font kk_inter_thin_font
                value page_name_value

        ## Таблица слотов.
        grid gui.file_slot_cols gui.file_slot_rows:
            style_prefix "slot"

            xpos 539 ycenter 0.5

            spacing gui.slot_spacing

            for i in range(gui.file_slot_cols * gui.file_slot_rows):

                $ slot = i + 1

                button:
                    action FileAction(slot)

                    has vbox

                    add FileScreenshot(slot) xalign 0.5

                    text FileTime(slot, format=_("{#file_time}%A, %d %B %Y, %H:%M"), empty=_("Пустой слот")):
                        style "slot_time_text"

                    text FileSaveName(slot):
                        style "slot_name_text"

                    key "save_delete" action FileDelete(slot)

        ## Кнопки для доступа к другим страницам.
        hbox:
            style_prefix "page"

            xcenter 0.6125 ycenter 0.85

            spacing gui.page_spacing

            textbutton _("<") action FilePagePrevious()

            if config.has_autosave:
                textbutton _("{#auto_page}А") action FilePage("auto")

            if config.has_quicksave:
                textbutton _("{#quick_page}Б") action FilePage("quick")

            ## range(1, 10) задаёт диапазон значений от 1 до 9.
            for page in range(1, 10):
                textbutton str(page) text_font kk_inter_thin_font action FilePage(page)

            textbutton _(">") action FilePageNext()


screen kk_preferences():

    tag menu

    add "gui/game_menu.png"
    add "gui/overlay/game_menu.png"
    use kk_navigator

    text _("НАСТРОЙКИ") xpos 160 ypos 50 color "#fff" font kk_inter_thin_font size 60

    text _("Режим экрана") xpos 539 ypos 230 color "#fff" font kk_inter_thin_font size 36
    textbutton _("Оконный"):
        style "radio_button" text_style "kk_mm_textbutton" text_size 32
        xpos 556 ypos 286 
        action Preference("display", "window")
    textbutton _("Полный"):
        style "radio_button" text_style "kk_mm_textbutton" text_size 32
        xpos 556 ypos 333 
        action Preference("display", "fullscreen")

    text _("Пропуск") xpos 909 ypos 230 color "#fff" font kk_inter_thin_font size 36
    textbutton _("Всего текста"):
        style "radio_button" text_style "kk_mm_textbutton" text_size 32
        xpos 928 ypos 286 
        action Preference("skip", "all")
    textbutton _("Прочитанного"):
        style "radio_button" text_style "kk_mm_textbutton" text_size 32
        xpos 928 ypos 333 
        action Preference("skip", "seen")


    text _("Скорость текста") xpos 539 ypos 450 color "#fff" font kk_inter_thin_font size 36
    bar value Preference("text speed") xpos 539 ypos 505 xmaximum 500

    text _("Скорость авточтения") xpos 539 ypos 577 color "#fff" font kk_inter_thin_font size 36
    bar value Preference("auto-forward time") xpos 539 ypos 632 xmaximum 500

    text _("Громкость музыки") xpos 1213 ypos 450 color "#fff" font kk_inter_thin_font size 36
    bar value Preference("music volume") xpos 1213 ypos 505 xmaximum 500

    text _("Громкость звуков") xpos 1213 ypos 577 color "#fff" font kk_inter_thin_font size 36
    bar value Preference("sound volume") xpos 1213 ypos 632 xmaximum 500

    text _("Громкость озвучки") xpos 1213 ypos 704 color "#fff" font kk_inter_thin_font size 36
    bar value Preference("voice volume") xpos 1213 ypos 759 xmaximum 500


    textbutton _("Настройки New Interface").upper():
        style "button" text_style "kk_mm_textbutton" text_size 30
        xpos 539 ypos 907
        action [ShowMenu("kk_interface_settings"), With(dissolve)]

    textbutton "Language".upper():
        style "button" text_style "kk_mm_textbutton" text_size 30
        xpos 1213 ypos 907
        action [ShowMenu("kk_language_menu"), With(dissolve)]


define kk_lang = None


screen kk_language_menu():

    tag menu

    add "gui/game_menu.png"
    add "gui/overlay/game_menu.png"
    use kk_navigator

    textbutton _("Настройки").upper():
        style "button" text_style "kk_mm_extra_textbutton"
        xpos 46 ypos 539
        action Hide("menu", transition=dissolve)

    vbox:
        xpos 542 ypos 282
        spacing 10
        textbutton _("English") style "button" text_idle_color "#fff" text_hover_color "#FF69B4" text_font kk_inter_thin_font text_size 36 action SetVariable("kk_lang", "english"), Show("smooth_language", transition=dissolve2)
        textbutton _("Русский") style "button" text_idle_color "#fff" text_hover_color "#FF69B4" text_font kk_inter_thin_font text_size 36 action SetVariable("kk_lang", None), Show("smooth_language", transition=dissolve2)
        textbutton _("Chinese") style "button" text_idle_color "#fff" text_hover_color "#FF69B4" text_font kk_inter_thin_font text_size 36 action SetVariable("kk_lang", "chinese"), Show("smooth_language", transition=dissolve2)
        textbutton _("Thai") style "button" text_idle_color "#fff" text_hover_color "#FF69B4" text_font kk_inter_thin_font text_size 36 action SetVariable("kk_lang", "thai"), Show("smooth_language", transition=dissolve2)
        textbutton _("Polish") style "button" text_idle_color "#fff" text_hover_color "#FF69B4" text_font kk_inter_thin_font text_size 36 action SetVariable("kk_lang", "polish"), Show("smooth_language", transition=dissolve2)
        textbutton _("German") style "button" text_idle_color "#fff" text_hover_color "#FF69B4" text_font kk_inter_thin_font text_size 36 action SetVariable("kk_lang", "german"), Show("smooth_language", transition=dissolve2)


screen smooth_language():

    add "black"
    timer 2 action Language(kk_lang), Hide("smooth_language", transition=dissolve2)


screen kk_extra():

    add "gui/game_menu.png"
    add "gui/overlay/game_menu.png"

    text _("Экстра").upper() xpos 307 ypos 50 color "#fff" font kk_inter_thin_font size 60

    use kk_navigator

    textbutton _("Фоны").upper():
        style "button" text_style "kk_mm_textbutton" text_size 42
        xpos 542 ypos 282
        action [ShowMenu("kk_bg_extra"), With(dissolve)]

    textbutton _("Иллюстрации").upper():
        style "button" text_style "kk_mm_textbutton" text_size 42
        xpos 542 ypos 399
        action [ShowMenu("kk_cg_extra"), With(dissolve)]

    textbutton _("Музыка").upper():
        style "button" text_style "kk_mm_textbutton" text_size 42
        xpos 542 ypos 516
        action [ShowMenu("kk_music_extra"), With(dissolve)]

    textbutton _("Модификации").upper():
        style "button" text_style "kk_mm_textbutton" text_size 42
        xpos 542 ypos 633
        action [ShowMenu("kk_mods_extra"), With(dissolve)]

    textbutton _("Ссылки").upper():
        style "button" text_style "kk_mm_textbutton" text_size 42
        xpos 542 ypos 750
        action [ShowMenu("kk_urls_extra"), With(dissolve)]


screen kk_bg_extra():

    tag menu

    use kk_extra

    textbutton _("Экстра").upper():
        style "button" text_style "kk_mm_extra_textbutton"
        xpos 46 ypos 633
        action Hide("menu", transition=dissolve)

    vbox:
        area(1020, 200, 4, 750)
        add "white" 

    viewport id "kk_id_bg_ex":
        area(1080, 200, 740, 750)
        mousewheel True
        vbox:
            spacing 10
            for bg in bg_list:
                add bg zoom 0.37

    vbar value YScrollValue("kk_id_bg_ex") ymaximum 750 xmaximum 2 xpos 1850 ypos 200

    
screen kk_cg_extra():

    tag menu

    use kk_extra

    textbutton _("Экстра").upper():
        style "button" text_style "kk_mm_extra_textbutton"
        xpos 46 ypos 633
        action Hide("menu", transition=dissolve)

    vbox:
        area(1020, 200, 4, 750)
        add "white" 

    viewport id "kk_id_cg_ex":
        area(1080, 200, 740, 750)
        mousewheel True
        vbox:
            spacing 10
            for cg in cg_list:
                add cg zoom 0.37
 
    vbar value YScrollValue("kk_id_cg_ex") ymaximum 750 xmaximum 2 xpos 1850 ypos 200


init python:
    mr = MusicRoom(fadeout=0.3, fadein=0.5)
    for i in music_list:
        mr.add(music_list[i], always_unlocked = True)


screen kk_music_extra():

    tag menu

    use kk_extra

    textbutton _("Экстра").upper():
        style "button" text_style "kk_mm_extra_textbutton"
        xpos 46 ypos 633
        action Hide("menu", transition=dissolve)

    vbox:
        area(1020, 200, 4, 750)
        add "white" 

    viewport id "kk_id_music_ex":
        area(1080, 200, 740, 750)
        mousewheel True
        vbox:
            spacing 10
            for n in music_list:
                button:
                    idle_child     Text ("▷ " + n.replace("_", " "), color="#aaa", font=kk_inter_thin_font, size=26)
                    hover_child    Text ("▶ " + n.replace("_", " "), color="#ccc", font=kk_inter_thin_font, size=26)
                    selected_child Text ("▶▶ " + n.replace("_", " "), color="#ccc", font=kk_inter_thin_font, size=26)
                    action mr.Play(music_list[n])

    vbar value YScrollValue("kk_id_music_ex") ymaximum 750 xmaximum 2 xpos 1850 ypos 200


screen kk_mods_extra():

    tag menu

    use kk_extra

    textbutton _("Экстра").upper():
        style "button" text_style "kk_mm_extra_textbutton"
        xpos 46 ypos 633
        action Hide("menu", transition=dissolve)

    vbox:
        area(1020, 200, 4, 750)
        add "white" 

    viewport id "kk_id_mods":
        mousewheel True
        area(1080, 200, 740, 750)
        vbox:
            spacing 15
            for mod in mods:
                textbutton mods[mod]:
                    style "button" text_style "kk_mm_textbutton" text_size 30
                    action SetVariable("_kk_start_var", mod), [Start("_kk_start_label"), With(dissolve)]


screen kk_urls_extra():

    tag menu

    use kk_extra

    textbutton _("Экстра").upper():
        style "button" text_style "kk_mm_extra_textbutton"
        xpos 46 ypos 633
        action Hide("menu", transition=dissolve)

    vbox:
        area(1020, 200, 4, 750)
        add "white" 

    vbox:
        xpos 1080 ypos 200
        spacing 15
        textbutton "Twitter":
            style "button" text_font kk_inter_thin_font
            action OpenURL("https://twitter.com/TroyHolmant/")
        textbutton "VK":
            style "button" text_font kk_inter_thin_font
            action OpenURL("https://vk.com/troyholman")
        textbutton "New Interface in Steam":
            style "button" text_font kk_inter_thin_font
            action OpenURL("https://steamcommunity.com/sharedfiles/filedetails/?id=2648251323")
