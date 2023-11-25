from LibRpa.api import ConsultaApi

class Utilitario:

    def __init__(self):
        self.consultaApi = ConsultaApi()
        pass

    def getIdPaginaOrigen(self, dataRobots, nombreRobot):
        configRobot = []
        for robot in dataRobots:
            if robot["nombreRobot"] == nombreRobot:
                configRobot = robot
                pass
        return configRobot["idPagina"]
    
    def isNone(self, datoValidar):
        if None == datoValidar:
            return "NULL"
        return datoValidar
    
    def isString(self, datoValidar):
        if None == datoValidar:
            return "NULL"
        return datoValidar
    
    def isNumber(self, datoValidar):
        datoValidar = str(datoValidar).replace("(", "").replace(",)", "").replace("'", "").split(".")[0]
        if None != datoValidar and '' != datoValidar and 'NULL' != datoValidar:
            try:
                return int(datoValidar)
            except Exception as err:
                print("Problemas al convertit a Number: ")
                print(err)
                return -9999
        else:
            return -9999
        
    def getLinkPagina(self, dataRobots, nombreRobot):
        configRobot = []
        for robot in dataRobots:
            if robot["nombreRobot"] == nombreRobot:
                configRobot = robot
                return configRobot
        if len(configRobot) == 0:
            return None
        
    def getHtmlVehiculos(self, link, consulta):
        self.consultaApi = ConsultaApi(link, consulta)
        return self.consultaApi.consultaApi()
    
    def isMoney(self, datoValidar):
        datoValidar = str(datoValidar).replace("(", "").replace(",)", "").replace("'", "").replace("$", "").replace(".", "").replace("us", "")
        if None != datoValidar and '' != datoValidar and 'NULL' != datoValidar:
            try:
                return int(datoValidar)
            except Exception as err:
                print("Problemas al convertit a Number: "+err)
                return -9999
        else:
            return -9999

        