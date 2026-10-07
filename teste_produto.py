from produto import produto

p1 = produto()
p1.codigo = 123456
p1.nome = "pratos de plástico"
p1.quantidade = 150
p1.preco = 9.99
p1.tipo = 0.1

p2 = produto()
p2.codigo = 678912
p2.nome = "talheres de plástico"
p2.quantidade = 350
p2.preco = 12.99
p2.tipo = 0.2

print(f"{p1.nome}: {p1.quantidade}: {p1.codigo}: {p1.preco}: {p1,tipo}  un")
print(f"{p2.nome}: {p2.quantidade}: {p2.codigo}: {p2.preco}: {p2.tipo}  un.")