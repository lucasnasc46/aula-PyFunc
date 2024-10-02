def calPrecoDesc(prod, desconto):
    total=0
    for x in prod:
        total += x['valor']

    valorDesconto = total * (1 - desconto/100)
    return valorDesconto

produtos=[
    {'nome': 'produtoA', 'valor':50},
    {'nome': 'produtoB', 'valor':30} 
]

precoFinal = calPrecoDesc(produtos, 20)

print(f"suas compras com desconto foi de {precoFinal}")