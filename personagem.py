from rpg import SerVivo

class Personagem(SerVivo):
  def __init__(self, vida, ataque, nome):
    super().__init__(vida, ataque)
    self.nome:str = nome