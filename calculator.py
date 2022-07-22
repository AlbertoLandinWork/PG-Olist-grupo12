from platform import machine
from flask import Flask, render_template, request
import pandas as pd
import statsmodels.api as sm
from sklearn.model_selection import train_test_split


app = Flask(__name__)

df_order_items = pd.read_csv("Datasets/olist_order_items_dataset.csv")
df_products = pd.read_csv("Datasets/olist_products_dataset.csv")
df_customers = pd.read_csv("Datasets/olist_customers_dataset.csv")
df_orders = pd.read_csv("Datasets/olist_orders_dataset.csv")
df_products["volume"] = df_products["product_weight_g"] * df_products["product_height_cm"] * df_products["product_width_cm"]

#Creamos nuestra tabla para usar
Tabla1=df_orders[["order_id","customer_id"]]
df_order_items=df_order_items.merge(Tabla1,on="order_id")
machin10=df_order_items[["product_id","freight_value","customer_id"]]
machin20= df_products[["product_id","product_weight_g", "volume"]]
machin30=df_customers[["customer_id","customer_state"]]
machin10 = machin10.merge(machin20, on="product_id")
machin10 = machin10.merge(machin30, on="customer_id")
machin10.dropna(inplace=True)



#selecionamos del dataset las filas que son de sao pablo





def calcular_precio(volumen, peso, region):

    machin10_sp = machin10[machin10.customer_state ==region]
    X = machin10_sp[['volume', 'product_weight_g']]
    y = machin10_sp['freight_value']

    X_train, X_test, y_train, y_test = train_test_split(
                                            X,
                                            y.values.reshape(-1,1),
                                            train_size   = 0.8,
                                            random_state = 1234,
                                            shuffle      = True
                                        )


    X_train = sm.add_constant(X_train, prepend=True)
    modelo = sm.OLS(endog=y_train, exog=X_train,)
    modelo = modelo.fit()
    a=modelo.params

    precio_fijo = a[0]
    volumen_cm3 = a[1]
    peso_g = a[2]

    return precio_fijo + volumen_cm3 * volumen + peso_g * peso



@app.route('/',methods=['GET', 'POST'])
def index():

    

    if request.method == 'POST':
        if request.form["peso"] == "" or request.form["volumen"] == "":
            return render_template('resultado.html', resultado="Rellena todos los campos")


        peso = float(request.form['peso'])
        volumen= float(request.form['volumen'])
        region = str(request.form['region'])

        resultado = str(round(calcular_precio(volumen, peso, region),2)) + " R$"
        return render_template('resultado.html',peso=peso, volumen=volumen, region=region, resultado=resultado)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
