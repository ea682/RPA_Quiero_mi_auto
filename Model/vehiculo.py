class Vehiculo:
    def __init__(self, idConcecionaria, idVehiculoPagina, marca, modelo, version, carroceria,  linkVehiculo):
        self.idConcecionaria = idConcecionaria
        self.idVehiculoPagina = idVehiculoPagina
        self.marca = marca
        self.modelo = modelo
        self.version = version
        self.carroceria = carroceria
        self.linkVehiculo = linkVehiculo
        pass

    def getIdConcecionaria(self):
        return self.idConcecionaria

    def getIdVehiculoPagina(self):
        return self.idVehiculoPagina
    
    def getMarca(self):
        return self.marca
    
    def getModelo(self):
        return self.modelo

    def getVersion(self):
        return self.version

    def getCarroceria(self):
        return self.carroceria

    def getLinkVehiculo(self):
        return self.linkVehiculo
