#  ····································
#  ·             Canmig Cai           ·
#  ·    Luis Felipe Depardon Jasso    ·
#  ·   Ricardo Adolfo González Terán  ·
#  ····································

import librerias as lb

def menu_cientificos():
    op=-1
    while op!=0:
      lb.limpia_pantalla()
      print("|----------------------------------------|")
      print("             MENU CIENTIFICOS            |")
      print("|----------------------------------------|")
      print("| 1) Altas de científicos                |")
      print("| 2) Bajas de científicos                |")
      print("| 3) consulta de científicos             |")
      print("| 4) Cambios de científicos              |")
      print("| 5) Regresar al menú principal          |")
      print("|----------------------------------------|")

      op = lb.pide_entero(0,5,"Indica la opcion deseada : ")
      if op == 1:
          altas_cientificos()
      if op == 2:
          bajas_cientificos()
      if op == 3:
          consultas_cientificos()
      if op == 4:
          cambios_cientificos()
      if op == 5:
        break

    lb.limpia_pantalla()



def altas_cientificos():
  
    lb.limpia_pantalla()
    print("|====================================================|")
    print("|                 ALTAS DE CIENTÍFICOS               |")
    print("|====================================================|")

    cone_bd=lb.conectar_bd()
    cursor=cone_bd.cursor()
    
    vid_c = lb.pide_cadena(1,5,"Indica el ID del Cientifico           :")
    vid_c = vid_c.upper()

    while len(vid_c) < 5:
      vid_c = "0" + vid_c
    
    if len(vid_c) > 5:
      pass

    else: 

      query = "SELECT * FROM cientificos WHERE id_ci = '"+vid_c+"'"
      grab = cursor.execute(query)

      if grab == 1:
        lb.error("\nEl cientifico ya se encuentra registrado en la base de datos...")
      else:
        
        vnom = lb.pide_cadena(1,15,"Indica el Nombre del Cientifico      :")
        vnom = vnom.upper()

        vap = lb.pide_cadena(1,15,"Indica el Ap. Paterno del Cientifico  :")
        vap = vap.upper()

        vam = lb.pide_cadena(1,15,"Indica el Ap. Materno del Cientifico  :")
        vam = vam.upper()

        vtel = lb.pide_cadena(10,10,"Indica el telefono del Cientifico    :")

        if vtel.isnumeric() == False:
          lb.error("El dato ingresado no es un numero telefonico...")

        else:
          vmail = lb.pide_cadena(3, 30, "Indica el correo del Cientifico   : ")

          if vmail.find("@") == -1:
            lb.error("El dato ingresado no es un correo electronico valido...")

          else:
            query="INSERT INTO cientificos VALUES('"+vid_c+"','"+vnom+"','"+vap+"','"+vam+"','"+vtel+"','"+vmail+"')"
            
            seguro=lb.pide_cadena(1,1,"Los datos son correctos, desea grabar [S/N]: ")
            seguro=seguro.upper()

            if seguro=="S":

                try:
                    x=cursor.execute(query)
                except:
                    x=0

                if x==0:
                  lb.error("Error hubo un problema al grabar en la base de datos") 
                else:
                    lb.error("Los datos han sido grabados correctamente")
            else:
                lb.error("La acción de grabar ha sido cancelada")

            cone_bd.commit()
            cone_bd.close()


def bajas_cientificos():

    lb.limpia_pantalla()

    print("|============================|")
    print("|   BAJA DE CIENTÍFICOS      |")
    print("|============================|")

    vid_c = lb.pide_cadena(5,5,"Indica el ID del Cientifico a ELIMINAR : ")
    vid_c = vid_c.upper()

    if len(vid_c) > 5:
      pass

    else:

      cone_bd = lb.conectar_bd()
      cursor = cone_bd.cursor()

      query = "SELECT * FROM proyectos WHERE id_ci_pro = '"+vid_c+"'"
      grab = cursor.execute(query)

      if grab == 1:
        lb.error("\nEl cientifico ya se encuentra registrado en un proyecto...")

      else: 

        query = "DELETE FROM cientificos WHERE id_ci='"+vid_c+"'"

        seguro = lb.pide_cadena(1,1,"seguro de eliminar [S/N] : ")
        seguro = seguro.upper()

        if seguro == "S":

            x = cursor.execute(query)
            if x == 0:
                lb.error("Error, matrícula inexistente en el archivo de cientificos...")
            else:
                lb.error("El registro ha sido eliminado correctamente")
        else:
            lb.error("La accion de ELIMINAR ha sido CANCELADA")

def consultas_cientificos():
  
    lb.limpia_pantalla()
    
    print("|----------------------------|")
    print("|  CONSULTAS DE CIENTIFICOS  |")
    print("|----------------------------|")

    vid_c=lb.pide_cadena(5,5, "Indica el ID del Cientifico a CONSULTAR      : ")
    vid_c=vid_c.upper()

    if len(vid_c) > 5:
      pass

    else:

      query="SELECT * FROM cientificos WHERE id_ci='"+ vid_c +"'"

      cone_bd = lb.conectar_bd()
      cursor = cone_bd.cursor()
      x = cursor.execute(query)
      
      if x == 0:
          lb.error("Error, matricula inexistente en el archivo de cientificos...")
      else:
          datos_cientificos=cursor.fetchone()
          print("\n")
          print("Nombre      : ",datos_cientificos[1])
          print("Ap. Paterno : ",datos_cientificos[2])
          print("Ap. Materno : ",datos_cientificos[3])
          print("Telefono    : ",datos_cientificos[4])
          print("Correo      : ",datos_cientificos[5])
          lb.error("")
          
      cone_bd.close()

def cambios_cientificos():
  
    lb.limpia_pantalla()
    
    print("|==========================|")
    print("| CAMBIOS DE CIENTÍFICOS   |")
    print("|==========================|")
    
    vid_c=lb.pide_cadena(5,5,"Indica la id del cientifico, [0] para terminar : ")
    vid_c=vid_c.upper()

    if len(vid_c) > 5:
      pass
    
    else:

      while vid_c != "0":
    
        cone_bd=lb.conectar_bd()
        cursor=cone_bd.cursor()

        query = "SELECT * FROM cientificos WHERE id_ci = '"+ vid_c +"'"
        validacion = cursor.execute(query)

        if validacion == 0:
          lb.error("El ID del Cientifico no existe en la base de datos...")

        else:

          print(" 1) Telefono  ")
          print(" 2) Correo    ")
          op = lb.pide_entero(0,2,"Indica la opcion deseada para cambiar: ")
      
          if op == 1:

            vtel = lb.pide_cadena(10,10,"Indica el nuevo telefono del cientifico : ")

            if vtel.isnumeric() == False:
              lb.error("El dato ingresado no es un numero telefonico...")

            else:

              query="UPDATE cientificos SET tel_ci='"+ vtel +"' WHERE id_ci='"+ vid_c +"'"

              grab = cursor.execute(query)

              if grab == 0:
                lb.error("Hubo un error al grbar en la base de datos...")

              else:
                lb.error("El cambio ha sido actualizado exitosamente...")

            
          elif op == 2:

            vmail = lb.pide_cadena(3,30,"Indica el nuevo correo del cientifico :")
            vmail = vmail.upper()

            query="UPDATE cientificos SET correo_ci = '"+vmail+"' WHERE id_ci = '"+vid_c+"'"
            
            cone_bd=lb.conectar_bd()
            cursor=cone_bd.cursor()

            grab = cursor.execute(query)

            if grab == 0:
              lb.error("Hubo un error al grbar en la base de datos...")

            else:
              lb.error("El cambio ha sido actualizado exitosamente...")
          
          elif op == 0:
            break

          else:
            lb.error("Opcion Invalida para cambio...")

        cone_bd.commit()
        cone_bd.close()
