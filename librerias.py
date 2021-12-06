#  ····································
#  ·             Canmig Cai           ·
#  ·    Luis Felipe Depardon Jasso    ·
#  ·   Ricardo Adolfo González Terán  ·
#  ····································

import pymysql as my

def conectar_bd():
    cone_bd=my.connect(host="localhost",
                       user="root",
                       passwd="",
                       database="centroinvestigacion")
    return cone_bd

def pide_entero(li, ls, let):
    x=ls+1
    while x<li or x>ls:
        x=int(input(let))
        if x<li or x>ls:
            print("Error, valor fuera de rango entre",li,"y",ls,"...")
            error("")
    return x

def pide_flotante(li, ls, let):
    x=ls+1
    while x<li or x>ls:
        x=float(input(let))
        if x<li or x>ls:
            print("Error, valor fuera de rango entre",li,"y",ls,"...")
            error("")
    return x

def pide_cadena(li, ls, let):
    long_cad=-1
    while long_cad<li or long_cad>ls:
        cad=input(let)
        long_cad=len(cad)
        if long_cad<li or long_cad>ls:
            print("Error, longitud de cadena entre",li,"y",ls,"...")
            error("")
        return cad

def error(let):
    print(let)
    print("Oprima [ENTER] para continuar...")
    input()

def limpia_pantalla():
    for i in range(45):
        print()

def pausa():
    input("[[ ENTER ]] para continuar ...")
