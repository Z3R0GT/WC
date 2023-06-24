from WC import *
from tkinter import Tk

NAME = "Dragon Hunter"

CREDIT = {"Main": "Z3R0_GT",
          "Image": "ThemeFinland",
          "Programmer": "Z3R0_GT",
          "History": "Honting Fap, \n Un extraño con sombrero de copa",
          "Stats": "Gio"
          }
SECRET = "ESTE EASTER EGG ES PARA BARRETO ALCANTARA IMANOL, UN BUEN AMIGO :D"

X_GLOBAL = 900
Y_GLOBAL = 500

TRANSFORM = f"{str(X_GLOBAL)}x{str(Y_GLOBAL)}"

NAMEVERSION = "Alpha-Priv "
VERSION = "0.3"

PATH_INFO = f"Path #18 news (05/09/2023): \n- Lib version {VERSION_LIB} \n- Current app version: {NAMEVERSION} {VERSION} \n- App is already for test in case except by load of   archive .json \n- we ready up for you feed back "

#SETS
WC.Config.set_dir("app/assets/images")
WC.Config.set_dir("app/UserSaved")

ICON = WC.System.load_archive(ID_FOLDER=1, name_archive="ICO.ico", TYPE="IMA")

WC.System.load_archive(ID_FOLDER=1, name_archive="BG_CREATE_PERSON.jpg", TYPE="IMA")
WC.System.load_archive(ID_FOLDER=1, name_archive="BG_CREDITS.jpg", TYPE="IMA")




class WindowMenu:
    def WindowMain():
        Window = Tk()
        Window.title(NAME)
        Window.geometry(TRANSFORM)
        Window.resizable(width=False, height=False)
        Window.iconbitmap(ICON)
        WC.Procces.CenterWindow(WINDOW=Window, WIDTH=X_GLOBAL, HEIGH=Y_GLOBAL)
   
        f_default = WC.Procces.CreateFont()
        f_title = WC.Procces.CreateFont(SIZE=24, IS_BLACK=True, IS_RALL=True, FAMILY="Helvetica")

        lb_bg = WC.Nodes.FuncLabel(NODE_MASTER=Window, TYPE="image", ID_IMA_DIR=1, ReX=900, ReY=500)

        lb_title = WC.Nodes.FuncLabel(
            NODE_MASTER=Window, FONT=f_title, TYPE="normal", TEXT=f"{NAME}", X=350)
        lb_credits = WC.Nodes.FuncLabel(
            NODE_MASTER=Window, FONT=f_default, TYPE="normal", TEXT=f"Programmed by {CREDIT['Programmer']}", X=310, Y=465) 
        
        a_panel_news = WC.Nodes.FuncText(
            NODE_MASTER=Window, FONT=f_default, X=10, Y=290, HEIGH=200, WIDTH=290)
        
        WC.Procces.TextEdit(NODE_TEXT=a_panel_news, TEXT=PATH_INFO, TYPE="default")
        
        b_new_game = WC.Nodes.FuncButton(NODE_MASTER=Window, FONT=f_default, TEXT="Nuevo juego", TYPE="load_window", IDS=[4], X=350, Y=300)
        
        b_load = WC.Nodes.FuncButton(NODE_MASTER=Window, FONT=f_default, TEXT="Cargar juego", TYPE="load_window", IDS=[5], X=350, Y=330)

        b_credits = WC.Nodes.FuncButton(NODE_MASTER=Window, FONT=f_default, TEXT="Creditos", TYPE="load_window", IDS=[2], X=360, Y=360)

        b_quit = WC.Nodes.FuncButton(NODE_MASTER=Window, FONT=f_default, TYPE="exit", TEXT="Salir", X=370, Y=390)
        
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

        WC.Procces.CenterWindow(WINDOW=Window, WIDTH=X, HEIGH=Y)

        f_default = WC.Procces.CreateFont()
        f_title = WC.Procces.CreateFont(SIZE=24, IS_BLACK=True, IS_RALL=True, FAMILY="Helvetica")


        lb_bg = WC.Nodes.FuncLabel(NODE_MASTER=Window, TYPE="image", ID_IMA_DIR=2, ReX=X, ReY=Y)

        lb_credit = WC.Nodes.FuncLabel(NODE_MASTER=Window, FONT=f_title, TYPE="normal", TEXT="Creditos", X=135)

        lb_message = WC.Nodes.FuncText(NODE_MASTER=Window, FONT=f_default, X=100, Y=40)

        WC.Procces.TextEdit(NODE_TEXT=lb_message, TYPE="default", TEXT=f"{CREDIT}")

        Y= ((Y+150)/2)

        b_exit = WC.Nodes.FuncButton(NODE_MASTER=Window, FONT=f_default, TEXT="salir", TYPE="exit", X=(X/2), Y=Y)
        b_menu = WC.Nodes.FuncButton(NODE_MASTER=Window, FONT=f_default, TEXT="Menu", TYPE="load_window", IDS=[1], X=((X-100)/2), Y=Y)

        return Window.mainloop()

WC.Procces.set_window(1, WindowMenu)
WC.Procces.set_window(2, WindowCredit)

WC.start_app(ID=1)