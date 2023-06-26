
# Short paths
init -1000 python:

    kk_all = "2648251323/kk/files/"
    kk_fonts = kk_all + "fonts/"
    kk_gui = "2648251323/kk/gui/"
    kk_other = kk_all + "other/"

    kk_inter_thin_font = kk_fonts + "InterTight-Light.ttf"
    kk_inter_light_font = kk_fonts + "InterTight-Light.ttf"


# Interface
init: 

    
    image kk_db = kk_gui + "GM/dialogue_box.png"
    image kk_game_menu = kk_gui + "GM/game_menu.png"
    image kk_nvl_box = kk_gui + "GM/nvl_box.png"

    image kk_int_hide = kk_gui + "GM/hide.png"
    image kk_int_menu = kk_gui + "GM/menu.png"
    image kk_int_history = kk_gui + "GM/history.png"
    image kk_small_shit = kk_gui + "GM/small_shit.png"

    image kk_choice_button = kk_gui + "GM/choice_button.png"

    image kk_notify_box = kk_gui + "GM/notify.png"


# History box

    image kk_who_box = kk_all + "gui/who_box.png"
    image kk_history_box = kk_all + "gui/history_box.png"


# Other

    image kk_bg = im.Blur(kk_other + "bg.jpg", 1.5)

    image kk_info_box = kk_all + "gui/info_box.png"
    image white = "#fff" 
    image kk_on = kk_all + "gui/on.png"


# Контейнеры для музыки, фонов и так далее
## Так как разраб разбил все по папкам, но затем начал скидывать в них все подряд, буду вручную делать
## мне легче все из контейнера доставать, чем прописыпать каждый в экране

    python:

        bg_list = ["images/bg/corridor.png", "images/bg/kitchen.png", "images/bg/rooma.png", "images/bg/roomc.png"]

        cg_list = []
        for cgf in kk_get_files_in("images/cg"):
            cg_list.append("images/cg/" + cgf)

        try:
            if music_list:
                pass
        except:
            music_list = dict()

        for mus in kk_get_files_in("music"):
            music_list[mus.rsplit('.', 1)[0]] = "music/" + mus
