import pandas as pd

def procesar_dataframe(df, cambiar_nombre_columnas=None, cambiar_tipo_columnas=None):
    """
    Función que se encarga de cambiar los nombres de las columnas y sus tipos de datos.

    Args:
        df (pd.DataFrame): El DataFrame a procesar.
        nombres_columnas (dict): Modifica el nombre del valor inicial por el segundo valor.
        cambiar_tipo_columnas (dict): Modifica el tipo de dato del valor inicial por el segundo valor.

    Returns:
        pd.DataFrame: El DataFrame con los cambios realizados.
    """

# Cambia el tipo de las columnas, en caso de recibir el diccionario. Para cada tipo de dato realizará
# una acción, con el fin de corregir valores nulos.
    if cambiar_tipo_columnas:
        for columna, tipo in cambiar_tipo_columnas.items():
            try:
                if columna in df.columns:
                    if tipo == "int":
                        df[columna] = df[columna].fillna(0).astype(int)
                    elif tipo == "float64":
                        df[columna] = pd.to_numeric(df[columna].str.replace(',', '.'), errors='coerce')
                    elif tipo == "datetime64":
                        df[columna] = pd.to_datetime(df[columna], format='%Y-%m-%d', errors='coerce')
                    else:
                        df[columna] = df[columna].astype(tipo)
                else:
                    print(f"⚠️ La columna '{columna}' no existe en el DataFrame.")
            except Exception as error:
                print(f"❌ Error al convertir la columna '{columna}' a {tipo}: {error}")
    return df