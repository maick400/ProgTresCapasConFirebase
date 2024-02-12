from App.conexion  import *
class Producto:
    def __init__(self, id, descripcion, tipo_producto, precio ):
        self.id = id; 
        self.descripcion = descripcion 
        self.tipo_producto = tipo_producto 
        self.precio = precio
        self.caducidad = precio

        
    def registar (self): 
        conec = conexion()
        conec.guardar ('Productos/', vars(self))
    @staticmethod
    def eliminar ( id ): 
        conec = conexion()
        conec.eliminar ('Productos/', id)
        
        
    @staticmethod 
    def editar (datos, key): 
        conec = conexion()
        print (f'datos: {datos}')
        conec.editar (f'Productos/{key}', datos )
        
    @staticmethod
    def listar (): 
        conec = conexion()
        return conec.obtener_data ('Productos/')
    @staticmethod
    def get (id):
        conec = conexion()
        prod = conec.obtener_data (f'Productos/{id}')
        print(prod)
        return prod
    
    