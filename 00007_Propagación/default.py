class Transferencia:
  def __init__(self, self, monto_a_transferir):
    self.monto = monto_a_transferir


  def realizar!(self, origen, destino):
    origen.debitar! self.monto
    destino.depositar! self.monto


