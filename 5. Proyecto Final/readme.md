## 🚀 Proyecto 5: Proyecto Final

<img align="center" src="./assets/EDA.webp" width="75%" />

## 🧠 Descripción del proyecto

Este proyecto ha consistido en un Análisis Exploratorio de Datos (EDA),
sobre un conjunto de datos específico con el objetivo de comprender su
estructura, identificar patrones y relaciones, y detectar cualquier
inconsistencia o valor atípico.
<br>
Durante el proceso de EDA, se han aplicado
técnicas estadísticas y visuales para analizar la distribución de las variables,
explorar correlaciones entre ellas, y verificar la presencia de valores faltantes o anómalos.
<br>
Una vez realizado el EDA, se ha creado un informe / dashboard interactivo
sobre los datos a través de PowerBI, con la finalidad de expresar de manera
visual, la transformación y representación final de los datos.

## 📁 Estructura del proyecto

La estructura del proyecto es la siguiente:

```bash
├── assets/                 # Contiene las imágenes del proyecto
├── data/                   # Contiene las carpetas con la info
│   ├── raw_data/           # Contiene los datos en bruto
│   └── transform_data/     # Contiene el archivo transformado
├── notebooks/              # Contiene los archivos ipynb
├── reports/                # Contiene el Dashboard de Power BI
├── src/                    # Contiene el archivo .py con las funciones
├── readme.md               # Descripción completa del proyecto
```

## 🛠️ Instalación y Requisitos

Este proyecto utiliza Python con Pandas, y necesita las siguientes dependencias:

- [Pandas](https://pandas.pydata.org/docs/)
- [NumPy](https://numpy.org/doc/)
- [Matplotlib](https://matplotlib.org/stable/contents.html)
- [Seaborn](https://seaborn.pydata.org/)
- [Plotly](https://plotly.com/python/)

Para instalar las dependencias, puedes ejecutar el siguiente comando dentro de un entorno virtual:

```bash
pip3 install seaborn
```

## 📊 Descripción de los datos

El análisis se realizó a partir de dos archivos de datos originales:

- **`club_games.csv`**: Contiene información sobre los partidos que han disputado los equipos,
  así como información del mismo: local/visitante, resultado, goles encajados...
- **`clubs.csv`**: Contiene información general sobre cada equipo; nombre del equipo,
  nombre del estadio, tamaño de la plantilla, cantidad de jugadores internacionales...

Estos archivos fueron combinados y transformados para generar un dataset final, que es el
que se utilizó en el análisis.

- **`transform_Data.csv`**: Incluye el set de datos final combinado, información general
  de cada equipo, juntos con los partidos que han disputado.

A continuación, se describen sus columnas:

| Columna                   | Descripción                                                | Tipo de dato | Ejemplo                     |
| ------------------------- | ---------------------------------------------------------- | ------------ | --------------------------- |
| `club_id`                 | Identificador único del club.                              | Integer      | 1001                        |
| `club_code`               | Código abreviado del club.                                 | Object       | FCB                         |
| `name`                    | Nombre del club.                                           | Object       | FC Barcelona                |
| `domestic_competition_id` | Identificador de la liga doméstica del club.               | Object       | ESP1                        |
| `total_market_value`      | Valor de mercado total del club.                           | Float        | 850.5                       |
| `squad_size`              | Tamaño total de la plantilla del club.                     | Integer      | 25                          |
| `average_age`             | Edad media de los jugadores del club.                      | Float        | 27.3                        |
| `foreigners_number`       | Número de jugadores extranjeros en el club.                | Integer      | 10                          |
| `foreigners_percentage`   | Porcentaje de jugadores extranjeros en la plantilla.       | Float        | 40.0                        |
| `national_team_players`   | Número de jugadores convocados a selecciones nacionales.   | Integer      | 5                           |
| `stadium_name`            | Nombre del estadio del club.                               | Object       | Camp Nou                    |
| `stadium_seats`           | Capacidad total del estadio.                               | Integer      | 99354                       |
| `net_transfer_record`     | Balance neto de transferencias del club.                   | Float        | -50.2                       |
| `coach_name`              | Nombre del entrenador del club.                            | Object       | Xavi Hernández              |
| `last_season`             | Última temporada registrada del club.                      | Integer      | 2023                        |
| `filename`                | Nombre del archivo de origen de los datos.                 | Object       | clubs_data.csv              |
| `url`                     | Enlace de referencia al club.                              | Object       | www.example.com/fcbarcelona |
| `game_id`                 | Identificador único del partido.                           | Integer      | 20231105                    |
| `own_goals`               | Goles anotados por el club en el partido.                  | Integer      | 3                           |
| `own_position`            | Posición del club en la tabla antes del partido.           | Integer      | 2                           |
| `own_manager_name`        | Nombre del entrenador del club en ese partido.             | Object       | Xavi Hernández              |
| `opponent_id`             | Identificador único del equipo rival.                      | Integer      | 2002                        |
| `opponent_goals`          | Goles anotados por el equipo rival en el partido.          | Integer      | 1                           |
| `opponent_position`       | Posición del equipo rival en la tabla antes del partido.   | Integer      | 5                           |
| `opponent_manager_name`   | Nombre del entrenador del equipo rival.                    | Object       | Carlo Ancelotti             |
| `hosting`                 | Indica si el club jugó como local (`1`) o visitante (`0`). | Integer      | 1                           |
| `is_win`                  | Indica si el club ganó el partido (`1`) o no (`0`).        | Integer      | 1                           |

## 🧾 Informe explicativo del análisis

#### 1. Introducción

El objetivo principal de este EDA (Exploratory Data Analysis) es analizar la información personal
de los equipos más prestigiosos del mundo, y los resultados que han obtenido sobre los partidos
que han disputado, con la finalidad de obtener una clara representación sobre los equipos que más
partidos han ganado.

El dataset del proyecto está formado por dos dataframes, los dos en formato csv. Ambos dataframes
han sido combinados, defininiendo nuestro set de datos final, con un tamaño de 120000 filas y 27 columnas.
Inicialmente encontramos variables con el tipo de dato object, datetime, date y float64. Estos últimos,
deberán ser modificados a int, solamente aquellas columnas, que no almacenen valores decimales, es decir,
únicamente valores enteros.

#### 2. Resumen del proceso

Una vez realizado el preanálisis, y estudiado a fondo nuestro set de datos, llega el momento de
comenzar con la limpieza y transformación de los datos. Los pasos realizados fueron:
<br>
• En primer lugar, se encontraron columnas con un 100% de valores nulos, que fueron eliminadas.
También había columnas con menos de un 5% de valores nulos, que fueron reemplazados por 0.
<br>
• Después, analizamos si existen valores duplicados, en este caso no hay ninguno.
<br>
• Por otro lado, modificamos el tipo de dato en las columnas necesarias, cambiando los valores
de float64 a int. Añadiendo el errors="coerce" en las columnas que lo necesite. Coerce añade
valores NaN, sobre las columnas que posean valores faltantes.
<br>
• Además, realizamos la estandarización de valores categóricos, de modo que eliminamos espacios
en los nombres de las columnas, y definimos todas las columnas como minúsculas, para evitar
problemas a la hora de hacer referencia a cualquier dato.

#### 3. Hallazgos clave

Los insights más relevantes obtenidos han sido:
<br>
• Los equipos españoles son los que más partidos han disputado. Aportando con Real Madrid y
FC Barcelona, dos de los cinco equipos con más victorias conseguidas.
<br>
• Además, hemos obtenido que la media de espectadores es de 30000, obteniendo estadios con
80000 espectadores y estadios con 10000, influyendo en la victoria o derrota del equipo.
<br>
• Obtenemos como las 5 grandes ligas; España, Inglaterra, Francia, Alemania e Italia, aportan
casi el 10% del total de los equipos, cada una de ellas. Formado en conjunto, algo más del 40%
del total de equipos.

#### 4. Visualización de hallazgos

A través de las visualizaciones obtenidas, podemos obtener una serie de conclusiones sobre nuestros datos:
<br>
• El histograma sobre los jugadores internacionales, nos informa que hay más de 15000 equipos que no aportan ningún jugador con su selección. Por otro lado, unos 500 equipos son capaces de tener en su plantilla una cifra superior o igual a 20, de jugadores que viajan con sus respectivas selecciones.
<br>
• El gráfico de Barras Apiladas nos muestra que el hosting (posición del equipo en el partido; local o visitante) influye a la hora del resultado final. Es decir, cuando el equipo juega como local hay una mayor probabilidad de que consiga la victoria.
<br>
• El boxplot nos permite analizar que las plantillas que tienen una mayor media de edad, es decir, poseen mayor veteranía, han conseguido mayor victorias, debido a la experiencia.

#### 5. Conclusiones

Tras realizar el análisis exploratorio de los datos, se identificaron varias conclusiones importantes:
<br>
• Podemos observar como los tres equipos con más partidos disputados son españoles. El Real Madrid es el equipo con más victorias, superando mínimamente al FC Barcelona. Sin embargo, el tercer equipo (Sevilla FC), tiene muchas menos victorias prácticamente con los mismos partidos disputados.
<br>
• Podemos observar como se producen el mismo número de derrotas y de victorias, con el mismo tamaño medio en la plantilla. Por lo tanto, el tamaño de la plantilla no influye sobre el resultado final del equipo.
<br>
• Podemos observar como el FC Barcelona y el Bayern Munchen tienen una mayor cantidad de victorias como visitantes. Real Madrid y Celtic tienen el mismo número de victorias tanto de locales, como de visitantes. Estos datos indican que los 4 equipos obtienen siempre un gran resultado como visitantes (tiene una mayor dificultad respecto a ser local).
<br>
• Podemos observar como la capacidad del estadio, está relacionada con las victorias del equipo. Un estadio con una capacidad pequeña tiene menor número de victorias, que un estadio con una gran capacidad. Por lo tanto, la capacidad influye en el resultado del equipo.
<br>

💻 Me encuentro totalmente ilusionado y preparado para seguir realizando este tipo de proyectos, y
aprender nuevas tecnologías y herramientas.

## 👤 Autor

Daniel Recio.
