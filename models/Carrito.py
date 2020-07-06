import sqlite3

from datetime import datetime


class Carrito():
    def __init__(self,cod_carrito,prod_nom,subtotal,clie_email):
        self.__cod_carrito=cod_carrito
        self.__prod_nom=prod_nom
        self.__subtotal=subtotal
        self.__clie_email=clie_email
    @property
    def cod_carrito(self):
        return self.__cod_carrito
    @property
    def prod_nom(self):
        return self.__prod_nom
    @property
    def subtotal(self):
        return self.__subtotal
    @property
    def clie_email(self):
        return self.__clie_email

    @cod_carrito.setter
    def cod_carrito(self, new_value):
        self.__cod_carrito = new_value

    @prod_nom.setter
    def prod_nom(self, new_value):
        self.__prod_nom = new_value

    @subtotal.setter
    def subtotal(self, new_value):
        self.__subtotal = new_value

    @clie_email.setter
    def clie_email(self, new_value):
        self.__clie_email = new_value

    def sumarcanasta(self):
        print("entre")
    def generarcarrito(self):
        estado_op = False
        database = sqlite3.connect("data/liniotrabfinal.db")  # ABRIR CONEXION CON BASE DE DATOS
        try:
            cursor = database.cursor()  # OBTENER OBJETO CURSOR
            query = '''
                    INSERT INTO carrito(cod_carrito, prod_nom, subtotal, clie_email)
                    VALUES ('{}', '{}', '{}', '{}')
                    '''.format(self.__cod_carrito, self.__prod_nom,
                               self.__subtotal, self.__clie_email)
            resultado = cursor.execute(query)
            database.commit()  # CONFIRMAR CAMBIOS QUERY

            estado_op = True
        except Exception as e:
            database.rollback()  # RESTAURAR ANTES DE CAMBIOS POR ERROR
            print("Error: {}".format(e))
        finally:
            database.close()  # CERRAR CONEXION CON BASE DE DATOS

        return estado_op
    def obtener_carrito(self,email):
        try:
            database = sqlite3.connect("data/liniotrabfinal.db")  # ABRIR CONEXION CON BASE DE DATOS
            cursor = database.cursor()  # OBTENER OBJETO CURSOR
            query = '''
            SELECT * FROM carrito where clie_email like {}
            '''.format(email)
            cursor.execute(query)
            carrito = cursor.fetchone()
        except Exception as e:
            print("Error: {}".format(e))
        finally:
            database.close()  # CERRAR CONEXION CON BASE DE DATOS
        return carrito

    def actualizar_carrito(self)-> bool:
        estado_op = False
        database = sqlite3.connect("data/liniotrabfinal.db")
        try:

            cursor = database.cursor()
            query = '''
            UPDATE carrito
            SET cod_carrito = '{}', prod_nom = '{}', subtotal = '{}', clie_email = '{}'
            WHERE clie_email = '{}'
            '''.format(self.__cod_carrito, self.__prod_nom, self.__subtotal,
                       self.clie_email)
            cursor.execute(query)
            database.commit()
            estado_op = True
        except Exception as e:
            database.rollback()  # RESTAURAR ANTES DE CAMBIOS POR ERROR
            print("Error: {}".format(e))
        finally:
            database.close()  # CERRAR CONEXION CON BASE DE DATOS

        return estado_op

    def __str__(self):
        return "{}-> cod_carrito= '{}', prod_nom = '{}', subtotal = '{}', clie_email = '{}'".format(self.__class__.__name__, self.__cod_carrito,
                                                                            self.__prod_nom, self.__subtotal,
                                                                            self.__clie_email,
                                                                           )
