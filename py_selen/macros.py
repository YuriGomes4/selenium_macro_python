from asyncio.windows_events import NULL
from inspect import Parameter
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class selen():

    brwser = callable
    ErrorLog = callable
    SuccessLog = callable

    def ag_miss(xxpath, nome="none"):
        if nome == "none":
            nome = xxpath
        
        while True:
            try:
                selen.brwser.find_element(By.XPATH, xxpath).click()
            except:
                selen.SuccessLog("ag_miss: " + nome + " sumiu")
                break
            else:
                selen.ErrorLog("ag_miss: " + nome + " não sumiu")

    def wait_click_xpath(xxpath, nome="none"):
        if nome == "none":
            nome = xxpath
        
        while True:
            try:
                elem = WebDriverWait(selen.brwser, 2).until(
                EC.element_to_be_clickable((By.XPATH, xxpath)) 
            )
            except:
                selen.ErrorLog("wait_click_xpath: " + nome + " não encontrado")
            else:
                while True:
                    try:
                        selen.brwser.find_element(By.XPATH, xxpath).click()
                    except:
                        selen.ErrorLog("wait_click_xpath: " + nome + " não pode ser clicado")
                        #sleep(1)
                    else:
                        selen.SuccessLog("wait_click_xpath: " + nome + " foi clicado")
                        break

                break

    def try_click_element(eleme, nome="none"):
        if nome == "none":
            nome = eleme

        Bool = False
        
        try:
            elem = WebDriverWait(selen.brwser, 2).until(
            EC.element_to_be_clickable(eleme) 
        )
        except:
            Bool = False
            selen.ErrorLog("wait_click_xpath: " + nome + " não encontrado")
        else:
            try:
                eleme.click()
            except:
                Bool = False
                selen.ErrorLog("wait_click_xpath: " + nome + " não pode ser clicado")
                #sleep(1)
            else:
                Bool = True
                selen.SuccessLog("wait_click_xpath: " + nome + " foi clicado")

        return Bool

    def try_click_xpath(xxpath, nome="none"):
        if nome == "none":
            nome = xxpath

        Bool = False
        
        try:
            elem = WebDriverWait(selen.brwser, 30).until(
            EC.element_to_be_clickable((By.XPATH, xxpath)) 
        )
        except:
            Bool = False
            selen.ErrorLog("wait_click_xpath: " + nome + " não encontrado")
        else:
            try:
                selen.brwser.find_element(By.XPATH, xxpath).click()
            except:
                Bool = False
                selen.ErrorLog("wait_click_xpath: " + nome + " não pode ser clicado")
                #sleep(1)
            else:
                Bool = True
                selen.SuccessLog("wait_click_xpath: " + nome + " foi clicado")

        return Bool


    def wait_click_selector(selector, nome="none"):
        if nome == "none":
            nome = selector
        
        while True:
            try:
                elem = WebDriverWait(selen.brwser, 2).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, selector)) 
            )
            except:
                selen.ErrorLog("wait_click_selector: " + nome + " não encontrado")
            else:
                while True:
                    try:
                        selen.brwser.find_element(By.CSS_SELECTOR, selector).click()
                    except:
                        selen.ErrorLog("wait_click_selector: " + nome + " não pode ser clicado")
                        #sleep(1)
                    else:
                        selen.SuccessLog("wait_click_selector: " + nome + " foi clicado")
                        break

                break

    def wait_click_element(eleme, nome="none"):
        if nome == "none":
            nome = str(eleme)
        
        while True:
            try:
                elem = WebDriverWait(selen.brwser, 2).until(
                EC.element_to_be_clickable(eleme) 
            )
            except:
                selen.ErrorLog("wait_click_element: " + nome + " não encontrado")
            else:
                while True:
                    try:
                        eleme.click()
                    except:
                        selen.ErrorLog("wait_click_element: " + nome + " não pode ser clicado")
                        #sleep(1)
                    else:
                        selen.SuccessLog("wait_click_element: " + nome + " foi clicado")
                        break

                break

    def ag_clickable(xxpath, nome="none"):
        if nome == "none":
            nome = xxpath
        
        while True:
            try:
                elem = WebDriverWait(selen.brwser, 30).until(
                EC.element_to_be_clickable((By.XPATH, xxpath)) 
            )
            except:
                selen.ErrorLog("ag_clickable: " + str(nome) + " não pode ser clicado")
                #sleep(1)
            else:
                selen.SuccessLog("ag_clickable: " + str(nome) + " pode ser clicado")
                break

    def ag_presence(xxpath, nome="none"):
        if nome == "none":
            nome = xxpath
        
        while True:
            try:
                elem = WebDriverWait(selen.brwser, 30).until(
                EC.presence_of_element_located((By.XPATH, xxpath)) 
            )
            except:
                selen.ErrorLog("ag_presence: " + nome + " não está presente")
            else:
                selen.SuccessLog("ag_presence: " + nome + " está presente")
                break

    def click_sendkeys(xxpath, keys, nome="none"):
        if nome == "none":
            nome = xxpath
        
        while True:
            try:
                ele = selen.brwser.find_element(By.XPATH, xxpath)
            except:
                selen.ErrorLog("click_sendkeys: " + nome + " não foi encontrado")
                sleep(1)
            else:
                selen.wait_click_xpath(xxpath, nome)
                selen.SuccessLog("click_sendkeys: " + nome + " foi clicado")
                try:
                    ele.send_keys(Keys.CONTROL + "a")
                    ele.send_keys(Keys.BACK_SPACE)
                    ele.clear()
                    ele.send_keys(keys)
                except:
                    sleep(1)
                else:
                    selen.SuccessLog("click_sendkeys: " + nome + " foi digitado")
                    break

    def remove_element_xpath(xxpath, nome="none"):
        if nome == "none":
            nome = xxpath
        
        while True:
            try:
                selen.brwser.execute_script("var l = document.evaluate('" + xxpath + "', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue; l.parentNode.removeChild(l);")
            except:
                selen.ErrorLog("remove_element_xpath: " + nome + " não foi encontrado")
            else:
                selen.SuccessLog("remove_element_xpath: " + nome + " foi removido")
                break

    def remove_element(element, nome="none"):
        if nome == "none":
            nome = str(element)
        
        while True:
            try:
                selen.brwser.execute_script("""
                var element = arguments[0];
                element.parentNode.removeChild(element);
                """, element)
            except:
                selen.ErrorLog("remove_element: " + nome + " não foi encontrado")
            else:
                selen.SuccessLog("remove_element: " + nome + " foi removido")
                break

    def wait_copy_xpath(xxpath, nome="none"):
        if nome == "none":
            nome = xxpath
        
        texto = ""

        while True:
            try:
                elem = WebDriverWait(selen.brwser, 2).until(
                EC.element_to_be_clickable((By.XPATH, xxpath)) 
            )
            except:
                selen.ErrorLog("wait_copy_xpath: " + nome + " não foi copiado")
            else:
                while True:
                    try:
                        texto = selen.brwser.find_element(By.XPATH, xxpath).text
                    except:
                        sleep(1)
                        #browser.find_element(By.XPATH, xxpath).click()
                    else:
                        selen.SuccessLog("wait_copy_xpath: " + nome + " foi copiado")
                        break

                break

        return texto