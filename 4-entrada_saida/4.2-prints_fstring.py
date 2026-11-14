nome = "Ana"
curso = "fundamentos de python"
preco = 49.9
codigo_peca = 7

print("Aluna: ", nome," | Curso: ", curso.title())
print(f"Aluna: {nome} | Curso: {curso.title()}")

print(f"Valor original (ponto): R$ {preco:.2f}".replace(".",","))
print(f"Código da peça: #{codigo_peca:05d}")