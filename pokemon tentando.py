class Pokemon:
    def __init__(self, nome, poder, vida):
        self.nome = nome
        self.poder = poder
        self.vida = vida
        
        
class pokemonFogo(Pokemon):
    def __init__(self, nome, poder, vida):
        super().__init__(nome, poder, vida)

class pokemonAquatico(Pokemon):
    def __init__(self, nome, poder, vida):
        super().__init__(nome, poder, vida)

class pokemonEletrico(Pokemon):
    def __init__(self, nome, poder, vida):
        super().__init__(nome, poder, vida)

pokemon1 = pokemonFogo("Charmander", 60, 100)
pokemon2 = pokemonAquatico("Squirtle", 60, 100)
pokemon3 = pokemonEletrico("Pikachu", 60, 100)

print(pokemon1.nome)


    
    