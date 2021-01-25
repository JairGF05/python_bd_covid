#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys
from conector import *
from funciones import *
#quitar visible en sql
def run():
    #table_name = "pruebas"
    #show_tables()
    #insert_multiple_values_clientes()
    #obtener_datos_clientes()
    #obtener_datos_consulta()
    #consulta_where()
    #consulta_order_by()
    #delete()
    #consulta_order_by_desc()
    #update()
    #inner_join_cliente_marca()
    #inner_join_cliente_modelo()
    #inner_join_cliente_modelo_fecha()
    #inner_join_cliente_vehiculo_fecha()
    #inner_join_cliente_opcion()
    #cliente_modelo()
    #cuantos_autos()
    while True:
        menu = """
        Bienvenido a datos covid-19 México 👨‍⚕️

        1- Muestra bases de datos
        2- Muestra tablas
        3- Muestra Fechas de Defunciones
        4- Suma decesos
        5- Suma deceso group by sector
        6- Suma deceso group by sector y fecha
        7- Suma deceso y sector
        8- Suma deceso y sector rollup
        0- Salir

        Selecciona una opción: """

        #dentro del input mandamos a llamar el menú declarado arriba
        opcion = input(menu)
        if opcion == '1':
            show_data_bases()
                

        elif opcion == '2':
            show_tables()
                

        elif opcion == '3':
            show_deads()
        
        elif opcion == '4':
            sum_deceso()

        elif opcion == '5':
            sum_deceso_group()
        
        elif opcion == '6':
            sum_deceso_group_doble()

        elif opcion == '7':
            sum_deceso_group1()

        elif opcion == '8':
            sum_deceso_with_rlup()      
        
        elif opcion == '0':
            break
        else:
            print("Opción no valida")



if __name__ == "__main__":
    run()
    