#  ····································
#  ·             Canmig Cai           ·
#  ·    Luis Felipe Depardon Jasso    ·
#  ·   Ricardo Adolfo González Terán  ·
#  ····································

import librerias as lb

def menu_proyectos():
    op = -1
    while op != 5:
      lb.limpia_pantalla()
      print("|----------------------------------------|")
      print("             MENU PROYECTOS              |")
      print("|----------------------------------------|")
      print("| 1) Altas de proyectos                  |")
      print("| 2) Bajas de proyectos                  |")
      print("| 3) consulta de proyectos               |")
      print("| 4) Cambios de proyectos                |")
      print("| 5) Regresar al menú principal          |")
      print("|----------------------------------------|")

      op=lb.pide_entero(1,5,"Indica la opcion deseada : ")

      if op==1:
          altas_proyectos()
      if op==2:
          bajas_proyectos()
      if op==3:
          consultas_proyectos()
      if op==4:
          cambios_proyectos()
      else:
        print("Opcion Invalida...")

    lb.limpia_pantalla()

def altas_proyectos():
  
    lb.limpia_pantalla()
    print("|====================================================|")
    print("|                 ALTAS DE PROYECTOS                 |")
    print("|====================================================|")

    cone_bd=lb.conectar_bd()
    cursor=cone_bd.cursor()
    
    vid_pro = lb.pide_cadena(1,5,"Indica el numero del proyecto: ")
    vid_pro = vid_pro.upper()

    while len(vid_pro) < 5:
      vid_pro = "0" + vid_pro
    
    if len(vid_pro) > 5:
      pass

    else: 

      query = "SELECT * FROM proyectos WHERE id_pro = '"+ vid_pro +"'"
      grab = cursor.execute(query)

      if grab == 1:
        lb.error("\nEl proyecto ya se encuentra registrado en la base de datos...")
      else:
        
        vnombre_proyecto = lb.pide_cadena(1,15,"Indica el nombre del proyecto: ")
        vnombre_proyecto = vnombre_proyecto.upper()

        varea_pro = lb.pide_cadena(1,15,"Indica el area del proyecto: ")
        varea_pro = varea_pro.upper()

        vdescripcion_pro = lb.pide_cadena(1,200,"Indica la descripcion del proyecto: ")
        vdescripcion_pro = vdescripcion_pro.upper()

        vid_ci_pro = lb.pide_cadena(5,5,"Indica la ID del cientifico encargado del proyecto: ")
        
        query = "SELECT * FROM cientificos WHERE id_ci = '"+ vid_ci_pro +"'"
        grab = cursor.execute(query)

        if grab == 0:
          lb.error("\nEl cientifico no esta dado de alta...")

        else:

          query="INSERT INTO proyectos VALUES('"+ vid_pro +"','"+ vnombre_proyecto +"','"+ varea_pro +"','"+ vdescripcion_pro +"','"+ vid_ci_pro +"')"
            
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

def bajas_proyectos():

    lb.limpia_pantalla()

    print("|============================|")
    print("|   BAJA DE PROYECTOS        |")
    print("|============================|")

    vid_pro = lb.pide_cadena(5,5,"Indica el numero del proyecto a ELIMINAR: ")
    vid_pro = vid_pro.upper()

    if len(vid_pro) > 5:
      pass

    else: 

      query = "DELETE FROM proyectos WHERE id_pro='"+ vid_pro+ "'"

      seguro = lb.pide_cadena(1,1,"seguro de eliminar [S/N] : ")
      seguro = seguro.upper()

      if seguro == "S":

          cone_bd = lb.conectar_bd()
          cursor = cone_bd.cursor()
          x = cursor.execute(query)
          if x == 0:
              lb.error("Error, numero de proyecto inexistente en el archivo de proyectos...")
          else:
              lb.error("El proyecto ha sido eliminado correctamente")
      else:
          lb.error("La accion de ELIMINAR ha sido CANCELADA")

def consultas_proyectos():
  
    lb.limpia_pantalla()
    
    print("|----------------------------|")
    print("|  CONSULTAS DE PROYECTOS    |")
    print("|----------------------------|")

    vid_pro=lb.pide_cadena(5,5, "Indica el numero de proyecto a CONSULTAR: ")
    vid_pro=vid_pro.upper()

    if len(vid_pro) > 5:
      pass

    else:

      query="SELECT * FROM proyectos WHERE id_pro='"+ vid_pro +"'"

      cone_bd = lb.conectar_bd()
      cursor = cone_bd.cursor()
      x = cursor.execute(query)
      
      if x == 0:
          lb.error("Error, proyecto inexistente en el archivo de proyectos...")
      else:
          datos_proyectos=cursor.fetchone()
          print("\n")
          print("Numero de proyectos                  : ", datos_proyectos[0])
          print("Nombre de proyecto                   : ", datos_proyectos[1])
          print("Area                                 : ", datos_proyectos[2])
          print("Descripcion                          : ", datos_proyectos[3])
          print("Cientifico al que esta asignado      : ", datos_proyectos[4])
          lb.error("")
          
      cone_bd.close()

def cambios_proyectos():
  
    lb.limpia_pantalla()
    
    print("|==========================|")
    print("| CAMBIOS DE PROYECTOS     |")
    print("|==========================|")
    
    vid_pro = -1

    while vid_pro != "0":
      
      vid_pro=lb.pide_cadena(1,5,"Indica la id del proyecto, [0] para terminar : ")
      vid_pro=vid_pro.upper()

      if len(vid_pro) > 5:
        pass
      
      elif vid_pro == "0":
        pass

      else:
    
        cone_bd=lb.conectar_bd()
        cursor=cone_bd.cursor()

        query = "SELECT * FROM proyectos WHERE id_pro = '"+ vid_pro +"'"
        validacion = cursor.execute(query)

        if validacion == 0:
          lb.error("El ID del proyecto no existe en la base de datos...")

        else:

          vid_ci_pro = lb.pide_cadena(0,5,"Indica el ID del nuevo cientifico: ")
          query = "SELECT * FROM cientificos WHERE id_ci = '"+ vid_ci_pro +"'"

          validacion = cursor.execute(query)
          
          if validacion == 0:
            lb.error("El nuevo cientifico no esta dado de lata en la base de datos...")

          else:

              query="UPDATE proyectos SET id_ci_pro='"+vid_ci_pro+"' WHERE id_pro='"+vid_pro+"'"

              grab = cursor.execute(query)

              if grab == 0:
                lb.error("Hubo un error al grbar en la base de datos...")

              else:
                lb.error("El cambio ha sido actualizado exitosamente...")

        cone_bd.commit()
        cone_bd.close()