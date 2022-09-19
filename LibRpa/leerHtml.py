from asyncio.windows_events import NULL
from bs4 import BeautifulSoup

class LeerHtml:

    def __init__(self, html) :
        self.html = BeautifulSoup(html, 'html.parser')
        pass

    def buscarEtiquetaClase(self, etiqueta, buscarClass):
        return self.html.find(etiqueta, class_=buscarClass)

    def buscarEtiquetaId(self,etiqueta, buscarID):
        
        return self.html.find(etiqueta, id=buscarID)

    def buscarEtiquetasClase(self, etiqueta, buscarClass):
        return self.html.find(etiqueta, class_=buscarClass)

    def buscarEtiquetasId(self, etiqueta, buscarID ):
        return self.html.find_all(etiqueta, id=buscarID)

    def obtenerImg(self, arrayContents):
        link = ""
        if arrayContents != None and len(arrayContents) != 0:
            for img in arrayContents.contents:
                try:
                    if img.has_attr('src'):
                        link = img['src']
                        break
                except:
                    pass
                pass
            pass
        return link

    def obtenerImgenes(self, arrayContents):
        links = []
        if arrayContents != None and len(arrayContents) != 0:
            for img in arrayContents.contents:
                try:
                    if img.has_attr('src'):
                        links.append(img['src'])
                except:
                    pass
                pass
            pass
        return links
        