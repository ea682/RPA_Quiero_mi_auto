from asyncio.windows_events import NULL
from LibRpa.api import ConsultaApi
from LibRpa.leerHtml import LeerHtml
from LibRpa.utiitario import Utilitario

#Servicios
from Service.sergioEscobarService import SergioEscobarService
from Service.quieroMiAuto import QuieroMiAuto

#Entity
from Entity.ingresoVehiculo import IngresoVehiculoEntiti

class SergioEscobarController():

    def __init__(self):
        self.quieroMiAuto = QuieroMiAuto()
        self.sergioEscobarService = SergioEscobarService()
        self.consultaApi = ConsultaApi()
        self.utilitario = Utilitario()
        self.leerHtml = ""
        self.dataRobots = self.consultaApi.leerConfigJson()["robots"]["data_robots"]
        self.linkConcecionaria = self.utilitario.getLinkPagina(self.dataRobots, "Sergio Escobar")
        self.idPagina = self.utilitario.getIdPaginaOrigen(self.dataRobots, "Sergio Escobar")
        pass

    def run(self):
        if self.linkConcecionaria == 0:
            return NULL
        responseApiSergioEscobar = self.sergioEscobarService.getNuevosAutos()["posts"]
        for vehiculoNuevo in responseApiSergioEscobar:
            
            linkPhotos = []
            linkPhotos = self.obtenerImgVehiculo(vehiculoNuevo["permalink"])
            ingresoVehiculo = IngresoVehiculoEntiti(
                self.idPagina,
                self.utilitario.isNone(vehiculoNuevo["_ceswp_brand_name"]), 
                self.utilitario.isNone(vehiculoNuevo["_ceswp_model_name"]),
                "",
                self.utilitario.isNone(vehiculoNuevo["permalink"]),
                self.utilitario.isNone(linkPhotos),
                self.utilitario.isNumber(self.utilitario.isNone(vehiculoNuevo["_ceswp_price_min"])),
                self.utilitario.isNone(vehiculoNuevo["combustible"]),
                "",
                "",
                0,
                0,
                "",
                "",
                0,
            )
            self.quieroMiAuto.ingresoVehiculo(ingresoVehiculo.__dict__)
        pass


    def obtenerImgVehiculo(self, linkVehiculo):
        arrayImg = []
        htmlVehiculo = self.sergioEscobarService.getHtmlVehiculos(linkVehiculo, "GET")
        #htmlVehiculo = htmlVehiculo.text
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

    