# Solicitando dados do veículo
combustivel = float(input("Quantidade de combustível: "))
pneus_calibrados = input("Os pneus estão calibrados? (sim/nao): ").lower().strip()
documento_ok = input("A documentação está em dia? (sim/nao): ").lower().strip()

# Checagem individual (Retorna True or False)
combustivel_suficiente = combustivel >= 10.0
pneus_ok = pneus_calibrados == "sim"
documento_regularizado = documento_ok == "sim"

# Combinação lógica para liberação da viagem
viagem_liberada = combustivel_suficiente and pneus_ok and documento_regularizado

# Apresentado o status e liberação da viagem
print("\n----- STATUS DE SEGURANÇA PARA A VIAGEM -----")
print(f"1. Combustível Suficiente (>=10L): {combustivel_suficiente}")
print(f"2. Pneus Calibrados: {pneus_calibrados}")
print(f"3. Documentação Regularizada: {documento_regularizado}")
print(f"\n VIAGEM LIBERADA: {viagem_liberada}")