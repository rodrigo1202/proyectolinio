import sqlite3
from datetime import datetime 

class Pedido(object):

    def __init__(self,cod_pedido:str , estado:str , fecha_pedido: datetime, costo_delivery:float, fecha_entrega: datetime,
                 hora_entrega:datetime, modo_pago:str, proveedor:str):

        self.__cod_pedido= cod_pedido
        self.__estado= estado
        self.__fecha_pedido = fecha_pedido
        self.__costo_delivery = costo_delivery
        self.__fecha_entrega = fecha_entrega
        self.__hora_entrega = hora_entrega
        self.__modo_pago = modo_pago
        self.__proveedor = proveedor

    @property
    def cod_pedido(self):
        return self.__cod_pedido
    @property
    def estado(self):
        return self.__estado
    @property
    def fecha_pedido(self):
        return self.__fecha_pedido
    @property
    def costo_delivery(self):
        return self.__costo_delivery
    @property
    def fecha_Entrega(self):
        return self.__fecha_entrega
    @property
    def hora_entrega(self):
        return self.__hora_entrega
    @property
    def modo_pago(self):
        return self.__modo_pago
    @property
    def proveedor(self):
        return self.__proveedor
    @cod_pedido.setter
    def cod_pedido(self,new_value):
        self.__cod_pedido = new_value
    @estado.setter
    def estado(self,new_value):
        self.__estado = new_value
    @proveedor.setter
    def proveedor(self,new_value):
        self.__proveedor = new_value
    @fecha_Entrega.setter
    def fecha_entrega(self,new_value):
        self.__fecha_entrega = new_value
    @hora_entrega.setter
    def hora_entrega(self,new_value):
        self.__hora_entrega=new_value
    @costo_delivery.setter
    def costo_delivery(self,new_value):
        self.__costo_delivery = new_value

    def __str__(self):
        return "{}-> cod_pedido= '{}', estado = '{}', proveedor = '{}', fecha_entrega = '{}', hora_entrega ='{}', costo_delivery = '{}'".format(self.__class__.__name__, self.__cod_pedido,
                                                                            self.__estado, self.__proveedor,
                                                                            self.__fecha_entrega,
                                                                            self.__hora_entrega, self.__costo_delivery)