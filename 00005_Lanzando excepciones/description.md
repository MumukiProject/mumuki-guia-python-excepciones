¿Interesante, no? No solamente tuvimos un mensaje de error claro que nos permite entender qué sucedió, sino que además evitó que se deposite dinero en la cuenta de destino :smile:. ¿Cómo fue esto posible?

La primera versión del método `debitar!` en `CuentaOrigen` se veía aproximadamente así:

```python
def debitar!(self, monto):
  if monto <= self.saldo
    self.saldo -= monto


```

Pero la segunda versión se ve así:

```python
def debitar!(self, monto):
  if monto > self.saldo
    raise "No se puede debitar, porque el monto $#{monto} es mayor al saldo $#{self.saldo}"


  self.saldo -= monto

```

Mediante la sentencia `raise mensaje` lo que hicimos fue _lanzar una excepción_: provocar un error explícito que _interrumpe_ el flujo del programa.

> ¡Más despacio cerebrito! :hand: Probá enviar `mensaje_raro` a `ObjetoRaro` (que ya cargamos por vos) en la consola...
>
> ```python
> module ObjetoRaro
>    def self.mensaje_rar(self):
>       raise "foo"
>       4
>
>
> ```
>
> ...y pensá: ¿se retorna el 4? ¿Por qué?


