import streamlit as st
import dofusbook_scraping as db
import re
image_path='images/'



######################
# Page Title
######################

st.set_page_config(page_title="CalcRoxx",page_icon=image_path+"logo_InvRoxx_tab.png",layout="wide")

######################
#SIDEBAR
######################

with st.sidebar:
    st.image(image_path+"logo_invroxx_transp.png" )

##############
# DOPOU
##############

st.write("## Calculateur de dégats de poussée")

lvl = st.number_input("Lvl",value=200,key=101)
dopou = st.number_input("DoPou",value=0,key=102)
repou = st.number_input("RePou",value=0,key=103)
nb_cases = st.number_input("Cases de poussée",value=4,key=104)
dégats_pou= (lvl/2+dopou-repou+32)/4*nb_cases

tab_dopou="""
| Dégats de la poussée|
| ----------- |
"""
tab_dopou+="| "+str(int(dégats_pou))+'\n'
st.write(tab_dopou)

##############
# SORTS
##############

st.write("## Calculateur de ligne de dégats de sort")

left_do, mid_do,right_do = st.columns((1,1,1))
with left_do:
    base_min = st.number_input("Dommages de base minimum de la ligne",value=8,key=210)
    base_max = st.number_input("Dommages de base maximum de la ligne",value=10,key=211)
    base_min_cc = st.number_input("Dommages critiques de base minimum de la ligne",value=11,key=212)
    base_max_cc = st.number_input("Dommages critiques de base maximum de la ligne",value=13,key=213)
with mid_do:
    stats = st.number_input("Stats (élémentaires + puissance)",value=1000,key=201)
    do = st.number_input("Dommages",value=100,key=202)
    cc = st.number_input("%critiques (donnés par le stuff + %cc de base de la ligne)",value=5,key=203)
    docri = st.number_input("Dommages Critiques",value=0,key=204)
with right_do:
    st.write("### Adversaire")
    reper= st.number_input("Résistances %",value=0,key=220)
    refix= st.number_input("Résistances fixes",value=0,key=221)
    recri= st.number_input("Résistances critiques",value=0,key=222)

    
dégats_min= base_min*((100+stats)/100)+do 
dégats_max= base_max*((100+stats)/100)+do 
mean_do=(dégats_min+dégats_max)/2

dégats_cc_min= base_min_cc*((100+stats)/100)+do+docri
dégats_cc_max= base_max_cc*((100+stats)/100)+do+docri
mean_do_cc=(dégats_cc_min+dégats_cc_max)/2

mean_do_globaux=cc/100*mean_do_cc+(100-cc)/100*mean_do

tab_do="""
| Dégats min | Dégats max | Dégats moyens |
| ----------- | ----------- | ----------- |
"""
tab_do+="| "+str(int(dégats_min))+" | "+str(int(dégats_max))+" | "+str(int(mean_do))+" |\n"

tab_do_cc="""
| Dégats cc min | Dégats cc max | Dégats cc moyens |
| ----------- | ----------- | ----------- |
"""
tab_do_cc+="| "+str(int(dégats_cc_min))+" | "+str(int(dégats_cc_max))+" | "+str(int(mean_do_cc))+" |\n"

tab_do_glob="""
| Dégats moyens globaux (crit et no crit compris)|
| ----------- |
"""
tab_do_glob+="| "+str(int(mean_do_globaux))+" |\n"

st.write(tab_do)
st.write(tab_do_cc)
st.write(tab_do_glob)