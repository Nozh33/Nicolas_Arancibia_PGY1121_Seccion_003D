import numpy as np
import random as rn
from Frutas import *
#########################################
fruta = Frutas()
def agregarContainer(arreglo_frutas):
    c = False
    while c == False:
        c = fruta.setCodigo(input("Ingrese codigo: "))

    c = False
    while c == False:
        c = fruta.setProducto(input("Ingrese tipo de producto: "))

    c = False
    while c == False:
        try:
            c = fruta.setValor(int(input("Ingrese valor del container: ")))
        except BaseException as error:
            print(f"error: {error}")

    fruta.destino = input("Ingrese destino del container: ")
    print("Container correctamente ingresado")
    return np.append(arreglo_frutas, fruta)

def buscarContainer(arreglo_frutas):
    codigo = input("Ingrese codigo de container: ")
    impuesto = 0
    flag = False
    for fruta in arreglo_frutas:
        if codigo == fruta.codigo:
            print(f"Codigo de container : {fruta.codigo}")
            print(f"Tipo de producto    : {fruta.producto}")
            print(f"Destino             : {fruta.destino}")
            print(f"Valor container     : ${fruta.valor}")
            if fruta.valor > 1200000:
                impuesto = fruta.valor * 0.10
            else:
                impuesto = fruta.valor * 0.05
            print(f"Impuesto de envio   : ${impuesto}")
            flag = True
            break
    if flag == False:
        print("Codigo de container no encontrado")

def imprimirCertificados(arreglo_frutas):
    codigo = input("Ingrese codigo de container: ")
    impuesto = 0
    flag = False
    for fruta in arreglo_frutas:
        if codigo == fruta.codigo:
            print("1- Certificado de Embarque")
            print("2- Certificado de Producto Original")
            try:
                op_cert = int(input("Seleccione tipo de Certificado (1-2): "))
                match op_cert:
                    case 1:
                        print("--------------------------------")
                        print("CERTIFICADO DE EMBARQUE")
                        print("--------------------------------")
                        print(f"Codigo de container : {fruta.codigo}")
                        print(f"Tipo de producto    : {fruta.producto}")
                        print(f"Destino             : {fruta.destino}")
                        print(f"Valor container     : ${fruta.valor}")
                        if fruta.valor > 1200000:
                            impuesto = fruta.valor * 0.10
                        else:
                            impuesto = fruta.valor * 0.05
                        print(f"Impuesto de envio   : ${impuesto}")
                        folio = rn.randint(100, 5000)
                        print(f"Numero de Folio     : {folio}")
                        print("--------------------------------")
                    case 2:
                        print("--------------------------------")
                        print("CERTIFICADO DE PRODUCTO ORIGINAL")
                        print("--------------------------------")
                        print(f"Codigo de container : {fruta.codigo}")
                        print(f"Tipo de producto    : {fruta.producto}")
                        print(f"Destino             : {fruta.destino}")
                        print(f"Valor container     : ${fruta.valor}")
                        if fruta.valor > 1200000:
                            impuesto = fruta.valor * 0.10
                        else:
                            impuesto = fruta.valor * 0.05
                        print(f"Impuesto de envio   : ${impuesto}")
                        folio = rn.randint(100, 5000)
                        print(f"Numero de Folio     : {folio}")
                        print("--------------------------------")
                    case _:
                        print("Seleccion invalida")
            except BaseException as error:
                print(f"error: {error}")
            flag = True
    if flag == False:
        print("Codigo de container no encontrado")

def salir():
    print("Nicolas Arancibia v.1, Adios")
    return False
########################################
arreglo_frutas = np.array([])
ciclo = True
while ciclo:
    print("Exportadora de Frutas Cholito")
    print("1- Ingresar Container")
    print("2- Buscar Container")
    print("3- Imprimir Certificados")
    print("4- Salir")
    try:
        op = int(input("Seleccione opcion (1-4): "))
        match op:
            case 1:
                arreglo_frutas = agregarContainer(arreglo_frutas)
            case 2:
                buscarContainer(arreglo_frutas)
            case 3:
                imprimirCertificados(arreglo_frutas)
            case 4:
                ciclo = salir()
            case _:
                print("Seleccion invalida")
    except BaseException as error:
        print(f"error: {error}")