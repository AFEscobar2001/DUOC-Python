import csv
import json

empresas = []
resultado = []

with open ("rut,nombre,ventas.csv", "r", encoding="utf8") as archivo_csv:
    lector = csv.DictReader(archivo_csv)
    
    for fila in lector:
        rut = fila["rut"]
        nombre = fila ["nombre"]
        ventas = int(fila["ventas"])
        
        if ventas <= 1000000:
            clasificacion = "Pequeño Contribuyente"
        elif ventas >= 2000000:
            clasificacion = "Gran Contribuyente"
        else:
            clasificacion = "Mediano Contibuyente"
        
        resultado.append({
            "rut" : rut,
            "nombre" : nombre,
            "ventas" : ventas,
            "clasificacion" : clasificacion
            
        })

print(lector)



with open("segmentacionEmpresas.json", "w", encoding="utf8") as salida:
    json.dump(resultado, salida, indent=1 )
    
    

