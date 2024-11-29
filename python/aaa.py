import pandas as pd
dict_professores = {
    'Professor 1': 1000,
    'Professor 2': 1000,
    'Professor 3': 1000,
    'Professor 4': 1000,
    'Professor 5': 1000
}
df = pd.DataFrame(dict_professores).T  # Transpor o DataFrame para organizar as colunas corretamente

print(df)