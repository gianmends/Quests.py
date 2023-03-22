class UrnaEletronica:
  def __init__(self):
    self.candidatos = [ {"nome_candidato": "Lula", "partido": "PT"},
                  {"nome_candidato": "Bolsonaro", "partido": "PL"}]

  def exibe_candidatos(self):
    for candidato in self.candidatos:
      print(candidato.get("nome_candidato"), candidato.get("partido"))
  
  def adicionar_novo_candidato(self, nome_candidato, partido):
    self.candidatos.append({"nome_candidato": nome_candidato, "partido": partido})
  
  def remover_ultimo_candidato(self):
    self.candidatos.pop()
  
  def atualizar_candidato(self, indice_candidato, chave, valor):
    try:
      self.candidatos[indice_candidato][chave] = valor
    except IndexError:
        print(f"Índice de candidato inválido {indice_candidato}")

urna = UrnaEletronica()

urna.adicionar_novo_candidato("Eneas", "LIVRE")

urna.remover_ultimo_candidato()

urna.atualizar_candidato(1, "nome_candidato", "Joao her")
urna.atualizar_candidato(1, "partido", "Joao her")


urna.exibe_candidatos()