class ContaBancaria:
  def __init__(self, titular, saldo):
    self.titular: str = titular
    self.saldo: float = saldo

  def depositar(self, valor):
    self.saldo += valor

  def sacar(self, valor):
    if valor <= self.saldo:
      self.saldo -= valor
    
    else:
      print("Saldo insuficiente")
  
  def consultar_saldo(self):
    print(f"Saldo atual: R${self.saldo}")

cliente = ContaBancaria("Giancarlo", 100)

#metodo = função
#atributo = definições da função

#herança = a capacidade de uma subclasse herdar uma classe. Ex: Class Animal e Class Cachorro.

#poliformismo = a capacidade que uma mesma função assume propriedades diferentes em outras subclasses. Ex: class animal: def fazer_barulho: pass / class cachorro: def fazer_barulho: print (au au)