"""
Window Controller (WC) a librelly for controll and create UI easy
with tkinter and PIL.

this lib is orient to build apps/games based on text, 
mode of saved archive JSON,
process automatly, and more!.

this lib was create by @Z3R0_GT (GitHub) in , if you find a bug
report to Z3R0_GT#3883
"""

### ----------------------Librerias----------------------###
import os
import json
import winsound

from Erno import *

from tkinter import Text, Label, Entry, StringVar, Scrollbar, Listbox, Button, OptionMenu, Scale, messagebox
from typing_extensions import Literal
from tkinter.font import Font
from PIL import Image, ImageTk

from tkVideoPlayer import TkinterVideo

### ----------------------Constantes----------------------###
VERSION_LIB = "6.0.1"
"""
Version de la libreria actual
"""
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
_ID_WINDOW = 1
"""
VARIABLE USADA PARA SABER CUAL ES LA VENTA A ABRIR CUANDO LA ANTERIOR SE CIERRE
||NO TOCAR||
"""
### ----------------------Constantes de funciones----------------------###

_ClassSystem_NAME_APP = ...

_WC_ITEM_CHOICE = ...

_ClassNode_ITEM_SELECT = []
_ClassNode_CURRENT = []

_ClassConfig__DIR_FOLDER = [os.path.dirname(__file__)]
_ClassConfig__VIDEO = []
_ClassConfig__SOUND = []
_ClassConfig__IMAGE = []

_ClassNode__ENTRY_DATA = ...
_ClassNode__IMA_TEMP = ...
_ClassNode__ENTRY_SCALE = [
    "MASTER", "MUSIC", "FVX", ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ...]
"""
Usa la tercera posición y mas para cualquier otro proposito
"""

_WC__TEMP = ...


def DEV():
    """
    Función que imprime los datos que actualmente estan guardados en la libreria
    """
    print(f"\n Version de la libreria: {VERSION_LIB} \
            \n Ventanas Cargadas: {CURRENT_WINDOW} \
            \n Nombre de la app: {_ClassSystem_NAME_APP} \
            \n Item escogido (interno): {_WC_ITEM_CHOICE} \
            \n Item escogido (FuncEntry): {_ClassNode_ITEM_SELECT} \
            \n Item escogido (FuncOptionMenu): {_ClassNode_CURRENT} \
            \n Item cambiante (FuncScale): {_ClassNode__ENTRY_SCALE} \
            \n Direcciones: {_ClassConfig__DIR_FOLDER} \
            \n Videos: {_ClassConfig__VIDEO} \
            \n Sonidos: {_ClassConfig__SOUND} \
            \n Imagenes cargadas: {_ClassConfig__IMAGE}")


class _WC:

    def _load_window():
        try:
            if _ID_WINDOW == 0:
                CURRENT_WINDOW[(_ID_WINDOW+1)][1].WindowMain()
            else:
                CURRENT_WINDOW[_ID_WINDOW][1].WindowMain()
        except:
            execute_error("LOAD_WINDOW")

    def _ClassSystem__save_archive(DATA: dict, ID_FOLDER: int, NAME_ARCHIVE: str, IS_ENCRIPT: bool):
        try:
            if IS_ENCRIPT:
                try:
                    ...
                except:
                    execute_error(TYPE="ENCRIPT", OPTIONS=[
                                  _ClassConfig__DIR_FOLDER[ID_FOLDER], NAME_ARCHIVE])
                    return
            else:
                with open(f"{_ClassConfig__DIR_FOLDER[ID_FOLDER]}/{NAME_ARCHIVE}.json", "w") as file:
                    file.write(DATA)
                    file.close()
                    execute_hecho("SAVE ARCHIVE")
        except:
            execute_error(TYPE="SAVE", OPTIONS=[
                          _ClassConfig__DIR_FOLDER[ID_FOLDER], NAME_ARCHIVE])
            return

    def _ClassSystem__load_archive(TYPE: Literal["JSON", "IMA", "VIDEO", "SOUND"], ID_FOLDER: int, NAME_ARCHIVE: str):
        if TYPE == "JSON":
            try:
                if NAME_ARCHIVE.find(".json") != -1:
                    with open(f"{_ClassConfig__DIR_FOLDER[ID_FOLDER]}/{NAME_ARCHIVE}") as file:
                        execute_hecho("LOAD JSON")
                        return json.load(file)
                else:
                    with open(f"{_ClassConfig__DIR_FOLDER[ID_FOLDER]}/{NAME_ARCHIVE}.json") as file:
                        execute_hecho("LOAD JSON")
                        return json.load(file)
            except:
                execute_error(TYPE="LOAD_JSON", OPTIONS=[
                              _ClassConfig__DIR_FOLDER[ID_FOLDER], NAME_ARCHIVE, TYPE])

        elif TYPE == "IMA":
            try:
                photo = os.path.join(
                    _ClassConfig__DIR_FOLDER[ID_FOLDER], NAME_ARCHIVE)
                _ClassConfig__IMAGE.append(photo)
                execute_hecho("LOAD IMA")
                return photo
            except:
                execute_error("LOAD_IMA", OPTIONS=[
                              _ClassConfig__DIR_FOLDER[ID_FOLDER], NAME_ARCHIVE, TYPE])
        elif TYPE == "VIDEO":
            try:
                _ClassConfig__VIDEO.append(os.path.join(
                    _ClassConfig__DIR_FOLDER[ID_FOLDER], NAME_ARCHIVE))
                a = _ClassConfig__VIDEO[-1]

                execute_hecho("LOAD_VIDEO")
                return a
            except Exception as e:
                execute_error("TEST", OPTIONS=[e])
        elif TYPE == "SOUND":
            try:
                _ClassConfig__SOUND.append(os.path.join(
                    _ClassConfig__DIR_FOLDER[ID_FOLDER], NAME_ARCHIVE))
                a = _ClassConfig__SOUND[-1]

                execute_hecho("LOAD_SOUND")
                return a
            except Exception as e:
                execute_error("TEST", OPTIONS=[e])

    def _ClassProcces__cur_item(ID: int, TYPE: Literal["ENTRYSCALE", "LISTDIR", "CURITEM", "CUR"]):

        if TYPE == "LISTDIR":
            return os.listdir(_ClassConfig__DIR_FOLDER[ID])
        elif TYPE == "ENTRYSCALE":
            return _ClassNode__ENTRY_SCALE[ID]
        elif TYPE == "CURITEM":
            return _ClassNode_ITEM_SELECT[ID]
        elif TYPE == "CUR":
            return _ClassNode_CURRENT[ID]

    def _ClassProcess__edit_text(NODE_TEXT: Text, TEXT: str, TYPE: Literal["default", "custom"], TYPE_RETURN: Literal["JSON", "IMA", "NORMAL"], ID_TO: int, LIST: list, IS_TEXT=True, IS_EMPY=True):

        def select(event, id, type):
            global _WC_ITEM_CHOICE

            sel = event.widget.curselection()
            if type == "JSON":
                if sel:
                    index = sel[0]
                    data = event.widget.get(index)
                    _WC_ITEM_CHOICE = _WC._ClassSystem__load_archive(
                        ID_FOLDER=id, NAME_ARCHIVE=data, TYPE="JSON")
            elif type == "IMA":
                if sel:
                    index = sel[0]
                    data = event.widget.get(index)
                    _WC_ITEM_CHOICE = _WC._ClassSystem__load_archive(
                        ID_FOLDER=id, NAME_ARCHIVE=data, TYPE="IMA")
            elif type == "NORMAL":
                if sel:
                    index = sel[0]
                    data = event.widget.get(index)
                    _WC_ITEM_CHOICE = data

        if IS_TEXT:
            if IS_EMPY == False:
                NODE_TEXT.delete("1.0", "end")

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
            NODE_TEXT.bind("<<LisboxSelect>>", lambda e: select(
                event=e, id=ID_TO, type=TYPE_RETURN))

            return NODE_TEXT

    def _ClassProcces__add_scroll(NODE_TEXT: Text, COORD: tuple(int, int) = ...):

        scroll = Scrollbar(master=NODE_TEXT, orient="vertical")
        scroll.config(command=NODE_TEXT.yview)

        NODE_TEXT["yscrollcommand"] = scroll.set

        scroll.grid(padx=660, ipady=178)
        return NODE_TEXT

    def _ClassProcces__set_trans(SET_NODE, ID_IMA: int, LEFT: int, UP: int, RIGHT: int, LOWER: int, IS_DEV=False):
        global _WC__TEMP

        coord = (LEFT, UP, RIGHT, LOWER)
        _ClassNode__IMA_TEMP = Image.open(f"{_ClassConfig__IMAGE[ID_IMA]}")

        reg = _ClassNode__IMA_TEMP.crop(coord)

        try:
            if IS_DEV == True:
                reg.show()
                reg.size

                if input("¿Quieres guardar la imagen?: Y/N \n>>") == "Y":
                    reg.save(
                        f"{_ClassConfig__DIR_FOLDER[0]}/temp/{_WC__TEMP+1}")
                    execute_hecho("SAVE IMA")
                else:
                    execute_hecho("NOT SAVE")
            else:
                dir_save = f"{_ClassConfig__DIR_FOLDER[0]}/temp/{_WC__TEMP+1}"
                reg.save(dir_save)
                SET_NODE.config(background=dir_save)

                execute_hecho("SET TRANSPARENT")
        except Exception as e:
            execute_error("TEST", OPTIONS=[e])

    def _ClassProcces_type_font(SIZE: int = 10, IS_BLACK: bool = False, IS_SLASH: bool = False, IS_RALL: bool = False, FAMILY: str = ""):
        type_font = ...

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

    def _ClassProcces_sound_play(int, ID_SONG: int = ...):
        try:
            song = winsound.PlaySound(
                _ClassConfig__SOUND[ID_SONG], winsound.SND_FILENAME)
            return song
        except Exception as e:
            execute_error("TEST", OPTIONS=[e])

    def _ClassNode_count(num, TYPE=..., TYPE_VOL=..., ID_VAR=...):
        global _ClassNode__ENTRY_SCALE

        if TYPE == "OTHER":
            while True:
                if (ID_VAR in range(0, 3)) != True:
                    _ClassNode__ENTRY_SCALE[ID_VAR] = num
                    break
                else:
                    ID_VAR += 1
        elif TYPE == "VOL":
            if TYPE_VOL == "GENERAL":
                # OPERACIONES DE SUBIDA Y BAJADA DE VOLUMEN
                # ||NO TOCAR||
                from ctypes import cast, POINTER
                from comtypes import CLSCTX_ALL
                from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume, ISimpleAudioVolume
                global _ClassSystem_NAME_APP
                _ClassNode__ENTRY_SCALE[0] = num

                speak = AudioUtilities.GetSpeakers()
                ID = speak.Activate(
                    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
                vol = cast(ID, POINTER(IAudioEndpointVolume))

                ses = AudioUtilities.GetAllSessions()

                for i in ses:
                    vol = i._ctl.QueryInterface(ISimpleAudioVolume)
                    try:
                        if _ClassSystem_NAME_APP.find(".exe") == 1:
                            if i.Process and i.Process.name() == _ClassSystem_NAME_APP:
                                vol.SetMasterVolume((float(num)/100), None)
                        else:
                            if i.Process and i.Process.name() == (f"{_ClassSystem_NAME_APP}.exe"):
                                vol.SetMasterVolume((float(num)/100), None)
                    except:
                        execute_error("SOUND", OPTIONS=[_ClassSystem_NAME_APP])

            elif TYPE_VOL == "music":
                # ESTA FUNCIÓN NO SOPORTA MAS DE UN CANAL, EN EL FUTURO DE ACTUALIZARA
                pass
            elif TYPE_VOL == "fvx":
                # ESTA FUNCIÓN NO ES SOPORTADA PARA MAS CANALES
                pass

    def _ClassNode_place(NODE_GENERAL, COORD: tuple):

        X, Y, HEIGH, WIDTH = COORD

        if HEIGH != 0 or WIDTH != 0:
            NODE_GENERAL.place(x=X, y=Y, width=WIDTH, height=HEIGH)
        else:
            NODE_GENERAL.place(x=X, y=Y)

    def _ClassNode_video_config(NODE_VIDEO: TkinterVideo, TYPE: Literal["play", "load", "frame"], ID_VIDEO: int = ..., IS_SPECIF_SEC: bool = True, VALUE: int = ...):
        try:
            if TYPE == "play":
                if NODE_VIDEO.is_paused():
                    NODE_VIDEO.play()
                else:
                    NODE_VIDEO.pause()
            elif TYPE == "load":

                NODE_VIDEO.load(_ClassConfig__VIDEO[ID_VIDEO])

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
        except Exception as e:
            execute_error("TEST", OPTIONS=[e])


class WC:
    """
    Clase madre para todos los demas nodos y sub-procesos /funciones
    """

    def StartApp(ID: int = 0):
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
                _WC._load_window()

        print("||APP END||")
        return

    class ClassNode:
        """
        Un conjunto de nodos pre-hechos y listos para usar o bien puede crear los suyos propios \n
        BUILD BY: @Z3R0_GT and @Gio334
        """

        def FuncScale(NODE_MASTER, START: int, END: int,
                      START_WITH: float,
                      ID_VAR: int,
                      INTERVAL: int,
                      TYPE: Literal["VOL_CUSTOM", "OTHER_CUSTOM", "OTHER_DEFAULT", "VOL_DEFAULT"],
                      TYPE_VOL: Literal["GENERAL", "MUSIC", "FVX"],
                      ORIENT: Literal["HORIZONTAL", "VERTICAL"] = "HORIZONTAL",
                      COORD: tuple[int, int, int, int] = ...):
            """
            Crea una linea de rango "START" hasta "END" con un tipo de los ya establecidos con "default" 
            o puede usar uno propio con "other". \n

            para consultar el valor de su objeto, considere usar "ConsulturItem" con "entry_scale"
            """
            try:
                X, Y = COORD

                if TYPE == "VOL_DEFAULT" or TYPE == "OTHER_DEFAULT":
                    if INTERVAL > 100:
                        INTERVAL = 5

                    if START_WITH > float(100) or START_WITH < float(0):
                        START_WITH = float(50)

                    if TYPE == "VOL_DEFAULT":
                        node_scale = Scale(master=NODE_MASTER, from_=0.0, to=100, orient=ORIENT, tickinterval=INTERVAL,
                                           command=lambda e: _WC._ClassNode_count(num=e, TYPE="VOL", TYPE_VOL=TYPE_VOL))
                    else:
                        node_scale = Scale(master=NODE_MASTER, from_=0.0, to=100, orient=ORIENT, tickinterval=INTERVAL,
                                           command=lambda e: _WC._ClassNode_count(num=e, TYPE="OTHER"))
                elif TYPE == "VOL_CUSTOM":
                    node_scale = Scale(master=NODE_MASTER, from_=START, to=END, orient=ORIENT, tickinterval=INTERVAL,
                                       command=lambda e: _WC._ClassNode_count(num=e, TYPE="VOL", TYPE_VOL=TYPE_VOL))
                elif TYPE == "OTHER":
                    node_scale = Scale(master=NODE_MASTER, from_=START, to=END, orient=ORIENT, tickinterval=INTERVAL,
                                       command=lambda e: _WC._ClassNode_count(num=e, TYPE="OTHER", ID_VAR=ID_VAR))

                if START_WITH:
                    node_scale.set(START_WITH)

                if TYPE == "VOL_DEFAULT" or TYPE == "OTHER_DEFAULT":
                    node_scale.place(x=X, y=Y, height=75, width=550)
                else:
                    _WC._ClassNode_place(NODE_GENERAL=node_scale, COORD=COORD)

                return node_scale
            except Exception as e:
                execute_error(TYPE="TEST", OPTIONS=[e])

        def FuncText(NODE_MASTER,
                     FONT: Font,
                     CAN_COPY=False,
                     COORDS: tuple[int, int, int, int] = ...):
            """
            crea una nodo de texto, especifica con "CAN_COPY" si quieres que el usuario pueda o no
            copiar el contenido de este
            """
            try:
                def a_copy(event):
                    if (12 == event.state and event.keysym == 'c'):
                        return
                    else:
                        return "break"

                node_text = Text(master=NODE_MASTER, font=FONT)
                if CAN_COPY != True:
                    node_text.bind("<Key>", lambda e: a_copy(e))

                _WC._ClassNode_place(NODE_GENERAL=node_text, COORD=COORDS)

                return node_text
            except Exception as e:
                execute_error(TYPE="TEST", OPTIONS=[e])

        def FuncLabel(NODE_MASTER,
                      TYPE: Literal["NORMAL", "IMAGE"] = "NORMAL",
                      ID_IMA: int = ...,
                      FONT: Font = ...,
                      TEXT: str = "",
                      COORDS: tuple[int, int, int, int] = ...,
                      COORD_RES: tuple = (0, 0)):
            """
            Crea una etiqueta(label) con un tipo para diferenciar si es imagen o un texto, caso que sea imagen usar: "ID_IMA_DIR" (que se asuma ya creado con "load_archive") y con "ReX" y "ReY" 
            para redimensionar la image, caso contrario, solo unar "TEXT" para crear una imagen normal.
            """
            try:

                if TYPE == "NORMAL":
                    node_label = Label(master=NODE_MASTER,
                                       font=FONT, text=TEXT)
                    _WC._ClassNode_place(NODE_GENERAL=node_label, COORD=COORDS)

                    return node_label
                elif TYPE == "IMAGE":
                    try:
                        ReX, ReY = COORD_RES
                    except Exception as e:
                        execute_error("TEST", OPTIONS=[e])

                    try:
                        ima = Image.open(f"{_ClassConfig__IMAGE[ID_IMA]}")

                        if ReX != 0 or ReY != 0:
                            ima_short = ima.resize((ReX, ReY))
                            _ClassNode__IMA_TEMP = ImageTk.PhotoImage(
                                ima_short)
                        else:
                            _ClassNode__IMA_TEMP = ImageTk.PhotoImage(ima)

                        node_label = Label(
                            master=NODE_MASTER, image=_ClassNode__IMA_TEMP)
                        _WC._ClassNode_place(
                            NODE_GENERAL=node_label, COORD=COORDS)

                        return node_label

                    except Exception as e:
                        execute_error("TEST", OPTIONS=[e])

            except Exception as e:
                execute_error("TEST", OPTIONS=[e])

        def FuncEntry(NODE_MASTER,
                      FONT: Font,
                      COORDS: tuple[int, int, int]):
            """
            crea un espacio en blanco para ingresar texto, este se puede recuperar con ENTRY_DATA.get()
            """
            try:
                _ClassNode__ENTRY_DATA = StringVar(master=NODE_MASTER)
                node_entry = Entry(master=NODE_MASTER, font=FONT,
                                   width=COORDS[2], textvariable=_ClassNode__ENTRY_DATA)
                _WC._ClassNode_place(NODE_GENERAL=node_entry, COORD=COORDS)

                return node_entry
            except Exception as e:
                execute_error("TEST", OPTIONS=[e])

        def FuncOptionMenu(NODE_MASTER,
                           OPTION_LIST: list,
                           FONT: Font,
                           COORD: tuple[int, int, int, int]):
            """
            crea un menu de opcion (se presenta como un boton)
            """
            try:
                LIST = StringVar(NODE_MASTER)
                LIST.set(OPTION_LIST[0])

                def sel_save(*args):
                    _ClassNode_CURRENT.append(f"{LIST.get()}")

                    for i in _ClassNode_CURRENT:
                        if i not in _ClassNode_ITEM_SELECT:
                            _ClassNode_ITEM_SELECT.append(i)

                node_menu = OptionMenu(NODE_MASTER, LIST, *OPTION_LIST)
                node_menu.config(font=FONT)
                _WC._ClassNode_place(node_menu, COORD=COORD)

                LIST.trace("w", sel_save)
                return node_menu
            except Exception as e:
                execute_error("TEST", OPTIONS=[e])

        def FuncListBox(NODE_MASTER, FONT: Font, COORD: tuple[int, int, int, int]):
            """
            crea una caja de lista con objetos
            """
            try:
                node_list = Listbox(master=NODE_MASTER, font=FONT)
                _WC._ClassNode_place(NODE_GENERAL=node_list, COORD=COORD)

                return node_list
            except Exception as e:
                execute_error("TEST", OPTIONS=[e])

        def FuncVideo(NODE_MASTER,
                      SCALED: bool = False,
                      COORD: tuple[int, int, int, int] = ...,
                      AUTO_PLAY: bool = False,
                      ID_VIDEO: int = ...):
            """
            Un nodo con la capacidad de reproducir de manera automatica apenas se inicie o por medio de un boton. \n
            en ese caso usar: "WC.ClassNode.FuncVideoPlayer".  \n
            Pero si quieres usar de manera auto, solo cambia el valor de auto a "True", envia un la ID del folder donde estan los videos, y el nombre del archivo (la extención también)
            """
            try:
                if SCALED != True:
                    node_video = TkinterVideo(master=NODE_MASTER)
                else:
                    node_video = TkinterVideo(
                        master=NODE_MASTER, scaled=SCALED)

                _WC._ClassNode_place(node_video, COORD)

                if AUTO_PLAY != False:
                    for i in range(2):
                        if i != 1:
                            _WC._ClassNode_video_config(
                                NODE_VIDEO=node_video, TYPE="play")
                        else:
                            _WC._ClassNode_video_config(
                                NODE_VIDEO=node_video, TYPE="load", ID_VIDEO=ID_VIDEO)

                return node_video
            except Exception as e:
                execute_error("TEST", OPTIONS=[e])

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
            try:
                CURRENT_WINDOW.append((ID, TAG))
            except Exception as e:
                execute_error("TEST", OPTIONS=[e])

        def consult_item(ID: int = ..., TYPE: Literal["LISTDIR", "ENTRYSCALE", "CURITEM", "CUR"] = ...):
            """
            Retorna una serie de varibles que dependiendo de "TYPE" pueden ser un item de listbox,
            un elemento de OptionMenu, un item elegido especificamente, o la dirección de un archivo. \n

            el uso es libre, siempre retornara un String la mayoria de las veces
            """
            return _WC._ClassProcces__cur_item(ID=ID, TYPE=TYPE)

        def sound_play(ID_SONG: int = ...):
            """
            Crea una instancia de musica/sonido para reproducirse, toda canción creada, es guardada
            en ID, si quiere volver a cargarla, solo tiene que usar "ID"+ "is_load" para ejecutarla
            """
            return _WC._ClassProcces_sound_play(ID_SONG=ID_SONG)

        def text_edit(NODE_TEXT: Text,
                      TYPE: Literal["default", "custom"],
                      TYPE_RETURN: Literal["JSON", "IMA", "NORMAL"],
                      TEXT,
                      ID_TO: int,
                      LIST: list,
                      IS_TEXT: bool = True,
                      IS_EMPY: bool = True):
            """
            edita un nodo de texto, elige un tipo para el saber la conexion a trabajar, setea el texto y especifica si es texto lo qie se trabaja o si esta limpio,
            es opcional si incluir una lista o no
            """
            return _WC._ClassProcess__edit_text(NODE_TEXT=NODE_TEXT, TEXT=TEXT, TYPE=TYPE, TYPE_RETURN=TYPE_RETURN, ID_TO=ID_TO, LIST=LIST, IS_TEXT=IS_TEXT, IS_EMPY=IS_EMPY)

        def create_font(SIZE=10,
                        IS_BLACK=False,
                        IS_SLASH=False,
                        IS_RALL=False,
                        FAMILY=""):
            """
            crea una fuente de un tamaño, aplicale condiciones de: \n
            - es negra: IS_BLACK \n
            - esta a un lado: IS_SLASH \n
            - tiene un ralla: IS_RALL \n

            y especifica el tipo de familia en el arbol
            """
            return _WC._ClassProcces_type_font(SIZE=SIZE, IS_BLACK=IS_BLACK, IS_RALL=IS_RALL, IS_SLASH=IS_SLASH, FAMILY=FAMILY)

        def center_window(WINDOW,
                          COORD: tuple(int, int)):
            """
            Retorna la venta indicada en el centro de la pantalla con sus medida exactas
            """
            WIDTH, HEIGH = COORD
            try:

                widthTot = WINDOW.winfo_screenwidth()
                highTot = WINDOW.winfo_screenheight()

                pos_w = round(widthTot/2-WIDTH/2)
                pos_h = round(highTot/2-HEIGH/2)

                return WINDOW.geometry(str(WIDTH)+"x"+str(HEIGH)+"+"+str(pos_w)+"+"+str(pos_h))
            except:
                execute_error("CENTER_WINDOW", OPTIONS=[WIDTH, HEIGH])

        def add_scroll(NODE_TEXT: Text):
            """
            Agrega un scroll a un "NODE_TEXT", siendo opcional 
            """
            if type(NODE_TEXT) != Text:
                execute_error("DIFFERENT", OPTIONS=["Text"])
            else:
                return _WC._ClassProcces__add_scroll(NODE_TEXT=NODE_TEXT)

    class ClassSytem:
        """
        Clase con funciones que intervienen directamente en el sistema del usuario, y en el funcionamiento correcto de la libreria. \n
        BUILD BY: @Z3R0_GT, @Gio334
        """

        def save_archive(ID_FOLDER: int,
                         NAME_ARCHHIVE: str,
                         DATA: dict,
                         IS_ENCRIPT: bool = False):
            """
            Guarda archivos en un ID ya seteado (vease en "set_dir"), con un nombre, enviele diccionario con data
            que se convierte automaticamente en un JSON, también es soportado el encriptamiento con: 
            ###----INCLUIR TIPO DE ENCRIPT ----###
            """
            _WC._ClassSystem__save_archive(
                DATA=DATA, ID_FOLDER=ID_FOLDER, IS_ENCRIPT=IS_ENCRIPT, NAME_ARCHIVE=NAME_ARCHHIVE)

        def load_archive(TYPE: Literal["JSON", "IMA", "VIDEO", "SOUND"],
                         ID_FOLDER: int,
                         NAME_ARCHIVE: str):
            """
            Carga un archivo con un ID segun lo hallas seteado (vease en "set_dir"), nombre al archivo
            y enviele un tipo.\n

            Nota: recuerde usar para "VIDEO" o "SOUND" incluir la extensión del archivo 
            """
            return _WC._ClassSystem__load_archive(TYPE=TYPE, ID_FOLDER=ID_FOLDER, NAME_ARCHIVE=NAME_ARCHIVE)

        def set_name_pros(NAME: str):
            """
            Es importante anotar que el nombre de la app sea igual al proceso que aparezca en el 
            administrador de tareas porque sino no lograra encontrarlo, solo es necesario una vez
            """
            _ClassSystem_NAME_APP = NAME

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
            except:
                execute_error("SET_DIR", [DIR])
