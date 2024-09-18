#Aula_07-condicionais
cod_bca = 'BCA001'
cod_bsa = 'BSA001'
linha = '--------------------------------------------------'
print('\n' + linha)
bebida = input("Insira o codigo da bebida em letra MAIUSCULA:  ")
if 'BAC' in bebida:
    print(linha)
    print(f"Essa bebida possui alcool, a venda é proibida para menores, o codigo é {bebida}")
    print(linha)
else:
    print(linha)
    print(f"Essa bebida não possui alcool, o codigo é {bebida}")
    print(linha)