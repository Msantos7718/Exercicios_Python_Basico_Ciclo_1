# Faça uma atualização no código do exercício anterior, agora o programa deve exibir o nome do produto, o valor do desconto e o valor final do produto.

# OUTPUT ESPERADO:

# Produto: FIAT TORO
# Preço: 200000
# Porcentagem de desconto: 15
# O FIAT TORO com 15.0% de desconto custará R$ 170000.0

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------
produto= input(' digite o nome do produto')
peco= float(input('qualo preco do produto'))
porcentagem = float(input('qual o porcentagem do desconto'))
desconto= preco * (porcentagem/100)
print(f'o { produto} com {porcentagem}% de desconto, custaraR${desconto}')