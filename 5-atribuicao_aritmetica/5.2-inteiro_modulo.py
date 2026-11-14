# Definindo o valor das variáveis
total_sensores = int(input("Quantos sensores pretende embalar?: "))
CAPACIDADE_CAIXA = 12

# Quantas caixas completas podemos encher?
caixas_fechadas = total_sensores // CAPACIDADE_CAIXA

# Quantos sensores vão sobrar avulsos?
sobra_sensores = total_sensores % CAPACIDADE_CAIXA

print(f"Preencher {caixas_fechadas} caixas e guardar {sobra_sensores} peças avulsas.")