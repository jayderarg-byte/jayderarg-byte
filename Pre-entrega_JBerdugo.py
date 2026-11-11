



lista_productos = ([["pan", "almacen", "3000"], 
                   ["leche", "lacteos", "3500"], 
                   ["azucar", "almacen", "1000"]
])

print(f"\n{'='*30} Bienvenido al sistema de gestión de productos. {'='*30}")

while True:
        print(" — "*39)
        print(f"|  MENÚ | [1] agregar producto  [2] visualizar productos  [3] buscar productos  [4] eliminar producto  [5] salir    | ")
        print(" — "*39)
        #print("/"*119)
        #MENU
        #debe perimitir elegir ente las funcionalidades disponibles: 
        #agregar productos, visualizar productos, buscar productos y eliminar productos.


        ingreso_usuario = input("\nEscriba una opcion del [MENÚ] (1-5): ").strip().lower()

        #AGREGAR PRODUCTOS
        if ingreso_usuario == "1":
            print("\n--- Seleccionaste: Agregar producto ---")
            #INGRESO DE DATOS DE PRODUCTOS
            #nombres, categorias, precios(sin centavos)
                #estos datos se deben almacenar en una lista
                    #cada producto debe ser presentado como una "sublista" de tres elementos:
                        #nombre, categoria, y precio

            while True:
                nombre_producto = input("\nIngrese el nombre del producto: ").strip().lower()
                categoria_producto = input("Ingrese la categoria del producto: ").strip().lower()
               
                precio_x = input("Ingrese el precio del producto (sin centavos): ")

                if precio_x.isdigit():
                    precio_producto = int(precio_x)
                    break
                

                else:
                    #alerta
                    print(f"\n{'='*10} 'ALERTA' precio no valido. Porfavor vuelva a ingresar los datos (en precio ingresar solo numeros enteros) {'='*10} ")
                    print("")
            lista_productos.append([nombre_producto, categoria_producto, f"${precio_producto}"])
            print(f"\n{"="*10} Producto agregado correctamente {"="*10}")
            for producto in lista_productos:
                print(f"|Nombre: {producto[0]}\t | Categoría: {producto[1]}\t | Precio: {producto[2]}\t |")
                
    
#VISUALIZAR
        #VISUALIZACION DE PRODUCTOS REGISTRADOS
            #funcionalidad de mostrar los productos registrados, debe ser ordenada y legible con cada producto numerado.
        elif ingreso_usuario == "2":
            print("\n--- Seleccionaste: Visualizar productos ---")
            i = 1

            for producto in lista_productos:
                 visualizador = print(f"{i}. Nombre del producto: {producto[0]}\t | Categoría: {producto[1]}\t | Precio: {producto[2]}\t")
                 i += 1
                 continue

#BUSCAR
    #funcionalidad de buscar productos por nombre.
    # si encuentra coincidencias, debe mostrar la informacion completa de los productos que coincidan. 
    # si no hay coincidencias, deber informar que no se encontraron resultados.

        elif ingreso_usuario == "3":

            print("\n--- Seleccionaste: Buscar productos ---")

            producto_buscado = input("\nEscribe el producto que buscas: ").strip().lower()
            encontrado = False

            for producto in lista_productos:
                 nombre_producto = producto[0].lower()

            #revisar
                 if producto_buscado in nombre_producto: #verificamos si el producto esta en la lista
                      print(f"\n{'='*30} Producto encontrado {'='*30} \nNombre: {producto[0]} | Categoría: {producto[1]} | Precio: {producto[2]}")
                      print("")
                      encontrado = True
            if not encontrado:
                 
                 print(f"\t\n{"="*10}Producto no encontrado{"="*10}")
                 print("")
                 
#ELIMINAR
    #el sistema debe permitir eliminar prodcutos de la lista, por su posicion (numero) en la lista.
        elif ingreso_usuario == "4":
            print("\n--- Seleccionaste: Eliminar producto ---")
            
            if len(lista_productos) == 0:
                print("No hay productos en la lista para eliminar.")

            else:
                print("\nProductos disponibles:")
                i = 1
                for producto in lista_productos:
                    print(f"{i}. Nombre: {producto[0]}\t | Categoría: {producto[1]}\t | Precio: {producto[2]}")
                    i += 1
                print("")
                
                # for producto in lista_productos:
                #     print(f"{i-1}. Nombre del producto: {producto[0]}\t | Categoría: {producto[1]}\t | Precio: {producto[2]}\t")
                #     i += 1

                posicion_producto_elimiar = int(input("Ingrese la posición/Número del producto a eliminar: "))
                indice_segun_usuario = posicion_producto_elimiar - 1

                if 0 <= indice_segun_usuario < len(lista_productos):
                    producto_eliminado = lista_productos.pop(indice_segun_usuario)

                    print(f"\nEl producto '{producto_eliminado[0]}' fue eliminado con éxito.")

                else:
                    print("Número de producto no valido. Ese producto no existe.")

#no se elimina el producto ingresado
    
#SALIR           
    #EL PROGRAMA DEBE CONTINUAR FUNCIONANDO HASTA QUE SE ELIJA LA OPCION DE SALIR.
        elif ingreso_usuario == "5":
            print("\n" + "\t" + ("=")*10, "Saliendo del programa...", ("=")*10)
            print("Usted acaba de salir del programa. ¡Hasta luego!")
            break #rompe el bucle while

        else:
            print("="*100)
            print(f"\t{"="*10} Opción no valida, Por favor elige un número del 1 al 5. {"="*10}")
            print("="*100)
  

