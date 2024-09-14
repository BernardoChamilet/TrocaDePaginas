import json

#Obtendo indices que as páginas são referenciadas
arq = open('otimoReferenciasT.json', 'r')
referenciasPaginas = json.load(arq)
arq.close()
#Obtendo arquivo de entrada e tranformando em lista
arq = open('acessos-pag-T.txt', 'r')
paginasAcessadas = arq.read()
arq.close()
paginasAcessadas = paginasAcessadas.strip().split('\n')
#Estabelendo tamanho máximo da memória
tamanhoMemoria = int(input("Quanto de memória tem? em KB"))
numMaxPaginasNaMemoria = int(tamanhoMemoria/4)
memoria = []
numVezesPaginaFoiCarregada = {}
numFaltasPagina = 0
cont = 0
#Percorrendo arquivo
for pagina in paginasAcessadas:
    #Vendo se a página está na memória
    if pagina not in memoria:
        #Vendo se memoria está cheia
        if len(memoria) == numMaxPaginasNaMemoria:
            #tira da memória a página que vai demorar mais para ser refenciada denovo
            maiorAteAgora = 0
            #percorre as páginas que estão na memória
            for p in range(0, len(memoria)):
                #para cada página que está na memória...
                deuBreak = False
                listaCopia = referenciasPaginas[memoria[p]].copy()
                for referencia in referenciasPaginas[memoria[p]]:
                    #encontra a próxima vez que ela será referenciada
                    if referencia > cont:
                        #atualiza o valor de maiorAteAgora se necessario
                        #maiorAteAgora guarda quando a pagina que vai demorar mais para ser referenciada vai ser referenciada
                        if referencia > maiorAteAgora:
                            maiorAteAgora = referencia
                            indiceDoDonoDoMaiorAteAgora = p
                        deuBreak = True
                        break
                    else:
                        #exclui da lista de referências as ocorrências que são menores que cont, e, portanto, já não vão mais ser usadas
                        listaCopia.remove(referencia)
                referenciasPaginas[memoria[p]] = listaCopia
                #Caso deuBreak for False significa que ele saiu do for porque nenhum dos indices que a página vai ser referenciada foi maior que cont,
                # o que significa que a página não vai mais ser usada, portanto ela é a que deve ser retirada da memória
                if not deuBreak:
                    indiceDoDonoDoMaiorAteAgora = p
                    break
            del memoria[indiceDoDonoDoMaiorAteAgora]
        #adcionando página na memória
        memoria.append(pagina)
        #incrementando número de vezes que essa página foi carregada e número de faltas de página
        numFaltasPagina += 1
        if pagina in numVezesPaginaFoiCarregada:
            numVezesPaginaFoiCarregada[pagina] += 1
        else:
            numVezesPaginaFoiCarregada[pagina] = 1
    cont += 1
#Resultados
print(f"Com o algoritmo Ótimo ocorrem {numFaltasPagina} faltas de pagina,")
acao = input("Deseja listar o numero de carregamentos (s/n)?")
if acao == "s":
    for chave, valor in numVezesPaginaFoiCarregada.items():
        print(f"{chave}   {valor}")