import pandas as pd
import numpy as np
import pyarrow.parquet as pq
import os
import yaml

def pandas_df_to_parquet(df, path) -> None:
    df.to_parquet(path, index=True)

if __name__ == "__main__":
    os.makedirs("data", exist_ok=True)
    SRC_PATH = "src/SAA_2010-2024_définitives_donnees_departementales.xlsx"
    SCHEMAS = "schemas_agreste_2010_2024.yaml"

    schemas = yaml.safe_load(open(SCHEMAS))
    correspondances = schemas["agreste_correspondance"]
    onglets = list(correspondances.keys())

    tables = {}
    for onglet in onglets:
        df = pd.read_excel(SRC_PATH,
                           engine="openpyxl",
                           header=5,
                           sheet_name=onglet)
        tables[onglet] = pd.wide_to_long(df=df,
                                         stubnames=schemas[correspondances[onglet]]["stubnames"],
                                         i=schemas[correspondances[onglet]]["i"],
                                         j=schemas[correspondances[onglet]]["j"],
                                         sep=schemas[correspondances[onglet]]["sep"])
        pandas_df_to_parquet(tables[onglet], f"data/agreste_2010_2024_{onglet}.parquet")