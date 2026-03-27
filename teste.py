import csv

total = 0
produtos = {}

with open('dados.csv', newline='', encoding= 'utf-8') as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        produto = linha['produto']
        preco = int(linha['preco'])
        quantidade = int(linha['quantidade'])
        total += preco * quantidade
        print(produto,'|qnt:',quantidade,'|R$:', preco)
        if produto in produtos:
            produtos[produto] += quantidade
        else:
            produtos[produto] = quantidade
print('\nTodos de vendas: ', total)

print('\nTodos os produtos: ')
for p, q in produtos.items():
    print(p, 'quantidade:',q)
