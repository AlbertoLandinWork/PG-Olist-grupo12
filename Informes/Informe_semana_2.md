# **Informe Semana 2 - Grupo 12**

## **1. Diseño adecuado del Modelo**
  A la hora de elaborar el diseño lógico de los datos, teniendo siempre en cuenta el objetivo de maximizar las ventas del E-Comerce y de aumentar el bienestar de los consumidores, decidimos crear un modelo de hechos y dimensiones capaz de satisfacer todas las consultas que consideraramos adecuadas y de proveer información apta, de relevancia y, en caso de ser posible, con poder predictivo para el mercado en cuestión. Fueron eliminados datos y columnas cuando se consideró que su aporte era irrelevante o nulo, y fueron agregadas columnas a partir de transformaciones de los datos originales cuando vimos en ellas poder de hacer un análisis más profundo y confiable.
  [Diagrama dimensiones](https://user-images.githubusercontent.com/99231030/179021043-2ffed5d8-f134-4eac-a795-06a3c57a54b6.jpg)
  
## **2. Documentación**
Requisitos para ejecutar la app:
- Instalar Docker version 4.8.1 o superior [Docker download page](https://www.docker.com/products/docker-desktop/)
- Descargar el repositorio del proyecto

Una vez instalador Docker y descagado el repositorio del proyecto, seguir las siguientes instrucciones:
- Entrar a la carpeta ProyectoDocker desde el terminal y ejecutar `sudo docker-compose up -d`
- Ejecutar el siguiente comando `sudo docker cp hive-site.xml spark-master:/spark/conf/hive-site.xml`
- Ejecutar `sudo docker cp data namenode:/data`
- Entrar a la consola de hadoop con `sudo docker exec -it namenode bash` 
- Ejecutar `hdfs dfs -put data /data`
- Salir de la consola de hadoop con `exit`
- Ingestar el archivo normalizacion.py al contenedor de spark con `sudo docker cp normalizacion.py spark-master:normalizacion.py`
- Entrar al contenedor de spark master con `sudo docker exec -it spark-master bash`
- Ejecutar `/spark/bin/spark-submit --master spark://spark-master:7077 normalizacion.py`

Con esto, ya tendremos nuestra app ejecutando en el ambiente docker, podemos comprobarlo abriendo el navegador y entrando a:

Hadoop:  [http://localhost:9870](http://localhost:9870)  

HUE: [http://localhost:8888](http://localhost:8888)  

Spark: [http://localhost:8080](http://localhost:8080)  




## **3. Pipeline para alimentar el DW**
### **Para la extracción, tranformación y carga de datos, hicimos un script en lenguaje pyspark:**
![](/images/librerias.png)
![](/images/ingesta.png)
![](/images/orderItems.png)
![](/images/CLOSED_DEALS.png)
![](/images/payments.png)
![](/images/products.png)
![](/images/carga.png)

## **4. Validación de datos**
  El presente trabajo consta de una consistente vocación por la conservación y presentación de datos que sean claros, estén limpios y tengan poder explicativo de los distintos fenómenos que van a ser estudiados. 
   Las principales transformaciones que sufrieron los datos obtenidos fueron:
   - Eliminación de columnas con baja precisión, ya sea por la cantidad de valores nulos, el parecido con otra columna o la definición de la variable en sí misma.
   - El proceso de transformación o eliminación de registros con valores nulos, no definidos o mal definidos.
   - La agrupación de columnas de distintas tablas.
   - El cambio de formato de los datos de diversas tablas.
   - Con el objetivo de realizar modelos predictivos fueron creadas nuevas columnas, combinando columnas originales, que serán utilizadas en modelos de Machine Learning.!
