class SerVivo:
  def __init__(self, vida, ataque):
    self.vida:int = vida
    self.ataque:int = ataque

class Personagem(SerVivo):
  def __init__(self, vida, ataque, nome):
    super().__init__(vida, ataque)
    self.nome:str = nome

class monstro(SerVivo):
  def __init__(self, vida, ataque, tipo):
    super().__init__(vida, ataque)
    self.tipo:str = tipo

class lobo(monstro):
  def __init__(self, vida, ataque, tipo, força):
    super().__init__(vida, ataque, tipo)
    self.força:int = força
  
class goblin(monstro):
  def __init__(self, vida, ataque, tipo, inteligencia):
    super().__init__(vida, ataque, tipo)
    self.interligencia:int = inteligencia
