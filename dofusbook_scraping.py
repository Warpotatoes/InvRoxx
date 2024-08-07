
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import selenium.common.exceptions as sele_excep

# from selenium.webdriver.edge.service import Service
# from selenium.webdriver.edge.options import Options

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

import re


FR_KEYS=['PdV', 'PP', 'PA', 'PM', 'PO', 'Initiative', 'Critique', 'Invocation', 'Soin', 'Vitalité', 'Sagesse', 'Force', 'Intelligence', 'Chance', 'Agilité', 'Puissance', 'Fuite', 'Esq. PA', 'Esq. PM', 'Pods', 'Tacle', 'Ret. PA', 'Ret. PM', 'Niv. Stuff', 'Do Critique', '% Ré Air', '% Ré Feu', 'Do Eau', 'Do Terre', 'Do Neutre', '% Ré Terre', 'Prospection', 'Do Feu', 'Do Air', 'Do Poussée', 'Ré Neutre', '% Ré Neutre', 'Ré Terre', 'Ré Feu', 'Ré Eau', '% Ré Eau', 'Ré Air', 'Ré Critique', 'Ré Poussée']
EN_KEYS=['PdV', 'PP', 'AP', 'MP', 'Range', 'Initiative', 'Critical', 'Summon', 'Heal', 'Vitality', 'Wisdom', 'Strength', 'Intelligence', 'Chance', 'Agility', 'Power', 'Dodge', 'AP Res.', 'MP Res.', 'Pods', 'Lock', 'AP Red', 'MP Red', 'Niv. Stuff', 'Da Critical', '% Re Air', '% Re Fire', 'Da Water', 'Da Earth', 'Da Neutral', '% Re Earth', 'Prospecting', 'Da Fire', 'Da Air', 'Da Pushback', 'Re Neutral', '% Re Neutral', 'Re Earth', 'Re Fire', 'Re Water', '% Re Water', 'Re Air', 'Re Critical', 'Re Pushback']
ES_KEYS=['PdV', 'PP', 'PA', 'PM', 'AL', 'Iniciativa', 'Crítico', 'Invocación', 'Cura', 'Vitalidad', 'Sabiduría', 'Fuerza', 'Inteligencia', 'Suerte', 'Agilidad', 'Potencia', 'Huida', 'Esq. PA', 'Esq. PM', 'Pods', 'Placaje', 'Ret. PA', 'Ret. PM', 'Niv. Stuff', 'Da Crítico', '% Re Aire', '% Re Fuego', 'Da Agua', 'Da Tierra', 'Da Neutro', '% Re Tierra', 'Prospección', 'Da Fuego', 'Da Aire', 'Da Empuje', 'Re Neutro', '% Re Neutro', 'Re Tierra', 'Re Fuego', 'Re Agua', '% Re Agua', 'Re Aire', 'Re Crítico', 'Re Empuje']

ALIASES=dict()
for i in range(len(FR_KEYS)):
    ALIASES[EN_KEYS[i]]=FR_KEYS[i]
    ALIASES[FR_KEYS[i]]=FR_KEYS[i]
    ALIASES[ES_KEYS[i]]=FR_KEYS[i]

def get_stats(url):
    if re.match("https://d-bk.net/(fr|en|es)/t/[a-zA-Z0-9]{4}",url):
        options = Options() 
        options.add_argument("--headless")
        
        # service = Service(executable_path="./webdriver/msedgedriver.exe")
        # driver = webdriver.Edge(service=service,options=options)

        service = Service(executable_path="./webdriver/chromedriver")
        driver = webdriver.Chrome(service=service,options=options)
        try :
            driver.get(url)
        except :
            driver.close()
            return 'Erreur : echec de la requete'

        delay = 10 # seconds

        try:
            WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'stat')))
        except TimeoutException:
            return 'Erreur : la requete a mis trop de temps'

        stats=driver.find_elements(By.CLASS_NAME,"stat")
        perso={key: -1000 for key in FR_KEYS}
        for stat in stats:#[:44]:
            s=stat.text.split("\n")
            if len(s)>1:
                if int(s[0])>perso[ALIASES[s[1]]]:
                    perso[ALIASES[s[1]]]=int(s[0])
        driver.close()
    else:
        return ("Mauvais lien, copiez collez le lien en haut a droite de la page dofusbook.") 

    
    return perso
