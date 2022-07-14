# **Informe Semana 1**
## **1. Entendimiento de la situación actual:**
Nuestro trabajo es el de ayudar a una empresa de E-Commerce Argentina a evaluar la posibilidad de expandirse a Brasil.

 Para esto, haremos un análisis de datos detallado de un conjunto de datos que nos fue provisto con 100k (cien mil) ordenes de venta de distintos puntos de venta en Brasil. Dicho conjunto de datos va desde el año 2016 hasta el año 2018.


## **2. Objetivos:**
Generar un reporte para el cliente, el cuál le permita (Puede ser más de uno, según se vea la necesidad):  

- Identificar cuáles son los productos con mayor y menor recaudación monetaria.

- Identificar cuáles son las categorías de productos con mayor y menor recaudación monetaria.

- Identificar cuáles son las ciudades y los estados con mayor número de ventas.

- Identificar la estrategia de captación de clientes más efectiva.

- Estimar la cantidad de vendedores necesaria por región

- Hallar si hay una correlación entre puntaje de producto e ingresos del mismo.


**KPI's:**
- Minimizar el coste de los fletes: Promedio actual: 450 Meta: 500. Propuesta: Incentivar a que más personas vendan sus productos en estados en los que hagan falta.
- Aumentar el volumen de ventas por mes en estados diferentes a Sao Paulo. Promedio actual: 500 Meta: 650 
- Satisfacción del cliente medida en el puntaje de los usuarios por producto: > Ejemplo: Promedio actual: 3.  Meta: 4.2. Propuesta para mejorar el análisis: Añadir un sistema que permita al usuario puntuar según diferentes motivos tales como: Tiempo de entrega, calidad del producto, diseño de la página de ventas, etc.
- Maximizar el número de ventas por campañas de marketing. Promedio actual: 300 Meta: 380. Propuesta de mejora: Registrar todas las fuentes de visitas al E-commerce para conocer la tasa de rebote, ya que actualmente vemos que el mayor número de ingresos monetarios por campaña es desconocido.

## **3. Alcance:**
- Creación de una base de datos
- Containerización del proyecto para poder usarlo en diferentes máquinas 
- Análisis general según los objetivos y los kpi's propuestos
- Reporte final con métricas y KPI's

## **4. Fuera de alcance:**

- Estimar el beneficio de las campañas de marketing debido a que no conocemos el valor de las mismas.
- Como poseemos datos hasta el año 2018, no será posible identificar los efectos que tuvo la pandemia en el patrón de consumo de los usuarios de Olist.
- Debido a la falta de información, no podemos segmentar a los clientes por sexo/edad de acuerdo a su comportamiento al comprar.


## **5. Solución propuesta:**
Haremos un primer acercamiento a los datos con python para entender su estructura e integridad, detectar los KPI's y hacer los cambios que consideremos pertinentes.  
Una vez entendidos los datos y hechos los cambios, procederemos a ingestarlos en una base de datos local donde haremos los análisis respectivos.  
Por último crearemos los reportes y las visualizaciones de los kPI's con gráficos que faciliten el entendimiento de los mismos.

### **Stack tecnológico propuesto:**  
- Python
- PostgresQL
- Hadoop
- Spark 
- Hive
- Docker
- Power BI
- Trello
- Google Colab
- Git y Github
- Google sheets
- Google Drive


## **6. Metodología de trabajo:**
Kanban  
>Se trata de un método visual de gestión de proyectos que permite a los equipos visualizar sus flujos de trabajo y la carga de trabajo. En un tablero Kanban, el trabajo se muestra en un proyecto en forma de tablero organizado por columnas.


## **7. Diseño detallado - Entregables:**
- Análisis explortorio de datos
- Diccionario de datos
- Diagrama Entidad - Relación
- Reporte semanal
- Informe semanal


## **8. Equipo de trabajo - Roles y responsabilidades:**

- Daniel Castillo Villamarín: Ingeniero de Datos

- Federico Kostzer: Analista de Datos

- Alberto Landín: Ingeniero de Datos

- Mariano Wilfrido Rodas: Analista de Datos

## **9. Cronograma general:**
![Ganttz](/images/gantz.png)
