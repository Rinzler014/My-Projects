#  ····································
#  ·             Canmig Cai           ·
#  ·    Luis Felipe Depardon Jasso    ·
#  ·   Ricardo Adolfo González Terán  ·
#  ····································

import librerias as lb
import cientificos as ci
import proyectos as pr
import reportes as rp

def menu_principal():
    op = -1
    while op!= 4:
        lb.limpia_pantalla()
        print("|---------------------|")
        print("|    MENU PRINCIPAL   |")
        print("|---------------------|")
        print("| 1) Cientificos      |")
        print("| 2) Proyectos        |")
        print("| 3) Reportes         |")
        print("| 4) Terminar         |")
        print("|---------------------|")

        op = lb.pide_entero(1,4,"Indica la opcion deseada : ")
        if op == 1:
            ci.menu_cientificos() 
        if op == 2:
            pr.menu_proyectos()
        if op == 3:
            rp.menu_reportes()
        else:
            print("Opcion Invalida...")
            
    lb.limpia_pantalla()

# Principal
menu_principal()