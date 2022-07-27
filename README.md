# Trabajo grupal PG-Olist
---
## Integrantes del grupo:
- ![Alberto Landín](https://www.linkedin.com/in/albertolandin)
- ![Daniel Castillo](https://www.linkedin.com/in/daniel-casvill/)
- ![Federico Kostzer](https://www.linkedin.com/in/federico-kostzer/)
- ![Mariano Rodas](https://www.linkedin.com/in/mariano-rodas-b93092136/)
---
## Propuesta - E-Commerce Public Dataset by Olist

Una empresa de E-Commerce de Argentina, esta evaluando la posibilidad de expandirse al Brasil, y para ello necesita entender como es el mercado de E-Commerce de alla. Para ello, se consiguio data de 100k de ordenes desde el 2016 hasta el 2018, de distintos puntos de venta en BRasil. Esto se puede ver desde distintas dimensiones, status de las ordenes, precios, pagos y perfomance de envios hacia los usuarios, productos e incluso reviws de los mismos escritos por diversos clientes. Asi mismo, se podra encontrar un archivo de geolocalizacion con todos los codigos postales de Brasil, junto con su latitud y longitud.

![Repositorio del enunciado originial](https://github.com/soyHenry/DS-Proyecto_Grupal_Olist)

---
# Ambientes de trabajo:

Para el desarrollo de este proyecto decidimos hacer un etl con herramientas de big data con el fin de hacerlo fácilmente escalable. Además, creamos un ambiente con herramientas de trabajo convencionales como respaldo. Ambos ambientes están empaquetado en Docker, cada uno  con su respectivo archivo de configuración YAML (.yml) para ser ejecutado con docker compose.  
 
El ambiente de trabajo de big data cuenta con un sistema de almacenamiento distribuido, un sistema de procesamiento distribuido que corre sobre memoria RAM, una base de datos estructurada (almacenada en el sistema de almacenamiento distribuido), e interfaz web. Todo el ciclo de etl funciona de forma automática con un script que se encarga de ello.

Por otro lado, el ambiente de trabajo convencional cuenta con una base de datos estructurada, interfaz web, y un script para la automazión del proceso de etl.

---
# Ambiente de trabajo Big Data:

Stack tecnológico:

- Docker
- Hadoop
- Spark
- Hive
- HUE


Requisitos para ejecutar la app:
- Instalar Docker version 4.8.1 o superior [Docker download page](https://www.docker.com/products/docker-desktop/)
- [Instalar Docker compose](https://docs.docker.com/compose/install/)
- [Descargar el repositorio](https://drive.google.com/file/d/1I_Bg069ysBUWIWGFJGSDB2xF7Os_zRtu/view?usp=sharing)

Una vez instalado Docker y descagado el repositorio del proyecto, seguir las siguientes instrucciones:
- Extrae el repositorio
- Desde el terminal entra a la carpeta "Docker-Hadoop-Hive-Spark-HUE" y ejecuta el siguiente comando para levantar el ambiente de docker: `sudo docker-compose up -d`
- Ejecuta el siguiente comando para añadir configuraciones a spark: `sudo docker cp hive-site.xml spark-master:/spark/conf/hive-site.xml`
- Ejecuta este comando para ingestar los datasets al contenedor de hadoop: `sudo docker cp data namenode:/data`
- Entra a la consola de hadoop con: `sudo docker exec -it namenode bash` 
- Ingesta los dataset al sistema de almacenamiento distribuido de hadoop con este comando: `hdfs dfs -put data /data`
- Sal de la consola de hadoop con: `exit`
- Ingesta el archivo "normalizacion.py" al contenedor de spark con: `sudo docker cp normalizacion.py spark-master:normalizacion.py`
- Entra al contenedor de spark master con: `sudo docker exec -it spark-master bash`
- Ejecuta este comando para correr el archivo "normalizacion.py", que es el encargado del proceso de etl: `/spark/bin/spark-submit --master spark://spark-master:7077 normalizacion.py`

Con esto, ya tendremos nuestra app ejecutando en el ambiente docker y nuestro datasets procesados e ingestados en hive, podemos comprobarlo abriendo el navegador y entrando a:

> [Hadoop web interface:](http://localhost:9870) Aquí podras ver todos los archivos almacenados en hadoop  
> [HUE web interface:](http://localhost:8888) Aquí puedes podrás ejecutar querys HQL sobre los datos ingestados  
> [Spark web interface:](http://localhost:8080) Aquí puedes ver el estado de los procesos realizados con spark  
---
# Ambiente de trabajo convencional:

## Guía rápida de uso
- Instalar Docker version 4.8.1 o superior [Docker download page](https://www.docker.com/products/docker-desktop/)
- [Instalar Docker compose](https://docs.docker.com/compose/install/)
- [Descargar el repositorio](https://drive.google.com/file/d/1fQl9lNeXWM1ZT0PY-4K1Gm3auXJKeugc/view)
- Ir a la carpeta ambiente_docker_de_respaldo/Docker_pgAdmin_Postgres
- Dentro de la carpeta ejecutar en la terminal el siguiente comando: `sudo docker-compose up`

Con esto, ya tendremos nuestra app ejecutando con nuestros datasets procesados y almacenados en postgres.
Para ver nuestra base de datos y ejecutar querys, podemos hacerlo en pgAdmin, por su interfaz web:
> [PgAdmin web interface](http://localhost:50508)

## Herramientas utilizadas en el proyecto
* Docker
* Docker-compose
* Python 3.10.3-slim-buster
* PostgreSQL 14.3
* pgAdmin 4 6.11

## Librerias
* sqlalchemy 1.4.37
* sqlalchemy-Utils 0.38.2
* pandas 1.4.1 
* psycopg2-binary 2.9.3
---


[https://drive.google.com/drive/folders/1DHrP4donr4Es-3hoM1nOg7reLCX7aTRT?usp=sharing](https://drive.google.com/drive/folders/1DHrP4donr4Es-3hoM1nOg7reLCX7aTRT?usp=sharing)
