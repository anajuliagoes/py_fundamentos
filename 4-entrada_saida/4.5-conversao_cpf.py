# Solicitando o CPF ao usuário
cpf = input("Digite seu CPF: ")

# Realizando a remoção do . e - e armazenando CPF limpo
cpf_limpo = cpf.replace(".","").replace("-","")

# Apresentando resultado do CPF limpo
print(f"CPF Limpo: {cpf_limpo}")