# Archivo generado automáticamente

def inicio():
    print("Bienvenido al Museo Virtual de Historia y Arte!")
    print("Puedes explorar distintas salas del museo.")
    op = input("Ir a la Sala de Arte" + " -> ")
    if op == "Ir a la Sala de Arte":
        arte()
    op = input("Ir a la Sala de Historia" + " -> ")
    if op == "Ir a la Sala de Historia":
        historia()

def arte():
    print("Has llegado a la Sala de Arte.")
    print("Aquí encontrarás pinturas clásicas y esculturas modernas.")
    op = input("Ir a la Sala de Ciencia" + " -> ")
    if op == "Ir a la Sala de Ciencia":
        ciencia()
    op = input("Regresar al inicio" + " -> ")
    if op == "Regresar al inicio":
        inicio()

def historia():
    print("Esta es la Sala de Historia.")
    print("Podrás ver objetos antiguos y conocer civilizaciones pasadas.")
    op = input("Ir a la Sala de Tecnología" + " -> ")
    if op == "Ir a la Sala de Tecnología":
        tecnologia()
    op = input("Regresar al inicio" + " -> ")
    if op == "Regresar al inicio":
        inicio()

def ciencia():
    print("Bienvenido a la Sala de Ciencia.")
    print("Observa experimentos interactivos y modelos del universo.")
    op = input("Ir a la Sala de Tecnología" + " -> ")
    if op == "Ir a la Sala de Tecnología":
        tecnologia()
    op = input("Volver a la Sala de Arte" + " -> ")
    if op == "Volver a la Sala de Arte":
        arte()

def tecnologia():
    print("Has llegado a la Sala de Tecnología.")
    print("Aquí se muestran inventos que cambiaron el mundo.")
    op = input("Ir a la Tienda del Museo" + " -> ")
    if op == "Ir a la Tienda del Museo":
        tienda()
    op = input("Regresar al inicio" + " -> ")
    if op == "Regresar al inicio":
        inicio()

def tienda():
    print("Esta es la Tienda del Museo.")
    print("Puedes comprar recuerdos y catálogos de las exposiciones.")
    op = input("Salir del museo" + " -> ")
    if op == "Salir del museo":
        fin()
    op = input("Regresar a la Sala de Tecnología" + " -> ")
    if op == "Regresar a la Sala de Tecnología":
        tecnologia()

def fin():
    print("Gracias por visitar el Museo Virtual!")
    print("Esperamos que vuelvas pronto.")

if __name__ == '__main__':
    inicio()