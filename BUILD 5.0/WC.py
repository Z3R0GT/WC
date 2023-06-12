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

from tkinter import Text, Label, Entry, StringVar, Scrollbar, Listbox, Button, OptionMenu
from typing_extensions import Literal
from tkinter.font import Font
from PIL import Image, ImageTk

__VERSION__ = 5.0
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

__ITEM_CHOICE = None
_Nodes__ITEM_SELECT = []
_Config__DIR_FOLDER = [os.path.dirname(__file__)]
_Nodes__IMAGE_LOAD = []

__ID_WINDOW = 1

def __DEV__(type: Literal["DEV", "CONSULT"] = ..., ID: int = ...):

    if type == "DEV":
        return {
            "Item selecionados": f"{_Nodes__ITEM_SELECT}",
            "Dirección de un folder": f"{_Config__DIR_FOLDER}",
            "Item escogido": f"{__ITEM_CHOICE}",
            "Numero de ventana": f"{__ID_WINDOW}",
            "Imagenes cargadas": f"{_Nodes__IMAGE_LOAD}",
            "Ventanas guardadas": f"{CURRENT_WINDOW}"
        }
    elif type == "CONSULT":
        return _Nodes__ITEM_SELECT[ID]


class _WC:
    def _System__save_archive(DATA_SAVE: dict, ID_FOLDER: int, NAME_ARCHIVE: str):
        try:
            with open(f"{_Config__DIR_FOLDER[ID_FOLDER]}/{NAME_ARCHIVE}.json", "w") as file:

                matrix = {"Data", DATA_SAVE}
                matrix_con = json.dumps(matrix, indent=1)

                file.write(matrix_con)
                file.close()
                return print("HECHO SAVEARCHIVE \n")
        except:
            return print(f"\n ||ERROR|| info= ID FOLDER: {_Config__DIR_FOLDER[ID_FOLDER]}; NAME ARCHIVE: {NAME_ARCHIVE} Error.\n")

    def _System__load_archive(ID_FOLDER: int, NAME_ARCHIVE: str, TYPE: Literal["JSON", "IMA"] = ...):
        try:
            if TYPE == "JSON":
                with open(f"{_Config__DIR_FOLDER[ID_FOLDER]}/{NAME_ARCHIVE}.json") as file:
                    return json.load(file)
            elif TYPE == "IMA":
                photo = os.path.join(
                    _Config__DIR_FOLDER[ID_FOLDER], NAME_ARCHIVE)
                _Nodes__IMAGE_LOAD.append(photo)
                print("HECHO LOADARCHIVE \n")
                return photo
        except:
            return print(f"\n ||ERROR|| info= ID FOLDER: {_Config__DIR_FOLDER[ID_FOLDER]}, LIST err: {TYPE} \n")

    def __Load_window():

        if __ID_WINDOW == 0:
            CURRENT_WINDOW[(__ID_WINDOW+1)][1].WindowMain()
        else:
            CURRENT_WINDOW[__ID_WINDOW][1].WindowMain()
        return print("HECHO LOAD WINDOW")

    def __call_back(event, id):

        selec = event.widget.curselection()
        if selec:
            index = selec[0]
            data = event.widget.get(index)
            __ITEM_CHOICE = _WC._System__load_archive(
                ID_FOLDER=id, NAME_ARCHIVE=data, TYPE="JSON")

    def __Nodes__copy(event):
        if (12 == event.state and event.keysym == 'c'):
            return
        else:
            return "break"

    def __Procces__edit_text(NODE_TEXT: Text, TEXT: str, TYPE: Literal["default", "custom"], LIST=[], IS_TEXT=True, IS_EMPY=True):

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
                           lambda e: _WC.__call_back(event=e, id=int(TYPE)))
            
            return NODE_TEXT

    def __Procces__add_scroll(NODE_TEXT: Text):

        scroll = Scrollbar(master=NODE_TEXT, orient="vertical")
        scroll.config(command=NODE_TEXT.yview)
        NODE_TEXT["yscrollcommand"] = scroll.set

        scroll.grid(padx=660, ipady=178)
        return NODE_TEXT

    def __Nodes__add_action_button(NODE_MASTER, TYPE: Literal["exit", "load_window", "entry", "save", "load", "test"] = ..., ID_WINDOW: int = ..., ID_FOLDER: int = ..., DATA_SAVE: dict = ...):

        if TYPE == "exit":
            CURRENT_WINDOW.insert(0, "EXIT")
            return NODE_MASTER.destroy()
        elif TYPE == "save":
            __ID_WINDOW = ID_WINDOW

            _WC._System__save_archive(
                DATA_SAVE=DATA_SAVE, ID_FOLDER=ID_FOLDER, NAME_ARCHIVE=ENTRY_DATA.get())

            NODE_MASTER.destroy()
        elif TYPE == "load_window":
            __ID_WINDOW = ID_WINDOW
            return NODE_MASTER.destroy()
        elif TYPE == "test":
            print("TEST IS READY")

    def _Procces_type_font(SIZE: int = 10, IS_BLACK: bool = False, IS_SLASH: bool = False, IS_RALL: bool = False, FAMILY: str = ""):
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


class WC:

    def start_app(ID: int):
        """
        Empieza el programa con una "ID" que se asume que es el menu y que ya fue creado con "set_window"
        """
        while True:
            if CURRENT_WINDOW[0] == "EXIT":
                break
            else:
                _WC.__Load_window()

        print("||APP END||")
        return

    class Nodes:

        def FuncButton(NODE_MASTER, FONT: Font, TYPE: Literal["exit", "load_window", "entry", "save", "load", "test"], IDS: list = ..., TEXT: str = ..., DATA: dict = ..., X=0, Y=0, HEIGH=0, WIDTH=0):
            """
            elige un tipo de boton acorde la necesidad, siendo los siguientes casos: \n
            1) si quieres cargar "load_window" usa "IDS" como un arreglo y en la primera posicion coloca el "ID" de ventana que se va usar \n
            2) al usar "save", se requiere que "IDS" tenga dos posiciones, en la primera la ID sea de la ventana, y la segunda la carpeta (que se asume creada previamente con "set_dir")\n
            3) si usaras "exit", esto cierra y termina el programa \n
            """
            node_button = None

            if TYPE == "load_window":
                node_button = Button(master=NODE_MASTER, text=TEXT, command=lambda: _WC.__Nodes__add_action_button(
                    NODE_MASTER=NODE_MASTER, TYPE=TYPE, ID_WINDOW=IDS[0]), font=FONT)
            elif TYPE == "save":
                node_button = Button(master=NODE_MASTER, text=TEXT, command=lambda: _WC.__Nodes__add_action_button(
                    NODE_MASTER=NODE_MASTER, TYPE=TYPE, ID_WINDOW=IDS[0], ID_FOLDER=IDS[1], DATA_SAVE=DATA), font=FONT)
            elif TYPE == "exit":
                node_button = Button(master=NODE_MASTER, text=TEXT, command=lambda: _WC.__Nodes__add_action_button(
                    NODE_MASTER=NODE_MASTER, TYPE=TYPE), font=FONT)
            else:
                node_button = Button(master=NODE_MASTER, text=TEXT, command=lambda: _WC.__Nodes__add_action_button(
                    NODE_MASTER=NODE_MASTER, TYPE=TYPE), font=FONT)

            if HEIGH == 0 or WIDTH == 0:
                node_button.place(x=X, y=Y)
            else:
                node_button.place(x=X, y=Y, height=HEIGH, width=WIDTH)

            return node_button

        def FuncText(NodeMaster, Font: Font, CAN_COPY=False, X=0, Y=0, HEIGH=0, WIDTH=0):
            """
            crea una nodo de texto, especifica con "CAN_COPY" si quieres que el usuario pueda o no
            copiar el contenido de este
            """
            NODE_TEXT = Text(master=NodeMaster, font=Font)
            if CAN_COPY == False:
                NODE_TEXT.bind("<Key>", lambda e: _WC.__Nodes__copy(e))
            NODE_TEXT.place(x=X, y=Y, width=WIDTH, height=HEIGH)

            return NODE_TEXT

        def FuncLabel(NODE_MASTER, TYPE: Literal["normal", "image"], ID_IMA_DIR: int = ..., FONT: Font = ..., TEXT: str = "",  X=0, Y=0, HEIGH=0, WIDTH=0, ReX=0, ReY=0):
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

            elif TYPE == "image":
                IMA_REW = None

                Photo = Image.open(f"{_Nodes__IMAGE_LOAD[ID_IMA_DIR]}")

                if ReX == 0 or ReY == 0:
                    IMA_REW = ImageTk.PhotoImage(Photo)
                else:
                    Photo_rew = Photo.resize((ReX, ReY))
                    IMA_REW = ImageTk.PhotoImage(Photo_rew)

                node_label = Label(NODE_MASTER, image=IMA_REW)
                node_label.place(x=X, y=Y)

            return node_label

        def FuncEntry(NODE_MASTER, FONT: Font, X: int = ..., Y: int = ..., WIDTH: int = ...):
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
                CURRENT = []
                CURRENT.append(f"{list.get()}")

                for i in CURRENT:
                    if i not in _Nodes__ITEM_SELECT:
                        _Nodes__ITEM_SELECT.append(i)

            list.trace("w", callback)
            return node_menu

        def FuncListBox(NODE_MASTER, FONT: Font, X=0, Y=0, HEIGH=0, WIDTH=0):
            """
            crea una caja de lista
            """
            node_lis = Listbox(master=NODE_MASTER, font=FONT)
            node_lis.place(x=X, y=Y, height=HEIGH, width=WIDTH)

            return node_lis

    class Procces:
        def set_window(ID: int, TAG):
            """
            setea una nueva venta para automatizar el proceso con ID, envia una clase que contenga la funcion
            WindowMain() para poder ser reconozible a la libreria
            """
            CURRENT_WINDOW.append((ID, TAG))

        def TextEdit(NODE_TEXT: Text, TYPE: Literal["default", "custom"], TEXT="", IS_TEXT=True, IS_EMPY=True, LIST: list = ...):
            """
            edita un nodo de texto, elige un tipo para el saber la conexion a trabajar, setea el texto y especifica si es texto lo qie se trabaja o si esta limpio,
            es opcional si incluir una lista o no
            """
            return _WC.__Procces__edit_text(NODE_TEXT=NODE_TEXT, TEXT=TEXT, TYPE=TYPE, IS_TEXT=IS_TEXT, IS_EMPY=IS_EMPY, LIST=LIST)

        def CreateFont(SIZE=10, IS_BLACK=False, IS_SLASH=False, IS_RALL=False, FAMILY=""):
            """
            crea una fuente de un tamaño, aplicale condiciones de: \n
            - es negra: IS_BLACK \n
            - esta a un lado: IS_SLASH \n
            - tiene un ralla: IS_RALL \n

            y especifica el tipo de familia en el arbol
            """
            return _WC._Procces_type_font(SIZE=SIZE, IS_BLACK=IS_BLACK, IS_RALL=IS_RALL, IS_SLASH=IS_SLASH, FAMILY=FAMILY)

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
            return _WC.__Procces__add_scroll(NODE_TEXT=NODE_TEXT)

    class System:

        def save_archive(data: dict, ID_FOLDER: int, name_archive: str):
            """
            guarda archivos en un ID ya seteado (vease en "set_dir"), con un nombre, enviele diccionario con data
            que se convierte automaticamente en un JSON 
            """
            _WC._System__save_archive(
                DATA_SAVE=data, ID_FOLDER=ID_FOLDER, NAME_ARCHIVE=name_archive)

        def load_archive(ID_FOLDER: int, name_archive: str, TYPE: Literal["JSON", "IMA"]):
            """
            Carga un archivo con un ID segun lo hallas seteado (vease en "set_dir"), nombre al archivo
            y enviele un tipo 
            """
            _WC._System__load_archive(
                ID_FOLDER=ID_FOLDER, NAME_ARCHIVE=name_archive, TYPE=TYPE)

    class Config:

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
                _Config__DIR_FOLDER.append(
                    os.path.join(_Config__DIR_FOLDER[0], DIR))
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
