# utilize o método enumerate para iterar sobre objetos em python

casas = ['rua 1, endereço 1', 'rua 2, endereço 2', 
         'rua 3, endereço 3']

for i, endereco in enumerate(casas):
    print("index: ", i)
    print("endereço: ", endereco)
    
"""
index:  0
endereço:  rua 1, endereço 1
index:  1
endereço:  rua 2, endereço 2
index:  2
endereço:  rua 3, endereço 3

"""