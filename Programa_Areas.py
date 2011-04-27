# -*- coding: utf_8 -*-

salir = False

while (salir==False):
	print "----------------------------------------------------------------- "
	print "|                                                               | "
	print "|                                                               | "
	print "|                PROGRAMA CALCULADOR DE ÁREAS                   | "
	print "|                                                               | "
	print "|Elija la opción deseada:                                       | "
	print "|                                                               | "
	print "|    a) Cuadrado           		            d) Trapecio        | "
	print "|                                                               | "
	print "|    b) Rectángulo                           e) Paralelogramo   | "
	print "|                                                               | "
	print "|    c) Triángulo                            f) Rombo           | "
	print "|                                                               | "
	print "|                                                               |  "
	print "|                       S) Salir                                | "
	print "----------------------------------------------------------------- "
	eleccion = raw_input()
	if (eleccion == "a"):
		print
		print 
		print 
		print "            ______________________               "
		print "           |                      |               "
		print "           |                      |               "
		print "           |                      |               "
		print "           |                      | l              "
		print "           |                      | a              "
		print "           |                      | d              "
		print "           |                      | o              "		
		print "           |                      |               "
		print "           |                      |               "
		print "           |______________________|"
		print "                    lado"
		print
		print " Área = lado x lado"
		print 
		lado = raw_input("Ingrese el valor del lado: ")
		print 
		print "El área vale: ", float(lado) * float (lado)
		print 
		raw_input("Presione enter para continuar")
		print 
	elif (eleccion == "b"):
		print 
		print 
		print 
		print "            ________________________________               "
		print "           |                      	       |               "
		print "           |                      	       |              "
		print "           |                      	       |   a            "
		print "           |                     	       |   n            "
		print "           |                      	       |   c            "
		print "           |                                |   h            "		
		print "           |                      	       |   o            "
		print "           |                      	       |                "
		print "           |                                |               "
		print "           |________________________________| "
		print "                        largo "
		print
		print " Área = largo x ancho"
		print
		largo = raw_input("Ingrese el valor del lado más largo (largo!): ")
		print
		ancho = raw_input("Ingrese el valor del lado más corto (ancho!): ")
		print "El área vale: ", float(ancho) * float(largo)
		print
		print
		raw_input("Presione enter para continuar")
	elif (eleccion == "c"):
		print 
		print 
		print 
		print "                    / \     "
		print "                   / | \     "
		print "                  /     \           	              "
		print "                 /   |a  \         	         "
		print "                /     l   \       	         "
		print "               /     |t    \       	         "
		print "              /       u     \       	         "		
		print "             /       |r      \       	        "
		print "            /         a       \     	         "
		print "           /         |         \ 	            "
		print "          /_____________________\    "
		print "                    base "
		print
		print " Área = (base x altura) % 2"
		print
		base = raw_input("Ingrese el valor de la base: ")
		print
		altura = raw_input("Ingrese el valor de la altura: ")
		print "El área vale: ", float(base)*float(altura)/2 
		print
		print
		raw_input("Presione enter para continuar")
	elif (eleccion == "d"):
		print 
		print 
		print 
		print
		print "                 base menor"
		print "                _____________"
		print "               /    a        \       	         "
		print "              /    |l         \             	         "		
		print "             /      t          \       	        "
		print "            /      |u           \     	         "
		print "           /        r            \ 	            "
		print "          /        |a             \     "
		print "         /_________________________\  "
		print "                  base mayor"
		print
                print "Éste es un trapecio isósceles, pero todas las áreas se calculan igual:"
		print " Área = (base Mayor + base menor) x altura) % 2"
		print
		base_M = raw_input("Ingrese el valor de la base Mayor: ")
		base_m = raw_input("Ingrese el valor de la base menor: ")
		altura = raw_input("Ingrese el valor de la altura: ")
		print "El área vale: ", (float(base_M) + float(base_m))*float(altura)/2
		print
		print
		raw_input("Presione enter para continuar")
	elif (eleccion == "e"):
		print 
		print 
		print 
		print
		print "                _______________"
		print "               / a             /       	         "
		print "              / |l            /              	         "		
		print "             /   t           /        	        "
		print "            /   |u          /       	         "
		print "           /     r         /       	            "
		print "          /     |a        /        "
		print "         /_______________/ "
		print "              base "
		print
                print " Área = base * altura"
		print
		base = raw_input("Ingrese el valor de la base: ")
		altura = raw_input("Ingrese el valor de la altura: ")
		print "El área vale: ", float(base) * float(altura)
		print
		print
		raw_input("Presione enter para continuar")
	elif (eleccion == "f"):
		print
		print 
		print "                    / \ "
		print "                   / | \            	               "
		print "                  /     \           	              "
		print "                 /   |d  \         	         "
		print "                /     i   \       	         "
		print "               /     |a    \       	         "
		print "              /       g     \       	         "		
		print "             /__diag_|_menor_\       	        "
		print "             \               /  "
		print "              \      |m     /  "
		print "               \      a    / "
		print "                \    |y   / "
		print "                 \    o  / "
		print "                  \  |r / "
		print "                   \   / "
		print "                    \ / "	
		print
		print " Área = (diagonal mayor x diagonal menor)"
		print
		diag_M = raw_input("Ingrese el valor de la diagonal Mayor: ")
		print
		diag_m = raw_input("Ingrese el valor de la diagonal menor: ")
		print "El área vale: ", float(diag_M)*float(diag_m)
		print
		print
		raw_input("Presione enter para continuar")
		print
	elif (eleccion == "S"):
		salir = True
	else:
		print "Opción no disponible"

