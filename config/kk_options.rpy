default persistent.kk_interface = True
default persistent.kk_font_size = 36
default kk_installed = True


style kk_name_text:
    font kk_fonts + "Oswald.ttf"
    size 56
    color "ffffff"

style kk_choice_button:
    size 45
    color "ffffff"
    hover_color "#FF69B4"
    font kk_fonts + "Oswald.ttf"  

style kk_int_text:
    size 30
    color "ffffff"
    font kk_fonts + "Oswald.ttf"      

style kk_int_button:
    size 36
    color "#ffffff"
    hover_color "FF69B4"
    font kk_fonts + "Oswald.ttf" 

style kk_mm_textbutton:
    size 40
    color "#fff"
    hover_color "#FF69B4"
    selected_idle_color "#FF69B4"
    selected_hover_color "#ffb4da"
    drop_shadow [ (1, 1), (2, 1) ] 
    drop_shadow_color "000"
    font kk_inter_thin_font

style kk_mm_extra_textbutton:
    size 40
    color "#FF69B4"
    hover_color "#ffb4da"
    font kk_inter_thin_font


init python:

    mods["kk"] = u"Interface Settings"


label kk:

    call screen kk_interface_settings with dissolve


init python:

    from renpy.store import store

    kk_version = "1.0"

    def kk_screens():
        renpy.display.screen.screens[("say", None)] = renpy.display.screen.screens[("kk_say", None)]
        renpy.display.screen.screens[("quick_menu", None)] = renpy.display.screen.screens[("kk_quick_menu", None)]
        renpy.display.screen.screens[("choice", None)] = renpy.display.screen.screens[("kk_choice", None)]
        renpy.display.screen.screens[("nvl", None)] = renpy.display.screen.screens[("kk_nvl", None)]
        renpy.display.screen.screens[("main_menu", None)] = renpy.display.screen.screens[("kk_main_menu", None)]
        renpy.display.screen.screens[("game_menu", None)] = renpy.display.screen.screens[("kk_ingame_menu", None)]
        renpy.display.screen.screens[("notify", None)] = renpy.display.screen.screens[("kk_notify", None)]
        renpy.display.screen.screens[("file_slots", None)] = renpy.display.screen.screens[("kk_file_slots", None)]
        

    def kk_d_screens():
        renpy.display.screen.screens[("kk_say", None)] = renpy.display.screen.screens[("say", None)]
        renpy.display.screen.screens[("kk_quick_menu", None)] = renpy.display.screen.screens[("quick_menu", None)]
        renpy.display.screen.screens[("kk_choice", None)] = renpy.display.screen.screens[("choice", None)]
        renpy.display.screen.screens[("kk_nvl", None)] = renpy.display.screen.screens[("nvl", None)]
        renpy.display.screen.screens[("kk_main_menu", None)] = renpy.display.screen.screens[("main_menu", None)]
        renpy.display.screen.screens[("kk_ingame_menu", None)] = renpy.display.screen.screens[("game_menu", None)]
        renpy.display.screen.screens[("kk_notify", None)] = renpy.display.screen.screens[("notify", None)]
        renpy.display.screen.screens[("kk_file_slots", None)] = renpy.display.screen.screens[("file_slots", None)]

    if persistent.kk_interface == True:
        kk_screens()
    else:
        kk_d_screens()

    std_set_for_preview = {}
    std_set = {}
    store.colors = {}
    store.names = {}
    store.names_list = []

    _show_two_window = True
    store.names_list.append('narrator')
    store.names_list.append('th')

    # Переключение вырезано из Бесконечного лета
    def char_define(x,is_nvl=False):
        global DynamicCharacter
        global _show_two_window
        global nvl
        global store
        gl = globals()
        v = "_voice"
        if  x == 'narrator':
            if  is_nvl:
                gl["narrator"] = Character(None, kind=nvl)
            else:
                gl["narrator"] = Character(None)
            return
        if  x == 'th':
            if  is_nvl:
                gl["th"] = Character(None, kind=nvl,what_prefix = "~ ",what_suffix=" ~")
            else:
                gl["th"] = Character(None, what_prefix = "~ ",what_suffix=" ~")
            return
        if  is_nvl:
            gl["x"] = DynamicCharacter("%s_name"%x, color=store.colors[x], kind=nvl, what_style="ffffff",who_suffix=":")
            gl["%s_name"%x] = store.names[x]
        else:
            gl[x] = DynamicCharacter("%s_name"%x, color=store.colors[x], show_two_window=_show_two_window,  what_style="ffffff")
            gl["%s_name"%x] = store.names[x]

    def set_mode_adv():
        nvl_clear()
        
        global menu
        global narrator
        menu = renpy.display_menu
        narrator = Character(None)
        global store
        for x in store.names_list:
            char_define(x)

    def set_mode_nvl():
        nvl_clear()
        
        global menu
        menu = nvl_menu
        
        global narrator
        global th
        narrator = nvl_narrator
        th_nvl = th
        
        global store
        for x in store.names_list:
            char_define(x,True)

    def reload_names(is_nvl=False):
        global store
        for x in store.names_list:
            char_define(x, is_nvl)

    set_mode_adv()
    reload_names()


## Helper functions
python early:
    import re, random

    def kk_get_files_in(dir=""):
        file_list = renpy.list_files() # Новая фича, поэтому не подсвечивается
        files = []
        for f in file_list:
            if re.match(dir,f):
                files.append(f[(len(dir)):].lstrip('/'))
        return files


init:

    transform kk_imagebutton:

        subpixel True

        on idle:
            ease .21 alpha 1 #matrixcolor TintMatrix("#fff")
            repeat
        on hover:
            ease .21 alpha 0.5 #matrixcolor TintMatrix("#FF69B4")
            repeat