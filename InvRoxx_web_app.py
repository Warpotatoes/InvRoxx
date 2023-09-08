import streamlit as st
 
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


######################
#SIDEBAR
######################

st.sidebar.image(image_path+"logo_invroxx_transp.png" )
st.sidebar.write("# Stats du personnage") 
st.sidebar.write("(les stats du parchotage et des points investis ne comptent pas pour les dégats des invo)") 

stats_perso={}

#stats
stats_perso["Vita"]=int(st.sidebar.text_input("Vitalité globale", value=0, max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))
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

left_column, right_column = st.columns((1,1))

with right_column:#summons images
    st.text("")
    st.text("")
    # st.text("")
    # st.text("")
    st.image(image_path+"dragonnet.png")
    st.text("")
    st.text("")
    # st.text("")
    # st.text("")
    # st.text("")
    st.image(image_path+"momie.png")
    st.text("")
    st.text("")
    st.image(image_path+"bouftou.png")
    st.text("")
    st.text("")
    st.image(image_path+"sanglier.png")
    st.text("")
    st.text("")
    st.image(image_path+"tofu.png")

with left_column: #Summons damages tables

    ######################
    #Dragonnet
    ######################

    st.write("## Dragonnet Rouge")

    drag_intel_base=300

    drag_intel=drag_intel_base+stats_perso["Intel"]/2
    drag_do=stats_perso["Dofeu"]/2

    dragofeu_min=(41*(100+drag_intel)/100+drag_do)//1
    dragofeu_max=(50*(100+drag_intel)/100+drag_do)//1

    insoi_min=(36*(100+drag_intel)/100+drag_do)//1
    insoi_max=(45*(100+drag_intel)/100+drag_do)//1


    tab_vita_drag="""
| Vitalité |
| ----------- |
"""
    tab_vita_drag+="| "+str(int(calcul_vita(265,0.25)))+" |\n"

    st.write(tab_vita_drag)
    st.text("")

    tab_drag="""
| Sort | Valeur min | Valeur max |
| ----------- | ----------- | ----------- |
"""
    tab_drag+="| Dragofeu | "+str(int(dragofeu_min))+" | "+str(int(dragofeu_max))+" |\n"
    tab_drag+="| Flamme Persistante (insoignable) | "+str(int(insoi_min))+" | "+str(int(insoi_max))+" |\n"
    
    st.write(tab_drag)

    st.text("")

    ######################
    #Momie
    ######################

    st.write("## Momie Koalak")

    momie_intel_base=300

    momie_intel=momie_intel_base+stats_perso["Intel"]/2
    momie_do=stats_perso["Dofeu"]/2
    momie_soin=stats_perso["Soin"]/2

    male_min=(26*(100+momie_intel)/100+momie_do)//1
    male_max=(35*(100+momie_intel)/100+momie_do)//1

    bande_min=(51*(100+momie_intel)/100+momie_soin)//1
    bande_max=(60*(100+momie_intel)/100+momie_soin)//1
    
    tab_vita_momie="""
| Vitalité |
| ----------- |
"""
    tab_vita_momie+="| "+str(int(calcul_vita(140,0.2)))+" |\n"

    st.write(tab_vita_momie)
    st.text("")

    tab_momie="""
| Sort | Valeur min | Valeur max |
| ----------- | ----------- | ----------- |
"""
    tab_momie+="| Malédiction Vampirique | "+str(int(male_min))+" | "+str(int(male_max))+" |\n"
    tab_momie+="| Bandelette soignante (soin) | "+str(int(bande_min))+" | "+str(int(bande_max))+" |\n"

    st.write(tab_momie) 

    st.text("")
    st.text("")


    ######################
    #Bouftou
    ######################

    st.write("## Bouftou")

    bouf_chance_base=300

    bouf_chance=bouf_chance_base+stats_perso["Chance"]/2
    bouf_do=stats_perso["Doeau"]/2

    morsure_min=(31*(100+bouf_chance)/100+bouf_do)//1
    morsure_max=(35*(100+bouf_chance)/100+bouf_do)//1

    tab_vita_bouf="""
| Vitalité |
| ----------- |
"""
    tab_vita_bouf+="| "+str(int(calcul_vita(265,0.25)))+" |\n"

    st.write(tab_vita_bouf)
    st.text("")

    tab_bouf="""
| Sort | Valeur min | Valeur max |
| ----------- | ----------- | ----------- |
"""
    tab_bouf+="| Morsure | "+str(int(morsure_min))+" | "+str(int(morsure_max))+" |\n"

    st.write(tab_bouf)

    st.text("")
    st.text("")

    ######################
    #Sanglier
    ######################

    st.write("## Sanglier")

    sangli_agi_base=300
    sangli_dopou_base=157

    sangli_agi=sangli_agi_base+stats_perso["Agi"]/2
    sangli_do=stats_perso["Doair"]/2

    embro_poussée=5
    embro_min=(25*(100+sangli_agi)/100+sangli_do)//1
    embro_max=(29*(100+sangli_agi)/100+sangli_do)//1
    embro_dopou=(lvl_invo/2+sangli_dopou_base+stats_perso["Dopou"]/2+32)*embro_poussée/4

    poussette_poussée=3
    poussette_min=(13*(100+sangli_agi)/100+sangli_do)//1
    poussette_max=(17*(100+sangli_agi)/100+sangli_do)//1
    poussette_dopou=(lvl_invo/2+sangli_dopou_base+stats_perso["Dopou"]/2+32)*poussette_poussée/4

    tab_vita_gligli="""
| Vitalité |
| ----------- |
"""
    tab_vita_gligli+="| "+str(int(calcul_vita(315,0.15)))+" |\n"

    st.write(tab_vita_gligli)
    st.text("")

    tab_gligli="""
| Sort | Valeur min | Valeur max | Dopou |
| ----------- | ----------- | ----------- | ----------- |
"""
    tab_gligli+="| Embrochement (dopou compris) | "+str(int(embro_min))+" | "+str(int(embro_max))+" | "+str(int(embro_dopou))+" |\n"
    tab_gligli+="| Poussette (pesanteur, dopou compris) | "+str(int(poussette_min))+" | "+str(int(poussette_max))+" | "+str(int(poussette_dopou))+" |\n"

    st.write(tab_gligli)

    st.text("")
    st.text("")
    ######################
    #Tofu
    ######################

    st.write("## Tofu")

    tofu_agi_base=500
    
    tofu_agi=tofu_agi_base+stats_perso["Agi"]/2
    tofu_do=stats_perso["Doair"]/2
    
    beco_min=(15*(100+tofu_agi)/100+tofu_do)//1
    beco_max=(18*(100+tofu_agi)/100+tofu_do)//1

    tab_vita_tofu="""
| Vitalité |
| ----------- |
"""
    tab_vita_tofu+="| "+str(int(calcul_vita(95,0.05)))+" |\n"

    st.write(tab_vita_tofu)
    st.text("")

    tab_tofu="""
| Sort | Valeur min | Valeur max |
| ----------- | ----------- | ----------- |
"""
    tab_tofu+="| Béco du Tofu | "+str(int(beco_min))+" | "+str(int(beco_max))+" |\n"

    st.write(tab_tofu)

    st.text("")

    ######################
    #substitution
    ######################

    st.write("## Substitution")

    degats_substi_min=(36*(100+stats_perso["Intel"]+0.80*stats_perso["pui"])/100+stats_perso["Dofeu"]+stats_perso["Do"])//1
    degats_substi_max=(40*(100+stats_perso["Intel"]+0.80*stats_perso["pui"])/100+stats_perso["Dofeu"]+stats_perso["Do"])//1

    soin_substi_min=(41*(100+stats_perso["Intel"])/100+stats_perso["Soin"])//1
    soin_substi_max=(45*(100+stats_perso["Intel"])/100+stats_perso["Soin"])//1

    tab_substi="""
| Sort | Valeur min | Valeur max |
| ----------- | ----------- | ----------- |
"""
    tab_substi+="| degats | "+str(int(degats_substi_min))+" | "+str(int(degats_substi_max))+" |\n"
    tab_substi+="| soin | "+str(int(soin_substi_min))+" | "+str(int(soin_substi_max))+" |\n"

    st.write(tab_substi)

    st.text("")

    ######################
    #martyr
    ######################

    st.write("## Martyr")

    degats_martyr=(60*(100+stats_perso["Chance"]+0.80*stats_perso["pui"])/100+stats_perso["Doeau"]+stats_perso["Do"])//1

    tab_martyr="""
| Valeur |
| ----------- |
"""
    tab_martyr+="| "+str(int(degats_martyr))+" |\n"

    st.write(tab_martyr)

    st.text("")
