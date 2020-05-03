class Transferencia:
  def __init__(self, self, monto_a_transferir):
    self.monto = monto_a_transferir


  def realizar!(self, origen, destino):
    origen.debitar! self.monto
    destino.depositar! self.monto



class CuentaOrigen:
  def __init_(self):
    self.saldo = 20


  def debitar!(self, monto):
    if monto > self.saldo
      raise "No se puede debitar, porque el monto $#{monto} es mayor al saldo $#{self.saldo}"


    if (monto <= self.saldo)
      self.saldo -= monto



  def sald(self):
    self.saldo



class CuentaDestino:
  def __init_(self):
    self.saldo = 100


  def depositar!(self, monto):
      self.saldo += monto


  def sald(self):
    self.saldo



transferencia = Transferencia(40)
cuenta_origen = CuentaOrigen
cuenta_destino = CuentaDestino
