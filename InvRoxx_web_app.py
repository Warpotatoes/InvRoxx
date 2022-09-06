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


######################
#SIDEBAR
######################

st.sidebar.image(image_path+"logo_InvRoxx.png" )
st.sidebar.write("# Stats du personnage") 

stats_perso={}

#stats
stats_perso["Intel"]=int(st.sidebar.text_input("Intelligence", value=100, max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))
stats_perso["Chance"]=int(st.sidebar.text_input("Chance", value=100, max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))
stats_perso["Agi"]=int(st.sidebar.text_input("Agilité", value=100, max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))

#do fixes
stats_perso["Dofeu"]=int(st.sidebar.text_input("Dommages Feu", value=0, max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))
stats_perso["Doeau"]=int(st.sidebar.text_input("Dommages Eau", value=0, max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))
stats_perso["Doair"]=int(st.sidebar.text_input("Dommages Air", value=0, max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))
stats_perso["Dopou"]=int(st.sidebar.text_input("Dommages de Poussée", value=0, max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))

#soin
stats_perso["Soin"]=int(st.sidebar.text_input("Soin", value=0, max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))


######################
#Variables générales
######################

martyr_non_bouf=621
substi_non_feu ="241-284"
substi_non_feu__soin ="299-345"
lvl_invo=6



left_column, right_column = st.columns((1,1))

with right_column:#summons images
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.image(image_path+"dragonnet.png")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
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

    drag_intel_base=350

    drag_intel=drag_intel_base+stats_perso["Intel"]/2
    drag_do=stats_perso["Dofeu"]/2

    dragofeu_min=(41*(100+drag_intel)/100+drag_do)//1
    dragofeu_max=(50*(100+drag_intel)/100+drag_do)//1

    insoi_min=(36*(100+drag_intel)/100+drag_do)//1
    insoi_max=(45*(100+drag_intel)/100+drag_do)//1

    drag_substitution=0.1141*stats_perso["Intel"] + 103.62 +stats_perso["Dofeu"]/2
    drag_substitusoin=0.1249*stats_perso["Intel"] + 131.13

    tab_drag="""
| Sort | Valeur min | Valeur max |
| ----------- | ----------- | ----------- |
"""
    tab_drag+="| Dragofeu | "+str(int(dragofeu_min))+" | "+str(int(dragofeu_max))+" |\n"
    tab_drag+="| Flamme Persistante (insoignable) | "+str(int(insoi_min))+" | "+str(int(insoi_max))+" |\n"
    tab_drag+="| Substitution (moyenne) | Dommages: "+str(int(drag_substitution))+" | Soin: "+str(int(drag_substitusoin))+" |\n"
    tab_drag+="| martyr | "+str(int(martyr_non_bouf))+" | fixe |\n"

    st.write(tab_drag)


    ######################
    #Momie
    ######################

    st.write("## Momie Koalak")

    momie_intel_base=350

    momie_intel=momie_intel_base+stats_perso["Intel"]/2
    momie_do=stats_perso["Dofeu"]/2
    momie_soin=stats_perso["Soin"]/2

    male_min=(26*(100+momie_intel)/100+momie_do)//1
    male_max=(35*(100+momie_intel)/100+momie_do)//1

    bande_min=(51*(100+momie_intel)/100+momie_soin)//1
    bande_max=(60*(100+momie_intel)/100+momie_soin)//1
    

    momie_substitution=0.1141*stats_perso["Intel"] + 103.62 +stats_perso["Dofeu"]/2
    momie_substitusoin=0.1249*stats_perso["Intel"] + 131.13 +momie_soin

    tab_momie="""
| Sort | Valeur min | Valeur max |
| ----------- | ----------- | ----------- |
"""
    tab_momie+="| Malédiction Vampirique | "+str(int(male_min))+" | "+str(int(male_max))+" |\n"
    tab_momie+="| Bandelette soignante (soin) | "+str(int(bande_min))+" | "+str(int(bande_max))+" |\n"
    tab_momie+="| Substitution (moyenne)| Dommages: "+str(int(momie_substitution))+" | Soin: "+str(int(momie_substitusoin))+" |\n"
    tab_momie+="| martyr | "+str(int(martyr_non_bouf))+" | fixe |\n"

    st.write(tab_momie) 

    ######################
    #Bouftou
    ######################

    st.write("## Bouftou")

    bouf_chance_base=350

    bouf_chance=bouf_chance_base+stats_perso["Chance"]/2
    bouf_do=stats_perso["Doeau"]/2

    morsure_min=(31*(100+bouf_chance)/100+bouf_do)//1
    morsure_max=(35*(100+bouf_chance)/100+bouf_do)//1

    martyr_bouf=0.2676*stats_perso["Chance"] + 243.06+stats_perso["Doeau"]/2

    tab_bouf="""
| Sort | Valeur min | Valeur max |
| ----------- | ----------- | ----------- |
"""
    tab_bouf+="| Morsure | "+str(int(morsure_min))+" | "+str(int(morsure_max))+" |\n"
    tab_bouf+="| Substitution | Dommages: "+substi_non_feu+" | Soin: "+substi_non_feu__soin+" |\n"
    tab_bouf+="| martyr | "+str(int(martyr_bouf))+" | fixe |\n"

    st.write(tab_bouf)

    ######################
    #Sanglier
    ######################

    st.write("## Sanglier")

    sangli_agi_base=350
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


    tab_gligli="""
| Sort | Valeur min | Valeur max |Dommages Poussée |
| ----------- | ----------- | ----------- |----------- |
"""
    tab_gligli+="| Embrochement (dopou compris) | "+str(int(embro_min))+" | "+str(int(embro_max))+" | "+str(int(embro_dopou))+" |\n"
    tab_gligli+="| Poussette (pesanteur, dopou compris) | "+str(int(poussette_min))+" | "+str(int(poussette_max))+" | "+str(int(poussette_dopou))+" |\n"
    tab_gligli+="| Substitution | Dommages: "+substi_non_feu+" | Soin: "+substi_non_feu__soin+" | - |\n"
    tab_gligli+="| martyr | "+str(int(martyr_non_bouf))+" | fixe | - |\n"

    st.write(tab_gligli)

    ######################
    #Tofu
    ######################

    st.write("## Tofu")

    tofu_agi_base=500
    
    tofu_agi=tofu_agi_base+stats_perso["Agi"]/2
    tofu_do=stats_perso["Doair"]/2
    
    beco_min=(14*(100+tofu_agi)/100+tofu_do)//1
    beco_max=(17*(100+tofu_agi)/100+tofu_do)//1



    tab_tofu="""
| Sort | Valeur min | Valeur max |
| ----------- | ----------- | ----------- |
"""
    tab_tofu+="| Béco du Tofu | "+str(int(beco_min))+" | "+str(int(beco_max))+" |\n"
    tab_tofu+="| Substitution | Dommages: "+substi_non_feu+" | Soin: "+substi_non_feu__soin+" |\n"
    tab_tofu+="| martyr | "+str(int(martyr_non_bouf))+" | fixe |\n"

    st.write(tab_tofu)
