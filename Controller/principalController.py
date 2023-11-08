from Controller.movicenterController import MovicenterController
from Controller.sergioEscobarController import SergioEscobarController

class PrincipalController:

    def __init__(self):
        self.movicenterController = MovicenterController()
        self.SergioEscobarController = SergioEscobarController()
        pass

    def runRobots(self):
        self.movicenterController.runVehiculosNuevos()
        self.SergioEscobarController.run()

        print("Se finaliza proceso de extraccion de informacion")
        pass