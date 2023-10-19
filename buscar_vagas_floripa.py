from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from auxiliares import gravar_json
from time import sleep


"""
Busca vagas de emprego no site https://www.vagasfloripa.com.br/vagas/.
"""
option = webdriver.ChromeOptions()
option.add_argument("start-maximized")
nav = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
    
url = "https://www.vagasfloripa.com.br/vagas/"

nav.get(url)

nav.find_elements('xpath', '//*[@id="list-vacancy"]/div/table/tbody/tr')
