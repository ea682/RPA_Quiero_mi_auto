from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def buscarXpath(driver, xpathBuscar):
    isEncontrado = False
    for i in range(30):
        try:
            driver.find_element(By.XPATH, xpathBuscar)
            isEncontrado = True
            print("Encontrado")
            break
        except Exception as err:
            #print(err)
            print("No encontrado intento "+str(i))
            pass
        time.sleep(1)
    return isEncontrado

driver = webdriver.Chrome(executable_path=r"C:\Users\erika\Downloads\chromedriver-103\chromedriver.exe")

driver.get('https://santiago.elsilencio.cl/')

if(buscarXpath(driver, "//*[@id='grid-data']")):
    listLink = []
    time.sleep(3)
    cantidadArticle = driver.find_element(By.XPATH, '/html/body/div[5]/div/section[4]/div/div/div/div').find_elements(By.TAG_NAME, "article")
    cantidadModelos = len(cantidadArticle)
    for u in range(1, cantidadModelos):
        article = driver.find_element(By.XPATH, ('/html/body/div[5]/div/section[4]/div/div/div/div/article[{0}]').format(u))
        linkModelo = article.find_element(By.TAG_NAME, 'a').get_attribute('href')
        listLink.append(linkModelo)
    
    
    

    datosModelos = []
    for link in listLink:
        driver.close()
        driver = webdriver.Chrome(executable_path=r"C:\Users\erika\Downloads\chromedriver-103\chromedriver.exe")
        driver.get(link)
        if(buscarXpath(driver, "/html/body/div[5]/div/section[2]/div/div/article/div/div[2]/ul/li[4]")):

            if link == "https://santiago.elsilencio.cl/escorts-vip/nazarena-5bc63dcb37701" or link == "https://santiago.elsilencio.cl/escorts-vip/aleja-629e19d792c59" or link == "https://santiago.elsilencio.cl/escorts-vip/agatha-5ca4fa97da906":
                print(123)
            estatura = driver.find_element(By.XPATH, "/html/body/div[5]/div/section[2]/div/div/article/div/div[2]/ul/li[4]").text
            if(estatura.find("KG") >= 0):
                try:
                    estatura = driver.find_element(By.XPATH, "//*[@id='profile']/div/div/article/div[2]/div[2]/ul/li[3]").text
                    if(estatura.find("KG") >= 0):
                        estatura = driver.find_element(By.XPATH, "/html/body/div[5]/div/section[2]/div/div/article/div/div[2]/ul/li[3]").text
                except:
                    try:
                        estatura = driver.find_element(By.XPATH, "/html/body/div[5]/div/section[2]/div/div/article/div/div[2]/ul/li[3]").text
                        if(estatura.find("KG") >= 0):
                            print("estatura")
                    except:
                        pass
                    pass
                
            datosModelos.append({"Link" :link, "Estatura" :  estatura})
            print(datosModelos)
    
    archi1=open(r"C:\Users\erika\Downloads\datos.txt","w") 
    archi1.write(str(datosModelos)) 
    archi1.close() 
    print("terminado :"+datosModelos)
    



