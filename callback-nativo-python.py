class ObservadorVariable:
    def __init__(self, valor_inicial):
        self._valor = valor_inicial
        self.callback = None # Aquí guardaremos la función a ejecutar

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, nuevo_valor):
        if self._valor != nuevo_valor:
            self._valor = nuevo_valor
            if self.callback:
                self.callback(self._valor) # Ejecuta el callback

# Uso
def mi_reaccion(nuevo_val):
    print(f"¡La variable cambió a: {nuevo_val}!")

obj = ObservadorVariable(10)
obj.callback = mi_reaccion # Registrar el callback

obj.valor = 20 # Salida: ¡La variable cambió a: 20!
obj.valor = 30 # Salida: ¡La variable cambió a: 30!
