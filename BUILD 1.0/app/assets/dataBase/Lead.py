VOL_1_CAP_1_SCENE_ALL = {
    "skip": "\n",
    "VOL_NAME": "Un nuevo mundo.",
    "CHAPTER_NAME_1": "Lujuria de un dragon.",
    "Scene 1 Des -2": "a",
    "Scene 1 Des -1": "b",
    "Scene 1 Des 0": "c",
    "Scene 1 Des 1": "d",
    "Scene 1 Des 2": "e"
}

SPECIES_PROTA = {
    "Dragon": [2, 10, 12],
    "Anfibio": [5, 5, 6],
    "Perro": [3, 8, 10]
}

CREATURE = {
    "Race":{
        "human cat": [10, 20, 6],
        "human dog": [4, 23, 5],
        "human fur": [2, 6, 14]
    },
    "Biome":{
        "Terrest":{
            "Neutral":{
                "Anzu":12, # Es un pavo dinosaurio
                "Lizard":20, #Lagarto similar al dragon pero no mata
                "Pie":13, #Es un ave de alas grande, pero no vuela 
                "Venano":26, #Es un venado azul
                "Quiet":23, #Similar a la jirafa pero hecho de energia
                
                "VARIANT":{
                    "Largo":10,
                    "Corto":20,
                    "Pequeño":15,

                    "Azulado":23,
                    "Engrecido":10,
                    "Exotico":12,
                    "Blanco": 17,

                    "ROJITO":10000000000 
                }
            },
            "Attack":{
                "Not name":[1,2,3], #Dragon cuadrupedo
                "Behemet":[0,0,0], #Insecto gigante

                "Caninusterra":[0,0,0], #"Perro" hecho de plantas
                "Carno Tirano":[0,0,0], #Carnotauro pero mas grande
            
                "VARIANT":{
                    "A":[0,0,0],
                    "B":[0,0,0],
                    "F":[0,0,0]
                }
            }
        },
        "Cave":{
            "Creature X":[0, 100, 200],
            "Terram iecit":[0,0,0],

            "VARIANT":{
                "Grande":[0,0,0],
                "Mediano":[0,0,0],
                "Pequeño":[0,0,0],

                "A":[0,0,0],
                "B":[0,0,0],
                "F":[0,0,0]
            }
        },
        "Under Water":{
            "Neutral":{
                "Picis":10
            },
            "Attack":{
                "Piraña":[0,0,0]
            }
        },
        "Sky up":{
            "Dragon":[2,10,12]
        },
        "Especial":{
            "BOSS":{
                "Infernun":[1200, 1200, 1200], #Es un dragon
                "Thotamatoa":[500,1200,350] #Es un cangrejo
            },
            "MIN_BOSS":{
                "Langosta Pistola":[0, 1000, 500] #Langosta con pistala 7w7
            }
        }
    }
}

def Base_Species(Type: str = ""):

    OptionList = []

    if Type == "Raze":
        OptionList = ["Dragon", "Anfibio", "Perro"]
    elif Type == "Prota":
        OptionList = ["Protagonista", "Asistencia"]

    else:
        OptionList = "A error has being ocurred!"

    return OptionList


def Base_History(Vol=0, Cap=0, Scene=0, Dession=0):
    Indice = [Vol, Cap, Scene, Dession]

    AddReturn = []

    if Indice[0] == 0 and Indice[1] == 0:
        AddReturn.append(VOL_1_CAP_1_SCENE_ALL["VOL_NAME"])
        if Indice[2] == 0:
            AddReturn.append(VOL_1_CAP_1_SCENE_ALL["CHAPTER_NAME_1"])
            for i in range(-2, 2):
                if Indice[3] == i:
                    AddReturn.append(
                        VOL_1_CAP_1_SCENE_ALL[f"Scene 1 Des {str(i)}"])

        return AddReturn
    else:
        return "error!"


def Base_Creature(INDEX_BASE:str, INDEX_TYPE:str, INDEX_RACE:str, INDEX_NAME:str, INDEX_VARIANT:str=""):
    
    TempVar = CREATURE[INDEX_BASE][INDEX_TYPE][INDEX_RACE][INDEX_NAME]    
    if INDEX_VARIANT != "":
        TempVar = TempVar + CREATURE[INDEX_BASE][INDEX_TYPE][INDEX_RACE]["VARIANT"][INDEX_VARIANT]

    print(TempVar)

a = Base_Creature(INDEX_BASE="Biome", INDEX_TYPE="Terrest", INDEX_RACE="Neutral", INDEX_NAME="Anzu", INDEX_VARIANT="Largo")

class SearchBase():

    def SearchDate(Vol, Cap, Scene, Dession):
        """
        Recived a date of "Vol (Volum)" && "Cap (Chapter)" \n

        search a date and return date in base on array
        """

        PreResult = Base_History(
            Vol=Vol, Cap=Cap, Scene=Scene, Dession=Dession)

        try:
            return PreResult
        except:
            return "A error has being ocurred!, report to: @Z3R0_GT#3883 in discord"

    def SearchOther(Type: str = ""):

        PreResult = Base_Species(Type=Type)

        if PreResult != "A error has being ocurred!":
            return PreResult
        else:
            return "A error has being ocurred!"

    def SearchStats(Type):
        return SPECIES_PROTA[str(Type)]
