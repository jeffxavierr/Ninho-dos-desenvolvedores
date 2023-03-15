class Pokemon():
    def __init__ (self, nome, tipo, vida, ataque):
        self.nome = nome
        self.tipo = tipo
        self.vida = vida
        self.ataque = ataque
    
    def perderVida(self, dano):
        self.vida = self.vida - dano 
             
        

if __name__ == "__main__" :
    pokemon1 = Pokemon("Treecko", "grama", 40, 2)
    pokemon2 = Pokemon("Hitmonlee", "Lutador", 40, 2)
    
while True:
    inicial = int(input('''
    Digite 1 para: Treecko
    Digite 2 para: Hitmonlee:  
    '''))
 
    if inicial < 1 or inicial > 2:  
        print("Tente novamente")
    else:
        break

if inicial == 1:
        inicial = "Treecko"
elif inicial == 2:
        inicial = "Hitmonlee"
print("prepare-se para a batalha com", inicial)

if inicial == "Treecko":
    rival = "Hitmonlee"
    print("o seu rival é o Hitmonlee")
elif inicial == "Hitmonlee":
    rival = "Treecko"
    print("o seu rival é o Treecko")
    

    
    





        
                  