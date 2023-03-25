class SerVivo:
  def __init__(self, vida, ataque):
    self.vida:int = vida
    self.ataque:int = ataque

class Personagem(SerVivo):
  def __init__(self, vida, ataque, nome):
    super().__init__(vida, ataque)
    self.nome:str = nome

class Monstro(SerVivo):
  def __init__(self, vida, ataque, tipo):
    super().__init__(vida, ataque)
    self.tipo:str = tipo

class Lobo(Monstro):
  def __init__(self, vida, ataque, tipo, força):
    super().__init__(vida, ataque, tipo)
    self.força:int = força
  
class Goblin(Monstro):
  def __init__(self, vida, ataque, tipo, inteligencia):
    super().__init__(vida, ataque, tipo)
    self.interligencia:int = inteligencia
