import numpy as np
def inserir(dados):
    #cria uma nova coluna
    dados = np.insert(dados, dados.shape[0], 0, axis=0)
    #cria uma nova linha
    dados = np.insert(dados, dados.shape[1], 0, axis=1)
    print('Vértice criado')
    return dados

#manipula os valores de dados
def manipula(dados):
    imprimir(dados)
    x = int(input('Qual o índice da coluna: '))
    y = int(input('Qual o índice da linha: '))
    peso = float(input('Qual o peso desse vértice: '))
    if x == y:
        print('Impossível inserir peso no próprio vértice')
    else: 
        #adiciona o peso numa coordenada já existente
        dados[y,x] = peso
        dados[x,y] = 0.0
    return dados

#imprime a matriz
def imprimir(dados):
    print('Imprimindo')
    print(0,end='\t')
    for i in range(len(dados)):
        print(i, end='\t')
    print('\n')
    for i in range(len(dados)):
        print(i, end = '\t')
        for j in range(len(dados)):
            print(dados[i][j], end = '\t')
        print('\n')

#carrega ou não um grafo pré salvo
def intro(dados):
    print('Deseja carregar um grafo pré-salvo? ')
    print('1 - Sim, carregar grafo')
    print('2 - Não, inserir/criar grafo')
    opcao = int(input('Digite: '))
    if opcao==1:
        dados = [[ 0.,  9., 75.,  0.,  0.],
                 [ 0.,  0., 95., 19., 42.], 
                 [ 0.,  0.,  0., 51.,  0.], 
                 [ 0.,  0.,  0.,  0., 31.], 
                 [ 0.,  0.,  0.,  0.,  0.]] 
        return dados
    if opcao==2:
        return dados

#retorna uma lista ordenada das ligações existentes no grafo
def organiza(dados):
    vertices = []
    for j in range(len(dados)):
        for i in range(len(dados)):
            if dados[j][i]!=0:
                vertices.append([dados[j][i],[j,i]])
    #ordena vertices do menor ao maior peso
    vertices = sorted(vertices)
    return vertices
    
#ordena e limpa os vertices repetidos na lista arestas
def ordena(arestas):
    arestas = sorted(set(arestas))
    return arestas 

#simula um xor : não nativo do python
def xor(x, y):
    return bool((x and not y) or (not x and y))

#printa o resultado
def visualiza(vertices, arestas, floresta):
    print('Vertices restantes: {}'.format(vertices))
    print('Arestas encontradas: {}'.format(arestas))
    print('Formato de floresta formada: [origem,destino] - peso')
    for i in range(len(floresta)):
        print(floresta[i][1],end='\t')
        print('-',end='\t')
        print(floresta[i][0])

def kruskal(dados):
    arestas = []  #arestas analisadas
    floresta = [] #floresta final
    vertices = [] #vértices a serem analisados
    vertices = organiza(dados) #ordena os vertices
    #passo inicial
    arestas = vertices[0][1] #arestas recebe o primeiro passo
    arestas = ordena(arestas) #ordena e exclui repetidos em arestas
    floresta = [vertices[0]] #floresta recebe o primeiro passo
    vertices.pop(0)
    #fim passo inicial
    print('Aresta inicial: {}'.format(arestas))
    print('Floresta inicial: {}'.format(floresta))
    print('Vertices restantes: {}'.format(vertices))
    #enquanto houver vertices a serem analisados
    while len(vertices)>0:
        #não foi incluido na floresta ainda
        if xor((vertices[0][1][0] in arestas),(vertices[0][1][1] in arestas)):
            print('não encontrado: {}'.format(vertices[0][1]))
            #ordena e exclui repetidos em arestas
            arestas = ordena(arestas)
            #inclui vertice em arestas
            arestas.extend(vertices[0][1])
            #ordena e exclui repetidos em arestas
            arestas = ordena(arestas)
            #inclui vertice na floresta
            floresta.extend([vertices[0]])
            #exclui vertice
            vertices.pop(0)
        #ja foi incluido na floresta/formaria ciclo
        else:
            print('já encontrado: {}'.format(vertices[0][1]))
            #ordena e exclui repetidos em arestas
            arestas = ordena(arestas)
            #exclui vertice
            vertices.pop(0)
    visualiza(vertices, arestas, floresta)    
