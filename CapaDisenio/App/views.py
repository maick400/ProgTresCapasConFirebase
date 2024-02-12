#Produtos 
from django import forms
from django.contrib import messages
from django.shortcuts import render, redirect
from App.forms.Porducto import *
import json

from App.Producto import *


def registrar_producto(request):
    if request.method == 'GET': 
        frm = frm_Producto()
        return render(request, 'Producto/agregar.html' , {'frm' : frm})
    if request.method == 'POST':
        frm = frm_Producto(request.POST)
        if frm.is_valid():
            Prod = Producto (**frm.cleaned_data).registar()
            messages.success(request,"Registro guardado correctamente.")
            
            return redirect ('listar')
        else:
            messages.warning (request,"Algunos campos son incorrectos.")
            return render(request, 'Producto/agregar.html' , {'frm' : frm})
        

def editar_producto(request, id ):
    if request.method == 'GET': 
        
        item = (Producto.get(id))
        frm = frm_Producto( initial= item)
        return render(request, 'Producto/editar.html' , {'frm' : frm})
    
    if request.method == 'POST':
        frm = frm_Producto(request.POST)
        if frm.is_valid():
            Producto.editar (key= id , datos= frm.cleaned_data)
            messages.success(request,"Registro guardado correctamente.")
            
            return redirect ('listar')
        else:
            messages.warning (request,"Algunos campos son incorrectos.")
            return render(request, 'Producto/editar.html' , {'frm' : frm})
        
        
def listar_producto (request):
    if request.method == 'GET': 
        prods = []
        
        data = Producto.listar()   
        if data:
            for key, value in data.items():
            
                item  = (value)
                item["key"] = key
                prods.append(item)
            
            
        return render (request, 'Producto/listar.html', {'prods': prods})
    
def eliminar_producto (request, id): 
    Producto.eliminar(id) 
    return redirect ('listar')

        
    
    
    
    
    
    


    
    
    