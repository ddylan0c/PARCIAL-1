from api.api import consultar_datos
from ui.ui import mostrar_datos

def main():
    """Función principal del programa"""
    departamento = input("Ingrese el nombre del departamento a consultar: ")
    
    try:
        limite = int(input("Ingrese el número de registros a obtener: "))
        if limite <= 0:
            raise ValueError
    except ValueError:
        print("Error: Debe ingresar un número entero positivo.")
        return
    
    df = consultar_datos(departamento, limite)
    
    if df.empty:
        print("No se encontraron datos.")
    else:
        mostrar_datos(df)

if __name__ == "__main__": #Se asegura que main se ejecute directamente y no como un modulo importado
    main()
