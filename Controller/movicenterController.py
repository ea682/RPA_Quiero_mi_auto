from Model.vehiculo import Vehiculo
from Model.detalleVehiculo import DetalleVehiculo
from Service.api import consultaApi

class MovicenterController():
    
    def __init__(self, robotMovicenterConfig):
        self.idConcecionaria = robotMovicenterConfig.getIdConcecionaria()
        self.configRobot = robotMovicenterConfig
        self.jsonVehiculos = {}
        self.listaVehiculos = []
        pass

    def getListaVehiculos(self):
        return self.listaVehiculos

    def obtenerVehiculosApi(self):
        api = consultaApi(self.configRobot)
        try:
            response = api.consultaApi()
            self.jsonVehiculos = response['data']
        except Exception as ex:
            print(ex)
            pass
        
    def procesarJson(self):
        for dataVehiculo in self.jsonVehiculos:
            self.listaVehiculos.append(self.llenarInfoVehiculo(dataVehiculo))
            self.listaVehiculos.append(self.llenarInfoVehiculo(dataVehiculo))

    def llenarInfoVehiculo(self, dataVehiculo):
        #Creamos link del vehiculo
        linkVehiculo = self.configRobot.getUrlPagina()+"/autos/"+dataVehiculo["key"]
        vehiculo = Vehiculo(
            str(self.idConcecionaria),
            dataVehiculo["key"],
            dataVehiculo["brand"],
            dataVehiculo["model"],
            None,
            dataVehiculo["bodyWork"],
            linkVehiculo,
        )

        return self.llenarDetalleVehiculo(vehiculo, dataVehiculo)
    
    def llenarDetalleVehiculo(self, vehiculo, dataVehiculo):
        detalleVehiculo = DetalleVehiculo(
            vehiculo.getIdConcecionaria(),
            vehiculo.getIdVehiculoPagina(),
            vehiculo.getMarca(),
            vehiculo.getModelo(),
            vehiculo.getVersion(),
            vehiculo.getCarroceria(),
            vehiculo.getLinkVehiculo(),

            dataVehiculo["listPrice"],
            dataVehiculo["transmission"],
            dataVehiculo["fuel"],
            dataVehiculo["traction"],
            None,
            dataVehiculo["country"],
            dataVehiculo["alarm"],
            dataVehiculo["electric_mirrors"],
            dataVehiculo["glassswing"],
            dataVehiculo["central_lock"],
            dataVehiculo["steering_wheel_controls"],
            dataVehiculo["electric_mirrors"],
            dataVehiculo["digital_radio"],
            dataVehiculo["sunroof"],
            dataVehiculo["adjustable_steering_wheel"]
            
            )
        return detalleVehiculo
             
