## 🚀 Proyecto 4: EDA con Python

<img align="center" src="./assets/banner_EDA.webp" width="75%" />

## 🧠 Descripción del proyecto

Este proyecto ha consistido en un Análisis Exploratorio de Datos (EDA),
sobre un conjunto de datos específico con el objetivo de comprender su
estructura, identificar patrones y relaciones, y detectar cualquier
inconsistencia o valor atípico.
<br>
Durante el proceso de EDA, se han aplicado
técnicas estadísticas y visuales para analizar la distribución de las variables,
explorar correlaciones entre ellas, y verificar la presencia de valores faltantes o anómalos.

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

- pandas
- numpy
- matplotlib.pyplot
- seaborn
- plotly

Para instalar las dependencias, puedes ejecutar el siguiente comando dentro de un entorno virtual:

```bash
pip3 install seaborn
```

## 🧾 Informe explicativo del análisis

#### 1. Introducción

El objetivo principal de este EDA (Exploratory Data Analysis) es analizar la cantidad de productos
suscritos (depósitos a plazos bancarios), en base al contacto directo con el cliente. A través, de
llamadas telefónicas sobre campañas de marketing de una institución portuguesa.

El dataset del proyecto está formado por dos dataframes, uno de ellos en formato csv y el otro en
xlsx (Excel). Ambos dataframes han sido combinados, definen nuestro set de datos final, con un tamaño
de 86170 filas y 29 columnas. Inicialmente encontramos variables con el tipo de dato object, datetime,
date y float64. Estos últimos, deberán ser modificados a int, solamente aquellas columnas, que no
almacenen valores decimales, es decir, únicamente valores enteros.

#### 2. Resumen del proceso

Una vez realizado el preanálisis, y estudiado a fondo nuestro set de datos, llega el momento de
comenzar con la limpieza y transformación de los datos. Los pasos realizados fueron:
<br>
• En primer lugar, se encontraron más de 40.000 valores nulos en todas las columnas, que fueron
reemplazados por 0.
<br>
• Después, analizamos si existen valores duplicados, en este caso no hay ninguno.
<br>
• Por otro lado, modificamos el tipo de dato en las columnas necesarias, cambiando los valores
de float64 a int. Añadiendo el errors="coerce" en las columnas que lo necesite. Coerce añade
valores NaN, sobre las columnas que posean valores faltantes. Como por ejemplo en las columnas;
'cons.price.idx', 'cons.conf.idx', 'euribor3m'...
<br>
• Además, realizamos la estandarización de valores categóricos, de modo que eliminamos espacios
en los nombres de las columnas, y definimos todas las columnas como minúsculas, para evitar
problemas a la hora de hacer referencia a cualquier dato. Como en el caso de 'Income' o
'Teenhome', debido a que ambas columnas comienzan por mayúsculas.
<br>
• Finalmente, modificamos el nombre de las columnas que contienen puntos, y pueden generar conflicto.
Haciendo referencia a las siguientes columnas; 'cons.price.idx', 'cons.conf.idx', 'nr.employed'.

#### 3. Hallazgos clave

Los insights más relevantes obtenidos han sido:
<br>
• La duración media en segundos de la última interacción con el cliente, es de 257 segundos. Promedio
calculado sobre la columna 'duration'.
<br>
• Además hemos obtenido que los valores, se encuentran muy alejados respecto de la media. Con una
varianza de 66908 respecto de la media.
<br>
• Realizando el conteo y porcentaje de valores nulos en cada columna, apreciamos que la gran mayoría
posee un % que ronda el 50, a excepción de dos columnas; 'default' y 'euribor3m' con un porcentaje
superior al 60%. Constituyendo las dos columnas con mayor número de valores nulos.
<br>
• Se ha realizado el cálculo sobre la proporción de clientes según su estado civil. Observamos como el
60% de los clientes están casados, el 28% están solteros, y tan solo el 11% se encuentran divorciados.

#### 4. Visualización de hallazgos

A través de las visualizaciones obtenidas, podemos obtener una serie de conclusiones sobre nuestros datos:
<br>
• El histograma demuestra como la mayoría de clientes tienen entre 20 y 60 años de edad. Con un predominio
sobre los 30 años. Tras esto, obtenemos que existen pocos clientes mayores de 60 años, información relevante
a la hora de la toma de decisiones. Datos calculados a través de la columna 'age'.
<br>
• El boxplot nos permite diferenciar que la mayoría de clientes, trabajan como admin, blue-collar y technician.
Este elemento visual, nos permite representar donde se encuentra el mayor volumen de datos, respecto del total,
representando visualmente el resto de valores alejados del total.
<br>
• El gráfico de pastel nos demuestra que más del 50% de los clientes, se encuentran casados. Información que
puede resultarnos útil a la hora de la toma de decisiones.
<br>
• El gráfico de barras nos expresa que la principal educación de los clientes ha sido; high.school y
university.degree siendo los dos valores con mayor frecuencia. Por ello, podemos determinar que obtenemos clientes
que se encuentran bien preparados y han obtenido una formación adecuada.

#### 5. Conclusiones

Tras realizar el análisis exploratorio de los datos, se identificaron varias conclusiones importantes:
<br>
• La mayoría de los clientes tiene entre 20 y 60 años de edad. Por lo que esas campañas de marketing, deben
contener nuevas tecnologías, puesto que predominan clientes entre 30 y 40 años.
<br>
• Se observó un predominio de personas casadas, respecto de personas solteras y divorciadas. Por ello,
debemos dirigirnos a los clientes, con contenido sobre personas casadas.
<br>
• Se encontraron los trabajos más predominantes dentro de la columna 'job', siendo: admin, blue-collar
y technician. Es importante analizar el porqué de esta información. Si se produce porque es el trabajo con
mejor salario, con las mejores condiciones o porque se debe mejorar el resto de trabajos, para lograr una media.
<br>
• En relación al estado civil y al trabajo de los clientes, observamos como los clientes divorciados, en su mayoría
trabajan como admin. Además, obtenemos como el trabajo con menor frecuencia de personas divorciadas es student. Por ello, llegamos a la conclusión de que nuestros datos están correctamente presentados, es decir, siendo estudiante aún no ha dado tiempo a estar divorciado.
<br>
• Finalmente, hemos obtenido que la media de edad de nuestros clientes es de 39 años. Siendo 17 el cliente más joven y
98 nuestro cliente más longevo. Además, atendiendo a la duración del contacto directo, obtenemos como la duración media
de la llamada en clientes jóvenes es de 100 segundos, y en cliente longevos la duración media es de 300 segundos. Tras
esto, llegamos a la conclusión que debemos mejorar la comunicación y la claridad para reducir la duración media de las
llamadas telefónicas.
<br>
• En términos de próximos pasos, se recomienda realizar un análisis más detallado de las variables relacionadas
con 'housing' y 'loan' y considerar un modelo predictivo para predecir si los clientes, poseen algún tipo de deuda o
préstamos hipotecario.
<br>

💻 Me encuentro totalmente ilusionado y preparado para seguir realizando este tipo de proyectos, y
aprender nuevas tecnologías y herramientas.

## 👤 Autor

Daniel Recio.
