class Animal:
    def __init__ (self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def emitirSom(self):
        print("Rosnar")

class Cachorro(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
    
    def emitirSom(self):
        print("auau")

class Gato(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
    
    def emitirSom(self):
        print("Miau")
        
class Pato(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
    
    def emitirSom(self):
        print("quack")
        
cachorro = Cachorro("Bruce", "2")
gato = Gato("Sininho", "4")
pato = Pato("Oliver", "3")

cachorro.emitirSom()
gato.emitirSom()
pato.emitirSom()





        
        

        
        
        