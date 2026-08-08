ids = []
nombres = []
documentos = []
correos = []
telefonos = []
edades = []
ciudades = []
estados = []
fechas = []
observaciones = []
resultados_nombres = []
resultados_documentos = []
resultados_correos = []
resultados_telefonos = []
resultados_edades = []
resultados_ciudades = []
#---------------------------------------------#
#--|menu_principal_autoverificador_de_datos|--#
#---------------------------------------------#
while True:
    print("menu principal autoverificador de datos")
    print("1) registrar datos")
    print("2) verificar datos")
    print("3) editar datos")
    print("4) eliminar datos")
    print("5) buscar datos")
    print("6) lista de datos")
    print("7) salir")
    opcion = input("seleccione una opción: ")
    #---------------------#
    #--|registrar_datos|--#
    #---------------------#
    if opcion == "1":
        if len(ids) == 0:
            id_dato = 1
        else:
            id_dato = ids[-1] + 1
        nombre = input("nombre: ")
        documento = input("documento: ")
        correo = input("correo: ")
        telefono = input("teléfono: ")
        try:
            edad = int(input("edad: "))
        except ValueError:
            edad = 0
        ciudad = input("ciudad: ")
        fecha = input("fecha: ")
        observacion = input("observación: ")
        estado = "pendiente"
        ids.append(id_dato)
        nombres.append(nombre)
        documentos.append(documento)
        correos.append(correo)
        telefonos.append(telefono)
        edades.append(edad)
        ciudades.append(ciudad)
        estados.append(estado)
        fechas.append(fecha)
        observaciones.append(observacion)
        resultados_nombres.append("pendiente")
        resultados_documentos.append("pendiente")
        resultados_correos.append("pendiente")
        resultados_telefonos.append("pendiente")
        resultados_edades.append("pendiente")
        resultados_ciudades.append("pendiente")
        print("datos registrados correctamente.")
        print("id:", id_dato)
        print("estado:", estado)
    #---------------------#
    #--|verificar_datos|--#
    #---------------------#
    elif opcion == "2":
        if len(ids) == 0:
            print("no existen datos registrados.")
        else:
            print("verificar datos")
            for i in range(len(ids)):
                print(
                    f"{ids[i]} | "
                    f"{nombres[i]} | "
                    f"{correos[i]} | "
                    f"{estados[i]}"
                )
            id_verificar = int(
                input("ingrese la id de los datos: ")
            )
            if id_verificar in ids:
                posicion = ids.index(id_verificar)
                #----------------------#
                #--|verificar_nombre|--#
                #----------------------#
                if nombres[posicion].strip() != "":
                    resultados_nombres[posicion] = "válido"
                else:
                    resultados_nombres[posicion] = "inválido"
                #-------------------------#
                #--|verificar_documento|--#
                #-------------------------#
                if (
                    documentos[posicion].strip() != ""
                    and documentos[posicion].isdigit()
                    and len(documentos[posicion]) >= 5
                ):
                    resultados_documentos[posicion] = "válido"
                else:
                    resultados_documentos[posicion] = "inválido"
                #----------------------#
                #--|verificar_correo|--#
                #----------------------#
                correo = correos[posicion]
                if (
                    "@" in correo
                    and "." in correo
                    and correo.index("@") > 0
                    and correo.rfind(".") > correo.index("@") + 1
                    and not correo.endswith(".")
                ):
                    resultados_correos[posicion] = "válido"
                else:
                    resultados_correos[posicion] = "inválido"
                #------------------------#
                #--|verificar_telefono|--#
                #------------------------#
                telefono = telefonos[posicion]
                if (
                    telefono.strip() != ""
                    and telefono.isdigit()
                    and len(telefono) >= 7
                ):
                    resultados_telefonos[posicion] = "válido"
                else:
                    resultados_telefonos[posicion] = "inválido"
                #--------------------#
                #--|verificar_edad|--#
                #--------------------#
                if (
                    isinstance(edades[posicion], int)
                    and edades[posicion] >= 0
                    and edades[posicion] <= 120
                ):
                    resultados_edades[posicion] = "válido"
                else:
                    resultados_edades[posicion] = "inválido"
                #----------------------#
                #--|verificar_ciudad|--#
                #----------------------#
                if ciudades[posicion].strip() != "":
                    resultados_ciudades[posicion] = "válido"
                else:
                    resultados_ciudades[posicion] = "inválido"
                #----------------------------#
                #--|resultado_verificacion|--#
                #----------------------------#
                print("resultado de la verificación")
                print(
                    "nombre:",
                    resultados_nombres[posicion]
                )
                print(
                    "documento:",
                    resultados_documentos[posicion]
                )
                print(
                    "correo:",
                    resultados_correos[posicion]
                )
                print(
                    "teléfono:",
                    resultados_telefonos[posicion]
                )
                print(
                    "edad:",
                    resultados_edades[posicion]
                )
                print(
                    "ciudad:",
                    resultados_ciudades[posicion]
                )
                if (
                    resultados_nombres[posicion] == "válido"
                    and resultados_documentos[posicion] == "válido"
                    and resultados_correos[posicion] == "válido"
                    and resultados_telefonos[posicion] == "válido"
                    and resultados_edades[posicion] == "válido"
                    and resultados_ciudades[posicion] == "válido"
                ):
                    estados[posicion] = "válido"
                    print("resultado:")
                    print("DATOS VÁLIDOS")
                else:
                    estados[posicion] = "requiere revisión"
                    print("resultado:")
                    print("DATOS REQUIEREN REVISIÓN")
            else:
                print("id no encontrada.")
    #------------------#
    #--|editar_datos|--#
    #------------------#
    elif opcion == "3":
        if len(ids) == 0:
            print("no existen datos registrados.")
        else:
            print("editar datos")
            for i in range(len(ids)):
                print(
                    f"{ids[i]} | "
                    f"{nombres[i]} | "
                    f"{correos[i]} | "
                    f"{estados[i]}"
                )
            id_buscar = int(
                input("ingrese la id de los datos: ")
            )
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos actuales")
                print("nombre:", nombres[posicion])
                print("documento:", documentos[posicion])
                print("correo:", correos[posicion])
                print("teléfono:", telefonos[posicion])
                print("edad:", edades[posicion])
                print("ciudad:", ciudades[posicion])
                print("fecha:", fechas[posicion])
                print(
                    "observación:",
                    observaciones[posicion]
                )
                nombres[posicion] = input(
                    "nuevo nombre: "
                )
                documentos[posicion] = input(
                    "nuevo documento: "
                )
                correos[posicion] = input(
                    "nuevo correo: "
                )
                telefonos[posicion] = input(
                    "nuevo teléfono: "
                )
                try:
                    edades[posicion] = int(
                        input("nueva edad: ")
                    )
                except ValueError:
                    edades[posicion] = 0
                ciudades[posicion] = input(
                    "nueva ciudad: "
                )
                fechas[posicion] = input(
                    "nueva fecha: "
                )
                observaciones[posicion] = input(
                    "nueva observación: "
                )
                estados[posicion] = "pendiente"
                resultados_nombres[posicion] = "pendiente"
                resultados_documentos[posicion] = "pendiente"
                resultados_correos[posicion] = "pendiente"
                resultados_telefonos[posicion] = "pendiente"
                resultados_edades[posicion] = "pendiente"
                resultados_ciudades[posicion] = "pendiente"
                print(
                    "datos actualizados correctamente."
                )
                print(
                    "estado: pendiente de verificación."
                )
            else:
                print("id no encontrada.")
    #--------------------#
    #--|eliminar_datos|--#
    #--------------------#
    elif opcion == "4":
        if len(ids) == 0:
            print("no existen datos registrados.")
        else:
            print("eliminar datos")
            for i in range(len(ids)):
                print(
                    f"{ids[i]} | "
                    f"{nombres[i]} | "
                    f"{estados[i]}"
                )
            id_buscar = int(
                input("ingrese la id de los datos: ")
            )
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print(
                    "nombre:",
                    nombres[posicion]
                )
                print(
                    "documento:",
                    documentos[posicion]
                )
                confirmacion = input(
                    "¿desea eliminar estos datos? (s/n): "
                )
                if confirmacion.upper() == "S":
                    ids.pop(posicion)
                    nombres.pop(posicion)
                    documentos.pop(posicion)
                    correos.pop(posicion)
                    telefonos.pop(posicion)
                    edades.pop(posicion)
                    ciudades.pop(posicion)
                    estados.pop(posicion)
                    fechas.pop(posicion)
                    observaciones.pop(posicion)
                    resultados_nombres.pop(posicion)
                    resultados_documentos.pop(posicion)
                    resultados_correos.pop(posicion)
                    resultados_telefonos.pop(posicion)
                    resultados_edades.pop(posicion)
                    resultados_ciudades.pop(posicion)
                    print(
                        "datos eliminados correctamente."
                    )
                else:
                    print(
                        "los datos no fueron eliminados."
                    )
            else:
                print("id no encontrada.")
    #------------------#
    #--|buscar_datos|--#
    #------------------#
    elif opcion == "5":
        if len(ids) == 0:
            print("no existen datos registrados.")
        else:
            id_buscar = int(
                input("ingrese la id de los datos: ")
            )
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("información de los datos")
                print("id:", ids[posicion])
                print("nombre:", nombres[posicion])
                print(
                    "documento:",
                    documentos[posicion]
                )
                print("correo:", correos[posicion])
                print(
                    "teléfono:",
                    telefonos[posicion]
                )
                print("edad:", edades[posicion])
                print(
                    "ciudad:",
                    ciudades[posicion]
                )
                print(
                    "estado:",
                    estados[posicion]
                )
                print(
                    "fecha:",
                    fechas[posicion]
                )
                print(
                    "observación:",
                    observaciones[posicion]
                )
                print("resultado de las validaciones")
                print(
                    "nombre:",
                    resultados_nombres[posicion]
                )
                print(
                    "documento:",
                    resultados_documentos[posicion]
                )
                print(
                    "correo:",
                    resultados_correos[posicion]
                )
                print(
                    "teléfono:",
                    resultados_telefonos[posicion]
                )
                print(
                    "edad:",
                    resultados_edades[posicion]
                )
                print(
                    "ciudad:",
                    resultados_ciudades[posicion]
                )
            else:
                print("id no encontrada.")
    #--------------------#
    #--|lista_de_datos|--#
    #--------------------#
    elif opcion == "6":
        if len(ids) == 0:
            print("no existen datos registrados.")
        else:
            validos = 0
            revisiones = 0
            pendientes = 0
            nombres_validos = 0
            nombres_invalidos = 0
            documentos_validos = 0
            documentos_invalidos = 0
            correos_validos = 0
            correos_invalidos = 0
            telefonos_validos = 0
            telefonos_invalidos = 0
            edades_validas = 0
            edades_invalidas = 0
            ciudades_validas = 0
            ciudades_invalidas = 0
            print("lista de datos")
            for i in range(len(ids)):
                print(
                    f"{ids[i]} | "
                    f"{nombres[i]} | "
                    f"{correos[i]} | "
                    f"{estados[i]}"
                )
                if estados[i] == "válido":
                    validos += 1
                elif estados[i] == "requiere revisión":
                    revisiones += 1
                elif estados[i] == "pendiente":
                    pendientes += 1
                if resultados_nombres[i] == "válido":
                    nombres_validos += 1
                elif resultados_nombres[i] == "inválido":
                    nombres_invalidos += 1
                if resultados_documentos[i] == "válido":
                    documentos_validos += 1
                elif resultados_documentos[i] == "inválido":
                    documentos_invalidos += 1
                if resultados_correos[i] == "válido":
                    correos_validos += 1
                elif resultados_correos[i] == "inválido":
                    correos_invalidos += 1
                if resultados_telefonos[i] == "válido":
                    telefonos_validos += 1
                elif resultados_telefonos[i] == "inválido":
                    telefonos_invalidos += 1
                if resultados_edades[i] == "válido":
                    edades_validas += 1
                elif resultados_edades[i] == "inválido":
                    edades_invalidas += 1
                if resultados_ciudades[i] == "válido":
                    ciudades_validas += 1
                elif resultados_ciudades[i] == "inválido":
                    ciudades_invalidas += 1
            print("estadísticas autoverificador de datos")
            print(
                "registros registrados:",
                len(ids)
            )
            print(
                "registros válidos:",
                validos
            )
            print(
                "requieren revisión:",
                revisiones
            )
            print(
                "pendientes:",
                pendientes
            )
            print("validación de nombres")
            print("válidos:", nombres_validos)
            print("inválidos:", nombres_invalidos)
            print("validación de documentos")
            print("válidos:", documentos_validos)
            print("inválidos:", documentos_invalidos)
            print("validación de correos")
            print("válidos:", correos_validos)
            print("inválidos:", correos_invalidos)
            print("validación de teléfonos")
            print("válidos:", telefonos_validos)
            print("inválidos:", telefonos_invalidos)
            print("validación de edades")
            print("válidas:", edades_validas)
            print("inválidas:", edades_invalidas)
            print("validación de ciudades")
            print("válidas:", ciudades_validas)
            print("inválidas:", ciudades_invalidas)
    #------------------------------#
    #--|salir_del_menu_principal|--#
    #------------------------------#
    elif opcion == "7":
        print(
            "gracias por utilizar el autoverificador de datos."
        )
        break
    else:
        print("opción no válida.")