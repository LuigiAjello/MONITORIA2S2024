import statistics as st
Dados=[5, 8, 7, 10, 15, 12, 9, 20, 25, 30, 8, 10, 9, 7, 5, 8, 14, 16, 18, 22, 7, 5, 8,9, 12, 15, 17, 20, 25, 10]
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


# A moda é 8 minutos, o que indica que este é o tempo mais comum que os clientes levam para concluir a compra. 
# A mediana é 10 minutos, representando o ponto central dos tempos, e a média é 13 minutos, um pouco mais alta, 
# indicando que alguns clientes levam mais tempo que o tempo médio. A variância e o desvio padrão mostram que há 
# uma dispersão considerável nos tempos de decisão dos clientes, sugerindo uma variação significativa no comportamento 
# de compra.






