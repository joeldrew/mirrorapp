import sqlite3 as dbapi

class new_client():
		
	def __init__(self):
		 print('Bienvenido a la app de  Mirror Hosting')


	def GetAll(self):
		#Metodo que muestra una lista con todos los clientes de la base de datos
		con= dbapi.connect('clientes.db')#Conexion con la base de datos
		cursor= con.cursor()#almacenamos nuetro cursor 	que nos servira para realizar operaciones en la base de datos
		cursor.execute(""" SELECT * FROM clientes""")#Ejecutamos nuestra sentencia sql
		#Listamos los clientes de la base de datos
		for cliente in cursor:
	 		print("*************************************")
	 		print("Nombre: "+cliente[0])
	 		print("Apellidos: "+cliente[1])
	 		print("Empresa: "+cliente[2])
	 		print("Telefono: "+cliente[3])
	 		print("Correo: "+cliente[4])
	 		print("Dominio: "+cliente[5])
	 		print("Paquete: "+cliente[6])
	 		print("*************************************")
	 	
		
	def PutData(self):
		con= dbapi.connect('clientes.db')#CONEXION A LA BASE DE DATOS
		cursor= con.cursor()#ALMACENAMOS NUSTRO CURSOR PARA REALIZAR CAMBIOS A LA BASE DE DATOS
		#ALMACENAMOS EN VARIABLES LOS DATOS DEL USUARIO
		nombre=raw_input('Escriba el nombre del cliente: ')
		apellidos =raw_input('EScriba los apellidos del cliente: ')
		empresa = raw_input('Escriba el nombre de la empresa: ')
		telefono = raw_input('Telefono del cliente: ')
		correo = raw_input('Correo Electronico: ')
		dominio=raw_input('Dominio ya verificado en WHOIS: ')
		paquete=raw_input('Paquete contratado: ')
		#EJECUTAMOS LA SENTENCIA SQL
		cursor.execute("""INSERT INTO clientes 
			(nombre,apellidos,empresa,telefono,correo,dominio,paquete) 
			values ('{0}','{1}','{2}','{3}','{4}','{5}','{6}')""".format(nombre,apellidos,empresa,telefono,correo,dominio,paquete))
		con.commit()#REALIZAMOS LOS CAMBIOS EN LA BASE DE DATOS
		cursor.close()#CERRAMOS LA CONEXION DEL CURSOR
		con.close()#CERRAMOS LA CONEXION A NUESTRA BASE DE DATOS

	def search(self):
		dominio = raw_input('Escriba el dominio el cual quiere buscar: ')#ALMACENAMOS EL DOMINIO A BUSCAR 	
		con = dbapi.connect('clientes.db')#CONEXION A LA BASE DE DATOS
	 	cursor = con.cursor()#ALMACENAMOS NUETRO CURSOR PARA REALIZAR CAMBIOS A LA BASE DE DATOS
	 	try:
	 		#INTENTAMOS EJECUTAR NUESTRA SENTENCIA SQL
	 		cursor.execute("""SELECT * FROM clientes where dominio = '{0}'""".format(dominio))
	 		num = len(cursor)#ALMACENAMOS EL NUMERO DE CLIENTES OBTENIDOS
	 		if num==0:# SI EL NUMERO DE CLIENTES ES 0 SE IMPRIMIRA UN MENSAJE AL USUARIO
	 			print('no se encontro ningun cliente')

	 	except :# SI SE HA TERMINADO LA BUSQUEDA
	 		print('Busqueda terminada con exito')
	 	else:
	 		#SI OCURRIO ALGUN ERROR
	 		print('Ocurrio un error inesperado intenete otra vez.')
	 	finally:
	 		#SI NO OCURRIO NINGUN ERROR SE IMPRIMIRA LOS DATOS DEL CLIENTE
	 		for cliente in cursor:
	 			print("*************************************")
	 			print("Nombre: "+cliente[0])
	 			print("Apellidos: "+cliente[1])
	 			print("Empresa: "+cliente[2])
	 			print("Telefono: "+cliente[3])
	 			print("Correo: "+cliente[4])
	 			print("Dominio: "+cliente[5])
	 			print("Paquete: "+cliente[6])
	 			print("*************************************")
	 		cursor.close()#CERRAMOS LA CONEXION A NUESTRO CURSOR
	 		con.close()#CERRAMOS NUESTRA CONEXION A LA BASE DE DATOS
	 	

	 	

	def delete(self):
		#ALMACENAMOS  EL DOMINIO QUE SE QUIERE ELMINAR
		dominio= raw_input('Escriba el dominio el cual quiere eliminar: ')
		#CONEXION A LA BASE DE DATOS
		con= dbapi.connect('clientes.db')
		#ALMACENAMOS NUESTRO CURSOR PARA REALIZAR ACCIONES EN LA BASE DE DATOS
		cursor= con.cursor()
		#EJECUTAMOS LA SENTENCIA SQL
		cursor.execute(""" DELETE  FROM clientes WHERE dominio ='{0}'""".format(dominio))
		con.commit()#HACEMOS LOS CAMBIOS EN LA BASE DE DATOS
		cursor.close()#CERRAMOS LA CONEXION CON EL CURSOR
	 	con.close()#CERRAMOS LA CONEXION CON LA BASE DE DATOS



	 	
	
cliente = new_client()
print("""SELECCIONE LA ACCION A REALIZAR ESCRIBIENDO EL NUMERO DE LA DERECHA
		0.- Nuevo cliente
		1.-Buscar cliente
		2.-Eliminar cliente
		3.- Mostrar todos los clientes""")
opc= raw_input('Numero de la accion a realizar: ')
if opc =='0':
	cliente.PutData()
elif opc =='1':
	cliente.search()
elif opc =='2':
	cliente.delete()
elif opc =='3':
	cliente.GetAll()