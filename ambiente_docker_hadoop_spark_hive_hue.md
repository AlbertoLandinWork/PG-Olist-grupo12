# _Ambiente Docker Hadoop Spark Hive Hue_

## Guía rápida de uso

* Instalar Docker version 4.8.1 o superior Docker download page
* Instalar Docker compose
* Ejecutar Docker
* Descargar el repositorio (https://github.com/AlbertoLandinWork/PG-Olist-grupo12 | https://drive.google.com/drive/folders/1DHrP4donr4Es-3hoM1nOg7reLCX7aTRT)

* Desde el terminal ir a la carpeta "Docker-Hadoop-Hive-Spark-HUE" 
* Ejecutar sudo docker-compose up -d
* Ejecuta sudo docker cp hive-site.xml spark-master:/spark/conf/hive-site.xml
* Ejecutar sudo docker cp data namenode:/data
* Ejecutar sudo docker exec -it namenode bash
* Ejecutar hdfs dfs -put data /data
* Sal de la consola de hadoop ejecutando exit
* Ejecuta sudo docker cp normalizacion.py spark-master:normalizacion.py
* Ejecuta sudo docker exec -it spark-master bash
* Ejecuta /spark/bin/spark-submit --master spark://spark-master:7077 normalizacion.py

## Herramientas utilizadas en el proyecto

* Docker
* Docker-compose
* Python 3.9.5
* Hadoop 3.2.1-java8
* Spark 3.0.0-hadoop3.2
* Hive hive:2.3.2
* Hue hue:4.6.0