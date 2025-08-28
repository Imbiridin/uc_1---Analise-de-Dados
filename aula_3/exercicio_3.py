'''Uma empresa precisa que quando o usuário difgitar o número 1, o programa imprimirá a palavra "Alimentos"
    Se o usuário digitar o número 2, imprimirá a palavra "Bebidas"
    Se o usuário digitar o número 3 ou 4, imprimirá a palavra "Cosméticos"
    Se o usuário dgitar o número 5 ou 6, imprimirá a palavra "Produtos de Limpeza"
    
    Qualuer outro o programa imprimirá "Categoria não encontrada"'''
    
produto = int(input('''Digite um número para selecionar uma categoria
                 
1 - Alimentos
2 - Bebidas
3 e 4 - Cosméticos
5 e 6 - Produtos de Limpeza

Escolha a categoria:'''))

if produto == 1:
    print("\nAlimentos")
elif produto == 2:
    print("\nBebidas")
elif produto == 3 or produto == 4:
    print("\nCosméticos")
elif produto == 5 or produto == 6:
    print("\nProdutos de Limpeza")
else:
    print("\nCategoria não encontrada!")