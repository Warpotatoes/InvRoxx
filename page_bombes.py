import streamlit as st
import dofusbook_scraping_requests as db
image_path='images/'


######################
# Page Title
######################

st.set_page_config(page_title="CalcoBoom",page_icon=image_path+"logo_InvRoxx_tab.png",layout="wide")

st.write("## Calculateur de dégats des bombes et murs")


######################
#SIDEBAR
######################

st.sidebar.image(image_path+"calcoboom_logo_nom_transp.png" )
st.sidebar.page_link("https://d-bk.net/fr/tl/11eJ",label='**Biblio DofusBook**',icon="📚")


db_stats="no_db"

db_link=st.sidebar.text_input("Lien dofusbook",placeholder="https://d-bk.net/fr/t/A7si")
if db_link!='':
    try:
        db_stats=db.get_stats(db_link)  
        if "db_name" in db_stats.keys():
            st.sidebar.write("Stuff sélectionné :")
            st.sidebar.write(" "+db_stats["db_name"])
    except Exception as e:
            st.sidebar.write(f"Erreur dans la récupération des stats : {e}")
    
    # if type(db_stats)==str:
    #     st.sidebar.write(db_stats)
    # else:
    #     st.sidebar.write("Si les stats sont mal récupérées verifiez votre lien ou relancez la recherche, dofusbook bug parfois")
stats_perso={}

st.sidebar.write("# Stats du personnage") 
# st.sidebar.write("(les stats du parchotage et des points investis ne comptent pas pour les dégats des invo, seul l'équipement compte)") 

if db_link=='' or type(db_stats)==str:
    stats_perso["Lvl"]=int(st.sidebar.number_input(label="Lvl",min_value=0,max_value=200,value=200))

    #stats
    stats_perso["Vita"]=int(st.sidebar.text_input("Vitalité globale", value=stats_perso["Lvl"]*5+50, max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))
    stats_perso["Intel"]=int(st.sidebar.text_input("Intelligence", value=0, max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))
    stats_perso["Chance"]=int(st.sidebar.text_input("Chance", value=0, max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))
    stats_perso["Agi"]=int(st.sidebar.text_input("Agilité", value=0, max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))
    stats_perso["pui"]=int(st.sidebar.text_input("Puissance", value=0, max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))

    #do fixes
    stats_perso["Dofeu"]=int(st.sidebar.text_input("Dommages Feu", value=0, max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))
    stats_perso["Doeau"]=int(st.sidebar.text_input("Dommages Eau", value=0, max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))
    stats_perso["Doair"]=int(st.sidebar.text_input("Dommages Air", value=0, max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))

    stats_perso["Do"]=int(st.sidebar.text_input("Dommages", value=0, max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))
else:
    stats_perso["Lvl"]=int(st.sidebar.number_input(label="Lvl",min_value=0,max_value=200,value=db_stats["Lvl"]))

    #stats
    stats_perso["Vita"]=int(st.sidebar.text_input("Vitalité globale", value=db_stats["Vitalité"], max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))
    stats_perso["Intel"]=int(st.sidebar.text_input("Intelligence", value=db_stats["Intelligence"], max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))
    stats_perso["Chance"]=int(st.sidebar.text_input("Chance", value=db_stats["Chance"], max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))
    stats_perso["Agi"]=int(st.sidebar.text_input("Agilité", value=db_stats["Agilité"], max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))
    stats_perso["pui"]=int(st.sidebar.text_input("Puissance", value=db_stats["Puissance"], max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))

    #do fixes
    stats_perso["Dofeu"]=int(st.sidebar.text_input("Dommages Feu", value=db_stats["Do Feu"], max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))
    stats_perso["Doeau"]=int(st.sidebar.text_input("Dommages Eau", value=db_stats["Do Eau"], max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))
    stats_perso["Doair"]=int(st.sidebar.text_input("Dommages Air", value=db_stats["Do Air"], max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))

    stats_perso["Do"]=int(st.sidebar.text_input("Dommages", value=db_stats["Do"], max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))

    # st.sidebar.write(db_stats)

st.sidebar.write("# Boosts sur roublard") 
stats_perso["roub_pui"]=int(st.sidebar.text_input("Puissance", value=0, max_chars=None, key=201, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))
stats_perso["roub_do"]=int(st.sidebar.text_input("Dommages", value=0, max_chars=None, key=202, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))
stats_perso["roub_per_do"]=int(st.sidebar.text_input("% dommages", value=0, max_chars=None, key=203, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))

st.sidebar.write("# Boosts sur bombe") 
stats_perso["bombe_pui"]=int(st.sidebar.text_input("Puissance", value=0, max_chars=None, key=211, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))
stats_perso["bombe_do"]=int(st.sidebar.text_input("Dommages", value=0, max_chars=None, key=212, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))
stats_perso["bombe_per_do"]=int(st.sidebar.text_input("% dommages", value=0, max_chars=None, key=213, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))

######################
#Variables générales
######################

# distance=st.pills("Distance explosion", ["cac","1 po"], selection_mode="single",default="cac")

def calcul_vita_bombes(pvroub,lvlroub,pvbase):
    return (pvroub-(lvlroub*5+50))*0.27+pvbase 

lvls_bombes = ["4", "5", "6"]
vita_bombes_base={"4": 19
                  ,"5": 23
                  ,"6" : 28}
st.session_state["bombes_posees"]=[True,False,False]
def calcul_bonus_combo(bombes_combo):#bonus combo de 1 à 10, 0 signifie qu'il n'y a pas de bombe
    combo_total=0

    #bombe 1
    if bombes_combo[0]<6:
        combo_total+=bombes_combo[0]*20
    else :
        combo_total+=100+30*(bombes_combo[0]-5)

    #bombe 2
    if bombes_combo[1]<6:
        combo_total+=bombes_combo[1]*20
    else :
        combo_total+=100+30*(bombes_combo[1]-5)

    #bombe 3
    if bombes_combo[2]<6:
        combo_total+=bombes_combo[2]*20
    else :
        combo_total+=100+30*(bombes_combo[2]-5)

    return combo_total

#distance=0 pour mur et 1 pour explosion
def calcul_degats_bombes(dommages_min=20,dommages_max=22,stats=1000,do=0,bonus_combo=750,distance=1):
    degats_min=int(dommages_min*(stats+100)/100+do)*(1-distance/10)
    degats_max=int(dommages_max*(stats+100)/100+do)*(1-distance/10)

    degats_min_combo=degats_min*(bonus_combo/100+1)
    degats_max_combo=degats_max*(bonus_combo/100+1)

    return degats_min_combo,degats_max_combo


######################
#BONUS COMBO
######################
st.write("### Bonus Combo")
st.write("""0 = pas de bombe\n
Pour voir les dégats d'explosion rajoutez tous les bonus combo qui vont booster la bombe qui explose.\n
Pour les dégats de mur rajoutez tous les bonus combo des bombes du mur.""")
bombes_combo=[0,0,0]
col_bombe_1, col_bombe_2, col_bombe_3 = st.columns((1,1,1))
bombes_combo[0]=col_bombe_1.number_input(label="Bombe 1",min_value=1,max_value=10,value=5)
bombes_combo[1]=col_bombe_2.number_input(label="Bombe 2",min_value=0,max_value=10,value=0)
bombes_combo[2]=col_bombe_3.number_input(label="Bombe 3",min_value=0,max_value=10,value=0)

bonus_combo_total=calcul_bonus_combo(bombes_combo)


######################
#Explobombe
######################
left_BF, right_BF = st.columns((1,1))
with left_BF:

    st.write("### Explobombe")

    #Lvl Bombe
    if stats_perso["Lvl"]>130:
        BF_lvl_base=lvls_bombes[2]
    elif stats_perso["Lvl"]>80:
        BF_lvl_base=lvls_bombes[1]
    else:
        BF_lvl_base=lvls_bombes[0]
    
    l_BF_in,r_BF_in=st.columns((1,1))
    BF_lvl_bombes_unchecked = st.pills("Lvl Bombe", lvls_bombes, selection_mode="single",default=BF_lvl_base,key=0)
    if BF_lvl_bombes_unchecked in lvls_bombes:
        BF_lvl_bombes=BF_lvl_bombes_unchecked
    else:
        BF_lvl_bombes=lvls_bombes[2]
    #dégats de base bombe
    explobombe_do={
        '4':(15,17,14,15)
        ,'5':(16,18,15,16)
        ,'6':(19,21,20,22)
    }
    BF_mur_do_min,BF_mur_do_max,BF_explo_do_min,BF_explo_do_max=explobombe_do[BF_lvl_bombes]

    tab_vita_BF="""
| Vitalité |
| ----------- |
"""
    tab_vita_BF+="| "+str(int(calcul_vita_bombes(stats_perso["Vita"],stats_perso["Lvl"],vita_bombes_base[BF_lvl_bombes])))+" |\n"
    st.write(tab_vita_BF)
    
    tab_BF="""
|   | Valeur min | Valeur max | Moyenne |
| ----------- | ----------- | ----------- | ----------- |
"""
    BF_mur_min,BF_mur_max=calcul_degats_bombes(BF_mur_do_min,BF_mur_do_max
                                                      ,stats=stats_perso['Intel']+stats_perso["pui"]+stats_perso["roub_pui"]
                                                      ,do=stats_perso['Dofeu']+stats_perso["Do"]+stats_perso["roub_do"]
                                                      ,bonus_combo=bonus_combo_total
                                                      ,distance=0)
    tab_BF+="| Mur | "+str(int(BF_mur_min))+" | "+str(int(BF_mur_max))+" | "+str(int((BF_mur_min+BF_mur_max)/2))+" |\n"

    BF_explo_min,BF_explo_max=calcul_degats_bombes(BF_explo_do_min,BF_explo_do_max
                                                      ,stats=stats_perso['Intel']+stats_perso["pui"]+stats_perso["bombe_pui"]+stats_perso["roub_pui"]
                                                      ,do=stats_perso['Dofeu']+stats_perso["Do"]+stats_perso["bombe_do"]+stats_perso["roub_do"]
                                                      ,bonus_combo=bonus_combo_total
                                                      ,distance=1)
    tab_BF+="| Explosion | "+str(int(BF_explo_min))+" | "+str(int(BF_explo_max))+" | "+str(int((BF_explo_min+BF_explo_max)/2))+" |\n"
    st.write(tab_BF)
    st.text("")
    # st.write(BF_mur_do_min,BF_mur_do_max
    #     ,stats_perso['Intel']+stats_perso["pui"]+stats_perso["roub_pui"]
    #     ,stats_perso['Dofeu']+stats_perso["Do"]+stats_perso["roub_do"]
    #     ,bonus_combo_total)
with right_BF:
    st.text("")
    st.image(image_path+"Explobombe.png")

######################
#Bombe à eau
######################
left_BE, right_BE = st.columns((1,1))
with left_BE:

    st.write("### Bombe à eau")

    #Lvl Bombe
    if stats_perso["Lvl"]>124:
        BE_lvl_base=lvls_bombes[2]
    elif stats_perso["Lvl"]>74:
        BE_lvl_base=lvls_bombes[1]
    else:
        BE_lvl_base=lvls_bombes[0]

    l_BE_in,r_BE_in=st.columns((1,1))
    BE_lvl_bombes_unchecked = st.pills("Lvl Bombe", lvls_bombes, selection_mode="single",default=BE_lvl_base,key=1)
    if BE_lvl_bombes_unchecked in lvls_bombes:
        BE_lvl_bombes=BE_lvl_bombes_unchecked
    else:
        BE_lvl_bombes=lvls_bombes[2]
    #dégats de base bombe
    bombe_a_eau_do={
        '4':(11,13,11,12)
        ,'5':(12,14,12,13)
        ,'6':(15,17,17,19)
    }
    BE_mur_do_min,BE_mur_do_max,BE_explo_do_min,BE_explo_do_max=bombe_a_eau_do[BE_lvl_bombes]

    tab_vita_BE="""
| Vitalité |
| ----------- |
"""
    tab_vita_BE+="| "+str(int(calcul_vita_bombes(stats_perso["Vita"],stats_perso["Lvl"],vita_bombes_base[BE_lvl_bombes])))+" |\n"
    st.write(tab_vita_BE)
    
    tab_BE="""
|   | Valeur min | Valeur max | Moyenne |
| ----------- | ----------- | ----------- | ----------- |
"""
    BE_mur_min,BE_mur_max=calcul_degats_bombes(BE_mur_do_min,BE_mur_do_max
                                                      ,stats=stats_perso['Chance']+stats_perso["pui"]+stats_perso["roub_pui"]
                                                      ,do=stats_perso['Doeau']+stats_perso["Do"]+stats_perso["roub_do"]
                                                      ,bonus_combo=bonus_combo_total
                                                      ,distance=0)
    tab_BE+="| Mur | "+str(int(BE_mur_min))+" | "+str(int(BE_mur_max))+" | "+str(int((BE_mur_min+BE_mur_max)/2))+" |\n"

    BE_explo_min,BE_explo_max=calcul_degats_bombes(BE_explo_do_min,BE_explo_do_max
                                                      ,stats=stats_perso['Chance']+stats_perso["pui"]+stats_perso["bombe_pui"]+stats_perso["roub_pui"]
                                                      ,do=stats_perso['Doeau']+stats_perso["Do"]+stats_perso["bombe_do"]+stats_perso["roub_do"]
                                                      ,bonus_combo=bonus_combo_total
                                                      ,distance=1)
    tab_BE+="| Explosion | "+str(int(BE_explo_min))+" | "+str(int(BE_explo_max))+" | "+str(int((BE_explo_min+BE_explo_max)/2))+" |\n"
    st.write(tab_BE)
    st.text("")
    # st.write(BE_mur_do_min,BE_mur_do_max
    #     ,stats_perso['Chance']+stats_perso["pui"]+stats_perso["roub_pui"]
    #     ,stats_perso['Doeau']+stats_perso["Do"]+stats_perso["roub_do"]
    #     ,bonus_combo_total)
with right_BE:
    st.text("")
    st.image(image_path+"Bombe_a_eau.png")

######################
#Tornabombe
######################
left_BA, right_BA = st.columns((1,1))
with left_BA:

    st.write("### Tornabombe")

    #Lvl Bombe
    if stats_perso["Lvl"]>100:
        BA_lvl_base=lvls_bombes[2]
    elif stats_perso["Lvl"]>50:
        BA_lvl_base=lvls_bombes[1]
    else:
        BA_lvl_base=lvls_bombes[0]
    
    l_BA_in,r_BA_in=st.columns((1,1))
    BA_lvl_bombes_unchecked = st.pills("Lvl Bombe", lvls_bombes, selection_mode="single",default=BA_lvl_base,key=2)
    if BA_lvl_bombes_unchecked in lvls_bombes:
        BA_lvl_bombes=BA_lvl_bombes_unchecked
    else:
        BA_lvl_bombes=lvls_bombes[2]
    #dégats de base bombe
    tornabombe_do={
        '4':(11,13,11,12)
        ,'5':(12,14,12,13)
        ,'6':(15,17,17,19)
    }
    BA_mur_do_min,BA_mur_do_max,BA_explo_do_min,BA_explo_do_max=tornabombe_do[BA_lvl_bombes]

    tab_vita_BA="""
| Vitalité |
| ----------- |
"""
    tab_vita_BA+="| "+str(int(calcul_vita_bombes(stats_perso["Vita"],stats_perso["Lvl"],vita_bombes_base[BA_lvl_bombes])))+" |\n"
    st.write(tab_vita_BA)
    
    tab_BA="""
|   | Valeur min | Valeur max | Moyenne |
| ----------- | ----------- | ----------- | ----------- |
"""
    BA_mur_min,BA_mur_max=calcul_degats_bombes(BA_mur_do_min,BA_mur_do_max
                                                      ,stats=stats_perso['Agi']+stats_perso["pui"]+stats_perso["roub_pui"]
                                                      ,do=stats_perso['Doair']+stats_perso["Do"]+stats_perso["roub_do"]
                                                      ,bonus_combo=bonus_combo_total
                                                      ,distance=0)
    tab_BA+="| Mur | "+str(int(BA_mur_min))+" | "+str(int(BA_mur_max))+" | "+str(int((BA_mur_min+BA_mur_max)/2))+" |\n"

    BA_explo_min,BA_explo_max=calcul_degats_bombes(BA_explo_do_min,BA_explo_do_max
                                                      ,stats=stats_perso['Agi']+stats_perso["pui"]+stats_perso["bombe_pui"]+stats_perso["roub_pui"]
                                                      ,do=stats_perso['Doair']+stats_perso["Do"]+stats_perso["bombe_do"]+stats_perso["roub_do"]
                                                      ,bonus_combo=bonus_combo_total
                                                      ,distance=1)
    tab_BA+="| Explosion | "+str(int(BA_explo_min))+" | "+str(int(BA_explo_max))+" | "+str(int((BA_explo_min+BA_explo_max)/2))+" |\n"
    st.write(tab_BA)
    st.text("")
    # st.write(BA_mur_do_min,BA_mur_do_max
    #     ,stats_perso['Agi']+stats_perso["pui"]+stats_perso["roub_pui"]
    #     ,stats_perso['Doair']+stats_perso["Do"]+stats_perso["roub_do"]
    #     ,bonus_combo_total)
with right_BA:
    st.text("")
    st.image(image_path+"Tornabombe.png")