from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement

class DriverRpa:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.elemento = None
        pass 

    def getElementoConsulta(self) -> WebElement:
        return self.elemento
    
    def getXpath(self, xpathBuscar: str, element = None) -> str:
        try:
            if None != element:
                return self.elemento.find_elements(By.XPATH, xpathBuscar)
            else:
                return self.driver.find_elements(By.XPATH, xpathBuscar)
        except Exception as err:
            print("Problemas al obtener elemento: "+err)
            pass
    
    def buscarXpath(self, xpathBuscar: str, element = None, iteracionesIngresadas = None) -> bool:
        isEncontrado = False
        iteraciones = 30
        if None != iteracionesIngresadas:
            iteraciones = iteracionesIngresadas
        for i in range(iteraciones):
            try:
                if None != element:
                    self.elemento = element.find_elements("xpath", xpathBuscar)
                    pass
                else:
                    self.elemento = self.driver.find_elements("xpath", xpathBuscar)
                if 0 != len(self.elemento):
                    isEncontrado = True
                    print("Intento: "+str(i))
                    print("Elemento encontrado: "+str(self.elemento))
                    break
                else:
                    print("Intento: "+str(i))
                    print("Elemento no encontrado: "+str(self.elemento))
                
                
            except Exception as err:
                print(err)
                print("No encontrado intento "+str(i))
                pass
            time.sleep(1)
        return isEncontrado
    
    def buscarName(self, name: str) -> bool:
        isEncontrado = False
        for i in range(30):
            try:
                self.driver.find_element(By.NAME, name)
                isEncontrado = True
                print("Encontrado")
                break
            except Exception as err:
                #print(err)
                print("No encontrado intento "+str(i))
                pass
            time.sleep(1)
        return isEncontrado
    
    def buscarId(self, id: str) -> bool:
        isEncontrado = False
        for i in range(30):
            try:
                self.driver.find_elements(By.ID, id)
                isEncontrado = True
                print("Encontrado")
                break
            except Exception as err:
                #print(err)
                print("No encontrado intento "+str(i))
                pass
            time.sleep(1)
        return isEncontrado
    
    def buscarClass(self, classTag: str, element = None) -> bool:
        isEncontrado = False
        for i in range(30):
            try:
                if None != element:
                    self.elemento = element.find_elements(By.CLASS_NAME, classTag)
                    pass
                else:
                    self.elemento = self.driver.find_elements(By.CLASS_NAME, classTag)
                isEncontrado = True
                print("Encontrado")
                break
            except Exception as err:
                #print(err)
                print("Problemas para encontrar la class_name "+str(i))
                pass
            time.sleep(1)
        return isEncontrado
    
    def getAttribute(self, nombreAttribute: str, element: WebElement) -> str:
        attriuteEncontrado = ""
        for i in range(30):
            try:
                if "VALUE" == nombreAttribute.upper():
                    return element.get_attribute("value")
                if "NAME" == nombreAttribute.upper():
                    return element.get_attribute("name")
                if "PLACEHOLDER" == nombreAttribute.upper():
                    return element.get_attribute("placeholder")
                if "TYPE" == nombreAttribute.upper():
                    return element.get_attribute("type")
                if "SRC" == nombreAttribute.upper():
                    return element.get_attribute("src")
                if "HREF" == nombreAttribute.upper():
                    return element.get_attribute("href")
                if "ITEMPROP" == nombreAttribute.upper():
                    return element.get_attribute("itemprop")
                break

            
            except Exception as err:
                #print(err)
                print("Problemas para encontrar la class_name "+str(i))
                pass
            time.sleep(1)
        return attriuteEncontrado

    def cambiarPagina(self, urlPagina : str) -> bool:
        isCambioPagina = False
        try:
            self.driver.get(urlPagina)
            isCambioPagina = True
        except Exception as err:
            print("Error cambiar pagina: ")
            print(err)
            pass
        return isCambioPagina
    
    def screenShot(self, direccionImg : str) -> bool:
        isEncontrado = False
        try:
            self.driver.save_screenshot(direccionImg)
            isEncontrado = True
        except Exception as err:
            print("Problemas con ScreenShot: ")
            print(err)
            pass
        return isEncontrado

    def sendKey(self, letra: str, element = None) -> bool:
        isSendKey = False
        try:
            if None != None:
                self.driver.send_keys(letra)
                pass
            else:
                element.send_keys(letra)
            isSendKey = True
        except Exception as err:
            print("Problemas al enviar la send key: ")
            print(err)
            pass
        return isSendKey
    
    def clickElemento(self, element: WebElement) -> bool:
        isOk = False
        try:
            element.click()
            isOk = True
        except Exception as err:
            print("Problemas con funcion click: ")
            print(err)
            pass
        return isOk
    
    def cerrarChromeDriver(self) -> bool:
        isOk = False
        try:
            self.driver.close()
            isOk = True
        except Exception as err:
            print("Problemas al cerrar el driver: ")
            print(err)
            pass
        return isOk
    
    