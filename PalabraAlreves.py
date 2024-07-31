palabra = input("Ingresar palabra: ")
#print(p¨[0])
#print(p[1])
print(palabra)
palabra_reversed = list(palabra).reverse()
for letra in palabra[::1]:
    print(letra)