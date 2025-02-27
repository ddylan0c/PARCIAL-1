import pandas as pd
from sodapy import Socrata

def consultar_datos(departamento, limite):
    """Consulta los datos de COVID-19 desde la API de Datos Abiertos de Colombia"""
    client = Socrata("www.datos.gov.co", None)  #Cliente sin autenticación
    departamento = departamento.upper()  #Convertir a mayúsculas

    try: #Obtiene los datos de la API, con el codigo que permite consultar los datos del covid-19
        resultados = client.get("gt2j-8ykr", where=f"departamento_nom = '{departamento}'", limit=limite)
        #where filtra los departamentos para que unicamente aparezcan datos que coincidan con el depto. ingresado y los limita
        if not resultados: #si no hay datos se devuelve un dataframe vacío
            print("No se encontraron datos para el departamento ingresado.")
            return pd.DataFrame()
        
        df = pd.DataFrame.from_records(resultados)
        return df
    
    except Exception as e:
        print(f"Error al consultar la API: {e}")
        return pd.DataFrame()



    

