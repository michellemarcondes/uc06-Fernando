#Aula 07-Condicionais_Faturamento
linha = '--------------------------------------------------'
print(linha)
qt_cc = int(input("Quantas latas de Coca Cola foram vendidas? "))
print(linha)
qt_ps = int(input("Quantas latas de Pepsi foram vendidas? "))
print(linha)
vl_cc = float(input("Qual o preço unitario da Coca Cola? "))
print(linha)
vl_ps = float(input("Qual o preço unitario da Pepsi? "))
print(linha)
investimento = int(input("Qual o valor do investimento dos produtos? "))
print(linha)
faturamento = (qt_cc * vl_cc) + (qt_ps * vl_ps)
if faturamento > investimento:
    print(f"Sua adega teve LUCRO, com um faturamento de R${faturamento:,.2f}")
else:
    print(f"Sua adega teve PREJUÍZO, com um faturamento de R${faturamento:,.2f} sendo menor que o valor de investimento, R${investimento:,.2f}")
