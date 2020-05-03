barco_pirata = Barco
saqueo = Saqueo(barco_pirata)
ciudad = Ciudad

def test_"El saqueo se realiza en el orden correcto":
  saqueo.realizar_contra!(ciudad)
  expect(Eventos.es).to eq ["puede_hacer_frente", "preparar", "desembarcar"]

