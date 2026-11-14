# Atribuindo variável
total_componentes = 255
OPERADORES = 4

# Quantos componentes inteiros cada operador vai processar
componentes = total_componentes // OPERADORES

# Cálculo da sobra
sobra_componentes = componentes % OPERADORES

print(f"Cada operador vai processar {componentes} componentes e vão sobrar {sobra_componentes} componentes no lote de sobra.")