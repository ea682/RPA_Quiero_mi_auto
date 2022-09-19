from asyncio.windows_events import NULL
import os
import requests
import json

class ConsultaApi:

    def __init__(self, urlPagina = NULL, tipoConsulta = NULL, jsonConsulta = NULL):
        self.urlPagina = urlPagina
        self.tipoConsulta = tipoConsulta
        self.jsonConsulta = jsonConsulta
        pass

    def consultaApi(self):
        try:
            if(self.tipoConsulta == "GET"):
                response = requests.get(self.urlPagina)
                if(response.status_code == 200):
                    return response
                else:
                    print("Codigo de respuesta api : "+response.status_code)
                    print("Mensaje de respuesta : "+response)
                    pass
            if(self.tipoConsulta == "POST"):
                response = requests.post(
                    self.urlPagina, json=self.jsonConsulta)
                if(response.status_code == 200 or response.status_code == 201):
                    return response.json()
                else:
                    print("Codigo de respuesta api : "+ str(response.status_code))
                    print("Mensaje de respuesta : "+response.text)
                    pass
        except ValueError as err:
            print("Fallo en la conexion APi: "+self.urlPagina)
            print(err.args)
            pass

    def leerConfigJson(self):
        dataConfig = {}
        rutaConfigJson = 'config.json'
        rutaOrigen = os.path.abspath(os.getcwd())
        rutaCompleta = os.path.join(rutaOrigen, rutaConfigJson)
        with open(rutaCompleta) as file:
            dataConfig = json.load(file)
        return dataConfig
        