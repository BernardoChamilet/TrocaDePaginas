#Obtendo arquivo de entrada e tranformando em lista
arq = open('acessos-pag-T.txt', 'r')
paginasAcessadas = arq.read()
arq.close()
paginasAcessadas = paginasAcessadas.strip().split('\n')
#Estabelendo tamanho máximo da memória
tamanhoMemoria = int(input("Quanto de memória tem? em KB"))
numMaxPaginasNaMemoria = int(tamanhoMemoria/4)
memoria = {}
numVezesPaginaFoiCarregada = {}
numFaltasPaginaNFU = 0
#Percorrendo arquivo
for pagina in paginasAcessadas:
    #Vendo se a página está na memória
    if pagina in memoria:
        #incrementa cont
        memoria[pagina] += 1
    else:
        #Vendo se memoria está cheia
        if len(memoria) == numMaxPaginasNaMemoria:
            #tira da memória a página com menor cont
            paginaComMenorCont = min(memoria,key=memoria.get)
            del memoria[paginaComMenorCont]
        #adcionando página na memória
        memoria[pagina] = 0
        #incrementando número de vezes que essa página foi carregada e número de faltas de página
        numFaltasPaginaNFU += 1
        if pagina in numVezesPaginaFoiCarregada:
            numVezesPaginaFoiCarregada[pagina] += 1
        else:
            numVezesPaginaFoiCarregada[pagina] = 1
#Resultados
print(f"Com o algoritmo NFU ocorrem {numFaltasPaginaNFU} faltas de pagina,")
acao = input("Deseja listar o numero de carregamentos de cada página (s/n)?")
if acao == "s":
    for chave, valor in numVezesPaginaFoiCarregada.items():
        print(f"{chave}   {valor}")