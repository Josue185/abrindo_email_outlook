#!/usr/bin/env python
# coding: utf-8

# In[120]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from time import sleep
servico = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=servico)


# In[121]:


#acessando site do e-mail
driver.get("https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1670420148&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3d5341e635-0174-4052-f3dd-acc78e897ced&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015") #Comando para acessar o site
sleep(2)

#colocando e-mail
campoEmail= driver.find_element(By.NAME, 'loginfmt')
campoEmail.send_keys("Seu email")

#Avançando para por a senha
driver.find_element("xpath",'//*[@id="idSIButton9"]').click()
sleep(1)
#colocando senha
CampoSenha= driver.find_element("xpath",'//*[@id="i0118"]')
CampoSenha.send_keys("Sua senha")
sleep(1)
#entrando na conta
driver.find_element("xpath",'//*[@id="idSIButton9"]').click()
sleep(2)

#manter conectado
driver.find_element("xpath",'//*[@id="KmsiCheckboxField"]').click()
#apertando Sim
driver.find_element("xpath",'//*[@id="idSIButton9"]').click()
sleep(2)




