#-----------------------------------------------------------Algoritmo Optimo------------------------------------------------------------#
def algoritmo_optimo():
    #Pedir Datos
    proceso = input("Ingrese los procesos separados por coma: ")
    n_marcos = int(input("Ingrese el No. Marcos: "))

    datos = proceso.replace(" ", "").split(",")
    for i in range(len(datos)):
        datos[i] = int(datos[i])
            
    #Algoritmo
    marcos = [None]*n_marcos # [None, None, ..., None]
    fallas = [False]*len(datos)
    salidas = [None]*len(datos)
    resultado = []

    prox = [len(datos)]*n_marcos
    remain = datos[::]
    k = 0
    for paginas in datos:
        del remain[0]
        i = 0
        while i < n_marcos:
            if paginas == marcos[i]:
                j = 0
                while j < len(remain):
                    if paginas == remain[j]:
                        prox[i] = j
                        break
                    j += 1
                if j == len(remain):
                    prox[i] = len(remain)
                break
            else:
                i += 1
        if i == n_marcos:
            m_pos = 0
            for j in range(len(prox)):
                if prox[m_pos] < prox[j]:
                    m_pos = j
            fallas[k] = True
            salidas[k] = marcos[m_pos]
            marcos[m_pos] = paginas
            j = 0
            while j < len(remain):
                if paginas == remain[j]:
                    prox[m_pos] = j
                    break
                j += 1
            if j == len(remain):
                prox[m_pos] = len(remain)
        for j in range(len(prox)):
            prox[j] -= 1 
        resultado.append(marcos[::])
        k += 1
    mostrar(datos, n_marcos, resultado, fallas, salidas)

#------------------------------------------------------------Algoritmo FIFO-------------------------------------------------------------#
def algoritmo_fifo():
    #Pedir Datos
    proceso = input("Ingrese los procesos separados por coma: ")
    n_marcos = int(input("Ingrese el No. Marcos: "))

    datos = proceso.replace(" ", "").split(",")
    for i in range(len(datos)):
        datos[i] = int(datos[i])
            
    #Algoritmo
    marcos = [None]*n_marcos # [None, None, ..., None]
    fallas = [False]*len(datos)
    salidas = [None]*len(datos)
    resultado = []

    pos = 0
    i = 0
    for pag in datos:
        if pag not in marcos:
            salidas[i] = marcos[pos]
            fallas[i] = True
            marcos[pos] = pag
            if pos < n_marcos - 1:
                pos += 1
            else:
                pos = 0
        resultado.append(marcos[::])
        i += 1
    mostrar(datos, n_marcos, resultado, fallas, salidas)

#-------------------------------------------------------------Algoritmo LRU-------------------------------------------------------------#
def algoritmo_lru():
    #Pedir Datos
    proceso = input("Ingrese los procesos separados por coma: ")
    n_marcos = int(input("Ingrese el No. Marcos: "))

    datos = proceso.replace(" ", "").split(",")
    for i in range(len(datos)):
        datos[i] = int(datos[i])
            
    #Algoritmo
    marcos = [None]*n_marcos # [None, None, ..., None]
    fallas = [False]*len(datos)
    salidas = [None]*len(datos)
    resultado = []

    priority = [i for i in range(n_marcos)] # [1, 2, 3, 4, ..., n_frame]
    k = 0
    for pag in datos:
        i = 0
        while i < n_marcos:
            if pag == marcos[i]:
                for j in range(n_marcos):
                    if i == priority[j]:
                        a = priority[j]
                        priority.append(a)
                        del priority[j]
                        break
                break
            else:
                i += 1
        if i == n_marcos:
            a = priority[0]
            priority.append(a)
            fallas[k] = True
            salidas[k] = marcos[a]
            marcos[a] = pag
            del priority[0]
        resultado.append(marcos[::])
        k += 1
    mostrar(datos, n_marcos, resultado, fallas, salidas)

#-------------------------------------------------------------Mostrar Tabla-------------------------------------------------------------#
def mostrar(datos, n_marcos, resultado, fallas, salidas):  
    cont = 0
    print()
    proceso = ""
    for num in datos:
        proceso += "  " + str(num) + "\t "
    print(proceso)
    print("+-------"*len(datos))
    proceso = ""
    for j in range(n_marcos):
        for i in range(len(resultado)):
            proceso += " |" + str(resultado[i][j]) + "\t"
        proceso += " |\n"
    print(proceso,"+-------"*len(datos))
    proceso = ""
    for F in fallas:
        if F:
            proceso += "  " + "F" + "\t "
            cont=cont+1
        else:
            proceso += "  " + " " + "\t "
    print(proceso)
    proceso = ""
    for num in salidas:
        if num is None:
            proceso += "  " + " " + "\t "
        else:
            proceso += "  " + str(num) + "\t "
    print(proceso)
    print("\nEl Numero de Fallas son: ", cont)
    print('\n')

#---------------------------------------------------------------- MENU ----------------------------------------------------------------#
if __name__ == "__main__":

    opcion = 0
    print ( "                                                       +-------------------------------------------------------+" )
    print ( "                                                       |           Algoritmos de páginas de memoria            |" )
    print ( "                                                       +-------------------------------------------------------+" )
    print('\n')
    while opcion != 4:
        print ( " +----------------------------------+ " )
        print ( " |               MENU               | " )
        print ( " +----------------------------------+ " )
        print ( " |     1) Algoritmo Optimo          | " )
        print ( " |     2) Algoritmo Fifo            | " )
        print ( " |     3) Algoritmo LRU             | " )
        print ( " |     4) Salir                     | " )
        print ( " +----------------------------------+ " )
        opcion = int(input("Selecciona el algoritmo que desea utilizar: "))

        if opcion == 1:
            algoritmo_optimo()
        elif opcion == 2:
            algoritmo_fifo()
        elif opcion == 3:
            algoritmo_lru()
        elif opcion == 4:
            print("¡GRACIAS POR UTILIZAR LA APLICACION!")