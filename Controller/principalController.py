from Controller.movicenterController import MovicenterController
from Controller.sergioEscobarController import SergioEscobarController
from Controller.autosCosmosController import AustosCosmosController
from LibRpa.driverRpa import DriverRpa
from threading import Thread

class PrincipalController:

    def __init__(self):
        self.movicenterController = MovicenterController()
        #self.sergioEscobarController = SergioEscobarController()
        
        self.threads = []
        pass

    def runRobots(self):
        #self.movicenterController.runVehiculosNuevos()
        #self.sergioEscobarController.run()
        t1 = Thread(target=self.runT1)
        t2 = Thread(target=self.runT2)
        
        t1.start()
        t2.start()

        print("Se finaliza proceso de extraccion de informacion")
        pass

    def runT1(self):
        chromeDriver = DriverRpa()
        austosCosmosController = AustosCosmosController(chromeDriver)
        austosCosmosController.runVehiculosNueos()

    def runT2(self):
        chromeDriver = DriverRpa()
        austosCosmosController = AustosCosmosController(chromeDriver)
        austosCosmosController.runVehiculosUsados()
