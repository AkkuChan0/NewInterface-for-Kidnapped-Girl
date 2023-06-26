## Новый интерфейс для игры "Kidnapped Girl"

--------------------------------------------------

#### Интерфейс был сделан по рофлу и из-за скуки. Можете использовать его где угодно. 

--------------------------------------------------

##### В коде имеются несколько переменных, которые вы можете использовать для проверок интерфейса:

1. bool: persistent.kk_interface:
persistent переменная, которая говорит, включен интерфейс или нет. True -- включено, False -- выключено.

```
if persistent.kk_interface:
	"Ого, интерфейс включён!"
else:
	"Эх, выключен... Вот незадача!"
```

2. bool: kk_installed:
Простая буловая переменная, показывающая, а установлен ли интерфейс вообще. 

```
if 'kk_installed' in locals():
	"Ты скачал интерфейс? Хорош!"
else:
	"Иди и скачивай интерфейс!"
```

##### Перейдём к функциям, которые вы можете использовать у себя.

1. set_mode_nvl() и set_mode_adv(): -- Вырезано из Бесконечного лета.
Данные функции используются для перевода разговорных персонажей в nvl режим и наоборот. set_mode_nvl() - из ADV в NVL. set_mode_adv() - наоборот.


##### Экраны, которые вы опять же можете использовать.

1. kk_notify(message, _time=4):
Данный экран выводит подсказку message на _time секунд (по умолчанию, т.е. при не указывании, стоит 4 секунды).

```
show screen kk_notify("Вот моя первая подсказка на 10 секунд.", 10)
```

#### Пока так.
#### Написан этот файл на скорую руку, ибо вряд ли кто-то его прочитает.




