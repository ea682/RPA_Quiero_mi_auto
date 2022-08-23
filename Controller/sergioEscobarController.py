from asyncio.windows_events import NULL
from Lib.api import ConsultaApi
from Lib.leerHtml import LeerHtml

from Service.sergioEscobarService import SergioEscobarService
from Service.quieroMiAuto import QuieroMiAuto

from Entity.ingresoVehiculo import IngresoVehiculoEntiti

class SergioEscobarController():

    def __init__(self):
        self.quieroMiAuto = QuieroMiAuto()
        self.sergioEscobarService = SergioEscobarService()
        self.consultaApi = ConsultaApi()
        self.leerHtml = ""
        self.dataRobots = self.consultaApi.leerConfigJson()["robots"]["data_robots"]
        self.linkConcecionaria = self.getLinkPagina()
        pass

    def run(self):
        responseApiSergioEscobar = self.sergioEscobarService.getNuevosAutos()["posts"]
        for vehiculoNuevo in responseApiSergioEscobar:
            
            linkPhotos = []
            linkPhotos = self.obtenerImgVehiculo(vehiculoNuevo["permalink"])
            ingresoVehiculo = IngresoVehiculoEntiti(
                vehiculoNuevo["_ceswp_brand_name"], 
                vehiculoNuevo["_ceswp_model_name"],
                "",
                vehiculoNuevo["permalink"],
                linkPhotos,
                int(vehiculoNuevo["_ceswp_price_list"]),
            )
            self.quieroMiAuto.ingresoVehiculo(ingresoVehiculo.__dict__)
        print(responseApiSergioEscobar)
        pass


    def obtenerImgVehiculo(self, linkVehiculo):
        arrayImg = []
        htmlVehiculo = self.sergioEscobarService.getHtmlVehiculos(linkVehiculo, "GET")
        htmlVehiculo = htmlVehiculo.text
        self.leerHtml = LeerHtml(htmlVehiculo)
        arrayImg.append(self.obtenerImgPrincipal())
        imgsVehiculo = self.obtenerImgsVehiculo()
        for imgVehiculo in imgsVehiculo:
            arrayImg.append(imgVehiculo)
        
        return arrayImg

    def obtenerImgsVehiculo(self):
        divImgs = self.leerHtml.buscarEtiquetaClase("div", "slider-gallery-int")
        return self.leerHtml.obtenerImgenes(divImgs)

    def obtenerImgPrincipal(self):
        divImgPrincipal = self.leerHtml.buscarEtiquetaClase("div", "img_model_mobile hidden-desktop text-center")
        return self.leerHtml.obtenerImg(divImgPrincipal)

    def getLinkPagina(self):
        configRobot = []
        for robot in self.dataRobots:
            if robot["nombreRobot"] == "sergioescobar":
                configRobot = robot
                pass
        return configRobot["urlPagina"]