from asyncio.windows_events import NULL
from LibRpa.api import ConsultaApi
from LibRpa.leerHtml import LeerHtml
from LibRpa.driverRpa import DriverRpa
from LibRpa.utiitario import Utilitario
import datetime
#Servicios
from Service.autosCosmosService import AustosCosmosService
from Service.quieroMiAuto import QuieroMiAuto

#Entity
from Entity.ingresoVehiculo import IngresoVehiculoEntiti

class AustosCosmosController():

    def __init__(self, driverChrome):
        self.quieroMiAuto = QuieroMiAuto()
        self.austosCosmosService = AustosCosmosService()
        self.consultaApi = ConsultaApi()
        self.utilitario = Utilitario()
        self.leerHtml = ""
        self.dataRobots = self.consultaApi.leerConfigJson()["robots"]["data_robots"]
        self.linkConcecionaria = self.utilitario.getLinkPagina(self.dataRobots, "AustosCosmos")["urlPagina"]
        self.linkConsultaNuevos = self.utilitario.getLinkPagina(self.dataRobots, "AustosCosmos")["urlNuevos"]
        self.linkConsultaUsados = self.utilitario.getLinkPagina(self.dataRobots, "AustosCosmos")["urlUsados"]
        self.idPagina = self.utilitario.getIdPaginaOrigen(self.dataRobots, "AustosCosmos")
        self.chrome = driverChrome
        self.Conbustible = None
        self.Cilindros = None
        self.Rendimiento = None
        self.rendimiento = None
        self.color = None
        self.trasmision = None
        self.year = -9999
        pass

    def runVehiculosNueos(self):
        
        listUrlVehiculos = []
        listUrlConsultadas = []

        self.chrome.cambiarPagina(self.linkConsultaNuevos)
        isPaginaSiguiente = False
        self.chrome.buscarXpath("//a[@class='pagenav btn m-next']")
        linkSiguientePagina = self.chrome.getElementoConsulta()

        while False == isPaginaSiguiente:

            self.chrome.buscarXpath("/html/body/main/div[3]/section/div")
            grillaVehiculos = self.chrome.getElementoConsulta()
            
            for elementsVehiculo in grillaVehiculos:
                self.chrome.buscarXpath("article", elementsVehiculo)
                vehiculos = self.chrome.getElementoConsulta()
                for vehiculo in vehiculos:
                    self.chrome.buscarXpath("a", vehiculo)
                    elementVehiculo = self.chrome.getElementoConsulta()
                    urlVehiculo = self.chrome.getAttribute("href", elementVehiculo[0])
                    listUrlVehiculos.append(urlVehiculo)

            if False != self.chrome.buscarXpath("//a[@class='pagenav btn m-next']"):
                linkElemento = self.chrome.getElementoConsulta()[0]
                linkSiguientePagina = self.chrome.getAttribute("href", linkElemento)

                str_match = list(filter(lambda x: linkSiguientePagina in x, listUrlConsultadas))
                
                if 0 == len(str_match):
                    self.chrome.cambiarPagina(linkSiguientePagina)
                    listUrlConsultadas.append(linkSiguientePagina)
                    #isPaginaSiguiente = True
                else:
                    isPaginaSiguiente = True
                    break
            else:
                isPaginaSiguiente = True
                break
        

        #Obtenemos los datos del vehiculo publicado
        self.getDataVehiculos(listUrlVehiculos)
        self.chrome.cerrarChromeDriver()
        
    def runVehiculosUsados(self):
        
        listUrlVehiculos = []
        listUrlConsultadas = []

        self.chrome.cambiarPagina(self.linkConsultaUsados)
        isPaginaSiguiente = False
        self.chrome.buscarXpath("//a[@class='pagenav btn m-next']")
        linkSiguientePagina = self.chrome.getElementoConsulta()

        while False == isPaginaSiguiente:

            self.chrome.buscarXpath("/html/body/main/div[3]/section/div")
            grillaVehiculos = self.chrome.getElementoConsulta()
            
            for elementsVehiculo in grillaVehiculos:
                self.chrome.buscarXpath("article", elementsVehiculo)
                vehiculos = self.chrome.getElementoConsulta()
                for vehiculo in vehiculos:
                    self.chrome.buscarXpath("a", vehiculo)
                    elementVehiculo = self.chrome.getElementoConsulta()
                    urlVehiculo = self.chrome.getAttribute("href", elementVehiculo[0])
                    listUrlVehiculos.append(urlVehiculo)

            if False != self.chrome.buscarXpath("//a[@class='pagenav btn m-next']"):
                linkElemento = self.chrome.getElementoConsulta()[0]
                linkSiguientePagina = self.chrome.getAttribute("href", linkElemento)

                str_match = list(filter(lambda x: linkSiguientePagina in x, listUrlConsultadas))
                
                if 0 == len(str_match):
                    self.chrome.cambiarPagina(linkSiguientePagina)
                    listUrlConsultadas.append(linkSiguientePagina)
                    #isPaginaSiguiente = True
                else:
                    isPaginaSiguiente = True
                    break
            else:
                isPaginaSiguiente = True
                break

        #Obtenemos los datos del vehiculo publicado
        self.getDataVehiculos(listUrlVehiculos)
        self.chrome.cerrarChromeDriver()

    def getDataVehiculos(self, listLinkVehiculos: list):

        for detalleVehiculo in listLinkVehiculos:
            self.chrome.cambiarPagina(detalleVehiculo)
            marca = ""
            modelo = ""
            version = ""
            year = 0
            kilimetros = ""
            precio = 0

            #Validamos que la pagina web este cargada
            if False != self.chrome.buscarXpath("/html/body/main/article/section/div[1]"):
                tituloVehiculo = self.chrome.getElementoConsulta()[0]
                getDatosVeiculos = tituloVehiculo.find_elements("xpath", "/html/body/main/article/section/div[1]/h1")[0].text
                listDatosVehiculos = getDatosVeiculos.split("\n")

                xpathYear = "/html/body/main/article/section/div[1]/div[2]//span[@itemprop='modelDate']"
                xpathKilometraje = "/html/body/main/article/section/div[1]/div[2]//span[@itemprop='mileageFromOdometer']"

                marca = listDatosVehiculos[0]
                modelo = listDatosVehiculos[1]
                #version = listDatosVehiculos[2]

                self.year = -9999
                if False != self.chrome.buscarXpath(xpathYear, None, 2) and 0 != len(self.chrome.getXpath(xpathYear)):
                    try:
                        self.year = self.chrome.getXpath(xpathYear)[0].text
                    except Exception as err:
                        print(err)
                
                if False != self.chrome.buscarXpath(xpathKilometraje, None, 2) and 0 != len(self.chrome.getXpath(xpathKilometraje)):
                    try:
                        kilimetros = self.chrome.getXpath(xpathKilometraje)[0].text
                    except Exception as err:
                        print(err)
                
                if False != self.chrome.buscarXpath("//strong[@itemprop='price']", None, 2):
                    precio = self.chrome.getXpath("//strong[@itemprop='price']")[0].text
                    precio = self.utilitario.isMoney(precio) 
                
                self.getDetallesTecnicos()
                
                hoy = datetime.date.today()

                ingresoVehiculoEntiti = IngresoVehiculoEntiti()
                ingresoVehiculoEntiti.setLinkVehiculo(detalleVehiculo)
                ingresoVehiculoEntiti.setMarca(marca)
                ingresoVehiculoEntiti.setModelo(modelo)
                ingresoVehiculoEntiti.setYear(hoy.year)
                ingresoVehiculoEntiti.setKilometraje(self.utilitario.isNumber(self.utilitario.isNone(kilimetros[:-3])))
                ingresoVehiculoEntiti.setPrecio(self.utilitario.isNumber(self.utilitario.isNone(precio)))
                ingresoVehiculoEntiti.setConbustible(self.utilitario.isString(self.Conbustible))
                ingresoVehiculoEntiti.setCilindrado(self.utilitario.isNumber(self.utilitario.isNone(self.Cilindros)))
                ingresoVehiculoEntiti.setColor(self.utilitario.isString(self.color))
                ingresoVehiculoEntiti.setRendimiento(self.utilitario.isString(self.rendimiento))

                self.quieroMiAuto.ingresoVehiculo(ingresoVehiculoEntiti.__dict__)
                print()
        self.chrome.cerrarChromeDriver()

    def getDetallesTecnicos(self):
        self.Conbustible = None
        self.Cilindros = None
        self.rendimiento = None
        self.color = None

        if False != self.chrome.buscarXpath("//td[text()='Combustible']/following-sibling::*[1]", None, 2):
            self.Conbustible = self.chrome.getXpath("//td[text()='Combustible']/following-sibling::*[1]")[0].text

        if False != self.chrome.buscarXpath("//td[text()='Cilindrada']/following-sibling::*[1]", None, 2):
            self.Cilindros = (self.chrome.getXpath("//td[text()='Cilindrada']/following-sibling::*[1]")[0].text).split(" ")[0]

        if False != self.chrome.buscarXpath("//td[text()='Rendimiento en ciudad']/following-sibling::*[1]", None, 2):
            self.rendimiento = (self.chrome.getXpath("//td[text()='Rendimiento en ciudad']/following-sibling::*[1]")[0].text).split(" ")[0]
        
        if False != self.chrome.buscarXpath("//span[@itemprop='color']", None, 2):
            self.color = (self.chrome.getXpath("//span[@itemprop='color']")[0].text)
        print()