import requests

class consultaApi:

    def __init__(self, configRobot):
        self.urlPagina = configRobot.getApiUrlNuevos()
        self.tipoConsulta = configRobot.getTipoConsulta()
        self.jsonConsulta = configRobot.getJsonConsulta()[0]
        pass

    def consultaApi(self):
        try:
            if(self.tipoConsulta == "GET"):
                response = requests.get(self.urlPagina)
                if(response.status_code == 200):
                    return response.json()
                else:
                    print("Codigo de respuesta api : "+response.status_code)
                    print("Mensaje de respuesta : "+response)
                    pass
            if(self.tipoConsulta == "POST"):
                response = requests.post(self.urlPagina, json=self.jsonConsulta)
                if(response.status_code == 200):
                    return response.json()
                else:
                    print("Codigo de respuesta api : "+response.status_code)
                    print("Mensaje de respuesta : "+response)
                    pass
        except ValueError as err:
            print(err.args)
            pass
        
        