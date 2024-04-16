# considere utilizar objetos para representar entidades
# no mundo real.
class Carro():
    def __init__(self, nome, placa, marca):
        self.nome = nome
        self.placa = placa
        self.marca = marca
    
    def setNome(self, nome):
        self.nome = nome
    
    def setPlaca(self, placa):
        self.placa = placa
    
    def setMarca(self, marca):
        self.marca= marca
        
    def deleteNome(self):
        self.nome = None 
        
    def deletePlaca(self):
        self.placa = None
        
    def deleteMarca(self):
        self.marca = None   
    
# Instanciando os objetos
onix = Carro(nome="onix", placa="abc-0912", marca="chevrolet")
gol = Carro(nome="gol", placa="def-3456", marca="volkswagen")
corolla = Carro(nome="corolla", placa="ghi-7890", marca="toyota")
carros = {0:onix, 
          1: gol,
          2: corolla}
print(f"O carro {carros[0].nome} tem a placa {carros[0].placa}")

# sem utilizar objetos 
carros = {
    0: {
        "nome": "onix",
        "placa": "abc-0912",
        "marca": "chevrolet",
    },
    1: {
        "nome": "gol",
        "placa": "def-3456",
        "marca": "volkswagen",
    },
    2: {
        "nome": "corolla",
        "placa": "ghi-7890",
        "marca": "toyota",
    },
}
