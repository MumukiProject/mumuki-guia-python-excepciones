class Saqueo:
  def __init__(self, self, barco_saqueador):
    self.barco = barco_saqueador


  def realizar_contra!(self, ciudad):
    self.barco.preparar_tripulacion!
    self.barco.desembarcar!(ciudad)
    if (ciudad.puede_hacerle_frente_a?(self.barco))
      raise "No se puede invadir la ciudad"



