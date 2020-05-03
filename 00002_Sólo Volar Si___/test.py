describe:
  pepita = Golondrina

  def test_"si Pepita vuela una vez, consume 20":
    pepita.volar_en_circulos!
    expect(pepita.energia).to eq 30


  def test_"si Pepita vuela dos veces, consume 40":
    pepita.volar_en_circulos!
    pepita.volar_en_circulos!
    expect(pepita.energia).to eq 10


  def test_"si le pedimos a Pepita que vuele 10 veces, consume solo 40":
    10.times { pepita.volar_en_circulos! }
    expect(pepita.energia).to eq 10

