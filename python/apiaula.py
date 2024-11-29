import requests
import pandas as pd
api ="http://www.ipeadata.gov.br/api/odata4/Metadados"
response = requests.get(api)
response.status_code
dados = response.json()
dados.keys()
dados = dados['value']
df = pd.DataFrame.from_dict(dados)
df.head()
df.columns
df.info()
df.describe()
df.shape
col =['SERCODIGO','SERNOME','SERCOMENTARIO']
df1 = df[col]
filter1 = df1.SERNOME.str.contains("ibge", regex=True, case=False)
filter2 = df1.SERNOME.str.contains("popula..o", regex=True, case=False)
df1.loc[filter1 & filter2]
#info das serie
cod="ADH12_POP18M"
url = f"http://www.ipeadata.gov.br/api/odata4/Metadados('{cod}')/Valores"
response = requests.get(url)
response.status_code
serie = response.json()["value"]
df_serie = pd.DataFrame.from_dict(serie)
