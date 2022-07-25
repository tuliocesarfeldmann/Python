from treeObjects import Tree
from Pessoa import Pessoa

arv = Tree()
print("Programa Arvore Binaria")
opcao = 0
id = 0
while opcao != 8:
    print("***********************************")
    print("Entre com a opcao:")
    print(" --- 1: Inserir")
    print(" --- 2: Excluir")
    print(" --- 3: Pesquisar")
    print(" --- 4: Exibir")
    print(" --- 5: Gerar arvore aleatória")
    print(" --- 6: Arvore para lista")
    print(" --- 7: Sair")
    print("***********************************")
    opcao = int(input("-> "))
    if opcao == 1:
        nome = str(input(" Informe o nome -> "))
        sobrenome = str(input(" Informe o sobrenome -> "))
        idade = int(input(" Informe a idade -> "))
        arv.inserir(Pessoa(id, sobrenome, nome, idade))
        id+=1
    elif opcao == 2:
        nome = str(input(" Informe o nome -> "))
        if arv.remover(nome) == False:
            print(" Valor nao encontrado!")
    elif opcao == 3:
        nome = str(input(" Informe o nome -> "))
        busca = arv.buscar(nome)
        if busca != None:
            print(busca.item.getRegistro())
        else:
            print(" Nao encontrado!")
    elif opcao == 4:
        arv.caminhar()
    elif opcao == 5:
        altura = int(input("Informe a altura da árvore: "))
        arv.gerarArvoreAleatoria(altura, id)
    elif opcao == 6:
        arr = []
        arr = arv.arvoreParaLista(arv.root, arr)
        print(arr)
    elif opcao == 7:
        break