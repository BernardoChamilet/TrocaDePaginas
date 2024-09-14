import json
#Obtendo arquivo de entrada e tranformando em lista
arq = open('acessos-pag-T2.txt', 'r')
paginasAcessadas = arq.read()
arq.close()
paginasAcessadas = paginasAcessadas.strip().split('\n')
#salvando indices que cada página é referenciada
ocorrenciasPagina = {}
for indice in range(0,len(paginasAcessadas)):
    pagina = paginasAcessadas[indice]
    if pagina in ocorrenciasPagina:
        ocorrenciasPagina[pagina].append(indice)
    else:
        ocorrenciasPagina[pagina] = [indice]
#Salvando em um json para o algoritmo ótimo usar
arq = open('otimoReferenciasT2.json','w')
json.dump(ocorrenciasPagina, arq)
arq.close()