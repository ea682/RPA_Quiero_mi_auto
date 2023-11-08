from asyncio.windows_events import NULL
from LibRpa.api import ConsultaApi
#from RPA_QUIERO_MI_AUTO import 


class MovicenterService:

    def __init__(self, jsonRequest = NULL):
        self.consultaApi = ConsultaApi()
        self.dataRobots = self.consultaApi.leerConfigJson()["robots"]
        self.dataRobots = self.consultaApi.leerConfigJson()["robots"]["data_robots"]
        self.jsonRequest = jsonRequest
        pass

    def getNuevosAutos(self):
        configRobot = []
        for robot in self.dataRobots:
            if robot["nombreRobot"] == "Movicenter":
                configRobot = robot
                pass
        apiMovicenter = ConsultaApi(configRobot["apiUrlNuevos"], configRobot["tipoConsulta"], configRobot["jsonConsulta"][0])
        responseApiMovicenter = apiMovicenter.consultaApi()
        return responseApiMovicenter