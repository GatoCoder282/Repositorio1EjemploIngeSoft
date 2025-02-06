def max_items_in_box(cajaX, cajaY, cajaZ, itemX, itemY, itemZ):
    # Lista de todas las posibles orientaciones del ítem
    orientaciones = [
        (itemX, itemY, itemZ),
        (itemX, itemZ, itemY),
        (itemY, itemX, itemZ),
        (itemY, itemZ, itemX),
        (itemZ, itemX, itemY),
        (itemZ, itemY, itemX)
    ]
    
    max_items = 0
    
    # Iterar sobre todas las orientaciones
    for orient in orientaciones:
        # Dimensiones del ítem en la orientación actual
        dimX, dimY, dimZ = orient
        
        # Verificar si el ítem cabe en la caja en esta orientación
        if dimX > cajaX or dimY > cajaY or dimZ > cajaZ:
            continue  # Si no cabe, pasar a la siguiente orientación
        
        # Calcular cuántos ítems caben en cada dimensión
        numX = cajaX // dimX
        numY = cajaY // dimY
        numZ = cajaZ // dimZ
        
        # Calcular el número total de ítems que caben en la caja
        total_items = numX * numY * numZ
        
        # Actualizar el máximo número de ítems
        if total_items > max_items:
            max_items = total_items
    
    return max_items

# Casos de prueba
print(max_items_in_box(100, 98, 81, 3, 5, 7))    # Salida: 7560
print(max_items_in_box(10, 10, 10, 9, 9, 11))    # Salida: 0
print(max_items_in_box(201, 101, 301, 100, 30, 20))  # Salida: 100
print(max_items_in_box(913, 687, 783, 109, 93, 53))  # Salida: 833
print(max_items_in_box(6, 5, 4, 3, 2, 1))        # Salida: 20
print(max_items_in_box(115, 113, 114, 3, 5, 7))  # Salida: 13984