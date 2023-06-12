from WC import *

while True:
    a = input("CONSULTA \n")

    if a == "VARIABLES":
        print(WC.DEV.DEVCONSULT())

    elif a == "SETDIR":
        B = input("DIRECCION: \n ")
        WC.Config.set_dir(DIR=B)

    elif a == "SAVE":    

        data = {
            "Nombre": "jose",
            "edad": "13",
            "apellido": "uwu"
        }

        WC.System.save_archive(data=data, ID_FOLDER=int(input("ID FOLDER: ")), name_archive=input("Nombre de archivo: \n"))
    elif a == "LOAD":
        pass

    elif a == "EXIT":
        break