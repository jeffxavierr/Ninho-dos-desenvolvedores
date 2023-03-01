a = int(input("informe o primeiro número:  "))
b = int(input("informe o segundo número:  "))
c = int(input("informe o terceiro número: "))
if a > b and a > c:
    print(a, "é o maior valor")
    if b > c:
        print(b, "é o segundo maior valor")
        print(c, "é o menor valor")
    else:
        print(c, "é o segundo maior valor")
        print(b, "é o segundo menor valor ")
if b > a and b > c:
    print(b, "é o maior valor")
    if a > c:
        print(a, "é o segundo maior valor")
        print(c, "é o menor valor")
    else:
        print(c, "é o menor valor")
        print(a, "é o maior valor")
if c > a and c > b:
    print(c, "é o maior valor")
    if a > b:
        print(a, "é o segundo maior valor")
        print(b, "é o menor valor")
    else:
        print(a, "é o menor valor")
        print(b, "é o segundo maior valor")