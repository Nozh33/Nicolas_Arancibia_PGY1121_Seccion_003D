class Frutas:
    codigo = ''
    producto = ''
    valor = 0
    destino = ''
    impuesto = 0

    def __init__(self):
        self.codigo = 'AA-01'
        self.producto = 'LIMONES'
        self.valor = 900000
        self.destino = 's/d'
        self.impuesto = 0

    def setCodigo(self, codigo):
        if len(codigo) == 5:
            if codigo[0:2].isalpha() and codigo[2:3] == '-' and codigo[3:5].isdigit():
                self.codigo = codigo
                return True
            else:
                print("Codigo invalido ej. 'AA-00'")
                return False
        else:
            print("Codigo debe ser de 5 caracteres")
            return False

    def setProducto(self, producto):
        if producto.upper() == 'LIMONES' or producto.upper() == 'PERAS' or producto.upper() == 'MANZANAS':
            self.producto = producto
            return True
        else:
            print("Producto solo pueden ser Limones, Peras o Manzanas")
            return False

    def setValor(self, valor):
        if valor >= 900000 and valor <= 4500000:
            self.valor = valor
            return True
        else:
            print("Valor de container debe ser entre $900.000 y $4.500.000")
            return False


