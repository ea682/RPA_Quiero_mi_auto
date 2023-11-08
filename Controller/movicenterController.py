from LibRpa.api import ConsultaApi
from LibRpa.utiitario import Utilitario

#Servicios
from Service.movicenterService import MovicenterService
from Service.quieroMiAuto import QuieroMiAuto

#Entti
from Entity.ingresoVehiculo import IngresoVehiculoEntiti

class MovicenterController():
    
    def __init__(self):
        self.quieroMiAuto = QuieroMiAuto()
        self.movicenterService = MovicenterService()
        self.consultaApi = ConsultaApi()
        self.utilitario = Utilitario()

        self.dataRobots = self.consultaApi.leerConfigJson()["robots"]["data_robots"]
        self.linkConcecionaria = self.utilitario.getLinkPagina(self.dataRobots, "Movicenter")['urlPagina']
        self.idPagina = self.utilitario.getIdPaginaOrigen(self.dataRobots, "Movicenter")
        pass

    def runVehiculosNuevos(self):
        getKilometraje = None
        getCilindrado = None
        getColor = None
        getRendimiento = None

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
                            getKilometraje = self.utilitario.isNumber(self.utilitario.isNone(vehiculo["value"]))
                        if "Cilindrada" == vehiculo["title"]:
                            getCilindrado = self.utilitario.isNumber(self.utilitario.isNone(vehiculo["value"]))
                        if "Color" == vehiculo["title"]:
                            getColor = self.utilitario.isNone(vehiculo["value"])
                        if "Rendimiento Km/L" == vehiculo["title"]:
                            getRendimiento = self.utilitario.isNone(vehiculo["value"])
                else:
                    getKilometraje = 0,
                    getCilindrado = self.utilitario.isNumber(self.utilitario.isNone(vehiculoNuevo["cilindrada"])),
                    getColor = self.utilitario.isNone(vehiculoNuevo["color"]),
                    getRendimiento = self.utilitario.isNone(None),
                
                ingresoVehiculoEntiti = IngresoVehiculoEntiti(
                    self.idPagina,
                    self.utilitario.isNone(vehiculoNuevo["brand"]), 
                    self.utilitario.isNone(vehiculoNuevo["model"]),
                    self.utilitario.isNone(vehiculoNuevo["bodyWork"]),
                    self.utilitario.isNone(linkVehiculo),
                    self.utilitario.isNone(listPhotos),
                    self.utilitario.isNumber(self.utilitario.isNone(vehiculoNuevo["price"])),
                    self.utilitario.isNone(vehiculoNuevo["fuel"]),
                    self.utilitario.isNone(vehiculoNuevo["country"]),
                    self.utilitario.isNone(vehiculoNuevo["traction"]),
                    self.utilitario.isNumber(self.utilitario.isNone(getKilometraje)),
                    self.utilitario.isNumber(self.utilitario.isNone(getCilindrado)),
                    self.utilitario.isNone(str(getColor).replace("(", "").replace(",)", "")),
                    self.utilitario.isNone(str(getRendimiento).replace("(", "").replace(",)", "")),
                    self.utilitario.isNumber(self.utilitario.isNone(str(vehiculoNuevo["year"]).replace("(", "").replace(",)", ""))),
                )

                self.quieroMiAuto.ingresoVehiculo(ingresoVehiculoEntiti.__dict__)
        else:
            print("Problemas con la API de Movicenter")
