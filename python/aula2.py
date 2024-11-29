import statistics as st
Dados = [3200, 4500, 1500, 2300, 3700, 2900, 4100, 2200, 5100, 3300, 1800,
2600, 3500, 4400, 3900, 2800, 2100, 4700, 3600, 3100, 3400, 4300, 2500, 3800,
2700, 4000, 1900, 3000, 4200, 2900, 3800, 2000, 2700, 4100, 4300, 3700, 4600,
2200, 3300, 4900]
def moda (Dados):
    moda = st.mode(Dados)
    return moda
def mediana (Dados):
    mediana = st.median(Dados)
    return mediana 
def media (Dados):
    media = st.mean(Dados)
    return media
def variancia (Dados):
    variancia = st.variance(Dados)
    return variancia
def desvio_Padrao (Dados):
    desvio_Padrao= st.stdev(Dados)
    return desvio_Padrao
print(f"A moda = {moda(Dados)}")
print(f"A mediana = {mediana(Dados)}")
print(f"A media = {media(Dados):.2f}")
print(f"A variancia= {variancia(Dados):.2f}")
print(f"O desvio padrao= {desvio_Padrao(Dados):.2f}")


# Sim, há uma variação considerável nos valores das faturas. A alta variância de 884512.82 reais² e o desvio padrão elevado 
# de 940.49 reais indicam que os valores das faturas estão bastante dispersos em relação à média. Isso sugere que há uma 
# grande diferença entre as faturas mais altas e as mais baixas, o que reflete uma ampla gama de hábitos de consumo entre os
# clientes. Em outras palavras, os dados mostram que existem perfis de consumo muito variados, com alguns clientes gastando 
# significativamente mais do que outros. Essa variação pode ser útil para identificar segmentos de clientes com 
# comportamentos de gasto distintos e potencialmente adaptar estratégias de marketing e ofertas para melhor atender a esses 
# diferentes perfis.
