from conector import *

def show_data_bases():
    
    ## executing the statement using 'execute()' method
    cursor.execute("SHOW DATABASES")

    ## 'fetchall()' method fetches all the rows from the last executed statement
    databases = cursor.fetchall() ## it returns a list of all databases present

    ## printing the list of databases
    print(databases)

   

def show_tables():
    ## getting all databases from db
    cursor.execute("SHOW TABLES")

    tables = cursor.fetchall() ## it returns list of tables present in the database

    ## showing all the tables one by one
    for table in tables:
        print(table)

#imprimir fechas de muertes
def show_deads():
    query = "SELECT numero_decesos, fecha_defuncion, sexo, edad, entidad_res, institucion \
            FROM decesos \
            INNER JOIN tiempo \
            ON decesos.fk_id_fecha = tiempo.id_fecha \
            INNER JOIN pacientes \
            ON pacientes.id_paciente = decesos.fk_id_paciente \
            INNER JOIN lugar \
            ON lugar.sector = decesos.fk_sector"
    print("#Decesos | Fecha Defunción | Sexo | Edad | Entidad | Institución")
    cursor.execute(query)

    myresult = cursor.fetchall()
    #print("Fecha Ingreso | Fecha Sintomas | Fecha Defunción")
    for x in myresult:
        print(x)

#imprimir acumulación de decesos
def sum_deceso():
    query = "SELECT sum(numero_decesos) FROM decesos WHERE 1"
    cursor.execute(query)

    myresult = cursor.fetchall()
    #print("Fecha Ingreso | Fecha Sintomas | Fecha Defunción")
    for x in myresult:
        print(x)

#imprimir acumulación de decesos group by sector
def sum_deceso_group():
    query = "SELECT sum(numero_decesos) FROM decesos GROUP BY fk_sector"
    cursor.execute(query)

    myresult = cursor.fetchall()
    #print("Fecha Ingreso | Fecha Sintomas | Fecha Defunción")
    for x in myresult:
        print(x)


#imprimir acumulación de decesos group by sector y fecha
def sum_deceso_group_doble():
    query = "SELECT sum(numero_decesos) FROM decesos GROUP BY fk_sector, fk_id_fecha"
    cursor.execute(query)

    myresult = cursor.fetchall()
    #print("Fecha Ingreso | Fecha Sintomas | Fecha Defunción")
    for x in myresult:
        print(x)

#imprimir acumulación de decesos group by sector
def sum_deceso_group1():
    query = "SELECT fk_sector, sum(numero_decesos) FROM decesos GROUP BY fk_sector"
    cursor.execute(query)

    myresult = cursor.fetchall()
    #print("Fecha Ingreso | Fecha Sintomas | Fecha Defunción")
    for x in myresult:
        print(x)

#imprimir acumulación de decesos group by sector
def sum_deceso_with_rlup():
    query = "SELECT fk_sector, sum(numero_decesos) FROM decesos GROUP BY fk_sector WITH ROLLUP"
    cursor.execute(query)

    myresult = cursor.fetchall()
    #print("Fecha Ingreso | Fecha Sintomas | Fecha Defunción")
    for x in myresult:
        print(x)

def insert_multiple_values_clientes():

    query = "INSERT INTO clientes (nombre, apellido, telefono, direccion) VALUES (%s, %s, %s, %s)"
    ## storing values in a variable
    
    values = [
        ("Jair", "Garcia", "5581227653", "11 sur"),
        ("Oswaldo", "Franco", "5582345678", "Wall street"),
        ("Patricia", "Benitez", "7635241324", "Benito Juarez 98"),
        ("Julio", "Benitez", "3425162567", "Alvaro Obregon 55"),
        ("Alondra", "Anzures", "2234156253", "Mariano salas 34"),
        ("Bill", "Gates", "1134156253", "Seattle stree 43"),
        ("Steve", "Jobs", "3034156253", "Palo alto 22"),
        ("Megan", "Fox", "6534156253", "Place Avenue 99"),
        ("Stephen", "King", "0934156253", "Hoorror street 33")
    ]

    ## executing the query with values
    cursor.executemany(query, values)

    ## to make final output we have to run the 'commit()' method of the database object
    db.commit()

    print(cursor.rowcount, "records inserted")

def obtener_datos_clientes():
    ## defining the Query
    query = "SELECT * FROM clientes"

    ## getting records from the table
    cursor.execute(query)

    ## fetching all records from the 'cursor' object
    records = cursor.fetchall()

    ## Showing the data
    for record in records:
        print(record)

def obtener_datos_consulta():
    ## defining the Query
    query = "SELECT nombre, apellido FROM clientes"

    ## getting 'user_name' column from the table
    cursor.execute(query)

    ## fetching all usernames from the 'cursor' object
    clientes = cursor.fetchall()

    ## Showing the data
    for cliente in clientes:
        print(cliente)

def consulta_where():
    ## defining the Query
    query = "SELECT * FROM clientes WHERE id_cliente = 2"

    ## getting records from the table
    cursor.execute(query)

    ## fetching all records from the 'cursor' object
    records = cursor.fetchall()

    ## Showing the data
    for record in records:
        print(record)

def consulta_order_by():
    ## defining the Query
    query = "SELECT nombre FROM clientes ORDER BY nombre"

    ## getting records from the table
    cursor.execute(query)

    ## fetching all records from the 'cursor' object
    records = cursor.fetchall()

    ## Showing the data
    for record in records:
        print(record)
    
def consulta_order_by_desc():
    ## defining the Query
    query = "SELECT nombre FROM clientes ORDER BY nombre DESC"

    ## getting records from the table
    cursor.execute(query)

    ## fetching all records from the 'cursor' object
    records = cursor.fetchall()

    ## Showing the data
    for record in records:
        print(record)

def delete():
    ## defining the Query
    query = "DELETE FROM clientes WHERE id_cliente = 2"

    ## executing the query
    cursor.execute(query)

    ## final step to tell the database that we have changed the table data
    db.commit()

def update():
    ## defining the Query
    query = "UPDATE clientes SET name = 'Monica' WHERE id_cliente = 1"

    ## executing the query
    cursor.execute(query)

    ## final step to tell the database that we have changed the table data
    db.commit()
    

#imprimir cliente y que modelo compro con su marca
def inner_join_cliente_marca():
    query = "SELECT nombre, apellido, fk_id_modelo \
        FROM clientes \
        INNER JOIN compras \
        ON clientes.id_cliente = compras.fk_id_cliente"

    cursor.execute(query)

    myresult = cursor.fetchall()

    for x in myresult:
        print(x)


def inner_join_cliente_modelo():
    query = "SELECT nombre, apellido, modelo\
        FROM clientes \
        INNER JOIN compras \
        ON clientes.id_cliente = compras.fk_id_cliente \
        INNER JOIN modelos \
        ON modelos.id_modelo = compras.fk_id_modelo"

    cursor.execute(query)

    myresult = cursor.fetchall()

    for x in myresult:
        print(x)
        
def inner_join_cliente_modelo_fecha():
    query = "SELECT nombre, apellido, modelo, fecha\
        FROM clientes \
        INNER JOIN compras \
        ON clientes.id_cliente = compras.fk_id_cliente \
        INNER JOIN modelos \
        ON modelos.id_modelo = compras.fk_id_modelo \
        ORDER BY fecha DESC "

    cursor.execute(query)

    myresult = cursor.fetchall()

    for x in myresult:
        print(x)
        
def inner_join_cliente_vehiculo_fecha():
    query = "SELECT nombre, apellido, marca, modelo, fecha\
        FROM clientes \
        INNER JOIN fechas \
        ON clientes.id_cliente = fechas.fk_id_cliente \
        INNER JOIN vehiculos \
        ON fechas.id_fecha = vehiculos.fk_id_fecha \
        ORDER BY fecha DESC "

    cursor.execute(query)

    myresult = cursor.fetchall()

    for x in myresult:
        print(x)
    
    #cliente,nombre de modelo que compró, precio y opcion de compra
def inner_join_cliente_opcion():
    
    query = "SELECT nombre, apellido, nombre_opcion, descuento\
        FROM clientes \
        INNER JOIN compras \
        ON clientes.id_cliente = compras.fk_id_cliente \
        INNER JOIN opciones \
        ON opciones.id_opcion = compras.fk_id_opcion  "

    cursor.execute(query)

    myresult = cursor.fetchall()

    for x in myresult:
        print(x)



def cliente_modelo():
    
    query = "SELECT nombre, apellido, fecha, nombre_opcion, modelo\
        FROM clientes \
        INNER JOIN compras \
        ON compras.fk_id_cliente = clientes.id_cliente \
        INNER JOIN opciones \
        ON opciones.id_opcion = compras.fk_id_opcion \
        INNER JOIN modelos \
        ON modelos.id_modelo = compras.fk_id_modelo "
    
    cursor.execute(query)

    myresult = cursor.fetchall()

    for x in myresult:
        print(x)


def cuantos_autos():
    query = "SELECT COUNT(fk_id_cliente) FROM compras ORDER BY fk_id_cliente "
        

    cursor.execute(query)

    myresult = cursor.fetchall()

    for x in myresult:
        print(x)
 
        
        
        


        




        