class Cliente:
    def __init__(self, nombre, apellido, direccion, correo):
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.correo = correo
        
    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}"
    
    def actualizar_direccion(self, nueva_direccion):
        self.direccion = nueva_direccion
        
    def enviar_correo(self, mensaje):
        
        pass


cliente_ejemplo = Cliente("Juan", "Pérez", "Calle siempre viva 712", "juan.perez@gmail.com")


cliente_ejemplo.actualizar_direccion("habana 4310")
print(f"Dirección actualizada de {cliente_ejemplo}: {cliente_ejemplo.direccion}")

mensaje_ejemplo = "Segurulo y Habana"
cliente_ejemplo.enviar_correo(mensaje_ejemplo)
print(f"Mensaje enviado a {cliente_ejemplo.correo}: {mensaje_ejemplo}")
