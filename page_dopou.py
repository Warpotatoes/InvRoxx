import streamlit as st
image_path='images/'



######################
# Page Title
######################

st.set_page_config(page_title="CalcOpou",page_icon=image_path+"logo_InvRoxx_tab.png",layout="wide")

######################
#SIDEBAR
######################

with st.sidebar:
    st.image(image_path+"calcopou_logo_nom_transp.png" )
    st.page_link("https://d-bk.net/fr/tl/11eJ",label='**Biblio DofusBook**',icon="📚")

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
