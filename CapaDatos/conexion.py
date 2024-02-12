from firebase import firebase 

class conexion:
    def __init__(self) :
        self.ccn = firebase.FirebaseApplication('https://proyectotrescapas-default-rtdb.firebaseio.com', None)

    def obtener_data (self, destino):
        return self.ccn.get(destino, '')
    

    
    def guardar (self, destino, datos):
        self.ccn.post (destino, datos)
        
    def editar (self, destino, datos):
        self.ccn.patch (f'{destino}', datos)
        
    def eliminar (self, destino, id):
        self.ccn.delete (f'{destino}', id)
        
    
    


