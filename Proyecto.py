"""
PIPELINE DE CARRITO DE COMPRAS:

¿QUÉ HACE ESTE CÓDIGO?
Simula el sistema de una caja registradora que recibe datos de un escáner.
A veces el escáner lee mal (mete espacios, mayúsculas o códigos erróneos).
Para solucionarlo, los datos pasan por un "Pipeline" (tubería de procesos) 
de 4 pasos secuenciales:

1. Limpieza: Estandariza los textos (quita espacios, convierte a minúsculas).
2. Filtrado: Verifica qué productos realmente existen en la tienda.
3. Cálculo: Agrupa los productos repetidos, suma cantidades y calcula precios.
4. Ordenamiento: Ordena el ticket final del más caro al más barato.

CONCEPTOS UTILIZADOS:
- Colecciones: Tuplas (configuración), Diccionarios (catálogo), Listas (cola 
  de escáner), Conjuntos/Sets (para agrupar sin duplicados).
- Funciones de orden superior: map() y filter().
- Funciones anónimas: lambda.
- Módulo operator: Sustituye operadores tradicionales (+, *) y bucles por 
  funciones optimizadas en C (methodcaller, itemgetter, mul, add).
=============================================================================
"""

import operator
import tkinter as tk
from tkinter import messagebox

# --- BASES DE DATOS SIMULADAS ---

# TUPLA: Datos que NUNCA deben cambiar durante la ejecución (Inmutables)
# Índice 0: Nombre de la tienda | Índice 1: Porcentaje de IVA
CONFIG_TIENDA = ("Supermercado Python", 0.16)

# DICCIONARIO: Catálogo de productos. Búsqueda ultra rápida por clave.
CATALOGO = {
    "manzana": 15.0,
    "leche": 25.5,
    "pan": 10.0,
    "cafe": 45.0
}

# LISTA: Datos crudos de entrada. Mutable, ordenada y permite duplicados.
# La iniciamos vacía para llenarla desde la interfaz gráfica.
articulos_escaneados = []


# --- DEFINICIÓN DEL PIPELINE (PASO A PASO) ---

def paso1_limpiar_datos(lista_cruda):
    """
    PASO 1: Estandarizar cadenas de texto.
    En lugar de usar un bucle 'for', usamos herramientas funcionales.
    """
    # operator.methodcaller crea una función que llama a un método específico del string.
    quitar_espacios = operator.methodcaller('strip')
    hacer_minusculas = operator.methodcaller('lower')
    
    # map() toma la función y la aplica a CADA elemento de la lista original.
    # Devuelve un objeto map, por lo que lo convertimos a lista con list().
    sin_espacios = list(map(quitar_espacios, lista_cruda))
    limpios = list(map(hacer_minusculas, sin_espacios))
    
    return limpios

def paso2_filtrar_catalogo(lista_limpia):
    """
    PASO 2: Separar productos válidos de los inválidos.
    """
    # lambda es una función anónima de una sola línea: 'dado un item, devuelve True si está en CATALOGO'
    # filter() deja pasar SOLO los elementos donde la lambda devolvió True.
    articulos_validos = list(filter(lambda item: item in CATALOGO, lista_limpia))
    
    # Resta de conjuntos (Set difference):
    # Convertimos ambas listas a conjuntos. Al conjunto de todos los items le 
    # restamos el conjunto de items válidos para descubrir cuáles fueron los errores.
    articulos_invalidos = list(set(lista_limpia) - set(articulos_validos))
    
    return articulos_validos, articulos_invalidos

def paso3_calcular_totales(articulos_validos):
    """
    PASO 3: Agrupar y calcular la matemática.
    """
    ticket = []
    subtotal_compra = 0
    
    # set() elimina los duplicados para que podamos iterar sobre productos únicos (ej. procesar "manzana" una vez)
    productos_unicos = set(articulos_validos)
    
    for item in productos_unicos:
        # Contamos cuántas veces aparece este producto en la lista original completa
        cantidad = articulos_validos.count(item)
        precio = CATALOGO[item]
        
        # operator.mul equivale a (cantidad * precio), operator.add equivale a (subtotal_compra + total_item)
        total_item = operator.mul(cantidad, precio)
        subtotal_compra = operator.add(subtotal_compra, total_item)
        
        # Guardamos el registro como una TUPLA dentro de la LISTA del ticket
        ticket.append((item, cantidad, precio, total_item))
        
    return ticket, subtotal_compra

def paso4_ordenar_ticket(ticket_desordenado):
    """
    PASO 4: Ordenar el ticket del importe mayor al menor.
    """
    # operator.itemgetter(3) le dice a sorted() que se fije en el índice 3 de 
    # nuestras tuplas (que corresponde a 'total_item') para decidir el orden.
    ticket_ordenado = sorted(ticket_desordenado, key=operator.itemgetter(3), reverse=True)
    return ticket_ordenado


# --- FUNCIÓN OQUESTADORA ORIGINAL (CONSOLA) ---

def procesar_compra(lista_compras):
    """
    Conecta la salida de un paso como la entrada del siguiente.
    """
    print(f"📦 Procesando {len(lista_compras)} artículos escaneados...\n")
    
    # Flujo secuencial
    datos_limpios = paso1_limpiar_datos(lista_compras)
    validos, invalidos = paso2_filtrar_catalogo(datos_limpios)
    ticket_bruto, subtotal = paso3_calcular_totales(validos)
    ticket_final = paso4_ordenar_ticket(ticket_bruto)
    
    # Cálculos de impuestos
    iva = operator.mul(subtotal, CONFIG_TIENDA[1])
    total = operator.add(subtotal, iva)
    
    # --- IMPRESIÓN DEL RESULTADO ---
    print(f"--- TICKET DE {CONFIG_TIENDA[0].upper()} ---")
    
    # Desempaquetado: extraemos las 4 variables de cada tupla directamente en el for
    for nombre, cant, precio_u, total_prod in ticket_final:
        print(f"{cant}x {nombre.capitalize()} (${precio_u}) -> ${total_prod}")
        
    print("-" * 35)
    print(f"Subtotal: ${subtotal}")
    print(f"IVA ({int(CONFIG_TIENDA[1]*100)}%): ${iva}")
    print(f"TOTAL A PAGAR: ${total}")
    
    if invalidos:
        print(f"\n⚠️ Alerta de escáner: Se rechazaron los siguientes artículos irreconocibles: {invalidos}")


# =============================================================================
#  INTERFAZ GRÁFICA (SIMULACIÓN DEL ESCÁNER) ---


def agregar_producto(event=None):
    """Captura el texto del input y lo mete a la lista y a la vista del carrito."""
    producto = entrada_producto.get()
    
    if producto.strip() == "":
        return
        
    articulos_escaneados.append(producto)
    lista_carrito.insert(tk.END, f"🛒 {producto}")
    entrada_producto.delete(0, tk.END)

def procesar_compra_gui():
    """Ejecuta el pipeline con los datos actuales y muestra el ticket en la ventana."""
    if not articulos_escaneados:
        messagebox.showwarning("Carrito vacío", "Agrega al menos un producto antes de pagar.")
        return

    # Usamos exactamente los mismos pasos del pipeline original
    datos_limpios = paso1_limpiar_datos(articulos_escaneados)
    validos, invalidos = paso2_filtrar_catalogo(datos_limpios)
    ticket_bruto, subtotal = paso3_calcular_totales(validos)
    ticket_final = paso4_ordenar_ticket(ticket_bruto)
    
    iva = operator.mul(subtotal, CONFIG_TIENDA[1])
    total = operator.add(subtotal, iva)
    
    # Construcción del texto para la interfaz gráfica
    texto_ticket = f"--- TICKET DE {CONFIG_TIENDA[0].upper()} ---\n\n"
    
    for nombre, cant, precio_u, total_prod in ticket_final:
        texto_ticket += f"{cant}x {nombre.capitalize()} (${precio_u}) -> ${total_prod}\n"
        
    texto_ticket += "-" * 35 + "\n"
    texto_ticket += f"Subtotal: ${subtotal}\n"
    texto_ticket += f"IVA ({int(CONFIG_TIENDA[1]*100)}%): ${round(iva, 2)}\n"
    texto_ticket += f"TOTAL A PAGAR: ${round(total, 2)}\n"
    
    if invalidos:
        texto_ticket += f"\n⚠️ ALERTA: Productos no reconocidos:\n{', '.join(invalidos)}\n"
        
    # Mostrar en la caja de resultados
    caja_resultado.config(state=tk.NORMAL)
    caja_resultado.delete(1.0, tk.END)
    caja_resultado.insert(tk.END, texto_ticket)
    caja_resultado.config(state=tk.DISABLED)

def limpiar_todo():
    """Reinicia el sistema completo para un nuevo cliente."""
    articulos_escaneados.clear()
    lista_carrito.delete(0, tk.END)
    caja_resultado.config(state=tk.NORMAL)
    caja_resultado.delete(1.0, tk.END)
    caja_resultado.config(state=tk.DISABLED)

# --- CONSTRUCCIÓN DE LA VENTANA PRINCIPAL ---
if __name__ == "__main__":
    ventana = tk.Tk()
    ventana.title("Simulador de Caja (Pipeline Data)")
    ventana.geometry("450x650")
    ventana.config(padx=20, pady=20)

    # Catálogo visual
    tk.Label(ventana, text=f"Catálogo Oficial: {', '.join(CATALOGO.keys())}", fg="gray").pack(pady=5)

    # Input de productos (Escáner)
    tk.Label(ventana, text="Escribe un producto y presiona Enter:", font=("Arial", 10, "bold")).pack()
    entrada_producto = tk.Entry(ventana, width=30, font=("Arial", 12))
    entrada_producto.pack(pady=5)
    entrada_producto.bind('<Return>', agregar_producto)

    # Botón Agregar
    btn_agregar = tk.Button(ventana, text="Agregar al Carrito", bg="lightblue", command=agregar_producto)
    btn_agregar.pack(pady=5)

    # Visualización de la lista de escaneo
    tk.Label(ventana, text="Datos crudos escaneados:", font=("Arial", 10, "bold")).pack(pady=(15, 0))
    lista_carrito = tk.Listbox(ventana, width=40, height=8)
    lista_carrito.pack()

    # Botones de Acción
    frame_botones = tk.Frame(ventana)
    frame_botones.pack(pady=15)

    btn_pagar = tk.Button(frame_botones, text="Ejecutar Pipeline", bg="lightgreen", font=("Arial", 10, "bold"), command=procesar_compra_gui)
    btn_pagar.grid(row=0, column=0, padx=10)

    btn_limpiar = tk.Button(frame_botones, text="Limpiar Caja", bg="#ffcccc", command=limpiar_todo)
    btn_limpiar.grid(row=0, column=1, padx=10)

    # Caja de Resultados (Ticket Final)
    tk.Label(ventana, text="Salida del Pipeline (Ticket):", font=("Arial", 10, "bold")).pack()
    caja_resultado = tk.Text(ventana, width=45, height=12, state=tk.DISABLED, bg="#f4f4f4")
    caja_resultado.pack()

    # Iniciar la aplicación
    ventana.mainloop()