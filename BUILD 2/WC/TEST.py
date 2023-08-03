from tkinter import Tk
from WC import *

from app.assets.dataBase.Lead import *

## ---------Constant of app---------##
ICON = WC.ClassSystem.LoadImage(NameArchive="ICO.ico")
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
VERSION = "0.2.1"

TYPE = SearchBase.SearchOther(Type="Prota")
RAZE = SearchBase.SearchOther(Type="Raze")

PATH_INFO = f"Path #18 news (05/09/2023): \n- Lib version {CUR_VERSION} \n- Current app version: {NAMEVERSION} {VERSION} \n- App is already for test in case except by load of   archive .json \n- we ready up for you feed back "

SavedData = os.listdir("app/UserSaved")

class WindowLoad:
    def WindowMain():
        Window = Tk()
        Window.title(NAME)
        Window.geometry(TRANSFORM)
        Window.resizable(width=False, height=False)
        Window.iconbitmap(ICON)
        WC.ClassProcces.CenterWindow(
            Window=Window, width=X_GLOBAL, height=Y_GLOBAL)

        # PROCCES
        archive = WC.ClassSystem.LoadData(NameFolder="UserSaved", NameArchive=max(SavedData))

        TempName = max(SavedData)
        TempBool = ".json"

        TempName = "".join(x for x in TempName if x not in TempBool)

        TempText = f"Ultimo archivo: {TempName}" + "\n Volumen:" + str(archive["Data"]["HistoryAdvanced"][0]) + "\n Capitulo:" + str(
            archive["Data"]["HistoryAdvanced"][1]) + "\n Esceneario:" + str(
            archive["Data"]["HistoryAdvanced"][2]) + "\n\n Nombre de personaje: \n" + str(archive["Data"]["Name"])

        # Symbol of Font
        Fdefault = WC.ClassProcces.CreateFont()
        Fmintext = WC.ClassProcces.CreateFont(size=9, Family="Helvetica")

        # Symbol of Label: LB//Name//
        LB_BG = WC.ClassNodes.FuncLabel(
            NodeMaster=Window, Font="a", Text_Or_Image="BG_MAIN_TITLE.jpg", Type="image", ReX=X_GLOBAL, ReY=Y_GLOBAL)

        LBVersion = WC.ClassNodes.FuncLabel(
            NodeMaster=Window, Font=Fdefault, Text_Or_Image=f"{NAMEVERSION, VERSION}", Y=475, X=715)

        # Symbol of text area: A//Name//
        AGamePanel = WC.ClassNodes.FuncText(
            NodeMaster=Window, Font=Fdefault, X=10, Y=28, heigh=400, width=150)
        WC.ClassProcces.TextEdit(
            NodeText=AGamePanel, text=TempText, Type="Panel")

        ASelecDate = WC.ClassNodes.FuncListBox(
            NodeMaster=Window, Font=Fdefault, X=200, Y=28, high=400, width=680)

        for i in range(len(SavedData)):
            WC.ClassProcces.TextEdit(
                NodeText=ASelecDate, Type="", List=f"{SavedData[i]}", isText=False)
            WC.ClassProcces.Addscroll(NodeText=ASelecDate)

        # Symbol of button: B//Name//
        Bexit = WC.ClassNodes.FuncButton(
            NodeMaster=Window, Font=Fdefault, TextInNode="Salir", Type="exit", X=123, Y=1)
        Bmenu = WC.ClassNodes.FuncButton(
            NodeMaster=Window, Font=Fdefault, Priori="changend", Type="load_window", IndexWindow=1, TextInNode="Menú", X=10, Y=1)

        Bnewgame = WC.ClassNodes.FuncButton(
            NodeMaster=Window, Font=Fdefault, TextInNode="Nuevo juego", Priori="changend", Type="load_window", IndexWindow=4, X=200, Y=360)

        Bload = WC.ClassNodes.FuncButton(
            NodeMaster=Window, Font=Fdefault, TextInNode="Cargar", Priori="changend", Type="load_window", IndexWindow=5, X=200, Y=400)

        return Window.mainloop()

class WindowNewGame:
    def WindowMain():
        Window = Tk()
        Window.geometry("250x500")
        Window.iconbitmap(ICON)
        Window.title(NAME)
        Window.resizable(width=False, height=False)
        WC.ClassProcces.CenterWindow(
            Window=Window, width=250, height=Y_GLOBAL)

        LB_BG = WC.ClassNodes.FuncLabel(
            NodeMaster=Window, Font="a", Text_Or_Image="BG_CREATE_PERSON.jpg", Type="image", X=0, Y=0, ReX=250, ReY=500)

        # Symbol of Font: F//Name//
        Ftitle = WC.ClassProcces.CreateFont(
            size=14, isBlack=True, isRall=True, Family="Helvetica")

        Fdeafult = WC.ClassProcces.CreateFont()
        Fmintext = WC.ClassProcces.CreateFont(size=8, Family="Helvetica")
        Ftitle = WC.ClassProcces.CreateFont(
            size=23, isBlack=True, isRall=True, Family="Helvetica")

        # Symbol of Label: LB//Name//_(tag)_(object tag)
        LB_credits = WC.ClassNodes.FuncLabel(
            NodeMaster=Window, Font=Fdeafult, Text_Or_Image="credits_label", Y=470)

        LB_creation_person = WC.ClassNodes.FuncLabel(
            NodeMaster=Window, Font=Ftitle, Text_Or_Image="Crear personaje", Y=30)

        LB_tag_Name = WC.ClassNodes.FuncLabel(
            NodeMaster=Window, Font=Fmintext, Text_Or_Image="Nombre de personaje", Y=130)

        LB_tag_Type = WC.ClassNodes.FuncLabel(
            NodeMaster=Window, Font=Fmintext, Text_Or_Image="¿Quieres prota o invitado?", Y=180)

        LB_tag_Rase = WC.ClassNodes.FuncLabel(
            NodeMaster=Window, Font=Fmintext, Text_Or_Image="¿Que raza eres?", Y=230)

        # Symbol of button: B//Name//
        Bmenu = WC.ClassNodes.FuncButton(
            NodeMaster=Window, Font=Fdeafult, TextInNode="Menu", Priori="changend", Type="load_window", IndexWindow=1, Y=3.4)

        Blogin = WC.ClassNodes.FuncButton(
            NodeMaster=Window, Font=Fdeafult, Priori="changend", Type="load_window", IndexWindow=5,  TextInNode="Cargar", X=195, Y=3.4)
        
        Data = {
            "Raze": f"{WC.ClassProcces.ConsulItem(1)}",
            "Impact": f"{WC.ClassProcces.ConsulItem(0)}",
            "Name": f"{WC.ClassProcces.ConsulItem(2)}",
            "Stats": SearchBase.SearchStats(Type=WC.ClassProcces.ConsulItem(1)),
            "HistoryAdvanced": [0, 0, 0, 0]
            }
        
        Bsave = WC.ClassNodes.FuncButton(
            NodeMaster=Window, Font=Fdeafult, Priori="entry_to_load", Type="entry_to_load", TextInNode="Guardar",IndexWindow=5, X=100, Y=400)

        
            

        # Symbol of Entry: E//Name//
        EName = WC.ClassNodes.FuncEntry(
            NodeMaster=Window, Font=Fdeafult, Y=155, width=30)

        # Symbol of Option Menu: OP//Name//
        OPType = WC.ClassNodes.FuncOptionMenu(
            NodeMaster=Window, OptionList=TYPE, Font=Fdeafult, X=5, Y=205, high=23, width=120)

        OPRaze = WC.ClassNodes.FuncOptionMenu(
            NodeMaster=Window, OptionList=RAZE, Font=Fdeafult, X=5, Y=253, high=23, width=80)

        return Window.mainloop()

class WindowGame:
    def WindowMain():
        Window = Tk()
        Window.title(NAME)
        Window.geometry(TRANSFORM)
        Window.resizable(width=False, height=False)
        Window.iconbitmap(ICON)
        WC.ClassProcces.CenterWindow(
            Window=Window, width=X_GLOBAL, height=Y_GLOBAL)

        archive = WC.ClassProcces.CurrentConsult(var="NEWINFO")

        # Symbol of font: F//Name//
        Fdefault = WC.ClassProcces.CreateFont()
        Fmintext = WC.ClassProcces.CreateFont(size=9, Family="Helvetica")
        Ftitle = WC.ClassProcces.CreateFont(
            size=14, isBlack=True, isSlash=True, isRall=True, Family="Helvetica")

        # Symbol of Label: LB//Name//
        TempVol = WC.ClassProcces.CurrentDate()

        LB_credits = WC.ClassNodes.FuncLabel(
            NodeMaster=Window, Font=Fdefault, Text_Or_Image=f"Creditos {CREDIT['History']}", X=20, Y=450)
        LB_vol = WC.ClassNodes.FuncLabel(
            NodeMaster=Window, Font=Ftitle, Text_Or_Image=f"VOLUMEN: {TempVol[0]}", X=200)
        LB_cap = WC.ClassNodes.FuncLabel(
            NodeMaster=Window, Font=Ftitle, Text_Or_Image=f"CAPITULO: {TempVol[1]}", X=500)

        # Symbol of Button: B//Name//
        Bexit = WC.ClassNodes.FuncButton(
            NodeMaster=Window, Font=Fdefault, TextInNode="Salir", Type="exit", X=123, Y=1)

        Bmenu = WC.ClassNodes.FuncButton(
            NodeMaster=Window, Font=Fdefault, Priori="changend", Type="load_window", IndexWindow=1, TextInNode="Menú", X=10, Y=1)

        Bdes_negative_2 = WC.ClassNodes.FuncButton(
            NodeMaster=Window, Font=Fdefault, Type="pass", TextInNode="des_neg_2", X=300, Y=430)
        Bdes_negative_1 = WC.ClassNodes.FuncButton(
            NodeMaster=Window, Font=Fdefault, Type="pass", TextInNode="des_neg_1", X=420, Y=430)

        Bdes_neutral = WC.ClassNodes.FuncButton(
            NodeMaster=Window, Font=Fdefault, Type="pass", TextInNode="des_neu", X=540, Y=430)

        Bdes_good_1 = WC.ClassNodes.FuncButton(
            NodeMaster=Window, Font=Fdefault, Type="pass", TextInNode="des_god_1", X=660, Y=430)
        Bdes_good_2 = WC.ClassNodes.FuncButton(
            NodeMaster=Window, Font=Fdefault, Type="pass", TextInNode="des_god_2", X=780, Y=430)

        # Symbol of text area: A//Name//
        Atext = WC.ClassNodes.FuncText(
            NodeMaster=Window, Font=Fdefault, X=200, Y=28, heigh=400, width=680)
        WC.ClassProcces.TextEdit(
            NodeText=Atext, text=archive["Data"]["Name"], Type="Panel")

        TempText = f"Estadisticas: \n  Nombre: "+ str(
            archive["Data"]["Name"]) + "\n\n Atributos: \n  Suerte: "+ str(
            archive["Data"]["Stats"][0]) + "\n  Fuerza: "+ str(
            archive["Data"]["Stats"][1]) + "\n  Velocidad: "+ str(
            archive["Data"]["Stats"][2]) + "\n  Influencia: " + str(
            archive["Data"]["HistoryAdvanced"][3])

        AInfo = WC.ClassNodes.FuncText(
            NodeMaster=Window, Font=Fmintext, X=10, Y=28, width=150, heigh=400)
        WC.ClassProcces.TextEdit(NodeText=AInfo, text=TempText, Type="Panel")

        return Window.mainloop()

class WindowMenu:
    def WindowMain():
        Window = Tk()
        Window.title(NAME)
        Window.geometry(TRANSFORM)
        Window.resizable(width=False, height=False)
        Window.iconbitmap(ICON)
        WC.ClassProcces.CenterWindow(
            Window=Window, width=X_GLOBAL, height=Y_GLOBAL)

        LB_BG = WC.ClassNodes.FuncLabel(
            NodeMaster=Window, Font="a", Text_Or_Image="BG_CREATE_PERSON.jpg", Type="image", X=0, Y=0, ReX=900, ReY=500)

        # Symbol of Font: F//Name//
        Fdefault = WC.ClassProcces.CreateFont()
        Ftitle = WC.ClassProcces.CreateFont(
            size=24, isBlack=True, isRall=True, Family="Helvetica")

        # Symbol of Label: LB//Name//
        LB_title = WC.ClassNodes.FuncLabel(
            NodeMaster=Window, Font=Ftitle, Text_Or_Image=f"{NAME}", X=350, Y=0)
        LB_credits = WC.ClassNodes.FuncLabel(
            NodeMaster=Window, Font=Fdefault, Text_Or_Image=f"Programmed by {CREDIT['Programmer']}", X=310, Y=465)

        # Symbol of text area: A//Name//
        ApanelNews = WC.ClassNodes.FuncText(
            NodeMaster=Window, Font=Fdefault, X=10, Y=290, heigh=200, width=290)

        WC.ClassProcces.TextEdit(
            NodeText=ApanelNews, text=PATH_INFO, Type="Panel")

        # Symbol of button: B//Name//
        BNewgame = WC.ClassNodes.FuncButton(
            NodeMaster=Window, Font=Fdefault, TextInNode="Nuevo Juego", Type="load_window", Priori="changend", IndexWindow=4, X=350, Y=300)

        Bload = WC.ClassNodes.FuncButton(
            NodeMaster=Window, Font=Fdefault, TextInNode="Cargar juego", Type="load_window", Priori="changend", IndexWindow=5, X=350, Y=330)

        Bcredit = WC.ClassNodes.FuncButton(
            NodeMaster=Window, Font=Fdefault, TextInNode="Creditos", Type="load_window", Priori="changend", IndexWindow=2, X=360, Y=360)
        
        Bquit = WC.ClassNodes.FuncButton(
            NodeMaster=Window, Font=Fdefault, TextInNode="Salir", Type="exit", X=370, Y=390)


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
        WC.ClassProcces.CenterWindow(Window=Window, width=X, height=Y)

        LB_BG = WC.ClassNodes.FuncLabel(
            NodeMaster=Window, Font="a", Text_Or_Image="BG_CREDITS.jpg", Type="image", ReX=X, ReY=Y)


        # Symbol of Font: F//Name//
        Fdefault = WC.ClassProcces.CreateFont()
        Ftitle = WC.ClassProcces.CreateFont(
            size=24, isBlack=True, isRall=True, Family="Helvetica")

        # Symbol of label: LB//Name//
        LB_credit = WC.ClassNodes.FuncLabel(
            NodeMaster=Window, Font=Ftitle, Text_Or_Image="Creditos", X=135)

        LB_mesage = WC.ClassNodes.FuncLabel(
            NodeMaster=Window, Font=Fdefault, Text_Or_Image=(f"Director: {CREDIT['Main']} \n\n"
                                                            f"Programador: {CREDIT['Programmer']} \n\n"
                                                            f"Imagenes: {CREDIT['Image']} \n\n"
                                                            f"Estadistica: {CREDIT['Stats']} \n\n"
                                                            f"Historia: {CREDIT['History']}"
                                                            ), X=100, Y=40)
        # Symbol of button: B//Name//
        Y = ((Y+150)/2)
        Bexit = WC.ClassNodes.FuncButton(
            NodeMaster=Window, Font=Fdefault, TextInNode="Salir", Type="exit", X=(X/2), Y=Y)

        Bmenu = WC.ClassNodes.FuncButton(
            NodeMaster=Window, Font=Fdefault, TextInNode="Menu", Priori="changend", Type="load_window", IndexWindow=1, X=((X-100)/2), Y=Y)

        return Window.mainloop()


WC.ClassProcces.SetWindow(1, WindowMenu)
WC.ClassProcces.SetWindow(2, WindowCredit)
WC.ClassProcces.SetWindow(3, WindowGame)
WC.ClassProcces.SetWindow(4, WindowNewGame)
WC.ClassProcces.SetWindow(5, WindowLoad)

WC.StartAPP(ID=1)