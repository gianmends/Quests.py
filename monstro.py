from rpg import SerVivo

class Monstro(SerVivo):
  def __init__(self, vida, ataque, tipo):
    super().__init__(vida, ataque)
    self.tipo:str = tipo