# Персонажи 

define senior_gpt = Character('Senior gpt', image='senior_gpt', color="#065AD0",callback=name_callback, cb_name="senior_gpt")
define main_character = Character('[name_mc]',image="gg", color="#F818FF",callback=name_callback, cb_name="gg")
define mike = Character('Макс',image='mike', color="#A15DF9", callback=name_callback, cb_name="mike")
define scientist = Character('Ученый',image='scientist', color="#0D6CF2", callback=name_callback, cb_name="scientist")
define robot = Character('Нейроникс.v.01',image='robot', color="#20B9F3", callback=name_callback, cb_name="robot")
define kate = Character('Катя',image='kate', color="#A15DF9", callback=name_callback, cb_name="kate")
define mother = Character('Мама',image='mother', color="#B13AEE", callback=name_callback, cb_name="mother")
define anna = Character('Аня',image='anna', color="#E36C1C", callback=name_callback, cb_name="anna")
define roma = Character('Рома',image='roma', color="#E38F1C", callback=name_callback, cb_name="roma")

# Переходы

define slowdissolve = Dissolve(1)
define slowdissolve1 = Fade(2.5)

# Фоновая музыка

define audio.calm = "audio/calm_music.mp3"
define audio.techno = "audio/technology.mp3"
define audio.noise = "audio/noise.mp3"
define audio.distur_2 = "audio/disturbing_music_2.mp3"
define audio.distur_1 = "audio/disturbing_music_1.mp3"

# Звуки игры

define audio.applause = "audio/applause.mp3"
define audio.bell = "audio/bell.mp3"
define audio.breakdown = "audio/breakdown.mp3"
define audio.closure = "audio/closure.mp3"
define audio.door = "audio/door_knock.mp3"
define audio.hit = "audio/hit.mp3"
define audio.keyboard = "audio/keyboard.mp3"
define audio.step = "audio/step.mp3"

# GIF

image virtual_web = Movie(play="virtual_web.mp4", pos=(0,0), anchor=(0, 0))
image laboratory_video = Movie(play="laboratory_video.mp4", pos=(0,0), anchor=(0, 0))

# Дополнительные спрайты(необходимы во время диалогов)

image gg внедоумении1 = At('gg внедоумении', sprite_highlight('gg'))
image gg задумчивая1 = At('gg задумчивая', sprite_highlight('gg'))
image gg испуганная1 = At('gg испуганная', sprite_highlight('gg'))
image gg обычная1 = At('gg обычная', sprite_highlight('gg'))
image gg радостная1 = At('gg радостная', sprite_highlight('gg'))
image gg смущенная1 = At('gg смущенная', sprite_highlight('gg'))
image gg угрюмая1 = At('gg угрюмая', sprite_highlight('gg'))
image gg удивленная1 = At('gg удивленная', sprite_highlight('gg'))

image gg пвнедоумении1 = At('gg пвнедоумении', sprite_highlight('gg'))
image gg пзадумчивая1 = At('gg пзадумчивая', sprite_highlight('gg'))
image gg писпуганная1 = At('gg писпуганная', sprite_highlight('gg'))
image gg побычная1 = At('gg побычная', sprite_highlight('gg'))
image gg прадостная1 = At('gg прадостная', sprite_highlight('gg'))
image gg псмущенная1 = At('gg псмущенная', sprite_highlight('gg'))
image gg пугрюмая1 = At('gg пугрюмая', sprite_highlight('gg'))
image gg пудивленная1 = At('gg пудивленная', sprite_highlight('gg'))

image mike обычный1 = At('mike обычный', sprite_highlight('mike'))
image mike улыбчивый1 = At('mike улыбчивый', sprite_highlight('mike'))
image mike задумчивый1 = At('mike задумчивый', sprite_highlight('mike'))

image senior_gpt обычный1 = At('senior_gpt обычный', sprite_highlight('senior_gpt'))
image senior_gpt ухмылка1 = At('senior_gpt ухмылка', sprite_highlight('senior_gpt'))

image robot обычный1 = At('robot обычный', sprite_highlight('robot'))
image robot ошибка1 = At('robot ошибка', sprite_highlight('robot'))

image kate обычная1 = At('kate обычная', sprite_highlight('kate'))
image kate задумчивая1 = At('kate задумчивая', sprite_highlight('kate'))

image scientist обычный1 = At('scientist обычный', sprite_highlight('scientist'))
image scientist угрюмый1 = At('scientist угрюмый', sprite_highlight('scientist'))

image mother обычная1 = At('mother обычная', sprite_highlight('mother'))
image mother улыбчивая1 = At('mother улыбчивая', sprite_highlight('mother'))
image mother злая1 = At('mother злая', sprite_highlight('mother'))

image anna обычная1 = At('anna обычная', sprite_highlight('anna'))
image anna задумчивая1 = At('anna задумчивая', sprite_highlight('anna'))

image roma обычный1 = At('roma обычный', sprite_highlight('roma'))
image roma угрюмый1 = At('roma угрюмый', sprite_highlight('roma'))



init:
    image lb = SnowBlossom("lbs", count=1, xspeed=(0), yspeed=(0))

image lbs:
    "animated1/web_1.jpeg"
    pause 1
    "animated1/web_2.jpeg"
    pause 1
    "animated1/web_3.jpeg"
    pause 1
    "animated1/web_4.jpeg"
    pause 1
    "animated1/web_5.jpeg"
    pause 1
    "animated1/web_6.jpeg"
    pause 1
    repeat


init:
    image web1 = SnowBlossom("webs", count=1,xspeed=(0), yspeed=(0))

image webs:
    "animated2/v_1.jpeg"
    pause .3
    "animated2/v_2.jpeg"
    pause .3
    "animated2/v_3.jpeg"
    pause .5
    "animated2/v_4.jpeg"
    pause .3
    "animated2/v_5.jpeg"
    pause .3
    "animated2/v_6.jpeg"
    pause .5
    "animated2/v_7.jpeg"
    pause .3
    "animated2/v_8.jpeg"
    pause .3
    "animated2/v_9.jpeg"
    pause .5
    repeat


# init:
#     image main = SnowBlossom("mains", count=1,xspeed=(0), yspeed=(0))

# image mains:
#     "animated3/screensaver_000.jpeg"
#     pause 1.24
#     "animated3/screensaver_014.jpeg"
#     pause .27
#     "animated3/screensaver_017.jpeg"
#     pause .09
#     "animated3/screensaver_018.jpeg"
#     pause .09
#     "animated3/screensaver_019.jpeg"
#     pause .09
#     "animated3/screensaver_020.jpeg"
#     pause .09
#     "animated3/screensaver_021.jpeg"
#     pause .09
#     "animated3/screensaver_022.jpeg"
#     pause .09
#     "animated3/screensaver_023.jpeg"
#     pause .09
#     "animated3/screensaver_024.jpeg"
#     pause .09
#     "animated3/screensaver_025.jpeg"
#     pause .09
#     "animated3/screensaver_026.jpeg"
#     pause .09
#     "animated3/screensaver_027.jpeg"
#     pause .09
#     "animated3/screensaver_028.jpeg"
#     pause .09
#     "animated3/screensaver_029.jpeg"
#     pause 2
#     "animated3/screensaver_052.jpeg"
#     pause .09
#     "animated3/screensaver_053.jpeg"
#     pause .09
#     "animated3/screensaver_054.jpeg"
#     pause .09
#     "animated3/screensaver_055.jpeg"
#     pause .09
#     "animated3/screensaver_056.jpeg"
#     pause .09
#     "animated3/screensaver_075.jpeg"
#     pause .09
#     "animated3/screensaver_076.jpeg"
#     pause .09
#     "animated3/screensaver_077.jpeg"
#     pause .09
#     "animated3/screensaver_078.jpeg"
#     pause .09
#     repeat

# init:
#     image main_scene = Movie(play="images/screensaver.mp4", size=(1920, 1080))

# label main_menu:
#     scene main_scene
#     jump main_menu_screen

# init:
#     #на весь экран
#     image movie = Movie(size=(config.screen_width, config.screen_height))
 
# label main_menu:
#     scene movie
#     $ renpy.music.play("images/screensaver.ogv", channel="movie", loop=True) #видео (можно без звука)
#     # $ renpy.music.play("muz.mp3", channel="music", loop=True) #мелодия для меню - не обязательно
#     jump main_menu_screen