"""
by @Z3R0_GT 2023  \n
Version 1.1 \n

official lib used: os, json, tkinter, PIL
custom lib used: Lead
"""
# Errores:
#   1)si ingresas un nombre como por ejemplo "jose.json", carga normal
#   pero retornara ese nombre "jose.json" (internamente es "jose.json".json)

import os
import json

from tkinter import Text, Label, Entry, StringVar, Scrollbar, Listbox, Button,  OptionMenu
from tkinter.font import Font
from PIL import Image, ImageTk

from app.assets.dataBase.Lead import *


## ---------Constant of Lib---------##
LIB_VERSION = 1.5
NEWINFO = None
CURRENT_WINDOW: int = 0

Matrix = {}
DataUser = {}

PrincipalFolder = os.path.dirname(__file__)
ImagenFolder = os.path.join(PrincipalFolder, "assets/images")

CURRENT_FINAL = []
## there function not Have information, but the "Class" yes ##

## ---------System Process---------##


def SaveArchives(Dictonary, NameArchive=""):
    try:
        with open(f"app/UserSaved/{NameArchive}.json", "w") as file:

            file.write(Dictonary)
            file.close()
    except:
        return "A error has bein ocurred!"


def LoadArchives(NameArchive=""):
    try:
        if os.path.join(PrincipalFolder, f"UserSaved/{NameArchive}"):
            with open(f"app/UserSaved/{NameArchive}") as file:
                ReturnData = json.load(file)
                return ReturnData
    except:
        return "A error has bein ocurred!"

## ---------Nodes Text---------##


def CallBack(event):
    global NEWINFO

    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        data = event.widget.get(index)
        NEWINFO = LibProcess.ClassSystem.LoadData(NameArchive=data)
        return data
    else:
        pass


def ctrlEvent(event):
    if (12 == event.state and event.keysym == 'c'):
        return
    else:
        return "break"


def EditText(NodeText, text="", Type="", isText=True, isEmpy=True, TextInNode="", List=[], Vol=0, Cap=0, Dession=0):
    if isText:
        if isEmpy == False:
            NodeText.delete("1.0", "end")

        content = None

        if isEmpy:
            if Type == "":
                content = SearchBase.SearchDate(
                    Vol=Vol, Cap=Cap, Dession=Dession)
                return NodeText.insert("insert", content)
            elif Type == "Panel":
                return NodeText.insert("insert", text)

        return content
    else:
        NodeText.insert("end", f"{List}")
        NodeText.bind("<<ListboxSelect>>", lambda e: CallBack(e))

        return NodeText

## ---------Procces Node---------##


def AddScroll(NodeText):

    Scroll = Scrollbar(master=NodeText, orient="vertical")
    Scroll.config(command=NodeText.yview)
    NodeText["yscrollcommand"] = Scroll.set

    Scroll.grid(padx=660, ipady=178)

    return NodeText


def AddActionButton(NodeMaster, indexWindow: int = 0, Type=""):
    global CURRENT_WINDOW

    if Type == "exit":
        CURRENT_WINDOW = 100
        return NodeMaster.destroy()
    elif Type == "entry":
        global NEWINFO

        LibProcess.ClassProcces.SaveDicArchive(
            raze=CURRENT_FINAL[1], type=CURRENT_FINAL[0], name=LibProcess.ClassProcces.UserEntry())
        NEWINFO = LibProcess.ClassSystem.LoadData(
            NameArchive=f"{LibProcess.ClassProcces.UserEntry()}.json")
        LibProcess.ClassProcces.CurrentWindow(index=3)
        NodeMaster.destroy()
    elif Type == "load_data":
        pass
    elif Type == "not_thing":
        print(Type)
        pass
    elif Type == "yes_thing":
        print(Type)
        pass
    elif Type == "make_thing":
        print(Type)
        pass
    elif Type == "exit_thing":
        print(Type)
        pass
    elif Type == "help_enemy_thing":
        print(Type)
        pass
    elif Type == "load_window":
        CURRENT_WINDOW = indexWindow
        return NodeMaster.destroy()
    elif Type == "pass":
        print("This button is online for action")
    else:
        print(Type, " is not found, sorry")


def TypeFont(size: int = 10, isBlack: bool = False, isSlash: bool = False, isRall: bool = False, Family: str = ""):
    global typeFont

    if isBlack and isSlash and isRall:
        typeFont = Font(family=Family, size=size, weight="bold",
                        slant="italic", underline=True)
    elif isBlack and isSlash:
        typeFont = Font(family=Family, size=size,
                        weight="bold", slant="italic")
    elif isBlack and isRall:
        typeFont = Font(family=Family, size=size,
                        weight="bold", underline=True)
    elif isRall and isSlash:
        typeFont = Font(family=Family, size=size,
                        slant="italic", underline=True)
    elif isBlack:
        typeFont = Font(family=Family, size=size, weight="bold")
    elif isSlash:
        typeFont = Font(family=Family, size=size, slant="italic")
    elif isRall:
        typeFont = Font(family=Family, size=size, underline=True)
    else:
        typeFont = Font(family="italic", size=size)

    return typeFont


def LoadImage(NameArchive=""):
    return os.path.join(ImagenFolder, NameArchive)

## ---------Test Func---------##


def MoveNode(Node, X: int = 0, Y: int = 0):
    """
    Test func for transform node
    """
    ReNode = Node
    ReNode.place(x=X, y=Y)

    return ReNode


class LibProcess():
    class ClassNodes():

        def FuncButton(NodeMaster, Font: Font, IndexWindow: int = 0, TextInNode="",  Type="", Priori="", X=0, Y=0, heigh=0, width=0):
            """
            Build a button with "NodeMaster",\n
            you must specific "Type" button and "Priori" if is special \n

            if "height" or "width" is 0, then, return X and Y; but not "height", "width" varibles.

            add a action to button with "type" (this process is automatic) : \n
            - exit: end program \n
            - entry: Entry a date from "stats_user" by "TextMaster" \n
            - load_data: load user date from "stats_user"
            - not_thing: nothing \n
            - yes_thing: make thing \n
            - make_thing: posibily of thing \n
            - exit_thing: exit with posibly \n
            - help_enemy_thing: help enemy \n
            - load_window: you can specify your window with "indexWindow" \n
            - pass: Text if button is online \n
            """
            global NodeName

            if Priori == "exit":
                NodeName = Button(master=NodeMaster, text=TextInNode,
                                  command=lambda: AddActionButton(
                                      NodeMaster=NodeMaster, Type=Type),
                                  font=Font)
            elif Priori == "changend":
                NodeName = Button(master=NodeMaster, text=TextInNode,
                                  command=lambda: AddActionButton(
                                      NodeMaster=NodeMaster, Type=Type, indexWindow=IndexWindow),
                                  font=Font)
            else:
                NodeName = Button(master=NodeMaster, text=TextInNode,
                                  command=lambda: AddActionButton(
                                      NodeMaster=NodeMaster, Type=Type),
                                  font=Font)

            if heigh == 0 or width == 0:
                NodeName.place(x=X, y=Y)
            else:
                NodeName.place(x=X, y=Y, width=width, height=heigh)

            return NodeName

        def FuncText(NodeMaster, Font: Font, X=0, Y=0, heigh=0, width=0):
            """
            if you edit the text on node, recommend use func
            - LibProcess().ClassProcces().TextEdit()
            """
            NodeText = Text(master=NodeMaster, font=Font)
            NodeText.bind("<Key>", lambda e: ctrlEvent(e))
            NodeText.place(x=X, y=Y, width=width, height=heigh)

            return NodeText

        def FuncLabel(NodeMaster, Font: Font, Text_Or_Image="", Type="Normal", X=0, Y=0, heigh=0, width=0, ReX=0, ReY=0):
            """
            you must specific "Type" node in:
            - Normal: return a normal label
            - Image: return a label with image (automatic), 
            but you use "ReX" and "ReY" for resize the image and use "Text_Or_Image" 
            varible for specific name of archive and extension
            """

            if Type == "Normal":
                NodeLabel = Label(master=NodeMaster,
                                  font=Font, text=Text_Or_Image)

                if heigh == 0 or width == 0:
                    NodeLabel.place(x=X, y=Y)
                else:
                    NodeLabel.place(x=X, y=Y, height=heigh, width=width)
            elif Type == "Image":
                global IMA_REW

                Photo = Image.open(f"{LoadImage(NameArchive=Text_Or_Image)}")

                if ReX == 0 or ReY == 0:
                    IMA_REW = ImageTk.PhotoImage(Photo)
                else:
                    Photo_rew = Photo.resize((ReX, ReY))
                    IMA_REW = ImageTk.PhotoImage(Photo_rew)

                NodeLabel = Label(NodeMaster, image=IMA_REW)
                NodeLabel.place(x=X, y=Y)

            return NodeLabel

        def FuncEntry(NodeMaster, Font: Font, X=0, Y=0, width=0):
            """
            if you consult Entry String, recommend use:  
            LibProcess().ClassProcces().UserEntry()
            """
            global EntryData

            EntryData = StringVar(master=NodeMaster)
            NodeEntry = Entry(master=NodeMaster, font=Font,
                              width=width, textvariable=EntryData)

            NodeEntry.place(x=X, y=Y)

            return NodeEntry

        def FuncListBox(NodeMaster, Font: Font, X=0, Y=0, high=0, width=0):
            """
            Create list box
            """
            NodeList = Listbox(master=NodeMaster, font=Font)
            NodeList.place(x=X, y=Y, height=high, width=width)

            return NodeList

        # TEST FUNC
        def FuncOptionMenu(NodeMaster, OptionList, Font, X=0, Y=0, width=0, high=0):

            list = StringVar(NodeMaster)
            list.set(OptionList[0])

            NodeMenu = OptionMenu(NodeMaster, list, *OptionList)
            NodeMenu.config(font=Font)
            if width != 0 and high != 0:
                NodeMenu.place(x=X, y=Y, width=width, height=high)
            else:
                NodeMenu.place(x=X, y=Y)

            def callback(*args):
                CURRENT = []
                CURRENT.append(f"{list.get()}")

                for i in CURRENT:
                    if i not in CURRENT_FINAL:
                        CURRENT_FINAL.append(i)

            list.trace("w", callback)
            return NodeMenu

    class ClassProcces():

        def SaveDicArchive(raze, type, name: str, lucky: int = 0, strong: int = 0, velocity: int = 0, vol: int = 0, cap: int = 0, scene: int = 0, dession: int = 0, isDefault=True):
            Data = {}

            if isDefault != True:
                Data = {
                    "Raze": f"{raze}",
                    "Impact": f"{type}",
                    "Name": f"{name}",
                    "Stats": [lucky, strong, velocity],
                    "HistoryAdvanced": [vol, cap, scene, dession]
                }
            else:
                Data = {
                    "Raze": f"{raze}",
                    "Impact": f"{type}",
                    "Name": f"{name}",
                    "Stats": SearchBase.SearchStats(Type=raze),
                    "HistoryAdvanced": [0, 0, 0, 0]
                }

            Matrix = {"Data": Data}
            DicConverted = json.dumps(Matrix, indent=1)

            SaveArchives(Dictonary=DicConverted, NameArchive=name)

        def CreateFont(size=10, isBlack=False, isSlash=False, isRall=False, Family=""):
            """
            Create a font with: "size", "isBlack", "isSlash", "isRall", Family is a string null \n

            Return "typeFont"
            """
            return TypeFont(size=size, isBlack=isBlack, isSlash=isSlash, isRall=isRall, Family=Family)

        def TextEdit(NodeText: Text, text="", Type="", isText=True, isEmpy=True, TextInNode="", List=[], Vol=0, Cap=0, Dession=0):
            """
            Edit text for a "NodeText", if "isEmpy" is false, then, clean "NodeText" and insert new information. \n
            Can edit text, and re-write \n

            if type can: 
            - Panel: edit NodeText all
            - "(NOTHING)": NodeText call another func
            """
            return EditText(NodeText=NodeText, text=text, Type=Type, isText=isText, isEmpy=isEmpy, TextInNode=TextInNode, List=List,
                            Vol=Vol, Cap=Cap, Dession=Dession)

        def UserEntry():
            """
            Return data of user (in this case, "name" of user)
            """
            return EntryData.get()

        def Addscroll(NodeText: Text):
            """
            Add scroll to NodeText
            """
            return AddScroll(NodeText=NodeText)

        def CurrentDate():
            """
            Return a list of history 
            """
            TempArray = SearchBase.SearchDate(Vol=NEWINFO["Data"]["HistoryAdvanced"][0], Cap=NEWINFO["Data"]["HistoryAdvanced"]
                                              [1], Scene=NEWINFO["Data"]["HistoryAdvanced"][2], Dession=NEWINFO["Data"]["HistoryAdvanced"][3])
            return TempArray

        def CurrentWindow(index: int):
            """
            Set current window 
            """
            global CURRENT_WINDOW
            CURRENT_WINDOW = index

        def CurrentConsult(var: str = "WINDOW"):
            """
            Return index of current window
            """
            if var != "WINDOW":
                return NEWINFO
            else:
                return CURRENT_WINDOW

        def CurrentDes():
            return CURRENT_FINAL

        def CenterWindow(Window, width: int, height: int):
            """
            Return center Screen from a window
            """
            widthTot = Window.winfo_screenwidth()
            highTot = Window.winfo_screenheight()

            pos_w = round(widthTot/2-width/2)
            pos_h = round(highTot/2-height/2)

            return Window.geometry(str(width)+"x"+str(height)+"+"+str(pos_w)+"+"+str(pos_h))

    class ClassSystem():

        def SaveData(NamePlayer: str, Dict={}):
            """
            Create a archive .json, Dict is save in it
            """
            SaveArchives(Dictonary=Dict, NameArchive=NamePlayer)

        def LoadData(NameArchive: str):
            """
            Load a archive with "NameArchive"
            """
            Verify = LoadArchives(NameArchive=NameArchive)

            if Verify == "A error has bein ocurred!":
                return Verify
            else:
                return Verify
