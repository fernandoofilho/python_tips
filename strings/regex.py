import re

# Encontrar todas as palavras que começam com 'a'
text = "apple banana avocado"
matches = re.findall(r'\ba\w+', text)
print(matches)  # Output: ['apple', 'avocado']
