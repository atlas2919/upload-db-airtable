import pandas as pd
import requests
import numpy as np

# Configurar la conexión con Airtable directamente con los valores
api_key = "SECRET_KEY_AIRTABLE"
base_id = "BASE_ID"
table_name = "TABLE_NAME"

# URL de la API de Airtable
airtable_url = f"https://api.airtable.com/v0/{base_id}/{table_name}"

# Encabezados para la autenticación en la API de Airtable
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# Cargar los archivos CSV
main_data = pd.read_csv('FILE_NAME.csv')

# Subir a Airtable todos los datos
for index, row in main_data.iterrows():
    fields = {}
    
    for column in main_data.columns:
        value = row[column]
        if pd.notna(value) and value != "NO_DISPONIBLE":  # Solo incluir el campo si no es NaN o "NO_DISPONIBLE"
            if isinstance(value, (int, float)):  # Si es un número, mantén el tipo de dato
                fields[column] = value
            else:  # Si es cualquier otro tipo, convertir a cadena
                fields[column] = str(value) if value != 'nan' else ''

    data = {
        "fields": fields
    }

    response = requests.post(airtable_url, headers=headers, json=data)
    if response.status_code == 200:
        print(f"Registro subido exitosamente: {row['PRODUCTO']} - {row['MERCADO']}")
    else:
        print(f"Error al subir el registro: {row['PRODUCTO']} - {row['MERCADO']}")
        print(response.json())

# Confirmación de que el programa terminó
print("Proceso de subida a Airtable completado. El programa ha finalizado.")