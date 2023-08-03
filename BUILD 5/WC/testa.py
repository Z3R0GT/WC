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

class WindowCredit:
    def WindowMain():
        X = 400
        Y = 300

        Window = Tk()
        Window.title(NAME)
        Window.geometry(f"{str(X)}x{str(Y)}")
        Window.resizable(width=False, height=False)
        Window.iconbitmap(ICON)

        WC.ClassProcces.CenterWindow(WINDOW=Window, WIDTH=X, HEIGH=Y)

        f_default = WC.ClassProcces.CreateFont()
        f_title = WC.ClassProcces.CreateFont(SIZE=24, IS_BLACK=True, IS_RALL=True, FAMILY="Helvetica")


        lb_bg = WC.ClassNode.FuncLabel(NODE_MASTER=Window, TYPE="image", ID_IMA_DIR=1, ReX=X, ReY=Y)

        lb_credit = WC.ClassNode.FuncLabel(NODE_MASTER=Window, TYPE="normal", FONT=f_title, TEXT="Creditos", X=135)

        lb_message = WC.ClassNode.FuncLabel(NODE_MASTER=Window, TYPE="normal", FONT=f_default, TEXT=(f"Director: {CREDIT['Main']} \n\n"
                                                         f"Programador: {CREDIT['Programmer']} \n\n"
                                                         f"Imagenes: {CREDIT['Image']} \n\n"
                                                         f"Estadistica: {CREDIT['Stats']} \n\n"
                                                         f"Historia: {CREDIT['History']}"
                                                         ), X=100, Y=40)
        Y= ((Y+150)/2)

        b_exit = WC.ClassNode.FuncButton(NODE_MASTER=Window, FONT=f_default, TEXT="salir", TYPE="exit", X=(X/2), Y=Y)
        b_menu = WC.ClassNode.FuncButton(NODE_MASTER=Window, FONT=f_default, TEXT="Menu", TYPE="load_window", IDS=[1], X=((X-100)/2), Y=Y)

        return Window.mainloop()

class WindowNewGame:
    def WindowMain():
        Window = Tk()
        Window.title(NAME)
        Window.geometry("250x500")
        Window.resizable(width=False, height=False)
        Window.iconbitmap(ICON)
        WC.ClassProcces.CenterWindow(WINDOW=Window, WIDTH=250, HEIGH=Y_GLOBAL)

        lb_bg = WC.ClassNode.FuncLabel(NODE_MASTER=Window, TYPE="image", ID_IMA_DIR=3, ReX=250, ReY=500)

        f_title = WC.ClassProcces.CreateFont(SIZE=23, IS_BLACK=True, IS_RALL=True, FAMILY="Helvetica")
        f_default = WC.ClassProcces.CreateFont()
        f_min_text = WC.ClassProcces.CreateFont(SIZE=8, FAMILY="Helvetica")

        lb_credits = WC.ClassNode.FuncLabel(NODE_MASTER=Window, FONT=f_default, TEXT="credits_label", Y=470)

        lb_creation_person = WC.ClassNode.FuncLabel(
            NODE_MASTER=Window, FONT=f_title, TEXT="Crear personaje", Y=30)

        lb_tag_name = WC.ClassNode.FuncLabel(
            NODE_MASTER=Window, FONT=f_min_text, TEXT="Nombre de personaje", Y=130)

        lb_tag_type = WC.ClassNode.FuncLabel(
            NODE_MASTER=Window, FONT=f_min_text, TEXT="¿Quieres prota o invitado?", Y=180)

        lb_tag_rase = WC.ClassNode.FuncLabel(
            NODE_MASTER=Window, FONT=f_min_text, TEXT="¿Que raza eres?", Y=230)

        e_name = WC.ClassNode.FuncEntry(NODE_MASTER=Window, FONT=f_default, Y=155, WIDTH=30)

        b_menu = WC.ClassNode.FuncButton(NODE_MASTER=Window, FONT=f_default, TEXT="Menu", TYPE="load_window", IDS=[1], Y=3.4)

        b_login = WC.ClassNode.FuncButton(NODE_MASTER=Window, FONT=f_default, TYPE="load_window", TEXT="Cargar Partida", IDS=[5], X=195, Y=3.4)

        op_type = WC.ClassNode.FuncOptionMenu(NODE_MASTER=Window, OPTION_LIST=TYPE, FONT=f_default, X=5, Y=205, HIGH=23, WIDTH=120)

        op_raze = WC.ClassNode.FuncOptionMenu(NODE_MASTER=Window, OPTION_LIST=RAZE, FONT=f_default, X=5, Y=253, HIGH=23, WIDTH=80)

        b_save = WC.ClassNode.FuncButton(NODE_MASTER=Window, FONT=f_default, TYPE="special_entry", TEXT="Guardar", IDS=[3,1], DATA=[Lead], X=100, Y=400)
        


        return Window.mainloop()

class WindowGame:
    def WindowMain():
        Window = Tk()
        Window.title(NAME)
        Window.geometry(TRANSFORM)
        Window.resizable(width=False, height=False)
        Window.iconbitmap(ICON)
        WC.ClassProcces.CenterWindow(WINDOW=Window, WIDTH=X_GLOBAL, HEIGH=Y_GLOBAL)

        f_title = WC.ClassProcces.CreateFont(SIZE=23, IS_BLACK=True, IS_RALL=True, FAMILY="Helvetica")
        f_default = WC.ClassProcces.CreateFont()
        f_min_text = WC.ClassProcces.CreateFont(SIZE=8, FAMILY="Helvetica")

        arch = WC.ClassProcces.ConsultItem(TYPE="item_choice")
        temp_date = Lead.SearchDate(Vol=arch["HistoryAdvanced"][0],Cap=arch["HistoryAdvanced"][1], Scene=arch["HistoryAdvanced"][2], Dession=arch["HistoryAdvanced"][3])

        lb_credit = WC.ClassNode.FuncLabel(NODE_MASTER=Window, TYPE="normal", FONT=f_default, TEXT=f"Creditos a {CREDIT['History']}", X=20, Y=450)

        lb_vol = WC.ClassNode.FuncLabel(NODE_MASTER=Window, TYPE="normal", TEXT=f"VOLUMEN: {temp_date[0]}", X=200)

        lb_cap = WC.ClassNode.FuncLabel(NODE_MASTER=Window, TYPE="normal", TEXT=f"VOLUMEN: {temp_date[1]}", X=500)

        b_exit = WC.ClassNode.FuncButton(NODE_MASTER=Window, FONT=f_default, TYPE="exit", TEXT="Salir", X=123, Y=1)

        b_menu = WC.ClassNode.FuncButton(NODE_MASTER=Window, FONT=f_default, TYPE="load_window", IDS=[1], TEXT="Menú", X=10, Y=1)

        for i in range(5):
            b_des = WC.ClassNode.FuncButton(NODE_MASTER=Window, FONT=f_default, TYPE="test", TEXT=f"des_{i}", X=(290+i*70), Y=430)

        a_text = WC.ClassNode.FuncText(NODE_MASTER=Window, FONT=f_default, X=200, Y=28, HEIGH=400, WIDTH=680)
        WC.ClassProcces.TextEdit(NODE_TEXT=a_text, TEXT=arch["Name"], TYPE="default")

        temp_text = f"Estadisticas: \n  Nombre: " + str(
            arch["Name"]) + "\n\n Atributos: \n  Suerte: " + str(
            arch["Stats"][0]) + "\n  Fuerza: " + str(
            arch["Stats"][1]) + "\n  Velocidad: " + str(
            arch["Stats"][2]) + "\n  Influencia: " + str(
            arch["HistoryAdvanced"][3])

        a_info = WC.ClassNode.FuncText(NODE_MASTER=Window, FONT=f_min_text, X=10, Y=28, WIDTH=150, HEIGH=400)
        WC.ClassProcces.TextEdit(NODE_TEXT=a_info, TEXT=temp_text, TYPE="default")

        return Window.mainloop()

class WindowLoad:
    def WindowMain():
        Window = Tk()
        Window.title(NAME)
        Window.geometry(TRANSFORM)
        Window.resizable(width=False, height=False)
        Window.iconbitmap(ICON)
        WC.ClassProcces.CenterWindow(WINDOW=Window, WIDTH=X_GLOBAL, HEIGH=Y_GLOBAL)

        last_name = max(SAVE_DATA)

        arch = WC.ClassSystem.load_archive(ID_FOLDER=1, TYPE="JSON", name_archive=last_name)

        temp_bool = ".json"
        temp_name = "".join(x for x in last_name if x not in temp_bool)

        temp_text = f"Ultimo archivo: {temp_name}" + "\n Volumen:" + str(arch["HistoryAdvanced"][0]) + "\n Capitulo:" + str(
            arch["HistoryAdvanced"][1]) + "\n Esceneario:" + str(
            arch["HistoryAdvanced"][2]) + "\n\n Nombre de personaje: \n" + str(arch["Name"])
        
        f_default = WC.ClassProcces.CreateFont()

        lb_bg = WC.ClassNode.FuncLabel(NODE_MASTER=Window, FONT=f_default, TYPE="image", ID_IMA_DIR=2, ReX=X_GLOBAL, ReY=Y_GLOBAL)
        f_min_text = WC.ClassProcces.CreateFont(SIZE=8, FAMILY="Helvetica")

        lb_version = WC.ClassNode.FuncLabel(NODE_MASTER=Window, FONT=f_default, TYPE="normal", TEXT=f"{NAMEVERSION, VERSION}", X=475, Y=715)

        a_game_panel = WC.ClassNode.FuncText(NODE_MASTER=Window, FONT=f_default, X=10, Y=28, HEIGH=400, WIDTH=150)
        WC.ClassProcces.TextEdit(NODE_TEXT=a_game_panel, TYPE="default", TEXT=temp_text)

        a_select_date = WC.ClassNode.FuncListBox(NODE_MASTER=Window, FONT=f_default, X=200, Y=28, HEIGH=400, WIDTH=680)

        for i in range(len(SAVE_DATA)):
            WC.ClassProcces.TextEdit(NODE_TEXT=a_select_date, TYPE="default", LIST=SAVE_DATA[i], IS_TEXT=False)
            WC.ClassProcces.Addscroll(NODE_TEXT=a_select_date)
        
        b_exit = WC.ClassNode.FuncButton(NODE_MASTER=Window, FONT=f_default, TEXT="Salir", TYPE="exit", X=123, Y=1)

        b_menu = WC.ClassNode.FuncButton(NODE_MASTER=Window,FONT=f_default, TYPE="load_window", IDS=[1], TEXT="Menú", X=10, Y=1)

        b_new_game = WC.ClassNode.FuncButton(NODE_MASTER=Window, FONT=f_default,TEXT="Nuevo juego", TYPE="load_window", IDS=[4], X=200, Y=360)

        b_load = WC.ClassNode.FuncButton(NODE_MASTER=Window, FONT=f_default, TEXT="Cargar", TYPE="load_window", IDS=[3], X=200, Y=400)
        return Window.mainloop()

WC.ClassProcces.set_window(1, WindowMenu)
WC.ClassProcces.set_window(2, WindowCredit)
WC.ClassProcces.set_window(3, WindowGame)
WC.ClassProcces.set_window(4, WindowNewGame)
WC.ClassProcces.set_window(5, WindowLoad)

WC.start_app(ID=1)