"""
Window Controller (WC) a librelly for controll and create UI easy
with tkinter and PIL.

this lib is orient to build apps/games based on text, 
mode of saved archive JSON,
process automatly, and more!.

this lib was create by @Z3R0_GT (GitHub) in , if you find a bug
report to Z3R0_GT#3883
"""

import os
import json
import winsound

from tkinter import Text, Label, Entry, StringVar, Scrollbar, Listbox, Button, OptionMenu
from typing_extensions import Literal
from tkinter.font import Font
from PIL import Image, ImageTk

from tkVideoPlayer import TkinterVideo

VERSION_LIB = "5.0.7"
CURRENT_WINDOW = ["CONTINUE"]
"""
Esta es una constante de estado, cuando esta en "CONTINUE" el programa podra correr con normalidad,
pero si esta en "EXIT" entonces el programa terminara, siendo la posicion 0 la mas importante y no debes de cambiarla bajo ninguna sircunstancia
salvo que quieres romper tu programa
"""

SECRET = "ESTE EASTER EGG ES PARA BARRETO ALCANTARA IMANOL, UN BUEN AMIGO :D"
"""
NO TOCAR EN UN "print" JAMAS!; esta variable es usar como probravación de libreria
caso que se use en un "print" puede causar un bug de flujo
"""

_WC__ITEM_CHOICE = None
_ClassNode__ITEM_SELECT = []
_ClassNode_CURRENT = []

_ClassConfig__DIR_FOLDER = [os.path.dirname(__file__)]
_ClassNode__IMAGE_LOAD = []
_ClassConfig__VIDEO = []
_ClassConfig__SOUND = []

_ID_WINDOW = 1
ENTRY_DATA = ""


def __DEV__():
    return {
        "Item selecionados": f"{_ClassNode__ITEM_SELECT}",
        "Dirección de un folder": f"{_ClassConfig__DIR_FOLDER}",
        "Item escogido": f"{_WC__ITEM_CHOICE}",
        "Numero de ventana": f"{_ID_WINDOW}",
        "Imagenes cargadas": f"{_ClassNode__IMAGE_LOAD}",
        "Ventanas guardadas": f"{CURRENT_WINDOW}",
        "Archivos de video": f"{_ClassConfig__VIDEO}",
        "Archivos de sonido": f"{_ClassConfig__SOUND}",
    }


class _WC:
    def _ClassSystem__save_archive(DATA_SAVE: dict, ID_FOLDER: int, NAME_ARCHIVE: str):
        try:
            with open(f"{_ClassConfig__DIR_FOLDER[ID_FOLDER]}/{NAME_ARCHIVE}.json", "w") as file:
                file.write(DATA_SAVE)
                file.close()
                return print("HECHO SAVEARCHIVE \n")
        except:
            return print(f"\n ||ERROR|| info= ID FOLDER: {_ClassConfig__DIR_FOLDER[ID_FOLDER]}; NAME ARCHIVE: {NAME_ARCHIVE} Error.\n")

    def _ClassSystem__load_archive(ID_FOLDER: int, NAME_ARCHIVE: str, TYPE: Literal["JSON", "IMA"] = ...):
        try:
            if TYPE == "JSON":
                if NAME_ARCHIVE.find(".json") != -1:
                    with open(f"{_ClassConfig__DIR_FOLDER[ID_FOLDER]}/{NAME_ARCHIVE}") as file:
                        print("HECHO LOAD JSON \n")
                        return json.load(file)
                else:
                    with open(f"{_ClassConfig__DIR_FOLDER[ID_FOLDER]}/{NAME_ARCHIVE}.json") as file:
                        print("HECHO LOAD JSON \n")
                        return json.load(file)

            elif TYPE == "IMA":
                photo = os.path.join(
                    _ClassConfig__DIR_FOLDER[ID_FOLDER], NAME_ARCHIVE)
                _ClassNode__IMAGE_LOAD.append(photo)
                print("HECHO LOADARCHIVE \n")
                return photo
        except:
            return print(f"\n ||ERROR|| info= ID FOLDER: {_ClassConfig__DIR_FOLDER[ID_FOLDER]}, LIST ERROR: {TYPE} \n")

    def _Load_window():

        if _ID_WINDOW == 0:
            CURRENT_WINDOW[(_ID_WINDOW+1)][1].WindowMain()
        else:
            CURRENT_WINDOW[_ID_WINDOW][1].WindowMain()
        return print("HECHO LOAD WINDOW")

    def _call_back(event, id):
        global __ITEM_CHOICE

        selec = event.widget.curselection()
        if selec:
            index = selec[0]
            data = event.widget.get(index)
            __ITEM_CHOICE = _WC._ClassSystem__load_archive(
                ID_FOLDER=id, NAME_ARCHIVE=data, TYPE="JSON")

    def _ClassNode__copy(event):
        if (12 == event.state and event.keysym == 'c'):
            return
        else:
            return "break"

    def _ClassProcces__edit_text(NODE_TEXT: Text, TEXT: str, TYPE: Literal["default", "custom"], LIST=[], IS_TEXT=True, IS_EMPY=True):

        if IS_TEXT:
            if IS_EMPY == False:
                NODE_TEXT.delete("1.0", "end")

            data = None

            if IS_EMPY:
                if TYPE == "default":
                    return NODE_TEXT.insert("insert", TEXT)
                # elif TYPE == "custom":
                    """
                    Toma otra serie de parametros de "LIST" y los activa bajo
                    ciertos criterios...
                    """
        else:
            NODE_TEXT.insert("end", f"{LIST}")
            NODE_TEXT.bind("<<ListboxSelect>>",
                           lambda e: _WC._call_back(event=e, id=1))

            return NODE_TEXT

    def _ClassProcces__add_scroll(NODE_TEXT: Text):

        scroll = Scrollbar(master=NODE_TEXT, orient="vertical")
        scroll.config(command=NODE_TEXT.yview)
        NODE_TEXT["yscrollcommand"] = scroll.set

        scroll.grid(padx=660, ipady=178)
        return NODE_TEXT

    def _ClassNode__add_action_button(NODE_MASTER, TYPE: Literal["exit", "load_window", "save_archive", "test", "special_entry", "special_entry_data"] = ..., ID_WINDOW: int = ..., ID_FOLDER: int = ..., DATA_SAVE=...):
        global _ID_WINDOW
        global ENTRY_DATA

        if TYPE == "exit":
            CURRENT_WINDOW.insert(0, "EXIT")
            return NODE_MASTER.destroy()
        elif TYPE == "save_archive":
            _ID_WINDOW = ID_WINDOW

            matrix_con = json.dumps(DATA_SAVE, indent=1)
            _WC._ClassSystem__save_archive(
                DATA_SAVE=matrix_con, ID_FOLDER=ID_FOLDER, NAME_ARCHIVE=ENTRY_DATA.get())

            return NODE_MASTER.destroy()
        elif TYPE == "load_window":
            _ID_WINDOW = ID_WINDOW
            return NODE_MASTER.destroy()
        elif TYPE == "test":
            print("TEST IS READY")
        elif TYPE == "special_entry":
            global __ITEM_CHOICE
            _ID_WINDOW = ID_WINDOW

            name = ENTRY_DATA.get()

            Data = {
                "Raze": WC.ClassProcces.ConsultItem(0, "item_select"),
                "Impact": WC.ClassProcces.ConsultItem(1, "item_select"),
                "Name": name,
                "Stats": DATA_SAVE[0].SearchStats(Type=WC.ClassProcces.ConsultItem(1, "item_select")),
                "HistoryAdvanced": [0, 0, 0, 0]
            }

            temp_save = json.dumps(Data, indent=1)
            _WC._ClassSystem__save_archive(
                DATA_SAVE=temp_save, ID_FOLDER=ID_FOLDER, NAME_ARCHIVE=name)

            __ITEM_CHOICE = _WC._ClassSystem__load_archive(
                ID_FOLDER=ID_FOLDER, NAME_ARCHIVE=name, TYPE="JSON")

            return NODE_MASTER.destroy()

        elif TYPE == "special_entry_data":
            _ID_WINDOW = ID_WINDOW

            temp_save = json.dumps(Data, indent=1)
            _WC._ClassSystem__save_archive(
                DATA_SAVE=temp_save, ID_FOLDER=ID_FOLDER, NAME_ARCHIVE=ENTRY_DATA.get())

            return NODE_MASTER.destroy()

    def _ClassProcces_type_font(SIZE: int = 10, IS_BLACK: bool = False, IS_SLASH: bool = False, IS_RALL: bool = False, FAMILY: str = ""):
        type_font = None

        if IS_BLACK and IS_SLASH and IS_RALL:
            type_font = Font(family=FAMILY, size=SIZE, weight="bold",
                             slant="italic", underline=True)
        elif IS_BLACK and IS_SLASH:
            type_font = Font(family=FAMILY, size=SIZE,
                             weight="bold", slant="italic")
        elif IS_BLACK and IS_RALL:
            type_font = Font(family=FAMILY, size=SIZE,
                             weight="bold", underline=True)
        elif IS_RALL and IS_SLASH:
            type_font = Font(family=FAMILY, size=SIZE,
                             slant="italic", underline=True)
        elif IS_BLACK:
            type_font = Font(family=FAMILY, size=SIZE, weight="bold")
        elif IS_SLASH:
            type_font = Font(family=FAMILY, size=SIZE, slant="italic")
        elif IS_RALL:
            type_font = Font(family=FAMILY, size=SIZE, underline=True)
        else:
            type_font = Font(family="italic", size=SIZE)

        return type_font

    def _ClassNode_video_config(NODE_VIDEO: TkinterVideo, TYPE: Literal["play", "load", "frame"], ID_FOLDER: int = ..., NAME: str = ..., IS_SPECIF_SEC: bool = True, VALUE: int = ...):

        if TYPE == "play":
            if NODE_VIDEO.is_paused():
                NODE_VIDEO.play()
            else:
                NODE_VIDEO.pause()
        elif TYPE == "load":
            NODE_VIDEO.load(path=os.path.join(
                _ClassConfig__DIR_FOLDER[ID_FOLDER], NAME))
        elif TYPE == "frame":
            if IS_SPECIF_SEC:
                NODE_VIDEO.seek(VALUE)
            else:
                ver_to = int(NODE_VIDEO.current_duration())+VALUE
                ver_limit = NODE_VIDEO.video_info()

                if ver_to < int(ver_limit["duration"]):
                    NODE_VIDEO.seek(ver_to)
                else:
                    NODE_VIDEO.seek(int(ver_limit["duration"]))

    def _ClassProcces_sound_play(ID: int, NAME_ARCHIVE: str = ..., is_load=False):

        if is_load != True:
            song = winsound.PlaySound(os.path.join(
                _ClassConfig__DIR_FOLDER[ID], NAME_ARCHIVE), winsound.SND_FILENAME)
            _ClassConfig__SOUND.append(song)
        else:
            song = _ClassConfig__SOUND[ID]

        return song

    def _ClassProcces__cur_item(ID: int, TYPE: Literal["item_select", "list_dir", "item_choice", "cur_item"]):
        global __ITEM_CHOICE
        global ENTRY_DATA

        if TYPE == "item_select":
            return _ClassNode__ITEM_SELECT[ID]
        elif TYPE == "cur_item":
            return _ClassNode_CURRENT[ID]
        elif TYPE == "list_dir":
            return os.listdir(_ClassConfig__DIR_FOLDER[ID])
        elif TYPE == "item_choice":
            return __ITEM_CHOICE


class WC:

    def start_app(ID: int):
        """
        Empieza el programa con una "ID" que se asume que es el menu y que ya fue creado con "set_window"
        """
        while True:
            if CURRENT_WINDOW[0] == "EXIT":
                break
            else:
                _WC._Load_window()

        print("||APP END||")
        return

    class ClassNode:

        def FuncButton(NODE_MASTER, FONT: Font, TYPE: Literal["exit", "load_window", "save_archive", "test", "special_entry", "special_entry_data"], IDS: list = ..., TEXT: str = ..., DATA=..., X=0, Y=0, HEIGH=0, WIDTH=0):
            """
            elige un tipo de boton acorde la necesidad, siendo los siguientes casos: \n
            1) si quieres cargar "load_window" usa "IDS" como un arreglo y en la primera posicion coloca el "ID" de ventana que se va usar \n
            2) al usar "save", se requiere que "IDS" tenga dos posiciones, en la primera la ID sea de la ventana, y la segunda la carpeta (que se asume creada previamente con "set_dir")\n
            3) si usaras "exit", esto cierra y termina el programa \n
            """
            node_button = None
            vy_pass = None

            print(f" DATA:  {DATA}")

            if TYPE == "special_entry":
                node_button = Button(master=NODE_MASTER, text=TEXT, command=lambda: _WC._ClassNode__add_action_button(
                    NODE_MASTER=NODE_MASTER, TYPE=TYPE, ID_WINDOW=IDS[0], ID_FOLDER=IDS[1], DATA_SAVE=DATA), font=FONT)
            elif TYPE == "special_entry_data":
                node_button = Button(master=NODE_MASTER, text=TEXT, command=lambda: _WC._ClassNode__add_action_button(
                    NODE_MASTER=NODE_MASTER, TYPE=TYPE, ID_WINDOW=IDS[0], ID_FOLDER=IDS[1], DATA_SAVE=DATA), font=FONT)
            elif TYPE == "load_window":
                node_button = Button(master=NODE_MASTER, text=TEXT, command=lambda: _WC._ClassNode__add_action_button(
                    NODE_MASTER=NODE_MASTER, TYPE=TYPE, ID_WINDOW=IDS[0]), font=FONT)
            elif TYPE == "save_archive":
                node_button = Button(master=NODE_MASTER, text=TEXT, command=lambda: _WC._ClassNode__add_action_button(
                    NODE_MASTER=NODE_MASTER, TYPE=TYPE, ID_WINDOW=IDS[0], ID_FOLDER=IDS[1], DATA_SAVE=DATA), font=FONT)
            else:
                vy_pass = True

            if vy_pass:
                if TYPE == "exit":
                    node_button = Button(master=NODE_MASTER, text=TEXT, command=lambda: _WC._ClassNode__add_action_button(
                        NODE_MASTER=NODE_MASTER, TYPE=TYPE), font=FONT)
                else:
                    node_button = Button(master=NODE_MASTER, text=TEXT, command=lambda: _WC._ClassNode__add_action_button(
                        NODE_MASTER=NODE_MASTER, TYPE=TYPE), font=FONT)

            if HEIGH == 0 or WIDTH == 0:
                node_button.place(x=X, y=Y)
            else:
                node_button.place(x=X, y=Y, height=HEIGH, width=WIDTH)

            return node_button

        def FuncButtonVideo(NODE_MASTER, FONT: Font, NODE_VIDEO: TkinterVideo, TYPE: Literal["play", "load", "frame"], ID_FOLDER: int = ..., NAME: str = ..., IS_SPECIF_SEC: bool = True, TEXT: str = ..., VALUE: int = ..., X=0, Y=0, HEIGH=0, WIDTH=0):

            node_button = Button(master=NODE_MASTER, text=TEXT, command=lambda: _WC._ClassNode_video_config(
                NODE_VIDEO=NODE_VIDEO, TYPE=TYPE, IS_SPECIF_SEC=IS_SPECIF_SEC, VALUE=VALUE, ID_FOLDER=ID_FOLDER, NAME=NAME), font=FONT)

            if HEIGH == 0 or WIDTH == 0:
                node_button.place(x=X, y=Y)
            else:
                node_button.place(x=X, y=Y, height=HEIGH, width=WIDTH)

            return node_button

        def FuncText(NODE_MASTER, FONT: Font, CAN_COPY=False, X=0, Y=0, HEIGH=0, WIDTH=0):
            """
            crea una nodo de texto, especifica con "CAN_COPY" si quieres que el usuario pueda o no
            copiar el contenido de este
            """
            NODE_TEXT = Text(master=NODE_MASTER, font=FONT)
            if CAN_COPY == False:
                NODE_TEXT.bind("<Key>", lambda e: _WC._ClassNode__copy(e))
            NODE_TEXT.place(x=X, y=Y, width=WIDTH, height=HEIGH)

            return NODE_TEXT

        def FuncLabel(NODE_MASTER, TYPE: Literal["normal", "image"] = "normal", ID_IMA_DIR: int = ..., FONT: Font = ..., TEXT: str = "",  X=0, Y=0, HEIGH=0, WIDTH=0, ReX=0, ReY=0):
            """
            Crea una etiqueta(label) con un tipo para diferenciar si es imagen o un texto, caso que sea imagen usar: "ID_IMA_DIR" (que se asuma ya creado con "load_archive") y con "ReX" y "ReY" 
            para redimensionar la image, caso contrario, solo unar "TEXT" para crear una imagen normal.
            """

            if TYPE == "normal":
                node_label = Label(master=NODE_MASTER,
                                   font=FONT, text=TEXT)

                if HEIGH == 0 or WIDTH == 0:
                    node_label.place(x=X, y=Y)
                else:
                    node_label.place(x=X, y=Y, height=HEIGH, width=WIDTH)

                return node_label

            elif TYPE == "image":
                global IMA_REW

                try:
                    Photo = Image.open(f"{_ClassNode__IMAGE_LOAD[ID_IMA_DIR]}")

                    if ReX == 0 or ReY == 0:
                        IMA_REW = ImageTk.PhotoImage(Photo)
                    else:
                        Photo_rew = Photo.resize((ReX, ReY))
                        IMA_REW = ImageTk.PhotoImage(Photo_rew)

                    node_label = Label(NODE_MASTER, image=IMA_REW)
                    node_label.place(x=X, y=Y)

                    return node_label
                except:
                    print("||ERROR|| IMAGEN NO ENCONTRADA")
                    WC.ClassNode.FuncLabel(NODE_MASTER=NODE_MASTER, TYPE="normal", FONT=FONT,
                                           TEXT="||IMAGEN NO ENCONTRADA||", HEIGH=HEIGH, WIDTH=WIDTH, X=X, Y=Y)

        def FuncEntry(NODE_MASTER, FONT: Font, X: int = 0, Y: int = 0, WIDTH: int = ...):
            """
            crea un espacio en blanco para ingresar texto, este se puede recuperar con ENTRY_DATA.get()
            """
            global ENTRY_DATA

            ENTRY_DATA = StringVar(master=NODE_MASTER)
            node_entry = Entry(master=NODE_MASTER, font=FONT,
                               width=WIDTH, textvariable=ENTRY_DATA)
            node_entry.place(x=X, y=Y)

            return node_entry

        def FuncOptionMenu(NODE_MASTER, OPTION_LIST: list, FONT, X=0, Y=0, WIDTH=0, HIGH=0):
            """
            crea un menu de opcion (se presenta como un boton)
            """
            list = StringVar(NODE_MASTER)
            list.set(OPTION_LIST[0])

            node_menu = OptionMenu(NODE_MASTER, list, *OPTION_LIST)
            node_menu.config(font=FONT)
            if WIDTH != 0 and HIGH != 0:
                node_menu.place(x=X, y=Y, width=WIDTH, height=HIGH)
            else:
                node_menu.place(x=X, y=Y)

            def callback(*args):
                global _ClassNode_CURRENT
                _ClassNode_CURRENT.append(f"{list.get()}")

                for i in _ClassNode_CURRENT:
                    if i not in _ClassNode__ITEM_SELECT:
                        _ClassNode__ITEM_SELECT.append(i)

            list.trace("w", callback)
            return node_menu

        def FuncListBox(NODE_MASTER, FONT: Font, X=0, Y=0, HEIGH=0, WIDTH=0):
            """
            crea una caja de lista
            """
            node_lis = Listbox(master=NODE_MASTER, font=FONT)
            node_lis.place(x=X, y=Y, height=HEIGH, width=WIDTH)

            return node_lis

        def FuncVideoPlayer(NODE_MASTER, SCALED: bool = False, HEIGH: int = ..., WIDTH: int = ..., X=0, Y=0):

            if SCALED:
                node_video = TkinterVideo(master=NODE_MASTER, scaled=SCALED)
            else:
                node_video = TkinterVideo(master=NODE_MASTER)

            if HEIGH != 0 or WIDTH != 0:
                node_video.place(x=X, y=Y, width=WIDTH, height=HEIGH)
            else:
                node_video.place(x=X, y=Y)

            return node_video

    class ClassProcces:
        def set_window(ID: int, TAG):
            """
            setea una nueva venta para automatizar el proceso con ID, envia una clase que contenga la funcion
            WindowMain() para poder ser reconozible a la libreria
            """
            CURRENT_WINDOW.append((ID, TAG))

        def ConsultItem(ID: int = ..., TYPE: Literal["item_select", "list_dir", "item_choice", "cur_item"] = "item_choice"):
            return _WC._ClassProcces__cur_item(ID=ID, TYPE=TYPE)

        def SoundPlay(ID: int, NAME_ARCHIVE: str = ..., is_load=False):
            """
            Crea una instancia de musica/sonido para reproducirse, toda canción creada, es guardada
            en ID, si quiere volver a cargarla, solo tiene que usar "ID"+ "is_load" para ejecutarla
            """
            return _WC._ClassProcces_sound_play(ID=ID, NAME_ARCHIVE=NAME_ARCHIVE, is_load=is_load)

        def TextEdit(NODE_TEXT: Text, TYPE: Literal["default", "custom"], TEXT="", IS_TEXT=True, IS_EMPY=True, LIST: list = ...):
            """
            edita un nodo de texto, elige un tipo para el saber la conexion a trabajar, setea el texto y especifica si es texto lo qie se trabaja o si esta limpio,
            es opcional si incluir una lista o no
            """
            return _WC._ClassProcces__edit_text(NODE_TEXT=NODE_TEXT, TEXT=TEXT, TYPE=TYPE, IS_TEXT=IS_TEXT, IS_EMPY=IS_EMPY, LIST=LIST)

        def CreateFont(SIZE=10, IS_BLACK=False, IS_SLASH=False, IS_RALL=False, FAMILY=""):
            """
            crea una fuente de un tamaño, aplicale condiciones de: \n
            - es negra: IS_BLACK \n
            - esta a un lado: IS_SLASH \n
            - tiene un ralla: IS_RALL \n

            y especifica el tipo de familia en el arbol
            """
            return _WC._ClassProcces_type_font(SIZE=SIZE, IS_BLACK=IS_BLACK, IS_RALL=IS_RALL, IS_SLASH=IS_SLASH, FAMILY=FAMILY)

        def CenterWindow(WINDOW, WIDTH: int, HEIGH: int):
            """
            Retorna la venta indicada en el centro de la pantalla con sus medida exactas
            """
            widthTot = WINDOW.winfo_screenwidth()
            highTot = WINDOW.winfo_screenheight()

            pos_w = round(widthTot/2-WIDTH/2)
            pos_h = round(highTot/2-HEIGH/2)

            return WINDOW.geometry(str(WIDTH)+"x"+str(HEIGH)+"+"+str(pos_w)+"+"+str(pos_h))

        def Addscroll(NODE_TEXT: Text):
            """
            agrega un scroll a un "NODE_TEXT"
            """
            return _WC._ClassProcces__add_scroll(NODE_TEXT=NODE_TEXT)

    class ClassSystem:

        def save_archive(data: dict, ID_FOLDER: int, name_archive: str):
            """
            guarda archivos en un ID ya seteado (vease en "set_dir"), con un nombre, enviele diccionario con data
            que se convierte automaticamente en un JSON 
            """
            _WC._ClassSystem__save_archive(
                DATA_SAVE=data, ID_FOLDER=ID_FOLDER, NAME_ARCHIVE=name_archive)

        def load_archive(ID_FOLDER: int, name_archive: str, TYPE: Literal["JSON", "IMA"]):
            """
            Carga un archivo con un ID segun lo hallas seteado (vease en "set_dir"), nombre al archivo
            y enviele un tipo 
            """
            return _WC._ClassSystem__load_archive(
                ID_FOLDER=ID_FOLDER, NAME_ARCHIVE=name_archive, TYPE=TYPE)

    class ClassConfig:

        def set_dir(DIR: str):
            """
            crea una nueva dirección escribiendo solo la carpeta siendo tal que haci: .

            ---CARPETA MADRE//root// \n
                |\n
                |\n
                |Carpeta_A:\n
                |---|\n
                |---|Carpeta_1...\n
                |---|\n
                |---|Contenido...\n
                |Carpeta_B:\n
                |---|\n
                |---|Carpeta_1...\n
                |---|\n
                |---|Contenido...\n

                siendo el comando: set_dir(DIR=Carpeta_A/Carpeta_1); creando de esta forma una nueva direccion (siendo 0 root)
            """
            try:
                _ClassConfig__DIR_FOLDER.append(
                    os.path.join(_ClassConfig__DIR_FOLDER[0], DIR))
                return print("HECHO SETDIR \n")
            except:
                return print("||ERROR|| info: FALLIDO SETDIR \n")

        pass

    class DEV:
        def DEVCONSULT():
            """
            Retorna una lista de valores privados (solo usar con consola)
            """
            return __DEV__()
