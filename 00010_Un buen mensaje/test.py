pepita = Golondrina

def test_"comer_alpiste! 0 debería fallar":
  expect { pepita.comer_alpiste! 0 }.to raise_error


def test_"comer_alpiste! -10 debería fallar":
  expect { pepita.comer_alpiste! -10 }.to raise_error


def test_"comer_alpiste! -10 debería lanzar un mensaje de error expresivo":
  begin
    pepita.comer_alpiste! -10
  rescue => e
    expect(["positiv", "negativ", "cantidad", "menor", "cero", "0", "-10"].any? { |it| e.message.include?(it) }).to be True



def test_"comer_alpiste! 10 NO debería fallar":
  pepita.comer_alpiste! 10
