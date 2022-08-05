from os import link
from Lib.configParser import configRobot
from Controller.sergioEscobarController import SergioEscobarController
from Controller.movicenterController import MovicenterController
import json

def runSergioEscobar(robotSergioEscobar):
    sergioEscobar = SergioEscobarController(robotSergioEscobar)
    sergioEscobar.obtenerVehiculosApi()
    sergioEscobar.procesarJson()

    dictVehiculosSergioEscobar = []

    for vehiculo in sergioEscobar.getListaVehiculos():
        jsonStr = json.dumps(vehiculo.__dict__)
        dictVehiculosSergioEscobar.append(jsonStr)

    print(dictVehiculosSergioEscobar)

def runMovicenter(robotMovicenterConfig):
    movicenter = MovicenterController(robotMovicenterConfig)
    movicenter.obtenerVehiculosApi()
    movicenter.procesarJson()

    dictVehiculosMoviCenter = []

    precioMenor = 1000000000
    precioMayor = 0

    linkMenor = ""
    linkMayor = ""
    for vehiculo in movicenter.getListaVehiculos():
        if(int(vehiculo.getPrecio()) < precioMenor):
            precioMenor = int(vehiculo.getPrecio())
            linkMenor = vehiculo.getLinkVehiculo()
            pass
        elif(int(vehiculo.getPrecio()) > precioMayor):
            precioMenor = int(vehiculo.getPrecio())
            linkMayor = vehiculo.getLinkVehiculo()
            pass
        jsonStr = json.dumps(vehiculo.__dict__)
        dictVehiculosMoviCenter.append(jsonStr)
    print("linkMenor : "+linkMenor)
    print("linkMayor : "+linkMayor)
    pass

#Cargamos las configuraciones de las concecionarias
sergioEscobarConfig = configRobot("sergioescobar")
movicenterConfig = configRobot("movicenter")

#Obtenemos los datos de los Robots
robotSergioEscobar = sergioEscobarConfig.getDataRobot()
robotMovicenterConfig = movicenterConfig.getDataRobot()

#Ejecuciones Robtos
#runSergioEscobar(robotSergioEscobar)
runMovicenter(robotMovicenterConfig)