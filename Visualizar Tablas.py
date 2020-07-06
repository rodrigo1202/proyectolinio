import sqlite3
NUMERO_TABLA={1:"CLIENTES", 2:"PEDIDOS", 3:"PRODUCTO", 4:"LINEA_PEDIDO"}
a=NUMERO_TABLA[1]
con = sqlite3.connect("data/liniotrabfinal.db")
cursor = con.cursor()
cursor.execute("select * from {}".format(a))
rows = cursor.fetchall()
print("linea :{}".format(a)+"S")
for row in rows:
    print(row)