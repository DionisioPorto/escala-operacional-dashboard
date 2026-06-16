import streamlit as st

from escala import (
    carregar_planilha,
    criar_mapa_datas,
    consultar_rede
)

st.set_page_config(
    page_title="Escala MVL",
    layout="wide"
)

st.title(
    "🚛 Escala Operacional"
)

arquivo = st.file_uploader(
    "Selecione a planilha",
    type=["xlsx"]
)

if arquivo:

    df, df_bruto = carregar_planilha(
        arquivo
    )

    mapa_datas = criar_mapa_datas(
        df,
        df_bruto
    )

    data = st.selectbox(
        "Selecione a data",
        list(mapa_datas.keys())
    )

    resultado = consultar_rede(
        arquivo,
        data
    )

    st.metric(
        "Total de Redes",
        len(resultado)
    )

    st.dataframe(
        resultado,
        use_container_width=True
    )