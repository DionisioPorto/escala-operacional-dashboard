import pandas as pd


def carregar_planilha(arquivo):

    df = pd.read_excel(
        arquivo,
        sheet_name="Valdebergue",
        header=12
    )

    df_bruto = pd.read_excel(
        arquivo,
        sheet_name="Valdebergue",
        header=None
    )

    return df, df_bruto


def criar_mapa_datas(df, df_bruto):

    mapa_datas = {}

    for i in range(58, 107):

        data = df_bruto.iloc[11, i]

        if pd.notna(data):

            coluna = df.columns[i]

            mapa_datas[
                str(pd.to_datetime(data).date())
            ] = coluna

    return mapa_datas


def consultar_rede(
    arquivo,
    data,
    operacao="MVL"
):

    df, df_bruto = carregar_planilha(arquivo)

    mapa_datas = criar_mapa_datas(
        df,
        df_bruto
    )

    coluna = mapa_datas[data]

    resultado = df[
        (df["Op"] == operacao)
        &
        (df[coluna] == "REDE")
    ]

    return resultado[
        [
            "Cidade",
            "Turno",
            "Colaborador"
        ]
    ]