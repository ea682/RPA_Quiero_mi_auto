from Model.vehiculo import Vehiculo


class DetalleVehiculo(Vehiculo):

    def __init__(self, idConcecionaria, idVehiculoPagina, marca, modelo, version, carroceria,  linkVehiculo, precio, transmision, combustible, traccion, rendimientoUrbano, origen, alarma, aireAcondicionado, alzaVidriosElectricos, cierreCentralizado, controlesVolante, espejosElectricos, radioDigital, sunroof, volanteAjustable):

        Vehiculo.__init__(self, idConcecionaria, idVehiculoPagina, marca, modelo, version, carroceria,  linkVehiculo)

        self.precio = precio
        self.transmision = transmision
        self.combustible = combustible
        self.traccion = traccion
        self.rendimientoUrbano = rendimientoUrbano
        self.origen = origen
        self.alarma = alarma
        self.aireAcondicionado = aireAcondicionado
        self.alzaVidriosElectricos = alzaVidriosElectricos
        self.cierreCentralizado = cierreCentralizado
        self.controlesVolante = controlesVolante
        self.espejosElectricos = espejosElectricos
        self.radioDigital = radioDigital
        self.sunroof = sunroof
        self.volanteAjustable = volanteAjustable


    def getPrecio(self):
        return self.precio

    def getTransmision(self):
        return self.transmision
    
    def getTransmision(self):
        return self.transmision

    def getTraccion(self):
        return self.traccion

    def getRendimientoUrbano(self):
        return self.rendimientoUrbano

    def getOrigen(self):
        return self.origen

    def getAlarma(self):
        return self.alarma

    def getAireAcondicionado(self):
        return self.aireAcondicionado

    def getAlzaVidriosElectricos(self):
        return self.alzaVidriosElectricos

    def getCierreCentralizado(self):
        return self.cierreCentralizado

    def getControlesVolante(self):
        return self.ControlesVolante

    def getEspejosElectricos(self):
        return self.espejosElectricos

    def getRadioDigital(self):
        return self.radioDigital

    def getSunroof(self):
        return self.sunroof

    def getVolanteAjustable(self):
        return self.VolanteAjustable