import ast
from Service.movicenterService import MovicenterService
from Service.quieroMiAuto import QuieroMiAuto

from Entity.ingresoVehiculo import IngresoVehiculoEntiti

from LibRpa.api import ConsultaApi

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
        if None != reponseMovicentar:
            dataVehiculosNuevos = reponseMovicentar["data"]
            for vehiculoNuevo in dataVehiculosNuevos:
                linkVehiculo = self.linkConcecionaria+"/autos/"+vehiculoNuevo["key"]
                listPhotos = vehiculoNuevo["photos"]
                if type(listPhotos) == str:
                    listPhotos = listPhotos[2:-2].replace(" ", "").replace("\"", "").split(",")
                ingresoVehiculoEntiti = IngresoVehiculoEntiti(
                    self.isNone(vehiculoNuevo["brand"]), 
                    self.isNone(vehiculoNuevo["model"]),
                    self.isNone(vehiculoNuevo["bodyWork"]),
                    self.isNone(linkVehiculo),
                    self.isNone(listPhotos),
                    self.isNone(int(vehiculoNuevo["price"])),
                )

                self.quieroMiAuto.ingresoVehiculo(ingresoVehiculoEntiti.__dict__)
                print()
        else:
            print("Problemas con la API de Movicenter")

    def getLinkPagina(self):
        configRobot = []
        for robot in self.dataRobots:
            if robot["nombreRobot"] == "movicenter":
                configRobot = robot
                pass
        return configRobot["urlPagina"]
    
    def isNone(self, datoValidar):
        if None == datoValidar:
            return "NULL"
        return datoValidar