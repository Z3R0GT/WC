"""
Window Controller (WC) a librelly for controll and create UI easy
with tkinter and PIL.

this lib is orient to build apps/games based on text, 
mode of saved archive JSON,
process automatly, and more!.

this lib was create by @Z3R0_GT (GitHub) in , if you find a bug
report to Z3R0_GT#3883
"""

###----------------------Librerias----------------------###
import os
import json
import winsound

from tkinter import Text, Label, Entry, StringVar, Scrollbar, Listbox, Button, OptionMenu, Scale, messagebox
from typing_extensions import Literal
from tkinter.font import Font
from PIL import Image, ImageTk

from tkVideoPlayer import TkinterVideo

###----------------------Constantes----------------------###
VERSION_LIB = "5.1"
"""
Version de la libreria actual
"""
CURRENT_WINDOW = ["CONTINUE"]
"""
Esta es una constante de estado, cuando esta en "CONTINUE" el programa podra correr con normalidad,
pero si esta en "EXIT" entonces el programa terminara, siendo la posicion 0 la mas importante y no debes de cambiarla bajo ninguna sircunstancia
salvo que quieres romper tu programa
"""

ERROR_INFO = f"Por favor, proceda con alguna de los siguientes alternativas. \n \
    - Coloquese en contacto con el Dev (en caso de descargar el software). \n \
    - Reinstale el Sofware o reestablesca las carpetas/archivos que alla eliminado. \n \
    - Declare correctamente las variables correspondientes al tipo de error. \n \
    - Abra el repositorio WC y abra un issue con el tag Bug/Error, llene la plantilla con los datos correspondientes."
"""
Usado para en caso de un error, se proceda a imprimir un texto en una ventana
se recomienda no cambiarlo.
"""

SECRET = "ESTE EASTER EGG ES PARA BARRETO ALCANTARA IMANOL, UN BUEN AMIGO :D"
"""
NO TOCAR EN UN "print" JAMAS!; esta variable es usar como probravación de libreria
caso que se use en un "print" puede causar un bug de flujo
"""
_Config_NAME_APP = ...

_WC__ITEM_CHOICE = ...
_ClassNode__ITEM_SELECT = []
_ClassNode_CURRENT = []

_ClassConfig__DIR_FOLDER = [os.path.dirname(__file__)]
_ClassNode__IMAGE_LOAD = []
_ClassConfig__VIDEO = []
_ClassConfig__SOUND = []

_ID_WINDOW = 1
"""
VARIABLE USADA PARA SABER CUAL ES LA VENTA A ABrIR CUANDO LA ANTERIOR SE CIERRE
||NO TOCAR||
"""
_ClassNode__ENTRY_DATA = ""
_ClassNode__ENTRY_SCALE = ["MASTER", "MUSIC", "FVX"]


def __DEV__():
    print(f"\n Item selecionados: {_ClassNode__ITEM_SELECT} \n Direccion de folders: {_ClassConfig__DIR_FOLDER} \
            \n Item Escogido: {_WC__ITEM_CHOICE} \n Numero de Ventana: {_ID_WINDOW} \
            \n Imagenes Cargadas: {_ClassNode__IMAGE_LOAD} \n Archivos de video: {_ClassConfig__VIDEO} \
            \n Archivos de sonido: {_ClassConfig__SOUND} \n Datos ingresado: {_ClassNode__ENTRY_DATA} \
            \n Datos sclae: {_ClassNode__ENTRY_SCALE} \n Datos de OptionMenu {_ClassNode_CURRENT}")


###----------------------Procesos Privados ||NO TOCAR||----------------------###
class _WC:
    def _ClassSystem__save_archive(DATA_SAVE: dict, ID_FOLDER: int, NAME_ARCHIVE: str):
        try:
            with open(f"{_ClassConfig__DIR_FOLDER[ID_FOLDER]}/{NAME_ARCHIVE}.json", "w") as file:
                file.write(DATA_SAVE)
                file.close()
                return print("HECHO SAVEARCHIVE \n")
        except:
            messagebox.showerror("Error al guardar", f"la carpeta especificada no existe o fue movida ({_ClassConfig__DIR_FOLDER[ID_FOLDER]}), {ERROR_INFO}")
            return print(f"\n ||ERROR|| info= ID FOLDER: {_ClassConfig__DIR_FOLDER[ID_FOLDER]}; NAME ARCHIVE: {NAME_ARCHIVE} Error.\n")

    def _ClassSystem__load_archive(ID_FOLDER: int, NAME_ARCHIVE: str, TYPE: Literal["JSON", "IMA"] = ...):
        if TYPE == "JSON":
            try:
                if NAME_ARCHIVE.find(".json") != -1:
                    with open(f"{_ClassConfig__DIR_FOLDER[ID_FOLDER]}/{NAME_ARCHIVE}") as file:
                        print("HECHO LOAD JSON \n")
                        return json.load(file)
                else:
                    with open(f"{_ClassConfig__DIR_FOLDER[ID_FOLDER]}/{NAME_ARCHIVE}.json") as file:
                        print("HECHO LOAD JSON \n")
                        return json.load(file)
            except:
                messagebox.showerror("Error load JSON", f"El archivo {NAME_ARCHIVE} no fue encontrado, {ERROR_INFO}")
                return print(f"\n ||ERROR|| info= ID FOLDER: {_ClassConfig__DIR_FOLDER[ID_FOLDER]}, LIST ERROR: {TYPE} \n")
        elif TYPE == "IMA":
                try:
                    photo = os.path.join(
                        _ClassConfig__DIR_FOLDER[ID_FOLDER], NAME_ARCHIVE)
                    _ClassNode__IMAGE_LOAD.append(photo)
                    print("HECHO LOADARCHIVE \n")
                    return photo
                except:
                    messagebox.showerror("Error load IMAGE", f"el archivo {NAME_ARCHIVE} no fue encontrado o la extensión no coincide, {ERROR_INFO}")
                    return print(f"\n ||ERROR|| info= ID FOLDER: {_ClassConfig__DIR_FOLDER[ID_FOLDER]}, LIST ERROR: {TYPE} \n")

    def _Load_window():
        try:
            if _ID_WINDOW == 0:
                CURRENT_WINDOW[(_ID_WINDOW+1)][1].WindowMain()
            else:
                CURRENT_WINDOW[_ID_WINDOW][1].WindowMain()
            return print("HECHO LOAD WINDOW")
        except:
            messagebox.showerror("Critical Error", f"Un error interno ocurrio, consulte con la consola (caso de ser dev) o {ERROR_INFO}")
            print(f"||CRITIC ERROR|| info= Parece que la ventana ingesada no cuenta con la función -WindowMain- o la venta que se tiene actualmente no coincide, \n por favor, registre correctamente su codigo, caso de no encontrar solución dirijase al repositorio WC,\n abra un issue con el tag Bug/Error ")

    def _call_back(event, id):
        #SE NECESITA ADAPTAR ESTO PARA TANTO CARGA, COMO RETORNAR UN OBJETO SELECIONADO
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
    def _ClassProcces__set_trans(NodeAll, ID_IMA, X, Y):
        """
        crea una instancia para transparencia (es automatica)
        """
        ...
    
    def _ClassProcces__add_scroll(NODE_TEXT: Text):

        scroll = Scrollbar(master=NODE_TEXT, orient="vertical")
        scroll.config(command=NODE_TEXT.yview)
        NODE_TEXT["yscrollcommand"] = scroll.set

        scroll.grid(padx=660, ipady=178)
        return NODE_TEXT

    def _ClassNode__add_action_button(NODE_MASTER, TYPE: Literal["exit", "load_window", "save_archive", "test", "special_entry", "special_entry_data"] = ..., ID_WINDOW: int = ..., ID_FOLDER: int = ..., DATA_SAVE=...):
        global _ID_WINDOW
        global _ClassNode__ENTRY_DATA

        if TYPE == "exit":
            CURRENT_WINDOW.insert(0, "EXIT")
            return NODE_MASTER.destroy()
        elif TYPE == "save_archive":
            _ID_WINDOW = ID_WINDOW

            matrix_con = json.dumps(DATA_SAVE, indent=1)
            _WC._ClassSystem__save_archive(
                DATA_SAVE=matrix_con, ID_FOLDER=ID_FOLDER, NAME_ARCHIVE=_ClassNode__ENTRY_DATA.get())

            return NODE_MASTER.destroy()
        elif TYPE == "load_window":
            _ID_WINDOW = ID_WINDOW
            return NODE_MASTER.destroy()
        elif TYPE == "test":
            print("TEST IS READY")
        elif TYPE == "special_entry":
            global __ITEM_CHOICE
            _ID_WINDOW = ID_WINDOW

            name = _ClassNode__ENTRY_DATA.get()

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
                DATA_SAVE=temp_save, ID_FOLDER=ID_FOLDER, NAME_ARCHIVE=_ClassNode__ENTRY_DATA.get())

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
            try:
                NODE_VIDEO.load(path=os.path.join(
                    _ClassConfig__DIR_FOLDER[ID_FOLDER], NAME))
            except:
                messagebox.showerror("Error Video", "Esta función sigue en desarrollo, consulte con la consola (no implmentar para un software)")
                print(f"||ERROr||, info=En caso de tener este error, subir una captura tanto de este error \n \
                        como del codigo que lo ocaciono a Github: https://github.com/Z3R0GT/WC/issues, en breve le respondemos!")
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

    def _ClassProcces__cur_item(ID: int, TYPE: Literal["item_select", "list_dir", "item_choice", "cur_item", "entry_scale"]):
        global __ITEM_CHOICE
        global _ClassNode__ENTRY_DATA


        if TYPE == "item_select":
            return _ClassNode__ITEM_SELECT[ID]
        elif TYPE == "cur_item":
            return _ClassNode_CURRENT[ID]
        elif TYPE == "list_dir":
            return os.listdir(_ClassConfig__DIR_FOLDER[ID])
        elif TYPE == "item_choice":
            return __ITEM_CHOICE
        elif TYPE == "entry_scale":
            return _ClassNode__ENTRY_SCALE.index[-1]

    def _ClassNode_count(num, TYPE=..., TYPE_VOL=...):
        global _ClassNode__ENTRY_SCALE

        if TYPE == "other":
            print(_ClassNode__ENTRY_SCALE)
            _ClassNode__ENTRY_SCALE.append(num)
        elif TYPE == "vol":
            if TYPE_VOL == "general":
                # OPERACIONES DE SUBIDA Y BAJADA DE VOLUMEN
                # ||NO TOCAR||
                from ctypes import cast, POINTER
                from comtypes import CLSCTX_ALL
                from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume, ISimpleAudioVolume
                global _Config_NAME_APP
                _ClassNode__ENTRY_SCALE[0] = num

                speak = AudioUtilities.GetSpeakers()
                ID = speak.Activate(
                    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
                vol = cast(ID, POINTER(IAudioEndpointVolume))

                ses = AudioUtilities.GetAllSessions()

                for i in ses:
                    vol = i._ctl.QueryInterface(ISimpleAudioVolume)
                    try:
                        if _Config_NAME_APP.find(".exe") == 1:
                            if i.Process and i.Process.name() == _Config_NAME_APP:
                                vol.SetMasterVolume((float(num)/100), None)
                        else:
                            if i.Process and i.Process.name() == (f"{_Config_NAME_APP}.exe"):
                                vol.SetMasterVolume((float(num)/100), None)
                    except:
                        print(f"||ERROR|| info = SCALE VOLUME, {_Config_NAME_APP} no existe, o esta mal escrito u otro, se recmienda re-crearlo con: \n \
                              WC.ClassConfig.set_name_pros()")

            elif TYPE_VOL == "music":
                # ESTA FUNCIÓN NO SOPORTA MAS DE UN CANAL, EN EL FUTURO DE ACTUALIZARA
                pass
            elif TYPE_VOL == "fvx":
                # ESTA FUNCIÓN NO ES SOPORTADA PARA MAS CANALES
                pass

###----------------------Invocación de objetos----------------------###
class WC:
    """
    Clase madre para todos los demas nodos y sub-procesos /funciones
    """

    def start_app(ID: int = 0):
        """
        Empieza el programa con una "ID" que se asume que es el menu y que ya fue creado con "set_window"
        """
        global _ID_WINDOW

        if ID != 1:
            _ID_WINDOW = ID

        while True:
            if CURRENT_WINDOW[0] == "EXIT":
                break
            else:
                _WC._Load_window()

        print("||APP END||")
        return

    class ClassNode:
        """
        Un conjunto de nodos pre-hechos y listos para usar o bien puede crear los suyos propios \n
        BUILD BY: @Z3R0_GT and @Gio334
        """

        def FuncScale(NODE_MASTER, START: int, END: int, TYPE: Literal["vol", "other", "default"], ORIENT: Literal["horizontal", "vertical"], TYPE_VOL: Literal["general", "music", "fvx"] = ..., START_WITH: float = 0.0, INTERVAL: int = 0, X=0, Y=0, HEIGH=0, WIDTH=0):
            """
            Crea una linea de rango "START" hasta "END" con un tipo de los ya establecidos con "default" 
            o puede usar uno propio con "other". \n

            para consultar el valor de su objeto, considere usar "ConsulturItem" con "entry_scale"
            """
            if TYPE == "default":
                if INTERVAL > 100:
                    INTERVAL = 10

                if START_WITH > 100.0 or START_WITH < 0.0:
                    START_WITH = 50.0

                node_scale = Scale(master=NODE_MASTER, from_=0.0, to=100.0, orient=ORIENT, tickinterval=INTERVAL,
                                   command=lambda e: _WC._ClassNode_count(num=e, TYPE="vol", TYPE_VOL=TYPE_VOL))
            elif INTERVAL != 0:
                node_scale = Scale(master=NODE_MASTER, from_=START, to=END, orient=ORIENT, tickinterval=INTERVAL,
                                   command=lambda e: _WC._ClassNode_count(num=e, TYPE=TYPE, TYPE_VOL=TYPE_VOL))
            else:
                node_scale = Scale(master=NODE_MASTER, from_=START, to=END, orient=ORIENT,
                                   command=lambda e: _WC._ClassNode_count(num=e, TYPE=TYPE, TYPE_VOL=TYPE_VOL))

            if START_WITH:
                node_scale.set(START_WITH)

            if TYPE == "default":
                node_scale.place(x=X, y=Y, height=75, width=600)
            elif WIDTH != 0 or HEIGH != 0:
                node_scale.place(x=X, y=Y, height=HEIGH, width=WIDTH)
            else:
                node_scale.place(x=X, y=Y)

            return node_scale

        def FuncButton(NODE_MASTER,
                       FONT: Font, 
                       TYPE: Literal["exit", "load_window", "save_archive", "test", "special_entry", "special_entry_data", "video"], 
                       VIDEO_INFO=["NODO_VIDEO", "IS_SPECIF_SEC:bool", "VALUE_TO_START", "NAME_ARCHIVE"], 
                       TYPE_VIDEO:Literal["play", "load", "frame"]=..., 
                       IDS: list = ..., 
                       TEXT: str = ..., 
                       DATA=..., 
                       X=0, Y=0, HEIGH=0, WIDTH=0):
            """
            elige un tipo de boton acorde la necesidad, siendo los siguientes casos: \n
            1) si quieres cargar "load_window" usa "IDS" como un arreglo y en la primera posicion coloca el "ID" de ventana que se va usar \n
            2) al usar "save", se requiere que "IDS" tenga dos posiciones, en la primera la ID sea de la ventana, y la segunda la carpeta (que se asume creada previamente con "set_dir")\n
            3) si usaras "exit", esto cierra y termina el programa \n
            4) en caso de usar "video", los valores a usar seran "TYPE_VIDEO", donde por medio de las llaves,
            enviaras toda la info necesaria, e IDS para especificar la ruta a cargar los videos.
            5) En caso de usar "special_entry" debera atender que los datos a guardar se haran por medio de una plantailla ya incluida aqui.
            6) en caso de usar "special_entry_data" debera de proveer usted la infromación a guardar en forma de diccionario y lo mismo que el anterior puntos.
            """
            node_button = ...
            vy_pass = ...
            
            if TYPE != "video":
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
            else:
                try:
                    node_button = Button(master=NODE_MASTER, text=TEXT, command=lambda: _WC._ClassNode_video_config(
                        NODE_VIDEO=VIDEO_INFO[0], TYPE=TYPE_VIDEO, IS_SPECIF_SEC=VIDEO_INFO[1], VALUE=VIDEO_INFO[2], ID_FOLDER=IDS[0], NAME=VIDEO_INFO[3]), font=FONT)

                    if HEIGH == 0 or WIDTH == 0:
                        node_button.place(x=X, y=Y)
                    else:
                        node_button.place(x=X, y=Y, height=HEIGH, width=WIDTH)

                    return node_button
                except:
                    print("||ERROR|| info= BUTTON_VIDEO, Si usted tiene este error, por favor, enviar captura del codigo donde \n \
                        se usa esta función con el tipo de video a GitHub: https://github.com/Z3R0GT/WC/issues, en breves le respondemos!")


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
            global _ClassNode__ENTRY_DATA

            _ClassNode__ENTRY_DATA = StringVar(master=NODE_MASTER)
            node_entry = Entry(master=NODE_MASTER, font=FONT,
                               width=WIDTH, textvariable=_ClassNode__ENTRY_DATA)
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
            crea una caja de lista con objetos
            """
            node_lis = Listbox(master=NODE_MASTER, font=FONT)
            node_lis.place(x=X, y=Y, height=HEIGH, width=WIDTH)

            return node_lis

        def FuncVideoPlayer(NODE_MASTER, SCALED: bool = False, HEIGH: int = ..., WIDTH: int = ..., X=0, Y=0, AUTO=False, ID:int=..., NAME_ARCHIVE:str=...):
            """
            Un nodo con la capacidad de reproducir de manera automatica apenas se inicie o por medio de un boton. \n
            en ese caso usar: "WC.ClassNode.FuncVideoPlayer".  \n
            Pero si quieres usar de manera auto, solo cambia el valor de auto a "True", envia un la ID del folder donde estan los videos, y el nombre del archivo (la extención también)
            """

            if SCALED:
                node_video = TkinterVideo(master=NODE_MASTER, scaled=SCALED)
            else:
                node_video = TkinterVideo(master=NODE_MASTER)

            if HEIGH != 0 or WIDTH != 0:
                node_video.place(x=X, y=Y, width=WIDTH, height=HEIGH)
            else:
                node_video.place(x=X, y=Y)

            if AUTO != False:
                for i in range(2):
                    if i != 1:
                        _WC._ClassNode_video_config(NODE_VIDEO=node_video, TYPE="play")
                    else:
                        _WC._ClassNode_video_config(NODE_VIDEO=node_video, TYPE="load", ID_FOLDER=ID, NAME=NAME_ARCHIVE)

            return node_video

    class ClassProcces:
        """
        Conjunto de datos creados para ser referenciados en multiples ocaciones del codigo y de real importancia. \n
        BUILD BY: @Z3R0_GT
        """

        def set_window(ID: int, TAG):
            """
            setea una nueva venta para automatizar el proceso con ID, envia una clase que contenga la funcion
            WindowMain() para poder ser reconozible a la libreria
            """
            CURRENT_WINDOW.append((ID, TAG))

        def ConsultItem(ID: int = ..., TYPE: Literal["item_select", "list_dir", "item_choice", "cur_item", "entry_scale"] = "item_choice"):
            """
            Retorna una serie de varibles que dependiendo de "TYPE" pueden ser un item de listbox,
            un elemento de OptionMenu, un item elegido especificamente, o la dirección de un archivo. \n

            el uso es libre, siempre retornara un String la mayoria de las veces
            """
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
            agrega un scroll a un "NODE_TEXT", siendo opcional 
            """
            return _WC._ClassProcces__add_scroll(NODE_TEXT=NODE_TEXT)

    class ClassSystem:
        """
        Clase con funciones que intervienen directamente en el sistema del usuario \n
        BUILD BY: @Z3R0_GT
        """

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
        """
        Serie de datos de configuración vitales en el funcionamiento de la libreria. \n
        BUILD BY: @Z3R0_GT and @Gio334
        """

        def set_name_pros(NAME: str):
            """
            Es importante anotar que el nombre de la app sea igual al proceso que aparezca en el 
            administrador de tareas porque sino no lograra encontrarlo, solo es necesario una vez
            """
            global _Config_NAME_APP

            _Config_NAME_APP = NAME

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
        """
        Clase creada solo para analizar y cotejar posiciones de diferentes variables. uso solo para el Dev (aqui se guarda todo). \n
        BUILD BY: @Gio334 
        """
        def DEVCONSULT():
            """
            Imprime una serie de datos provenientes de la libreria, (revisar en la consola)
            """
            __DEV__()
