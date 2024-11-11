import streamlit as st
import dofusbook_scraping_requests as db
image_path='images/'


######################
# Page Title
######################

st.set_page_config(page_title="InvRoxx",page_icon=image_path+"logo_InvRoxx_tab.png",layout="wide")

st.title("InvRoxx : Le calculateur de roxx de tes invo préférées")
st.write('''
   
''')
st.write('''
   
''')

st.write("### Tu peux voir de nombreux exemples de stuff pour osa dans tous les éléments et tous niveaux sur ma bibliothèque de stuff : https://touch.dofusbook.net/fr/membre/244671-warp/equipements")
st.write("### Dans la suite de l'outil on part du principe que l'osa est lvl 200 et ses invo sont lvl 6")


######################
#SIDEBAR
######################

st.sidebar.image(image_path+"logo_invroxx_transp.png" )
# st.sidebar.write("# Stats du personnage") 
# st.sidebar.write("(les stats du parchotage et des points investis ne comptent pas pour les dégats des invo, seul l'équipement compte)") 

db_link=st.sidebar.text_input("Lien dofusbook",placeholder="https://d-bk.net/fr/t/A7si")
if db_link!='':
    db_stats=db.get_stats(db_link)  
    if "db_name" in db_stats.keys():
        st.sidebar.write("# "+db_stats["db_name"])
    # if type(db_stats)==str:
    #     st.sidebar.write(db_stats)
    # else:
    #     st.sidebar.write("Si les stats sont mal récupérées verifiez votre lien ou relancez la recherche, dofusbook bug parfois")
stats_perso={}

st.sidebar.write("# Stats du personnage") 

if db_link=='' or type(db_stats)==str:
        
    #stats
    stats_perso["Vita"]=int(st.sidebar.text_input("Vitalité globale", value=1150, max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))
    stats_perso["Intel"]=int(st.sidebar.text_input("Intelligence", value=0, max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))
    stats_perso["Chance"]=int(st.sidebar.text_input("Chance", value=0, max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))
    stats_perso["Agi"]=int(st.sidebar.text_input("Agilité", value=0, max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))
    stats_perso["pui"]=int(st.sidebar.text_input("Puissance", value=0, max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))

    #do fixes
    stats_perso["Dofeu"]=int(st.sidebar.text_input("Dommages Feu", value=0, max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))
    stats_perso["Doeau"]=int(st.sidebar.text_input("Dommages Eau", value=0, max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))
    stats_perso["Doair"]=int(st.sidebar.text_input("Dommages Air", value=0, max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))
    stats_perso["Dopou"]=int(st.sidebar.text_input("Dommages de Poussée", value=0, max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))

    #soin
    stats_perso["Soin"]=int(st.sidebar.text_input("Soin", value=0, max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))

    stats_perso["Do"]=int(st.sidebar.text_input("Dommages", value=0, max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))
else:
    
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
    stats_perso["Dopou"]=int(st.sidebar.text_input("Dommages de Poussée", value=db_stats["Do Poussée"], max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))

    #soin
    stats_perso["Soin"]=int(st.sidebar.text_input("Soin", value=db_stats["Soin"], max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))

    stats_perso["Do"]=int(st.sidebar.text_input("Dommages", value=0, max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))


######################
#Variables générales
######################

lvl_invo=6

def calcul_vita(base,multi):
    vita=base+multi*(stats_perso["Vita"]-1150)
    if vita>0 :
        return vita
    else:
        return 0


######################
#Dragonnet
######################
left_drag, right_drag = st.columns((1,1))
with left_drag:

    st.write("## Dragonnet Rouge")

    drag_intel_base=350

    drag_intel=drag_intel_base+stats_perso["Intel"]/2
    drag_do=stats_perso["Dofeu"]/2

    dragofeu_min=(41*(100+drag_intel)/100+drag_do)//1
    dragofeu_max=(50*(100+drag_intel)/100+drag_do)//1

    insoi_min=(36*(100+drag_intel)/100+drag_do)//1
    insoi_max=(45*(100+drag_intel)/100+drag_do)//1


    tab_vita_drag="""
| Vitalité | Bonus au T1 : +20% par mob |
| ----------- | ----------- |
"""
    tab_vita_drag+="| "+str(int(calcul_vita(170,0.2)))+" | "+str(int(calcul_vita(170,0.2)*0.2))+"\n"

    st.write(tab_vita_drag)
    st.text("")

    tab_drag="""
| Sort | Valeur min | Valeur max | Moyenne |
| ----------- | ----------- | ----------- | ----------- |
"""
    tab_drag+="| Dragofeu | "+str(int(dragofeu_min))+" | "+str(int(dragofeu_max))+" | "+str(int((dragofeu_min+dragofeu_max)/2))+" |\n"
    tab_drag+="| Flamme Persistante (insoignable) | "+str(int(insoi_min))+" | "+str(int(insoi_max))+" | "+str(int((insoi_min+insoi_max)/2))+" |\n"
    
    st.write(tab_drag)
    st.text("")

with right_drag:
    st.text("")
    st.image(image_path+"dragonnet.png")


######################
#Momie
######################
left_momie, right_momie = st.columns((1,1))
with left_momie:

    st.write("## Momie Koalak")

    momie_intel_base=350

    momie_intel=momie_intel_base+stats_perso["Intel"]/2
    momie_do=stats_perso["Dofeu"]/2
    momie_soin=stats_perso["Soin"]/2

    male_min=(26*(100+momie_intel)/100+momie_do)//1
    male_max=(35*(100+momie_intel)/100+momie_do)//1

    bande_min=(51*(100+momie_intel)/100+momie_soin)//1
    bande_max=(60*(100+momie_intel)/100+momie_soin)//1
    
    tab_vita_momie="""
| Vitalité | Bonus au T1 : +20% par mob |
| ----------- | ----------- |
"""
    tab_vita_momie+="| "+str(int(calcul_vita(135,0.15)))+" | "+str(int(calcul_vita(135,0.15)*0.2))+"\n"

    st.write(tab_vita_momie)
    st.text("")

    tab_momie="""
| Sort | Valeur min | Valeur max | Moyenne |
| ----------- | ----------- | ----------- | ----------- |
"""
    tab_momie+="| Malédiction Vampirique | "+str(int(male_min))+" | "+str(int(male_max))+" | "+str(int((male_min+male_max)/2))+" |\n"
    tab_momie+="| Bandelette soignante (soin) | "+str(int(bande_min))+" | "+str(int(bande_max))+" | "+str(int((bande_min+bande_max)/2))+" |\n"

    st.write(tab_momie) 
    st.text("")

with right_momie:
    st.text("")
    st.image(image_path+"momie.png")


######################
#Craqueleur
######################
left_craq, right_craq = st.columns((1,1))
with left_craq:

    st.write("## Craqueleur")

    craq_chance_base=150

    craq_chance=craq_chance_base+stats_perso["Chance"]/2
    craq_do=stats_perso["Doeau"]/2

    ecrasement_min=(28*(100+craq_chance)/100+craq_do)//1
    ecrasement_max=(33*(100+craq_chance)/100+craq_do)//1

    frappe_etourdissante_min=(33*(100+craq_chance)/100+craq_do)//1
    frappe_etourdissante_max=(37*(100+craq_chance)/100+craq_do)//1


    tab_vita_craq="""
| Vitalité | Bonus au T1 : +20% par mob |
| ----------- | ----------- |
"""
    tab_vita_craq+="| "+str(int(calcul_vita(350,0.2)))+" | "+str(int(calcul_vita(350,0.2)*0.2))+"\n"

    st.write(tab_vita_craq)
    st.text("")

    tab_craq="""
| Sort | Valeur min | Valeur max | Moyenne |
| ----------- | ----------- | ----------- | ----------- |
"""
    tab_craq+="| Ecrasement | "+str(int(ecrasement_min))+" | "+str(int(ecrasement_max))+" | "+str(int((ecrasement_min+ecrasement_max)/2))+" |\n"
    tab_craq+="| Frappe étourdissante (rall 2 pa) | "+str(int(frappe_etourdissante_min))+" | "+str(int(frappe_etourdissante_max))+" | "+str(int((frappe_etourdissante_min+frappe_etourdissante_max)/2))+" |\n"
    
    st.write(tab_craq)
    st.text("")

with right_craq:
    st.text("")
    st.image(image_path+"craqueleur.png")


######################
#Bouftou
######################
left_bouf, right_bouf = st.columns((1,1))
with left_bouf:

    st.write("## Bouftou")

    bouf_chance_base=150 #  150

    bouf_chance=bouf_chance_base+stats_perso["Chance"]/2
    bouf_do=stats_perso["Doeau"]/2

    morsure_min=(31*(100+bouf_chance)/100+bouf_do)//1
    morsure_max=(35*(100+bouf_chance)/100+bouf_do)//1

    tab_vita_bouf="""
| Vitalité | Bonus au T1 : +20% par mob |
| ----------- | ----------- |
"""
    tab_vita_bouf+="| "+str(int(calcul_vita(260,0.2)))+" | "+str(int(calcul_vita(260,0.2)*0.2))+"\n"

    st.write(tab_vita_bouf)
    st.text("")

    tab_bouf="""
| Sort | Valeur min | Valeur max | Moyenne |
| ----------- | ----------- | ----------- | ----------- |
"""
    tab_bouf+="| Morsure | "+str(int(morsure_min))+" | "+str(int(morsure_max))+" | "+str(int((morsure_min+morsure_max)/2))+" |\n"

    st.write(tab_bouf)
    st.text("")

with right_bouf:
    st.text("")
    st.image(image_path+"bouftou.png")

######################
#Sanglier
######################
left_gligli, right_gligli = st.columns((1,1))
with left_gligli:

    st.write("## Sanglier")

    sangli_agi_base=350
    sangli_dopou_base=157 #dans les stats du gligli c'est marqué 60 mais en pratique ça tape comme si 157

    sangli_agi=sangli_agi_base+stats_perso["Agi"]/2
    sangli_do=stats_perso["Doair"]/2

    embro_poussée=5
    embro_min=(25*(100+sangli_agi)/100+sangli_do)//1
    embro_max=(29*(100+sangli_agi)/100+sangli_do)//1
    embro_dopou=(lvl_invo/2+sangli_dopou_base+stats_perso["Dopou"]/2+32)*embro_poussée/4

    poussette_poussée=3
    poussette_min=(28*(100+sangli_agi)/100+sangli_do)//1
    poussette_max=(32*(100+sangli_agi)/100+sangli_do)//1
    poussette_dopou=(lvl_invo/2+sangli_dopou_base+stats_perso["Dopou"]/2+32)*poussette_poussée/4

    tab_vita_gligli="""
| Vitalité | Bonus au T1 : +20% par mob |
| ----------- | ----------- |
"""
    tab_vita_gligli+="| "+str(int(calcul_vita(310,0.1)))+" | "+str(int(calcul_vita(310,0.1)*0.2))+"\n"

    st.write(tab_vita_gligli)
    st.text("")

    tab_gligli="""
| Sort | Valeur min | Valeur max | Dopou | Moyenne |
| ----------- | ----------- | ----------- | ----------- | ----------- |
"""
    tab_gligli+="| Embrochement (dopou compris) | "+str(int(embro_min))+" | "+str(int(embro_max))+" | "+str(int(embro_dopou))+" | "+str(int((embro_min+embro_max)/2+embro_dopou))+" |\n"
    tab_gligli+="| Poussette (pesanteur, dopou compris) | "+str(int(poussette_min))+" | "+str(int(poussette_max))+" | "+str(int(poussette_dopou))+" | "+str(int((poussette_min+poussette_max)/2+poussette_dopou))+" |\n"

    st.write(tab_gligli)
    st.text("")

with right_gligli:
    st.text("")
    st.image(image_path+"sanglier.png")

######################
#Tofu
######################
left_tofu, right_tofu = st.columns((1,1))
with left_tofu:

    st.write("## Tofu")

    tofu_agi_base=350
    
    tofu_agi=tofu_agi_base+stats_perso["Agi"]/2
    tofu_do=stats_perso["Doair"]/2
    
    beco_min=(15*(100+tofu_agi)/100+tofu_do)//1
    beco_max=(18*(100+tofu_agi)/100+tofu_do)//1

    tab_vita_tofu="""
| Vitalité | Bonus au T1 : +20% par mob |
| ----------- | ----------- |
"""
    tab_vita_tofu+="| "+str(int(calcul_vita(95,0.05)))+" | "+str(int(calcul_vita(95,0.05)*0.2))+"\n"

    st.write(tab_vita_tofu)
    st.text("")

    tab_tofu="""
| Sort | Valeur min | Valeur max | Moyenne |
| ----------- | ----------- | ----------- | ----------- |
"""
    tab_tofu+="| Béco du Tofu | "+str(int(beco_min))+" | "+str(int(beco_max))+" | "+str(int((beco_min+beco_max)/2))+" |\n"

    st.write(tab_tofu)
    st.text("")

with right_tofu:
    st.text("")
    st.image(image_path+"tofu.png")

######################
#substitution
######################
left_substi, right_substi = st.columns((1,1))
with left_substi:

    st.write("## Substitution")

    degats_substi_min=(36*(100+stats_perso["Intel"]+0.80*stats_perso["pui"])/100+stats_perso["Dofeu"]+stats_perso["Do"])//1
    degats_substi_max=(40*(100+stats_perso["Intel"]+0.80*stats_perso["pui"])/100+stats_perso["Dofeu"]+stats_perso["Do"])//1

    soin_substi_min=(41*(100+stats_perso["Intel"])/100+stats_perso["Soin"])//1
    soin_substi_max=(45*(100+stats_perso["Intel"])/100+stats_perso["Soin"])//1

    tab_substi="""
| Sort | Valeur min | Valeur max | Moyenne |
| ----------- | ----------- | ----------- | ----------- |
"""
    tab_substi+="| degats | "+str(int(degats_substi_min))+" | "+str(int(degats_substi_max))+" | "+str(int((degats_substi_min+degats_substi_max)/2))+" |\n"
    tab_substi+="| soin | "+str(int(soin_substi_min))+" | "+str(int(soin_substi_max))+" | "+str(int((soin_substi_min+soin_substi_max)/2))+" |\n"

    st.write(tab_substi)
    st.text("")

with right_substi:
    st.text("")
    st.image(image_path+"substi.png")


######################
#martyr
######################
left_martyr, right_martyr = st.columns((1,1))
with left_martyr:

    st.write("## Martyr")

    degats_martyr=(60*(100+stats_perso["Chance"]+0.80*stats_perso["pui"])/100+stats_perso["Doeau"]+stats_perso["Do"])//1

    tab_martyr="""
| Degats |
| ----------- |
"""
    tab_martyr+="| "+str(int(degats_martyr))+" |\n"

    st.write(tab_martyr)
    st.text("")

with right_martyr:
    st.text("")
    st.image(image_path+"martyr.png")
