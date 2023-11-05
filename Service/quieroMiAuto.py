from LibRpa.api import ConsultaApi

class QuieroMiAuto:

    def __init__(self):
        self.consultaApi = ConsultaApi()
        self.configApiQuieroMiAuto = self.consultaApi.leerConfigJson()["API"]
        self.urlIngresoVehiculo = self.configApiQuieroMiAuto["URL_API"]
        pass

    def ingresoVehiculo(self, jsonRequest):
        rutaCompleta = self.urlIngresoVehiculo + self.configApiQuieroMiAuto["URL_DATA_VEHICULO"]
        apiQuieroMiAuto = ConsultaApi(rutaCompleta, "POST", jsonRequest)
        responseApiQuieroMiAuto = apiQuieroMiAuto.consultaApi()
        return responseApiQuieroMiAuto
