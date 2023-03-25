from monstro import Monstro

class Lobo(Monstro):
  def __init__(self, vida, ataque, tipo, força):
    super().__init__(vida, ataque, tipo)
    self.força:int = força