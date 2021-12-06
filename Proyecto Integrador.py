#Ricardo Adolfo Gonzalez Terán 
#ITESM Campus Toluca
#A01769410

#-*- coding:utf-8 -*-

nombre_archivo="DATA_1.csv"

def crear_archivo():
	print("Indica el nombre del archivo sin extencion")
	nombre_archivo=str(input("-->"))
	archivo=open(nombre_archivo+".csv", "w+")
	archivo.write("Nombre,Apellido,Telefono,Matricula,1er Parcial,2do Parcial,Examen Final,Promedio de Examenes,Calificacion Final,\n")
	archivo.close()
	print("-"*80)

def registrar_alumno():
	print("Ingresa el nombre de su archivo sin extension, si no creó un acrhivo el nombre será \"DATA_1\":")
	nombre_archivo=str(input("-->"))
	archivo=open(nombre_archivo+".csv", "a+")
	print("Ingrese el primer nombre del alumno:")
	nombre_al=str(input("-->"))
	archivo.write(nombre_al+",")
	print("Ingrese el apellido paterno del alumno:")
	appellido_al=str(input("-->"))
	archivo.write(appellido_al+",")
	print("Ingrese el telefono de contacto del alumno:")
	tel_contacto=str(input("-->"))
	archivo.write(tel_contacto+",")
	print("Ingrese la matricula del alumno, empezando por: A0(...)")
	id_student=str(input("-->"))
	archivo.write(id_student+",")
	print("Ingrese calificacion del 1er examen parcial:")
	primer_parcial=str(input("-->"))
	archivo.write(primer_parcial+",")
	print("Ingrese calificacion del 2do examen parcial:")
	segundo_parcial=str(input("-->"))
	archivo.write(segundo_parcial+",")
	print("Ingrese calificacion del Examen Final:")
	test_final=str(input("-->"))
	archivo.write(test_final+",")
	promedio_examenes=round((((int(primer_parcial))+(int(segundo_parcial))+(int(test_final)))/3),2)
	calificacion_final=((int(primer_parcial)*0.3)+(int(segundo_parcial)*0.3)+(int(test_final)*0.4))
	archivo.write(str(promedio_examenes))
	archivo.write(",")
	archivo.write(str(calificacion_final))
	archivo.write(",\n")
	print("-"*80)
	print("Alumno creado con exito!")
	print("-"*80)

def leer_archivo():
	print("Ingresa el nombre de tu archivo sin extención, se usara csv, si no creó un acrhivo el nombre será \"DATA_1\": ")
	name_archivo=str(input("-->"))

	while 1:

		print("Deseas?")
		print("1. Leer Todo la base de datos")
		print("2. Encontrar a un alumno en específico")
		opcion_lectura=int(input("-->"))

		if opcion_lectura==1:
			archivo=open(name_archivo+".csv","r")
			archive=archivo.read()
			archive=archive.replace(","," ")
			posicion=archive.find("\n")
			registro_gen=archive[posicion:]
			print("-"*80)
			print(registro_gen, "\n\r")
			archivo.close()
			print("Completado!")
			print("-"*80)
			break

		elif opcion_lectura==2:
			archivo=open(name_archivo+".csv","r")
			archive=archivo.read()
			archive=archive.replace(","," ")
			print("Ingrese el nombre del alumno:")
			name_student=str(input("-->"))
			posicion_inicial=archive.find(name_student)
			archive2=archive[posicion_inicial:]
			posicion_final=archive2.find("\n")
			registro_esp=archive2[0:posicion_final]
			print("-"*80)
			print(registro_esp, "\n\r")
			print("Completado!")
			print("-"*80)
			break

		else:
			print("Opcion no valida...")

def editar_registro():
	print("Ingresa el nombre de tu archivo sin extencion, se usara csv, si no creó un acrhivo el nombre será \"DATA_1\":")
	name_archivo=str(input("-->"))
	archivo=open(name_archivo+".csv","r")
	archive=archivo.read()

	print("Que desea editar?")
	print("1. Primer Examen Parcial")
	print("2. Segundo Examen Parcial")
	print("3. Examen Final")

	opcion_edit=int(input("-->"))

	while 1:


		if opcion_edit==1:
			archivo=open(name_archivo+".csv","r+")
			archive=archivo.read()
			archive=archive.replace(","," ")
			print("Ingrese el nombre del alumno:")
			name_student=str(input("-->"))
			posicion_inicial=archive.find(name_student)
			archive2=archive[posicion_inicial:]
			posicion_final=archive2.find("\n")
			registro_al=archive2[0:posicion_final]
			print("-"*80)
			print("Encontrado, el alumno es:", registro_al)
			print("-"*80)
			registro_lista=registro_al.split()
			print("Ingrese nueva calificacion para el 1er Parcial, actualmente el puntaje es", registro_lista[4])
			grade_1=str(input("-->"))
			registro_lista[4]=grade_1
			promedio_examenes=round((((int(registro_lista[4]))+(int(registro_lista[5]))+(int(registro_lista[6])))/3),2)
			final_grade=((int(registro_lista[4])*0.3)+(int(registro_lista[5])*0.3)+(int(registro_lista[6])*0.4))
			registro_lista[7]=(str(promedio_examenes))
			registro_lista[8]=(str((final_grade)))
			separador=","
			lista_a_str=separador.join(registro_lista)
			lista_a_str="\n"+lista_a_str+"\n"
			final_grade_modificated=(lista_a_str)
			archivo.seek(posicion_inicial)
			archivo.write(final_grade_modificated+" ")
			print("-"*80)
			print("✅Calificación Modificada con exito")
			print("-"*80)
			archivo.close()
			break

		if opcion_edit==2:
			archivo=open(name_archivo+".csv","r+")
			archive=archivo.read()
			archive=archive.replace(","," ")
			print("Ingrese el nombre del alumno:")
			name_student=str(input("-->"))
			posicion_inicial=archive.find(name_student)
			archive2=archive[posicion_inicial:]
			posicion_final=archive2.find("\n")
			registro_al=archive2[0:posicion_final]
			print("-"*80)
			print("Encontrado, el alumno es:", registro_al)
			print("-"*80)
			registro_lista=registro_al.split()
			print("Ingrese nueva calificacion para el 1er Parcial, actualmente el puntaje es", registro_lista[5])
			grade_1=str(input("-->"))
			registro_lista[5]=grade_1
			promedio_examenes=round((((int(registro_lista[4]))+(int(registro_lista[5]))+(int(registro_lista[6])))/3),2)
			final_grade=((int(registro_lista[4])*0.3)+(int(registro_lista[5])*0.3)+(int(registro_lista[6])*0.4))
			registro_lista[7]=(str(promedio_examenes))
			registro_lista[8]=(str(final_grade))
			separador=","
			lista_a_str=separador.join(registro_lista)
			lista_a_str=lista_a_str+"\n"
			final_grade_modificated=(lista_a_str)
			archivo.seek(posicion_inicial)
			archivo.write(final_grade_modificated+" ")
			print("-"*80)
			print("✅Calificación Modificada con exito")
			print("-"*80)
			archivo.close()
			break

		if opcion_edit==3:
			archivo=open(name_archivo+".csv","r+")
			archive=archivo.read()
			archive=archive.replace(","," ")
			print("Ingrese el nombre del alumno:")
			name_student=str(input("-->"))
			posicion_inicial=archive.find(name_student)
			archive2=archive[posicion_inicial:]
			posicion_final=archive2.find("\n")
			registro_al=archive2[0:posicion_final]
			print("-"*80)
			print("Encontrado, el alumno es:", registro_al)
			print("-"*80)
			registro_lista=registro_al.split()
			print("Ingrese nueva calificacion para el 1er Parcial, actualmente el puntaje es", registro_lista[6])
			grade_1=str(input("-->"))
			registro_lista[6]=grade_1
			promedio_examenes=round((((int(registro_lista[4]))+(int(registro_lista[5]))+(int(registro_lista[6])))/3),2)
			final_grade=((int(registro_lista[4])*0.3)+(int(registro_lista[5])*0.3)+(int(registro_lista[6])*0.4))
			registro_lista[7]=(str(promedio_examenes))
			registro_lista[8]=(str(final_grade))
			separador=","
			lista_a_str=separador.join(registro_lista)
			lista_a_str=lista_a_str+"\n"
			final_grade_modificated=(lista_a_str)
			archivo.seek(posicion_inicial)
			archivo.write(final_grade_modificated+" ")
			print("-"*80)
			print("✅Calificación Modificada con exito")
			print("-"*80)
			archivo.close()
			break

		else:
			print("Opcion Invalida...")
			print("-"*80)

while 1:

	print("***Bitacora de Estdiantes***\n\r")

	print("Que desea hacer?")
	print("1. Crear nuevo archivo")
	print("2. Leer los registros")
	print("3. Registrar alumno")
	print("4. Modificar Calificaciones")
	print("6. Borrar todos los registros")
	print("7. Salir")

	opcion1=int(input("-->"))

	if opcion1==1:
		archivo=crear_archivo()
		print("Archivo Creado con exito!")
		print("-"*80)

	elif opcion1==2:
		archivo=leer_archivo()

	elif opcion1==3:
		archivo=registrar_alumno()

	elif opcion1==4:
		archivo=editar_registro()

	elif opcion1==5:
		print("WORK_IN_PROGRESS")

	elif opcion1==6:
		archivo=crear_archivo()
		print("Registros borrados con exito!")
		print("-"*80)

	elif opcion1==7:
		print("OPERATION_CANCELLED_BY_USER...")
		break

	else:
		print("Opcion Invalida...Reintente")
		print("-"*80)