
import streamlit as st
import pandas as pd

st.title("🚀 Chamsys HeadHunter")
st.subheader("Generatore istantaneo di file .csv per MagicQ")

fixture = st.text_input("Marca e Modello della macchina:", "Prolights Diamond 7")

if st.button("Genera file per Chamsys"):
    # Qui inseriremo la logica di ricerca automatica che stiamo perfezionando
    st.write(f"Analisi in corso per: {fixture}...")
    
    # Esempio di dati generati
    dati = {'Channel': [1, 2], 'Name': ['PAN', 'TILT'], 'Type': ['PHT_PAN', 'PHT_TILT']}
    df = pd.DataFrame(dati)
    
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Scarica CSV", data=csv, file_name=f"{fixture}.csv", mime='text/csv')
