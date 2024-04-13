# considere utilizar operadores ternarios para melhorar a legibilidade do seu codigo em python.

# convencional
idade = 20
if idade >= 18:
    status = "adulto"
else:
    status = "menor"

# operador ternário
idade = 20
status = "adulto" if idade >= 18 else "menor"
