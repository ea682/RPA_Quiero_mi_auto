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
        self.idPagina = self.getLinkPagina()
        pass

    def runVehiculosNuevos(self):
        getKilometraje = None
        getCilindrado = None
        getColor = None
        getRendimiento = None
        getYear = None

        reponseMovicentar = self.movicenterService.getNuevosAutos()
        if None != reponseMovicentar:
            dataVehiculosNuevos = reponseMovicentar["data"]

            for vehiculoNuevo in dataVehiculosNuevos:
                linkVehiculo = self.linkConcecionaria+"/autos/"+vehiculoNuevo["key"]
                listPhotos = vehiculoNuevo["photos"]
                if type(listPhotos) == str:
                    listPhotos = listPhotos[2:-2].replace(" ", "").replace("\"", "").split(",")
                    
                if "api_nuevos" != vehiculoNuevo["type"]:
                    for vehiculo in vehiculoNuevo["listFeatures"]:
                        if "Kilometraje" == vehiculo["title"]:
                            getKilometraje = self.isNumber(self.isNone(vehiculo["value"]))
                        if "Cilindrada" == vehiculo["title"]:
                            getCilindrado = self.isNumber(self.isNone(vehiculo["value"]))
                        if "Color" == vehiculo["title"]:
                            getColor = self.isNone(vehiculo["value"])
                        if "Rendimiento Km/L" == vehiculo["title"]:
                            getRendimiento = self.isNone(vehiculo["value"])
                else:
                    getKilometraje = 0,
                    getCilindrado = self.isNumber(self.isNone(vehiculoNuevo["cilindrada"])),
                    getColor = self.isNone(vehiculoNuevo["color"]),
                    getRendimiento = self.isNone(None),
                
                ingresoVehiculoEntiti = IngresoVehiculoEntiti(
                    self.isNone(vehiculoNuevo["brand"]), 
                    self.isNone(vehiculoNuevo["model"]),
                    self.isNone(vehiculoNuevo["bodyWork"]),
                    self.isNone(linkVehiculo),
                    self.isNone(listPhotos),
                    self.isNumber(self.isNone(vehiculoNuevo["price"])),
                    self.isNone(vehiculoNuevo["fuel"]),
                    self.isNone(vehiculoNuevo["country"]),
                    self.isNone(vehiculoNuevo["traction"]),
                    self.isNumber(self.isNone(getKilometraje)),
                    self.isNumber(self.isNone(getCilindrado)),
                    self.isNone(str(getColor).replace("(", "").replace(",)", "")),
                    self.isNone(str(getRendimiento).replace("(", "").replace(",)", "")),
                    self.isNumber(self.isNone(str(vehiculoNuevo["year"]).replace("(", "").replace(",)", ""))),
                )

                self.quieroMiAuto.ingresoVehiculo(ingresoVehiculoEntiti.__dict__)
        else:
            print("Problemas con la API de Movicenter")

    def getLinkPagina(self):
        configRobot = []
        for robot in self.dataRobots:
            if robot["nombreRobot"] == "movicenter":
                configRobot = robot
                pass
        return configRobot["urlPagina"]
    
    def getIdPaginaOrigen(self):
        configRobot = []
        for robot in self.dataRobots:
            if robot["nombreRobot"] == "Movicenter":
                configRobot = robot
                pass
        return configRobot["idPagina"]
    
    def isNone(self, datoValidar):
        if None == datoValidar:
            return "NULL"
        return datoValidar
    
    def isNumber(self, datoValidar):
        datoValidar = str(datoValidar).replace("(", "").replace(",)", "").replace("'", "").split(".")[0]
        if None != datoValidar and '' != datoValidar and 'NULL' != datoValidar:
            return int(datoValidar)
        else:
            return 0