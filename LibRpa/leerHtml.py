from asyncio.windows_events import NULL
from bs4 import BeautifulSoup
from lxml import html
from lxml import etree
import requests

#page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
#tree = html.fromstring(page.content)
#This will create a list of buyers:
#buyers = tree.xpath('//div[@title="buyer-name"]/text()')
#This will create a list of prices
#prices = tree.xpath('//span[@class="item-price"]/text()')


class LeerHtml:

    def __init__(self, htmlText) :
        self.htmlText = BeautifulSoup(htmlText, 'html.parser')
        self.tree = html.fromstring(htmlText)
        pass

    def getTexto(self):
        return self.htmlText
    
    def converLxmlToBeautifulSoup(self, textLxml):
        textLxml1 = etree.tostring(textLxml[0]).decode()
        textoBeautiful = BeautifulSoup(textLxml1, 'lxml')
        return textoBeautiful
    
    def converBeautifulSoupToLxml(self, textBeautifulSoup):
        textoBeautiful = str(textBeautifulSoup)
        textLxml = html.fromstring(textoBeautiful)
        return textLxml

    def buscarXpath(self, xpath, textoHtml = None, isConvert = False):
        htmlTextBuscar = None
        if None == textoHtml:
            htmlTextBuscar = self.tree
        else:
            if False != isConvert:
                htmlTextBuscar = self.converBeautifulSoupToLxml(textoHtml)
            else:
                htmlTextBuscar = textoHtml

        return htmlTextBuscar.xpath(xpath)
    
    def buscarEtiquetaClase(self, etiqueta, buscarClass, textoHtml = None, isConvert = False):
        htmlTextBuscar = None
        if None == textoHtml:
            htmlTextBuscar = self.htmlText
        else:
            if False != isConvert:
                htmlTextBuscar = self.converLxmlToBeautifulSoup(textoHtml)
            else:
                htmlTextBuscar = textoHtml

        return htmlTextBuscar.find(etiqueta, class_=buscarClass)
    
    def buscarEtiquetasClase(self, etiqueta, buscarClass, textoHtml = None, isConvert = False):
        htmlTextBuscar = None
        if None == textoHtml:
            htmlTextBuscar = self.htmlText
        else:
            if False != isConvert:
                htmlTextBuscar = self.converLxmlToBeautifulSoup(textoHtml)
            else:
                htmlTextBuscar = textoHtml

        return htmlTextBuscar.find_all(etiqueta, class_=buscarClass)

    def buscarEtiquetaId(self,etiqueta, buscarID, textoHtml = None, isConvert = False):
        htmlTextBuscar = None
        if None == textoHtml:
            htmlTextBuscar = self.htmlText
        else:
            if False != isConvert:
                htmlTextBuscar = self.converLxmlToBeautifulSoup(textoHtml)
            else:
                htmlTextBuscar = textoHtml
            
        return htmlTextBuscar.find(etiqueta, id=buscarID)

    def buscarEtiquetasId(self, etiqueta, buscarID , textoHtml = None, isConvert = False):
        htmlTextBuscar = None
        if None == textoHtml:
            htmlTextBuscar = self.htmlText
        else:
            if False != isConvert:
                htmlTextBuscar = self.converLxmlToBeautifulSoup(textoHtml)
            else:
                htmlTextBuscar = textoHtml

        return htmlTextBuscar.find_all(etiqueta, id=buscarID)

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
        