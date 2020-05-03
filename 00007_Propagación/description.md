Como decíamos recién, las excepciones no abortan simplemente la evaluación del método, sino que también abortan la evaluación de toda la cadena de envío de mensajes.

Por ejemplo, si bien en el programa anterior `CuentaOrigen.debitar!(monto)` era un mensaje que podía lanzar una excepción....

```python
def debitar!(self, monto):
  if monto > self.saldo
    raise "No se puede debitar, porque el monto $#{monto} es mayor al saldo $#{self.saldo}"


  self.saldo -= monto

```

...esta excepción no sólo evitaba que se evaluara `saldo -= monto`, sino que también evitaba que `CuentaDestino.depositar! monto` se enviara. Mirá el código de `realizar!` en `Transferencia`:

```python
  def realizar!(self, origen, destino):
    origen.debitar! self.monto
    destino.depositar! self.monto

```

A esto nos referimos cuando decimos que las excepciones interrupen el flujo del programa :sunglasses:.

> Veamos si se entiende: agregá a la clase `Transferencia` un método `deshacer!` que sea exactamente al revés del `realizar!`: debe revertir la transferencia, moviendo el monto de la cuenta destino a la de origen.
>
> Como ahora tanto la cuenta origen como la cuenta destino pueden `debitar` y `depositar`, unificamos su comportamiento en una clase `Cuenta`. La podés ver en la solapa Biblioteca.
