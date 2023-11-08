class Utilitario:

    def __init__(self):

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
    
    def isNumber(self, datoValidar):
        datoValidar = str(datoValidar).replace("(", "").replace(",)", "").replace("'", "").split(".")[0]
        if None != datoValidar and '' != datoValidar and 'NULL' != datoValidar:
            return int(datoValidar)
        else:
            return 0
        
    def getLinkPagina(self, dataRobots, nombreRobot):
        configRobot = []
        for robot in dataRobots:
            if robot["nombreRobot"] == nombreRobot:
                configRobot = robot
                return configRobot
        if len(configRobot) == 0:
            return None

        