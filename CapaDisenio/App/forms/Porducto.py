from django import forms

class frm_Producto (forms.Form):
    id =  forms.CharField(label= 'Id', required=True)
    descripcion = forms.CharField(label= 'Descripcion', required=True)
    tipo_producto = forms.ChoiceField(choices= (('VIV','VIVERES'), ('CNF', 'CONFITERIA')), required= True)
    precio = forms.FloatField(label= 'Precio' , min_value= 0 , required=True)
    
    
    
