pepita = Golondrina

def test_"Si una golondrina vuela una vez, consume 20":
  pepita.volar_en_circulos!
  expect(pepita.energia).to eq 30


def test_"Si una golondrina vuela dos veces, consume 40":
  pepita.volar_en_circulos!
  expect(pepita.energia).to eq 10


def test_"Si le pedimos a una golondrina que vuele 3 veces, lanza una excepción y consume sólo 40":
  expect { pepita.volar_en_circulos! }.to raise_error
  expect(pepita.energia).to eq 10


def test_"La excepción que se lanza tiene la descripción correcta":
  expect { pepita.volar_en_circulos! }.to raise_error("No tengo suficiente energía")
