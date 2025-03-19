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

lorem

#### 3. Hallazgos clave

lorem

#### 4. Visualización de hallazgos

lorem

#### 5. Conclusiones

lorem

💻 Me encuentro totalmente ilusionado y preparado para seguir realizando este tipo de proyectos, y
aprender nuevas tecnologías y herramientas.

## 👤 Autor

Daniel Recio.
