![logo](logo.png)

# WC
***
Window Controller (controlador de ventanas) o WC es una libreria que empaqueta otras tanto grandes como pequeñas, proveyendo múltiples funciones para facilitar el crear GUIs, creado por
Z3R0_GT con la iniciativa de "Facilitar el desarrollo de GUIs con python, sin perder mucho tiempo en el proceso con investigaciones para averiguar como lograrlo".

tenemos la vision de ser una libreria usada por varias personas para facilitarles el proceso del desarrollo, con el objetivo de ser lo mas simples posibles

## INSLACIÓN
***
Usa el siguiente comando para poder instalar la libreria (actualmente alojada gracias a Pypi)

```python
pip install Widget-Controller
```

## ¿COMO SE USA?
***
```python

from WC import *
from assets.libs.Lead import *
from tkinter import Tk

# CREA UNA REFERENCIA A CARPETAS QUE SE USAN (2>N)
WC.ClassConfig.set_dir(DIR="saves")  # guardados
WC.ClassConfig.set_dir(DIR="assets/images")  # imagenes
WC.ClassConfig.set_dir(DIR="assets/song")  # musica/sonidos
WC.ClassConfig.set_dir(DIR="assets/vid")  # videos

# CARGAR IMAGENES DE REFERENCIA (0>N)
WC.ClassSystem.load_archive(ID_FOLDER=2, name_archive="BG_CREATE_PERSON.jpg", TYPE="IMA")
WC.ClassSystem.load_archive(ID_FOLDER=2, name_archive="BG_CREDITS.jpg", TYPE="IMA")
WC.ClassSystem.load_archive(ID_FOLDER=2, name_archive="BG_MAIN_TITLE.jpg", TYPE="IMA")

ICON = WC.ClassSystem.load_archive(ID_FOLDER=2, name_archive="ICON.ico", TYPE="IMA")
NAME = "Dragon Hunter"

CREDIT = {"Main": "Z3R0_GT",
          "Image": "ThemeFinland",
          "Programmer": "Z3R0_GT",
          "History": "Honting Fap, \n Un extraño con sombrero de copa",
          "Stats": "Gio"}

SECRET = "ESTE EASTER EGG ES PARA BARRETO ALCANTARA IMANOL, UN BUEN AMIGO :D"

X_GLOBAL = 900
Y_GLOBAL = 500

TRANSFORM = f"{str(X_GLOBAL)}x{str(Y_GLOBAL)}"
NAMEVERSION = "AlphaPriv"
VERSION = "0.3"

TYPE = Lead.SearchOther(Type="Prota")
RAZE = Lead.SearchOther(Type="Raze")


PATH_INFO = f"Noticias de paquete #20 (17/06/2023): \n-Version de libreria {VERSION_LIB}. \n-APP version: {NAMEVERSION} {VERSION}. \n-Esta version es actulizada al español, mas muy pronto podra soportar ingles, disfruta!, además, gracias apoyarme."
SAVE_DATA = WC.ClassProcces.ConsultItem(ID=1, TYPE="list_dir")

class WindowMenu:
    def WindowMain():
        Window = Tk()
        Window.title(NAME)
        Window.geometry(TRANSFORM)
        Window.resizable(width=False, height=False)
        Window.iconbitmap(ICON)
        WC.ClassProcces.CenterWindow(WINDOW=Window, WIDTH=X_GLOBAL, HEIGH=Y_GLOBAL)

        lb_bg = WC.ClassNode.FuncLabel(
            NODE_MASTER=Window, TYPE="image", ID_IMA_DIR=2, X=-2, ReX=900, ReY=500)

        f_default = WC.ClassProcces.CreateFont()
        f_title = WC.ClassProcces.CreateFont(
            SIZE=24, IS_BLACK=True, IS_RALL=True, FAMILY="Helvetica")

        lb_title = WC.ClassNode.FuncLabel(
            NODE_MASTER=Window, FONT=f_title, TYPE="normal", TEXT=f"{NAME}", X=(X_GLOBAL/2.5))
        lb_credits = WC.ClassNode.FuncLabel(
            NODE_MASTER=Window, FONT=f_default, TYPE="normal", TEXT=f"Programmed by {CREDIT['Programmer']}", X=((X_GLOBAL-55)/2), Y=465)

        a_panel_news = WC.ClassNode.FuncText(
            NODE_MASTER=Window, FONT=f_default, X=10, Y=290, HEIGH=200, WIDTH=290)
        WC.ClassProcces.TextEdit(NODE_TEXT=a_panel_news,
                            TEXT=PATH_INFO, TYPE="default")

        b_new_game = WC.ClassNode.FuncButton(
            NODE_MASTER=Window, FONT=f_default, TEXT="Nuevo juego", TYPE="load_window", IDS=[4], X=((X_GLOBAL-35)/2), Y=300)

        b_load = WC.ClassNode.FuncButton(NODE_MASTER=Window, FONT=f_default,
                                     TEXT="Cargar juego", TYPE="load_window", IDS=[5], X=((X_GLOBAL-40)/2), Y=330)

        b_credits = WC.ClassNode.FuncButton(
            NODE_MASTER=Window, FONT=f_default, TEXT="Creditos", TYPE="load_window", IDS=[2], X=((X_GLOBAL-25)/2), Y=360)

        b_quit = WC.ClassNode.FuncButton(
            NODE_MASTER=Window, FONT=f_default, TYPE="exit", TEXT="Salir", X=(X_GLOBAL/2), Y=390)

        return Window.mainloop()

WC.ClassProcces.set_window(1, WindowMenu)

WC.start_app(ID=1)
```
Este es un ejemplo sacado directamente de BUILD 5.0 del archivo "testa.py", en cual podran encontrar dicho ejemplo, o pueden usar la BUILD 4.0 si desean verlo de manera dinamica (con interacción de consola)

## LIBRERIAS
***
- Usamos las siguientes librerias externas (no viene pre-instalados con python):
    - Pillow.
    - tkVideoPlayer.

- Pre-instalados:
    - os.
    - json.
    - winsound

# ¿QUE OFRECEMOS?
***
- Usamos un tipeado similar a java para crear GUIs basicas, teniendo las siguientes funciones:
    - Inicio de aplicacion para correr mutiples ventanas como un solo proceso
    - Nodos:
        - Botones, Áreas de texto, Etiquetas tanto para incluir imagenes adaptables como texto corriente, Áreas específicas para incluir entrada de usuario, menú de opciones, lista de botones.
    - Procesos:
        - Puedes crear fuentes de texto (todas provenientes de tkinter), Editar áreas de texto, crear ventanas (necesario para ejecución de programa), centrar ventanas, incluir barra de movimiento (scroll).
    - Sistema:
        - guardar y cargar archivos json (se usa diccionarios para este caso), la carga de videos, imagenes e otros, todo guardados para solo servir como llamada.
        - crear y almacenar direcciones para su posterior uso.
    - Desarrollador:
        - puedas tambien revisar un listado de objetos en general, tanto datos almacenados, funciones y ventana creadas y objetos guardados dentro de la libreria.

dentro de cada carpeta, se encuentra la versión correspondiente a WC con un pequeño ejemplo para que puedas testear las capacidades de la versión elegida, también es compatible (Version 4) para usarlo con consola.

# VERSIONES
***
Numero de versión que resibe o no soporte, ademas del tiempo de experación de soporte.

| Version    | Soporte                       | Cotenido                  |
| -------    | ------------------            | ---------                 |
| 6.0 > ...  | ❎                            |aun en pruebas (25/07/2023|
| 5.0 > 6.0  | ✅                            |Versión de MP3 Y MP4      |
| 4.0 > 4.9  | ✅                            |Carga pantalla            |
| 1.0 > 2.0  | ❎                            |Base de librería          |

Las versiones se aplicarán bajo el siguiente condicionamiento para identificar y tener la capacidad de leer:
--(Nombre de contrucción) (Versión numérica de lanzamiento).(Número de revisión actulizado)--, por ejemplo: 

BUILD 3.2   -- en este caso se puede decir, que la versión a tratar es la BUILD cuya versión 3, la revisión de codigo corresponde a la segunda vez desde que se lanzó. 
Sin embargo en caso de encontrar un tercer numero como en este caso: 
BUILD 5.0.1 -- se puede interpretar que la BUILD esta en su versión 5, no se a revisado desde que se lanzó pero es la primera versión pre-liminar para lanzar una revisión pronto (el tercer numero).

## Notas
***
1. Soporte implica solución de errores, mas no significa actualización, si quiere una version con mas funciones mira las versiones presentes y sus respectivos datos.

2. no somos dueños de ninguna libreria usada en este proyecto, en caso obtenga algun error, puede reportarlo o consultar en la página de GitHub (https://github.com/Z3R0GT/WC/issues).

3. las librerias que aparecen en [ LIBRERIAS](#librerias) pueden llegar a pertenecer a la ultima versión sea que se halla publicado o aun se este trabajando en ella
## Capturas
***
<img src="https://github.com/Z3R0GT/WC/blob/main/Screenshot/ExampleCode.png">
