import ast
from Service.movicenterService import MovicenterService
from Service.quieroMiAuto import QuieroMiAuto

from Entity.ingresoVehiculo import IngresoVehiculoEntiti
from Lib.api import ConsultaApi

class MovicenterController():
    
    def __init__(self):
        self.quieroMiAuto = QuieroMiAuto()
        self.movicenterService = MovicenterService()
        self.consultaApi = ConsultaApi()
        self.dataRobots = self.consultaApi.leerConfigJson()["robots"]["data_robots"]
        self.linkConcecionaria = self.getLinkPagina()
        pass

    def runVehiculosNuevos(self):
        reponseMovicentar = self.movicenterService.getNuevosAutos()
        dataVehiculosNuevos = reponseMovicentar["data"]
        for vehiculoNuevo in dataVehiculosNuevos:
            linkVehiculo = self.linkConcecionaria+"/autos/"+vehiculoNuevo["key"]
            listPhotos = ast.literal_eval(vehiculoNuevo["photos"])
            ingresoVehiculoEntiti = IngresoVehiculoEntiti(
                vehiculoNuevo["brand"], 
                vehiculoNuevo["model"],
                vehiculoNuevo["bodyWork"],
                linkVehiculo,
                listPhotos,
                int(vehiculoNuevo["listPrice"]),
            )
            self.quieroMiAuto.ingresoVehiculo(ingresoVehiculoEntiti.__dict__)
        return 

    def getLinkPagina(self):
        configRobot = []
        for robot in self.dataRobots:
            if robot["nombreRobot"] == "movicenter":
                configRobot = robot
                pass
        return configRobot["urlPagina"]