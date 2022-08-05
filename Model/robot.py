class Robot:
    def __init__(self, idConcecionaria, nombre, status, urlPagina, apiUrlNuevos, apiUrlUsados, tipoConsulta, jsonConsulta, autos, motociletas, isApi, isSelenium):
        self.idConcecionaria = idConcecionaria
        self.nombre = nombre
        self.status = status
        self.urlPagina = urlPagina
        self.apiUrlNuevos = apiUrlNuevos
        self.apiUrlUsados = apiUrlUsados
        self.tipoConsulta = tipoConsulta
        self.jsonConsulta = jsonConsulta
        self.autos = autos
        self.motociletas = motociletas
        self.isApi = isApi
        self.isSelenium = isSelenium
        pass

    def getIdConcecionaria(self):
        return self.idConcecionaria

    def getNombre(self):
        return self.nombre

    def getStatus(self):
        return self.status

    def getUrlPagina(self):
        return self.urlPagina

    def getApiUrlNuevos(self):
        return self.apiUrlNuevos

    def getApiUrlUsados(self):
        return self.apiUrlUsados

    def getTipoConsulta(self):
        return self.tipoConsulta

    def getJsonConsulta(self):
        return self.jsonConsulta

    def getAutos(self):
        return self.autos

    def getMotociletas(self):
        return self.motociletas

    def getIsApi(self):
        return self.isApi

    def getIsSelenium(self):
        return self.isSelenium
