"""
Window Controller (WC) a librelly for controll and create UI easy
with tkinter and PIL.

this lib is orient to build apps/games based on text with JSON,
process automatly, and more!.

this lib was create by @Z3R0_GT (GitHub), if you find a bug
report to Z3R_GT#3883
"""

## ---------Libs Imports---------##
import os
import json

from tkinter import Text, Label, Entry, StringVar, Scrollbar, Listbox, Button,  OptionMenu
from tkinter.font import Font
from PIL import Image, ImageTk

from app.assets.dataBase.Lead import *
## ---------Constant of Lib---------##
LIB_VERSION = 2.0
CURRENT_WINDOW = ["CONTINUE"]

_ClassNodes__ITEM_SELECT = []
__DIR_FOLDER = None
__ITEM_CHOICE = None
ID = 1


MAIN_FOLDER = os.path.dirname(__file__)

def DEV_CONSULT():
    print(_ClassNodes__ITEM_SELECT)

class _WC:

    ## ---------System Process---------##
    def __SaveArchives(Data: dict, DirFolder: str, NameArchive=""):
        try:
            with open(f"{MAIN_FOLDER}/app/{DirFolder}/{NameArchive}.json", "w") as file:
                file.write(Data)
                file.close()
        except:
            return f"{DirFolder} is not find or Data has error."

    def _ClassSystem__LoadArchives(DirFolder: str, NameArchive=""):
        try:
            if os.path.join(MAIN_FOLDER, f"app/{DirFolder}/{NameArchive}"):
                with open(f"{MAIN_FOLDER}/app/{DirFolder}/{NameArchive}") as file:
                    ReturnData = json.load(file)
                    return ReturnData
        except:
            return f"{DirFolder} is not find."

    def _ClassSystem__loadImage(NameArchive: str):
        ImaFolder = os.path.join(MAIN_FOLDER, "app/assets/images")

        return os.path.join(ImaFolder, NameArchive)
    
    def _ClassNodes__loadImage(NameArchive: str):
        ImaFolder = os.path.join(MAIN_FOLDER, "app/assets/images")

        return os.path.join(ImaFolder, NameArchive)
    
    def __loadWindow():
        global ID

        if ID == 0:
            CURRENT_WINDOW[(ID+1)][1].WindowMain()
            return
        else:
            CURRENT_WINDOW[ID][1].WindowMain()
            return

    ## ---------Nodes Text process---------##
    def __CallBack(event):
        global __ITEM_CHOICE

        selection = event.widget.curselection()
        if selection:
            index = selection[0]
            data = event.widget.get(index)
            __ITEM_CHOICE = WC.ClassSystem.LoadData(NameFolder="UserSaved", NameArchive=data)
            return data
        else:
            pass

    def _ClassNodes__ctrlEvent(event):
        if (12 == event.state and event.keysym == 'c'):
            return
        else:
            return "break"

    def _ClassProcces__editText(NodeText: Text, text: str, Type: str = "", isText=True, isEmpy=True, TextInNode="", List=[], Vol=0, Cap=0, Dession=0):
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
                else:
                    return NodeText.insert("insert", TextInNode)
            return content
        else:
            NodeText.insert("end", f"{List}")
            NodeText.bind("<<ListboxSelect>>", lambda e: _WC.__CallBack(e))

            return NodeText

    def _ClassProcces__addScroll(NodeText: Text):

        Scroll = Scrollbar(master=NodeText, orient="vertical")
        Scroll.config(command=NodeText.yview)
        NodeText["yscrollcommand"] = Scroll.set

        Scroll.grid(padx=660, ipady=178)

        return NodeText

    ## ---------Nodes process---------##

    def _ClassNodes__addActionButton(NodeMaster, Type: str, indexWindow: int = 0, Data:dict={}):
        global CURRENT_WINDOW
        global ID

        if Type == "exit":
            CURRENT_WINDOW.insert(0, "EXIT")
            return NodeMaster.destroy()
        elif Type == "load_window":
            ID = indexWindow
            return NodeMaster.destroy()
        elif Type == "entry_to_load":
            ID = indexWindow

            __DIR_FOLDER = Data["FolderSave"]

            Matrix = {"Data", Data}
            MatrixConvert = json.dumps(Matrix, indent=1)

            _WC.__SaveArchives(
                Data=MatrixConvert, DirFolder=__DIR_FOLDER, NameArchive=EntryData.get())
            _ClassNodes__ITEM_SELECT[2] = EntryData.get()

            NodeMaster.destroy()

    def _ClassProcces__typeFont(size: int = 10, isBlack: bool = False, isSlash: bool = False, isRall: bool = False, Family: str = ""):
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

    def _ClassProcces__ConsultItem(ID:int):
        return _ClassNodes__ITEM_SELECT[ID]

class WC:

    def StartAPP(ID: int):
        while True:
            if CURRENT_WINDOW[0] == "EXIT":
                break
            else:
                _WC.__loadWindow()
        print("App is end")
        return

    class ClassNodes:
        def FuncButton(NodeMaster, Font: Font, IndexWindow: int = 0, TextInNode="", Data={},  Type="", Priori="", X=0, Y=0, heigh=0, width=0):
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

            if Priori == "changend":
                NodeName = Button(master=NodeMaster, text=TextInNode,
                                  command=lambda: _WC.__addActionButton(
                                      NodeMaster=NodeMaster, Type=Type, indexWindow=IndexWindow),
                                  font=Font)
            elif Priori == "entry_to_load":
                NodeName = Button(master=NodeMaster, text=TextInNode,
                                  command=lambda: _WC.__addActionButton(
                                      NodeMaster=NodeMaster, Type=Type, indexWindow=IndexWindow, Data=Data),
                                  font=Font)            
            else:
                NodeName = Button(master=NodeMaster, text=TextInNode,
                                  command=lambda: _WC.__addActionButton(
                                      NodeMaster=NodeMaster, Type=Type),
                                  font=Font)

            if heigh == 0 or width == 0:
                NodeName.place(x=X, y=Y)
            else:
                NodeName.place(x=X, y=Y, width=width, height=heigh)

            return NodeName

        def FuncText(NodeMaster, Font: Font, CanCopy=True, X=0, Y=0, heigh=0, width=0):
            """
            if you edit the text on node, recommend use func
            - LibProcess().ClassProcces().TextEdit()
            """
            NodeText = Text(master=NodeMaster, font=Font)
            if CanCopy:
                NodeText.bind("<Key>", lambda e: _WC.__ctrlEvent(e))
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

            elif Type == "image":
                global IMA_REW

                Photo = Image.open(
                    f"{_WC.__loadImage(NameArchive=Text_Or_Image)}")

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
            WC.ClassProcces.UserEntry()
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

        def FuncOptionMenu(NodeMaster, OptionList, Font, X=0, Y=0, width=0, high=0):
            """
            Create a options list
            """
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
                    if i not in _ClassNodes__ITEM_SELECT:
                            _ClassNodes__ITEM_SELECT.append(i)
                        
            list.trace("w", callback)
            return NodeMenu

    class ClassProcces:

        def ConsulItem(ID:int):
            return _WC.__ConsultItem(ID=ID)

        def SetWindow(ID: int, Tag):
            """
            Set a window, ID is a procces, and Tag must has "Class" not others
            """
            CURRENT_WINDOW.append((ID, Tag))

        def TextEdit(NodeText: Text, text="", Type="", isText=True, isEmpy=True, TextInNode="", List=[], Vol=0, Cap=0, Dession=0):
            """
            Edit text for a "NodeText", if "isEmpy" is false, then, clean "NodeText" and insert new information. \n
            Can edit text, and re-write \n

            if type can: 
            - Panel: edit NodeText all
            - "(NOTHING)": NodeText call another func
            """
            return _WC.__editText(NodeText=NodeText, text=text, Type=Type, isText=isText, isEmpy=isEmpy, TextInNode=TextInNode, List=List,
                                  Vol=Vol, Cap=Cap, Dession=Dession)

        def CreateFont(size=10, isBlack=False, isSlash=False, isRall=False, Family=""):
            """
            Create a font with: "size", "isBlack", "isSlash", "isRall", Family is a string null \n

            Return "typeFont"
            """
            return _WC.__typeFont(size=size, isBlack=isBlack, isSlash=isSlash, isRall=isRall, Family=Family)

        def CenterWindow(Window, width: int, height: int):
            """
            Return center Screen from a window
            """
            widthTot = Window.winfo_screenwidth()
            highTot = Window.winfo_screenheight()

            pos_w = round(widthTot/2-width/2)
            pos_h = round(highTot/2-height/2)

            return Window.geometry(str(width)+"x"+str(height)+"+"+str(pos_w)+"+"+str(pos_h))

        def Addscroll(NodeText: Text):
            """
            Add scroll to NodeText
            """
            return _WC.__addScroll(NodeText=NodeText)

    class ClassSystem:

        def LoadData(NameFolder: str, NameArchive: str):
            """
            load data, specif name of folder and archive
            """
            Verify = _WC.__LoadArchives(
                DirFolder=NameFolder, NameArchive=NameArchive)

            if Verify != f"{NameFolder} is not find":
                return Verify

        def LoadImage(NameArchive:str):
            """
            Return a path of image
            """
            return _WC.__loadImage(NameArchive=NameArchive)

        #TRASH
        def SaveData(Data: dict, DirFolder: str, NameArchive: str):
            """
            Save data in "DirFolder" and set "NameArchive"
            """
            global __DIR_FOLDER
            __DIR_FOLDER = DirFolder

            Matrix = {"Data", Data}
            DicConverted = json.dumps(Matrix, indent=1)

            _WC.__SaveArchives(Data=DicConverted,
                               DirFolder=DirFolder, NameArchive=NameArchive)

