transferencia = Transferencia(40)

def test_"Realizar una transferencia de la cuenta origen a la destino falla":
  expect { transferencia.realizar!(cuenta_origen, cuenta_destino) }. to raise_error


def test_"Deshacer una transferencia de la cuenta destino a la origen las deja con los saldos correctos":
  transferencia.deshacer!(cuenta_origen, cuenta_destino)
  expect(cuenta_origen.saldo).to eq 60
  expect(cuenta_destino.saldo).to eq 60

