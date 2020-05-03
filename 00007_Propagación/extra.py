class Cuenta:
  def __init__(self, self, saldo_inicial):
    self.saldo = saldo_inicial


  def debitar!(self, monto):
    if monto > self.saldo
      raise "No se puede debitar, porque el monto $#{monto} es mayor al saldo $#{self.saldo}"


    self.saldo -= monto


  def depositar!(self, monto):
      self.saldo += monto


  def sald(self):
    self.saldo



cuenta_origen = Cuenta(20)
cuenta_destino = Cuenta(100)
