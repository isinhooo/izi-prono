import streamlit as st

st.set_page_config(page_title="Izi Prono - Prédictions Foot", page_icon="⚽", layout="centered")

st.title("⚽ IZI PRONO")
st.subheader("Prédiction Foot Intelligente")

equipes = ["Real Madrid", "Barcelone", "Man City", "Arsenal", "PSG", "Bayern", "Liverpool", "Dortmund", "Inter", "Milan AC", "Sénégal", "Maroc", "Côte d'Ivoire"]

col1, col2 = st.columns(2)
with col1:
    domicile = st.selectbox("Équipe Domicile", equipes)
with col2:
    exterieur = st.selectbox("Équipe Extérieur", [e for e in equipes if e != domicile])

st.divider()

forme_dom = st.slider(f"Forme {domicile} (5 derniers matchs)", 0, 15, 9)
forme_ext = st.slider(f"Forme {exterieur} (5 derniers matchs)", 0, 15, 7)

cote_dom = st.number_input(f"Cote Victoire {domicile}", value=2.10)
cote_nul = st.number_input("Cote Match Nul", value=3.20)
cote_ext = st.number_input(f"Cote Victoire {exterieur}", value=3.50)

if st.button("🔮 PRÉDIRE LE MATCH", use_container_width=True):
    score_dom = forme_dom * 0.6 + (4 - cote_dom) * 2
    score_ext = forme_ext * 0.6 + (4 - cote_ext) * 2
    
    st.divider()
    st.subheader("Résultat Izi Prono :")
    
    if score_dom > score_ext + 2:
        st.success(f"✅ VICTOIRE {domicile.upper()} - Confiance: {int((score_dom/(score_dom+score_ext))*100)}%")
        st.write(f"Score probable: 2-1 ou 1-0 pour {domicile}")
        prono = f"1 - {domicile}"
    elif score_ext > score_dom + 2:
        st.success(f"✅ VICTOIRE {exterieur.upper()} - Confiance: {int((score_ext/(score_dom+score_ext))*100)}%")
        st.write(f"Score probable: 1-2 ou 0-1 pour {exterieur}")
        prono = f"2 - {exterieur}"
    else:
        st.warning(f"⚖️ MATCH NUL probable - Confiance: 55%")
        st.write(f"Score probable: 1-1")
        prono = "X - Nul"

    st.info(f"💡 Conseil Pari: Double Chance {prono}")

st.caption("Izi Prono v1.0 - Créé par Isidore")
