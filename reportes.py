#  ····································
#  ·             Canmig Cai           ·
#  ·    Luis Felipe Depardon Jasso    ·
#  ·   Ricardo Adolfo González Terán  ·
#  ····································

import librerias as lb

def menu_reportes():
    op = -1
    while op != 6:
        lb.limpia_pantalla()
        print("|==================================================|")
        print("|                 MENU DE REPORTES                 |")
        print("| 1) Lista de científicos                          |")
        print("| 2) Lista de proyectos                            |")
        print("| 3) Lista de proyectos por área                   |")
        print("| 4) Lista de cientificos por área                 |")
        print("| 5) Lista de proyectos asignados a un cientifico  |")
        print("| 6) Regresa al menu principal                     |")
        print("|==================================================|")

        op = lb.pide_entero(1,6,"Indica la opcion deseada : ")
        if op == 1 or op == 4:
            reportes_cientificos(op)
        if op == 2 or op == 3 or op == 5:
            reportes_proyectos(op)
        else:
            print("Opcion Invaida...")


def espa(posiciones,elemento):
    x=(posiciones-len(elemento))*" "
    return x

def reportes_cientificos(op):

    if op == 1:

        query = "SELECT * FROM cientificos ORDER BY id_ci"
    
    elif op == 4:

        varea_pro = lb.pide_cadena(1, 15, "Ingresa el area para listar los cientificos: ")
        varea_pro = varea_pro.upper()
        query = "SELECT * FROM cientificos, proyectos WHERE id_ci = id_ci_pro and area_pro = '"+ varea_pro +"'"

    lb.limpia_pantalla()
    print("===============================================================================================================================================")
    print("====================================================== LISTADO DE CIENTIFICOS =================================================================")
    print("ID del cientifico  Nombre           Ap.paterno       Ap. Materno      Telefono         Correo                                                  ")
    print("===============================================================================================================================================")
    cone_bd = lb.conectar_bd()
    cursor = cone_bd.cursor()
    x = cursor.execute(query)
    lista = cursor.fetchall()
    for reg in lista:
        print(" "*12 + reg[0]+"  "+reg[1]+espa(17,reg[1])+reg[2]+espa(17,reg[2])+reg[3]+espa(17,reg[3])+reg[4]+espa(17,reg[4])+reg[5])

    lb.error("")
    cone_bd.close()
    

def reportes_proyectos(op):

    if op == 2:

        query="SELECT * FROM proyectos ORDER BY id_pro"

    if op == 3:

        varea_pro=lb.pide_cadena(1,15,"Indicala area a listar :")
        varea_pro=varea_pro.upper()
        query = "SELECT * FROM proyectos WHERE area_pro='"+ varea_pro +"' ORDER BY id_ci_pro"
    
    if op == 5:

        vid_ci = lb.pide_cadena(5,5,"Indica el ID del cientifico para listar sus proyectos: ")
        query = "SELECT * FROM proyectos WHERE id_ci_pro = '"+ vid_ci +"' ORDER BY id_ci_pro"


    lb.limpia_pantalla()
    print("=====================================================================================================================")
    print("============================================== LISTADO DE PROYECTOS =================================================")
    print("Numero de proyecto  Nombre           Area              Cientifico Asignado                   Descripcion             ")
    print("=====================================================================================================================")
    cone_bd = lb.conectar_bd()
    cursor = cone_bd.cursor()
    x = cursor.execute(query)
    lista = cursor.fetchall()
    for reg in lista:
        descripcion_pro=reg[3][0:39] + "\n" + " "*78 + reg[3][40:79] + "\n" + " "*78 + reg[3][79:119] + "\n" + " "*78 + reg[3][120:159] + "\n" + reg[3][160:200]
        print(" "*12, (reg[0]+" "*2+reg[1]+espa(17,reg[1])+reg[2]+espa(17,reg[2])), reg[4]+espa(20,reg[2]),(descripcion_pro))

    lb.error("")
    cone_bd.close()

