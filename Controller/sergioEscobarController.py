from Model.vehiculo import Vehiculo
from Service.api import consultaApi

class SergioEscobarController():
    
    def __init__(self, robotSergioEscobar):
        self.idConcecionaria = robotSergioEscobar.getIdConcecionaria()
        self.UrlObtenerVehiculos = robotSergioEscobar.getApiUrl()
        self.jsonVehiculos = {}
        self.listaVehiculos = []
        pass

    def getListaVehiculos(self):
        return self.listaVehiculos

    def obtenerVehiculosApi(self):
        api = consultaApi(self.UrlObtenerVehiculos)
        try:
            response = api.consultaApiGet()
            self.jsonVehiculos = response['posts']
        except Exception as ex:
            print(ex)
            pass
        
    def procesarJson(self):
        for dataVehiculo in self.jsonVehiculos:
            self.listaVehiculos.append(self.llenarInfoVehiculo(dataVehiculo))

    def llenarInfoVehiculo(self, dataVehiculo):
        vehiculo = Vehiculo(
            str(self.idConcecionaria),
            dataVehiculo["post_id"],
            dataVehiculo["_ceswp_brand_name"],
            dataVehiculo["_ceswp_model_name"],
            dataVehiculo["_ceswp_version_name"],
            dataVehiculo["_ceswp_price_amicar"],
            dataVehiculo["transmision"],
            dataVehiculo["combustible"],
            dataVehiculo["permalink"]
        )
        return Vehiculo
            
             

