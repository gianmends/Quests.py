from monstro import Monstro

class Goblin(Monstro):
  def __init__(self, vida, ataque, tipo, inteligencia):
    super().__init__(vida, ataque, tipo)
    self.interligencia:int = inteligencia