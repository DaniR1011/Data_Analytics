import pandas as pd

def procesar_dataframe(df, cambiar_nombre_columnas=None, cambiar_tipo_columnas=None):
    """
    Función que cambia los nombres de las columnas y sus tipos de datos.

    Args:
        df (pd.DataFrame): El DataFrame a procesar.
        cambiar_nombre_columnas (dict, opcional): Diccionario con los nombres originales como claves y los nuevos nombres como valores.
        cambiar_tipo_columnas (dict, opcional): Diccionario con los nombres de columnas como claves y los tipos de datos deseados como valores.

    Returns:
        pd.DataFrame: El DataFrame con los cambios aplicados.
    """

    # Cambiar el tipo de las columnas si se proporciona el diccionario
    if cambiar_tipo_columnas:
        for columna, tipo in cambiar_tipo_columnas.items():
            try:
                if columna in df.columns:
                    if tipo in ["int", "Int64"]:
                        df[columna] = df[columna].astype("Int64")  # Permite valores nulos
                    elif tipo == "float64":
                        if df[columna].dtype == "object":  # Solo si es tipo texto
                            df[columna] = df[columna].str.replace(",", ".", regex=False)
                        df[columna] = pd.to_numeric(df[columna], errors="coerce")
                    elif tipo == "datetime64":
                        df[columna] = pd.to_datetime(df[columna], format="%Y-%m-%d", errors="coerce")
                    elif tipo == "category":
                        if not df[columna].isna().all():  # Solo si tiene datos
                            df[columna] = df[columna].astype("category")
                    else:
                        df[columna] = df[columna].astype(tipo)
                else:
                    print(f"⚠️ La columna '{columna}' no existe en el DataFrame.")
            except Exception as error:
                print(f"❌ Error al convertir la columna '{columna}' a {tipo}: {error}")

    return df  # Asegurar que el DataFrame se devuelva correctamente
