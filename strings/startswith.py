sequences = [
    "10010001",
    "10010110",
    "10011000",
    "11001010",
    "11010011",
    "10101010",
    "11110000",
    "01100101",
    "01010111",
    "00111010"
]

# Verificando se uma string começa com um prefixo
filtered_sequences = [s for s in sequences if s.startswith("1001")]
print(filtered_sequences)
# ['10010001', '10010110', '10011000']
