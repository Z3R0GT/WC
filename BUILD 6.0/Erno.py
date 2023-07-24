"""
Liberia usada para ejecutar error propios de WC, creado por @Z3R0_GT y @Gio334
(puede encontrar los perfiles en GitHub)
"""

from tkinter import messagebox
from typing_extensions import Literal

_execute_error__INFO = f"por favor, proceda con alguna de los siguientes alternativas. \n \
    - Coloquese en contacto con el Dev (en caso de descargar el software). \n \
    - Reinstale el Sofware o reestablesca las carpetas/archivos que alla eliminado. \n \
    - Declare correctamente las variables correspondientes al tipo de error. \n \
    - Abra el repositorio WC y abra un issue con el tag Bug/Error, llene la plantilla con los datos correspondientes."
"""
Usado para en caso de un error, se proceda a imprimir un texto en una ventana
se recomienda no cambiarlo.
"""
_execute_error__TEMP = []

def execute_error(TYPE:Literal["ENCRIPT", "SAVE", "LOAD_JSON", "TEST", "LOAD_IMA",
                         "LOAD_WINDOW", "VIDEO", "SOUND", 
                         "ITEM", "COUNT", "SOUND_IMPORT", 
                         "SET_IMA", "SET_WINDOW", "CENTER_WINDOW", 
                         "SET_DIR", "DIFFERENT"], OPTIONS=[]):
    
    t = f"Error {TYPE}"

    try:
        if TYPE == "ENCRIPT":
            messagebox.showerror(f"{t}", "Un error interno al encriptar ocurrio, informar al repositorio WC, abre un Issue con el tag Bug/Error")
            print(f"\n ||ERROR|| info= ID FOLDER: {OPTIONS[0]}; NAME ARCHIVE: {OPTIONS[1]}, #001\n")

        elif TYPE == "SAVE":
            messagebox.showerror(f"{t}", f"la carpeta especificada no existe o fue movida ({OPTIONS[0]}), {_execute_error__INFO}")
            print(f"\n ||ERROR|| info= ID FOLDER: {OPTIONS[0]}; NAME ARCHIVE: {OPTIONS[1]}, #002\n")

        elif TYPE == "LOAD_JSON":
            messagebox.showerror(f"{t}", f"El archivo {OPTIONS[1]} no fue encontrado, {_execute_error__INFO}")
            print(f"\n ||ERROR|| info= ID FOLDER: {OPTIONS[0]}, LIST ERROR: {OPTIONS[2]}, #003\n")

        elif TYPE == "LOAD_IMA":
            messagebox.showerror(f"{t}", f"el archivo {OPTIONS[1]} no fue encontrado o la extensión no coincide, {_execute_error__INFO}")
            print(f"\n ||ERROR|| info= ID FOLDER: {OPTIONS[0]}, LIST ERROR: {OPTIONS[2]}, #004 \n")

        elif TYPE == "LOAD_WINDOW":
            messagebox.showerror(f"{t}", f"Un error interno ocurrio, consulte con la consola (caso de ser dev) o {_execute_error__INFO}")
            print(f"||CRITIC ERROR|| info= Parece que la ventana ingesada no cuenta con la función -WindowMain- o la venta que se tiene actualmente  \
                no coincide, \n por favor, registre correctamente su codigo, caso de no encontrar solución dirijase al repositorio WC,\n abra un  \
                issue con el tag Bug/Error, #005 ")
            
        elif TYPE == "CENTER_WINDOW":
            messagebox.showerror(f"{t}", f"Parece que la pantalla fue incorrectamente actualizada, asegurese que el tamaño sea correcto o {_execute_error__INFO}")
            if type(OPTIONS[0]) == int and type(OPTIONS[1]) == int and type(OPTIONS[2]) == int and type(OPTIONS[3]) == int:
                print(f"||ERROR|| info= Error desconocido, tiene que verificar la sintaxis, #006")
            else:
                for i in range(len(OPTIONS)):
                    if type(OPTIONS[i]) == str:
                        _execute_error__TEMP.append(f"Dato enviado: {OPTIONS[i]}")
                        _execute_error__TEMP.append(f"Positión: {i}")
                print(f"||ERROR|| info= Parece que los datos {_execute_error__TEMP} enviados a -CenterWindow- no coinciden con un -int- #007")

        elif TYPE == "SET_DIR":
            messagebox.showerror(f"{t}", f"La dirección especificada por comando/ingresado no coincide, fue movido o no existe, \
                                revisa la sintanxis o {_execute_error__INFO}")
            print(f"||ERROR|| info= DIR: {OPTIONS[0]}, #008")
        elif TYPE == "TEST":
            messagebox.showerror(f"{t}", f"Este bug aun no tiene causa ni motivo (función experimental), se recomienda ir al repositorio WC, \
                                abrir un issue y resportar este con el tag Bug/Error y subir una captura de la consola")
            print(f"||ERROR|| info= EXCEPTION: \n {repr(OPTIONS[0])}, #009")
        elif TYPE == "SET_IMA":
            messagebox.showerror(f"{t}", f"La imagen {OPTIONS[0]} no fue encontrada o fue movida de directorio, {_execute_error__INFO}")
            print(f"||ERROR|| info= IMA: {OPTIONS[0]}, GENERAL: {OPTIONS[1]}, ID: {OPTIONS[2]}, #010")
        elif TYPE == "SET_WINDOW":
            messagebox.showerror(f"{t}", f"El ID o la función enviada, no procede correctamente, revise la sintaxis o {_execute_error__INFO}")
            print(f"||ERROR|| info= ID: {OPTIONS[0]}, TAG/FUNC: {OPTIONS[1]}, #011")
        elif TYPE == "SOUND":
            messagebox.showerror(f"{t}", f"El proceso ({OPTIONS[0]}) puede estar incorrecto, asegurese de escribir bien: WC.ClassConfig.set_name_pros()")
            print(f"||ERROR|| info= SCALE VOLUME, NAME: {OPTIONS[0]}, #012")        
        elif TYPE == "DIFFERENT":
            messagebox.showerror(f"{t}", f"el nodo no es un {OPTIONS[0]}")
            print(f"||ERROR|| info= DIFFERENT TYPE, NODE: {OPTIONS[0]}, #013")


    except:
        messagebox.showerror("Error Erno", "Un bug desconocido ocurrio en -Erno- se recomienda reinstalar el software o reportarlo al repositorio WC")
        print(f"||ERNO ERROR|| info= TYPE: {TYPE}, OPTION: {OPTIONS}")

def execute_hecho(OPTION:str):
    print(f"HECHO {OPTION} \n")





