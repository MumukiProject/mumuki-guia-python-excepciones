Que los objetos _fallen silenciosamente_ es malo porque perdemos la confianza en ellos :broken_heart:: no estamos seguros de que el objeto haya cumplido con nuestra orden.

Esto no parece tan terrible cuando del vuelo de las golondrinas se trata, pero ¿y si estamos haciendo una transferencia bancaria?

```python
class Transferencia:
  def __init__(self, self, monto_a_transferir):
    self.monto = monto_a_transferir


  def realizar!(self, origen, destino):
    origen.debitar! self.monto
    destino.depositar! self.monto



transferencia = Transferencia(40)
cuenta_origen = CuentaOrigen
cuenta_destino = CuentaDestino

```

¿Qué sucedería si realizamos la transferencia y `debitar!` **no** debitara de la cuenta origen cuando no tiene saldo?

> ¡Descubrilo! Haciendo consultas en la consola, averiguá con cuánto dinero comienzan y terminan la `cuenta_origen` y la `cuenta_destino`.
>
> Asumí que ambas cuentas entienden el mensaje `saldo`.

