# **Informe Semana 2 - Grupo 12**

## **1. Diseño adecuado del Modelo**
  A la hora de elaborar el diseño lógico de los datos, teniendo siempre en cuenta el objetivo de maximizar las ventas del E-Comerce y de aumentar el bienestar de los consumidores, decidimos crear un modelo de hechos y dimensiones capaz de satisfacer todas las consultas que consideraramos adecuadas y de proveer información apta, de relevancia y, en caso de ser posible, con poder predictivo para el mercado en cuestión. Fueron eliminados datos y columnas cuando se consideró que su aporte era irrelevante o nulo, y fueron agregadas columnas a partir de transformaciones de los datos originales cuando vimos en ellas poder de hacer un análisis más profundo y confiable.
  [Diagrama dimensiones](https://user-images.githubusercontent.com/99231030/179021043-2ffed5d8-f134-4eac-a795-06a3c57a54b6.jpg)
  
## **2. Documentación**
Requisitos para ejecutar la app:
- Instalar Docker version 4.8.1 o superior [Docker download page](https://www.docker.com/products/docker-desktop/)
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
>[Spark web interface:](http://localhost:8080) Aquí puedes ver el estado de los procesos realizados con spark  




## **3. Pipeline para alimentar el DW**
### **Para la extracción, tranformación y carga de datos, hicimos un script en lenguaje pyspark:**
~~~Python
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
spark= SparkSession.builder.appName('Pipeline').config("hive.metastore.warehouse.dir", "/user/hive/metastore/").master("spark://spark-master:7077").enableHiveSupport().getOrCreate()


df_sellers= spark.read.csv("hdfs://namenode:9000/data/olist_sellers_dataset.csv", header= "True")
df_closed_deals= spark.read.csv("hdfs://namenode:9000/data/olist_closed_deals_dataset.csv", header= "True")
df_customers= spark.read.csv("hdfs://namenode:9000/data/olist_customers_dataset.csv", header= "True")
df_geolocation= spark.read.csv("hdfs://namenode:9000/data/olist_geolocation_dataset.csv", header= "True")
df_products= spark.read.csv("hdfs://namenode:9000/data/olist_products_dataset.csv", header= "True")
df_order_reviews= spark.read.csv("hdfs://namenode:9000/data/olist_order_reviews_dataset.csv", header= "True")
df_order_payments= spark.read.csv("hdfs://namenode:9000/data/olist_order_payments_dataset.csv", header= "True")
df_orders= spark.read.csv("hdfs://namenode:9000/data/olist_orders_dataset.csv", header= "True")
df_category_name_translation= spark.read.csv("hdfs://namenode:9000/data/product_category_name_translation.csv", header= "True")
df_marketing_qualified_leads= spark.read.csv("hdfs://namenode:9000/data/olist_marketing_qualified_leads_dataset.csv", header= "True")
df_order_items= spark.read.csv("hdfs://namenode:9000/data/olist_order_items_dataset.csv", header= "True")


"""
        Transformacion df_closed_deals.
"""

# Eliminamos las columnas que no seran de interes en el analisis y/o contengan una alta proporcion de valores nulos
df_closed_deals= df_closed_deals.drop("sdr_id", "sr_id", "has_company", "has_gtin", "average_stock", "declared_product_catalog_size")

#Cambiamos el formato de la columna "won_date" a datetime
df_closed_deals= df_closed_deals.select("mql_id", "seller_id", F.to_timestamp(F.col("won_date"), "yyyy-MM-dd HH:mm:ss").alias("won_date"), "business_segment", "lead_type", "lead_behaviour_profile", "business_type", "declared_monthly_revenue")

# Eliminamos las filas que contengan valores "other"
df_closed_deals= df_closed_deals[df_closed_deals["business_segment"] != "other"]

# Eliminamos los valores nulos
df_closed_deals= df_closed_deals.dropna()


"""
        Transformacion df_costumers
"""
df_customers= df_customers.select("customer_id", "customer_unique_id", df_customers["customer_zip_code_prefix"].cast("Int"), "customer_city", "customer_state")



"""
        Transformacion df_marketing_qualified_leads
"""
df_marketing_qualified_leads= df_marketing_qualified_leads.dropna()
df_marketing_qualified_leads= df_marketing_qualified_leads.select("mql_id", "first_contact_date", "landing_page_id", F.regexp_replace('origin', 'unknown', 'other').alias("origin"))




"""
        Normalizacion df_order_reviews
"""
#Datos formato de fecha a las columnas que lo requieren:
df_order_reviews= df_order_reviews.select("review_id", "order_id", "review_score", "review_comment_title", "review_comment_message", F.to_timestamp(F.col("review_creation_date"), "yyyy-MM-dd HH:mm:ss").alias("review_creation_date"), F.to_timestamp(F.col("review_answer_timestamp"), "yyyy-MM-dd HH:mm:ss").alias("review_answer_timestamp"))


df_order_reviews = df_order_reviews.dropDuplicates(["order_id"])

### Eliminamos las columnas que no seran de interes en el analisis y/o contengan una alta proporcion de valores nulos
df_order_reviews= df_order_reviews.drop("review_comment_title", "review_comment_message", "review_creation_date", "review_answer_timestamp")




"""
        ## Normalizacion df_orders
"""
# Eliminamos las columnas que no seran de interes en el analisis y/o contengan una alta proporcion de valores nulos
df_orders= df_orders.drop("order_purchase_timestamp","order_estimated_delivery_date")

# Pasamos las columnas "order_approved_at", "order_delivered_carrier_date" y "order_delivered_customer_date"  a datatime
df_orders= df_orders.select("order_id", "customer_id", "order_status", F.to_timestamp(F.col("order_approved_at"), "yyyy-MM-dd HH:mm:ss").alias("order_approved_at"), F.to_timestamp(F.col("order_delivered_carrier_date"), "yyyy-MM-dd HH:mm:ss").alias("order_delivered_carrier_date"), F.to_timestamp(F.col("order_delivered_customer_date"), "yyyy-MM-dd HH:mm:ss").alias("order_delivered_customer_date"))

# Eliminamos valores nulos
df_orders= df_orders.dropna()



"""
        ## Normalizacion df_order_payments
"""
## Eliminamos las columnas que no seran de interes en el analisis y/o contengan una alta proporcion de valores nulos
df_order_payments= df_order_payments.drop('payment_installments','payment_sequential')

#Borramos las filas cuyos valores aparezcan como "not_defined"
df_order_payments= df_order_payments[df_order_payments['payment_type'] != 'not_defined']



"""
        ## Normalizacion df_products
"""
# Traducimos el nombre de las categorias al ingles
df_products= df_products.join(df_category_name_translation, on=['product_category_name'], how='left')

# Eliminamos las columnas que no seran de interes en el analisis y/o contengan una alta proporcion de valores nulos
df_products= df_products.drop("product_description_lenght", "product_name_lenght", "product_photos_qty", "product_category_name")

# Eliminamos filas que contengan valores nulos
df_products= df_products.dropna()

#Creamos una columna llamada "volume" a traves de multiplicar las dimensiones de los productos

df_products= df_products.select("product_id", "product_weight_g", "product_length_cm", "product_height_cm", "product_width_cm", (df_products['product_length_cm'] * df_products['product_width_cm'] * df_products['product_height_cm']).alias('volumen'))




"""
        Normalizacion df_order_items
"""
#Eliminamos las columnas que no seran de interes en el analisis y/o contengan una alta proporcion de valores nulos
df_order_items= df_order_items.drop("shipping_limit_date", "order_item_id")
Tabla1= df_order_items[["order_id", "price"]]
Tabla1= Tabla1.select("order_id", Tabla1["price"].cast("int"))
tabla1= Tabla1.groupby("order_id").sum('price')


tabla2= df_order_items[["order_id", "freight_value"]]
tabla2= tabla2.drop_duplicates(["order_id"])


tabla1= tabla1.join(tabla2, on= "order_id")

tabla1= tabla1.select("order_id", (tabla1["sum(price)"] - tabla1["freight_value"]).alias("Beneficio"))
df_order_items= df_order_items.join(tabla1, on= "order_id")



"""
        Creacion de las Tablas en Hive
"""
df_closed_deals.write.saveAsTable("closed_deals")
df_customers.write.saveAsTable("customers")
df_marketing_qualified_leads.write.saveAsTable("marketing_qualified_leads")
df_order_reviews.write.saveAsTable("order_reviews")
df_orders.write.saveAsTable("orders")
df_order_payments.write.saveAsTable("order_payments")
df_products.write.saveAsTable("products")
df_order_items.write.saveAsTable("order_items")
~~~

## **4. Validación de datos**
  El presente trabajo consta de una consistente vocación por la conservación y presentación de datos que sean claros, estén limpios y tengan poder explicativo de los distintos fenómenos que van a ser estudiados. 
   Las principales transformaciones que sufrieron los datos obtenidos fueron:
   - Eliminación de columnas con baja precisión, ya sea por la cantidad de valores nulos, el parecido con otra columna o la definición de la variable en sí misma.
   - El proceso de transformación o eliminación de registros con valores nulos, no definidos o mal definidos.
   - La agrupación de columnas de distintas tablas.
   - El cambio de formato de los datos de diversas tablas.
   - Con el objetivo de realizar modelos predictivos fueron creadas nuevas columnas, combinando columnas originales, que serán utilizadas en modelos de Machine Learning.!
