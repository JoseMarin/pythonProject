from models import coche


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    c = coche("rojo", 8)

    # print(c._coche__color)

    if isinstance(c, coche):
        print("El objeto creado es instancia de la clase Coche")

    print(c.color)
    c.color = "verde"
    del c.color

    """Acelera el coche"""
    c.acelera()
    print(c)





