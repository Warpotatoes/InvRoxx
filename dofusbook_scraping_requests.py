import requests as req

FR_KEYS=['Lvl','PA', 'PM', 'PO', 'Initiative', 'Critique', 'Invocation', 'Soin', 'Vitalité', 'Sagesse', 'Force', 'Intelligence', 'Chance', 'Agilité', 'Puissance', 'Fuite', 'Esq. PA', 'Esq. PM', 'Pods', 'Tacle', 'Ret. PA', 'Ret. PM',  'Do Critique', '% Ré Air', '% Ré Feu', 'Do Eau', 'Do Terre', 'Do Neutre', '% Ré Terre', 'Prospection', 'Do Feu', 'Do Air', 'Do Poussée', 'Ré Neutre', '% Ré Neutre', 'Ré Terre', 'Ré Feu', 'Ré Eau', '% Ré Eau', 'Ré Air', 'Ré Critique', 'Ré Poussée', "Do"]
EN_KEYS=['Lvl','AP', 'MP', 'Range', 'Initiative', 'Critical', 'Summon', 'Heal', 'Vitality', 'Wisdom', 'Strength', 'Intelligence', 'Chance', 'Agility', 'Power', 'Dodge', 'AP Res.', 'MP Res.', 'Pods', 'Lock', 'AP Red', 'MP Red',  'Da Critical', '% Re Air', '% Re Fire', 'Da Water', 'Da Earth', 'Da Neutral', '% Re Earth', 'Prospecting', 'Da Fire', 'Da Air', 'Da Pushback', 'Re Neutral', '% Re Neutral', 'Re Earth', 'Re Fire', 'Re Water', '% Re Water', 'Re Air', 'Re Critical', 'Re Pushback', "Da"]
ES_KEYS=['Lvl','PA', 'PM', 'AL', 'Iniciativa', 'Crítico', 'Invocación', 'Cura', 'Vitalidad', 'Sabiduría', 'Fuerza', 'Inteligencia', 'Suerte', 'Agilidad', 'Potencia', 'Huida', 'Esq. PA', 'Esq. PM', 'Pods', 'Placaje', 'Ret. PA', 'Ret. PM',  'Da Crítico', '% Re Aire', '% Re Fuego', 'Da Agua', 'Da Tierra', 'Da Neutro', '% Re Tierra', 'Prospección', 'Da Fuego', 'Da Aire', 'Da Empuje', 'Re Neutro', '% Re Neutro', 'Re Tierra', 'Re Fuego', 'Re Agua', '% Re Agua', 'Re Aire', 'Re Crítico', 'Re Empuje', "Da"]

ALIASES=dict()
for i in range(len(FR_KEYS)):
    ALIASES[EN_KEYS[i]]=FR_KEYS[i]
    ALIASES[FR_KEYS[i]]=FR_KEYS[i]
    ALIASES[ES_KEYS[i]]=FR_KEYS[i]

TRAD_DB_STATS={
    # stats du perso
    'scroll_vi': 'Vitalité',
    'scroll_sa': 'Sagesse',
    'scroll_fo': 'Force',
    'scroll_in': 'Intelligence',
    'scroll_ch': 'Chance',
    'scroll_ag': 'Agilité',
    'base_vi': 'Vitalité',
    'base_sa': 'Sagesse',
    'base_fo': 'Force',
    'base_in': 'Intelligence',
    'base_ch': 'Chance',
    'base_ag': 'Agilité',

    #fm global
    'pa': "PA",
    'pm': "PM",
    'po': "PO",
    'vi': "Vitalité",
    'sa': "Sagesse",
    'fo': "Force",
    'in': "Intelligence",
    'ch': "Chance",
    'ag': "Agilité",
    'pu': "Puissance",
    'ii': "Initiative",
    'cc': "Critique",
    'ic': "Invocation",
    'so': "Soin",
    'pp': "Prospection",
    'fu': "Fuite",
    'ta': "Tacle",
    'dmg': "Do",
    'dnf': "Do Neutre",
    'dtf': "Do Terre",
    'dff': "Do Feu",
    'def': "Do Eau",
    'daf': "Do Air",
    'dc': "Do Critique",
    'dp': "Do Poussée",
    'dw': "non attribué",
    'ds': "non attribué",
    'dm': "non attribué",
    'dd': "non attribué",
    'deg': "non attribué",
    'rn': "Ré Neutre",
    'rt': "Ré Terre",
    'rf': "Ré Feu",
    're': "Ré Eau",
    'ra': "Ré Air",
    'rnp': "% Ré Neutre",
    'rtp': "% Ré Terre",
    'rfp': "% Ré Feu",
    'rep': "% Ré Eau",
    'rap': "% Ré Air",
    'rc': "Ré Critique",
    'rp': "Ré Poussée",
    'rm': "non attribué",
    'rd': "non attribué",
    'rw': "non attribué",
    'epa': "Esq. PA",
    'epm': "Esq. PM",
    'rpa': "Ret. PA",
    'rpm': "Ret. PM",
    'pd': "Pods",
    'pi': "non attribué",
    'pip': "non attribué",
    'rv': "non attribué",

}

def get_db_id(short_url):
    try:
        response = req.get(short_url, allow_redirects=True)
        spl=response.url.split("/")
        return spl[5][:-3]  
        # Retourne l'URL finale après toutes les redirections
    except req.RequestException as e:
        print(f"Erreur lors de la requête: {e}")
        return None
    
def get_db_data(url):
    db_id=get_db_id(url)
    resp = req.get("https://touch.dofusbook.net/stuffs/touch/public/"+str(db_id),allow_redirects=True)
    return resp.json()

def get_stats(url):
    data= get_db_data(url)

    perso_stats=data["stuffStats"] # 1 element = 1 stat
    fmitems=data["fmItems"] # chaque element est un item sous forme dict, chaque element d'un item est un fm qui lui est rajouté
    fmglobal=data["fmGlobal"] #  1 element = 1 stat
    items=data["items"] #list d'items, chaque item est un dict dont la clef "effects" est une liste d'effets où chaque effet est un dict contenant les clefts suivantes 'name': 'nomdelastat','type': 'E', 'min': 0,'max': 0,
    panos=data["cloths"] # list de pano, chaque item est un dict dont la clef "effects" est une liste d'effets où chaque effet est un dict contenant les clefts suivantes 'name': 'nomdelastat','type': 'E', 'value' : 1
    

    perso={key: 0 for key in FR_KEYS}

    perso["Lvl"]=data["stuff"]["character_level"]
    perso["db_name"]=data["stuff"]["name"]
    perso["PA"]=7
    if perso["Lvl"]<100:
        perso["PA"]-=1
    perso["PM"]=3
    perso["Invocation"]=1
    perso["Vitalité"]=50+5*perso["Lvl"]

    for elt in perso_stats:
        perso[TRAD_DB_STATS[elt]]+=perso_stats[elt]
    
    for elt in fmglobal:
        perso[TRAD_DB_STATS[elt]]+=fmglobal[elt]
    
    for item in fmitems:
        for elt in fmitems[item]:
            perso[TRAD_DB_STATS[elt]]+=fmitems[item][elt]
    
    for item in items:
        for stat in item["effects"]:
            if stat["type"]=='E':
                if stat["min"]>=0:
                    perso[TRAD_DB_STATS[stat["name"]]]+=stat["max"]
                else:
                    perso[TRAD_DB_STATS[stat["name"]]]+=stat["min"]

    for pano in panos:
        for stat in pano["effects"]:
            if stat["type"]=='E':
                perso[TRAD_DB_STATS[stat["name"]]]+=stat["value"]

    #bonus dérivés de stats
    # perso["Soin"]+=max(0,perso["Intelligence"]/10//1)
    perso["Fuite"]+=max(0,perso["Chance"]/10//1)
    perso["Tacle"]+=max(0,perso["Agilité"]/10//1)
    perso["Esq. PA"]+=max(0,perso["Sagesse"]/10//1)
    perso["Esq. PM"]+=max(0,perso["Sagesse"]/10//1)
    perso["Ret. PA"]+=max(0,perso["Sagesse"]/10//1)
    perso["Ret. PM"]+=max(0,perso["Sagesse"]/10//1)
    perso["Initiative"]+=max(0,perso["Intelligence"])+max(0,perso["Chance"])+max(0,perso["Agilité"])+max(0,perso["Force"])

    
    return perso
