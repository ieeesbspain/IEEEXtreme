"""Solution to problem of IEEEXtreme 10.0."""


def convertir(base, letras, value):
    salida = 0

    value = value.strip("+ ")
    i = len(value) - 1
    for dig in value:
        salida += letras.index(dig) * (base ** i)
        i -= 1

    return salida


def int2base(x, base, digs):
    digits = ''
    while x:
        digits = digs[x % base] + digits
        x /= base
    return digits


def main():
    lenCadenas = 0
    base, letras = raw_input().split(" ")

    print(base + " " + letras)
    sumando1 = raw_input()
    lenCadenas = len(sumando1)
    print(sumando1)

    sumando2 = raw_input()
    print(sumando2)
    print(raw_input())

    raw_input()  # result

    base = int(base)

    sumando1 = convertir(base, letras, sumando1)
    sumando2 = convertir(base, letras, sumando2)

    resultado = sumando1 + sumando2

    final = int2base(resultado, base, letras)
    espacios = lenCadenas - len(final)
    final = ' ' * espacios + final
    print(final)

if __name__ == '__main__':
    main()
