from asyncio.windows_events import NULL
from tkinter import EXCEPTION
from LibRpa.api import ConsultaApi

class SergioEscobarService:

    def __init__(self, jsonRequest = NULL):
        self.consultaApi = ConsultaApi()
        self.dataRobots = self.consultaApi.leerConfigJson()["robots"]["data_robots"]
        self.jsonRequest = jsonRequest
        pass

    def getNuevosAutos(self):
        try:
            configRobot = []
            for robot in self.dataRobots:
                if robot["nombreRobot"] == "Sergio Escobar":
                    configRobot = robot
                    pass
            if len(configRobot) == 0:
                return NULL
            #Validamos que el json contenga algo para la consulta
            if len(configRobot["jsonConsulta"]) == 0:
                pass
                apiMovicenter = ConsultaApi(
                    configRobot["apiUrlNuevos"], 
                    configRobot["tipoConsulta"]
                    )
            else:
                apiMovicenter = ConsultaApi(
                    configRobot["apiUrlNuevos"], 
                    configRobot["tipoConsulta"], 
                    configRobot["jsonConsulta"][0]
                    )
                pass
            responseApiMovicenter = apiMovicenter.consultaApi()
            return responseApiMovicenter.json()
        except EXCEPTION as e:
            print(e)
            pass
        
    def getHtmlVehiculos(self, link, consulta):
        self.consultaApi = ConsultaApi(link, consulta)
        return self.consultaApi.consultaApi()