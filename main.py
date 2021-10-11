import numpy as np
import kruskal as kr
if __name__ == '__main__':
    x = 1
    dados = np.zeros((1,1))
    dados = kr.intro(dados)
    while x!=0:
        print("1 - Inserir vértice")
        print('2 - Inserir peso em um vértice')
        print('3 - Imprimir grafo (Matriz)')
        print('4 - Kruskal')
        print('0 - Sair')
        x = int(input('Digite a opção: '))
        if x==1:
            if len(dados)<20:
                dados = kr.inserir(dados)
            else:
                print('Número máximo atingido')
                print('Não é possível inserir mais vértices')
        elif x==2:
            dados = kr.manipula(dados)
        elif x==3:
            kr.imprimir(dados)
        elif x==4:
            kr.kruskal(dados)