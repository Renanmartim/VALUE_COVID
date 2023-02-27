import pandas as pd
import re
import plotly.express as px

file = pd.read_csv("covid_19_clean_complete.csv")

def corrige_colunas (col_name):
    return re.sub(r"[/| ]", "", col_name).lower()

file.columns = [corrige_colunas(col) for col in file.columns]

#df = file.loc[file.countryregion == "Brazil"]

brasil = file.loc[(file.countryregion == "Brazil") & (file.confirmed > 0)]

confirmados = file['confirmed'].max()

px.line(brasil, 'date', 'confirmed', title='Casos confirmados')




