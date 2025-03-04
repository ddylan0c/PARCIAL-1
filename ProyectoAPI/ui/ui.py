import pandas as pd

def mostrar_datos(df):
    """Muestra los datos en una tabla con los campos requeridos"""
    if df.empty: #Si el Dataframe está vacio:
        print("No se encontraron datos para la consulta.")
        return
    
    columnas_deseadas = ['departamento_nom', 'ciudad_municipio_nom', 'edad', 'fuente_tipo_contagio', 'estado', 'pais_viajo_1_nom']
    
    # Itera las columnas en columnas deseadas y comprueba si están en las columnas del dataframe
    # En el caso de estar, añade la columna a la lista
    columnas_disponibles = [col for col in columnas_deseadas if col in df.columns]
    
    # Si alguna columna no está en los datos, agregarla con "No disponible"
    for col in columnas_deseadas:
        if col not in df.columns:
            df[col] = "No disponible"

    # Seleccionar las columnas deseadas (departamento, ciudad, edad, etc...)
    df = df[columnas_deseadas]

    # Renombrar columnas para una mejor legibilidad
    df.columns = ['Departamento', 'Ciudad', 'Edad', 'Tipo', 'Estado', 'País']

    # Imprimir encabezado de la tabla
    print("\n--- Datos de COVID-19 Consultados ---\n")
    print("{:<15} {:<20} {:<5} {:<15} {:<10} {:<15}".format("Departamento", "Ciudad", "Edad", "Tipo", "Estado", "País"))
    print("-" * 80)

    # Imprimir filas con los datos
    for _, row in df.iterrows(): #Se ignora _ y df.iterrows devuelve un iterador con los datos de cada fila
        print("{:<15} {:<20} {:<5} {:<15} {:<10} {:<15}".format(
            row['Departamento'],
            row['Ciudad'],
            row['Edad'],
            row['Tipo'],
            row['Estado'],
            row['País']
        ))



