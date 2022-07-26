from tree import Tree
from binarytree import build

arv = Tree()
print("Programa Arvore Binaria")
opcao = 0
while opcao != 8:
    print("***********************************")
    print("Entre com a opcao:")
    print(" --- 1: Inserir")
    print(" --- 2: Excluir")
    print(" --- 3: Pesquisar")
    print(" --- 4: Exibir")
    print(" --- 5: Gerar arvore aleatória")
    print(" --- 6: Arvore para lista")
    print(" --- 7: Mostrar árvore graficamante")
    print(" --- 8: Sair do programa")
    print("***********************************")
    opcao = int(input("-> "))
    if opcao == 1:
        x = int(input(" Informe o valor -> "))
        arv.inserir(x)
    elif opcao == 2:
        x = int(input(" Informe o valor -> "))
        if arv.remover(x) == False:
            print(" Valor nao encontrado!")
    elif opcao == 3:
        x = int(input(" Informe o valor -> "))
        if arv.buscar(x) != None:
            print(" Valor Encontrado")
        else:
            print(" Valor nao encontrado!")
    elif opcao == 4:
        arv.caminhar()
    elif opcao == 5:
        altura = int(input("Informe a altura da árvore: "))
        arv.gerarArvoreAleatoria(altura)
    elif opcao == 6:
        a = []
        a = arv.arvoreParaLista(arv.root, a)
        print(a)
    elif opcao == 7:
        arr = []
        arr = arv.imprimirGraficamente(arr)
        bst = build(arr)
        print(bst)
    elif opcao == 8:
        break
